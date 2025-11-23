# SafeRoute AI - Toronto Risk Map

**AI-powered safe route navigation system** using real Toronto crime data, OpenStreetMap infrastructure, and intelligent weight calculation for risk-aware pathfinding.

## 🎯 Project Overview

SafeRoute AI analyzes Toronto's downtown area to create a **weighted routing graph** that enables safe path calculation between any two points. The system combines:
- Real crime statistics (normalized by population)
- Street network topology from OpenStreetMap
- Points of Interest (POIs) density analysis
- Intelligent weight calculation for each intersection and street segment

## 🚀 Features

- **Interactive Risk Visualization**: Dark-themed map with color-coded streets (🟢 safe → 🔴 dangerous)
- **Weighted Routing Graph**: 11,495 intersection nodes + 13,195 street edges
- **Smart Weight Calculation**: Multi-factor analysis considering crime rates, POI density, and street characteristics
- **Real Toronto Data**: Crime rates from 2024 across 158 neighborhoods
- **Ready for Pathfinding**: Graph structure prepared for A* or Dijkstra algorithms

## 📊 How It Works

### 1. **Crime Risk Calculation**
Uses **crime RATES** (already normalized by population) from Toronto Open Data:

```python
# Crime type weights (based on severity)
HOMICIDE: 10.0    # Most severe
SHOOTING: 10.0
ROBBERY: 5.0
ASSAULT: 3.0
BREAK & ENTER: 2.0
AUTO THEFT: 2.0
THEFT FROM MV: 1.0
THEFT OVER: 1.0
BIKE THEFT: 1.0

# Calculate neighborhood risk score
risk_score = Σ(crime_rate × weight) for all crime types
risk_normalized = (risk - min) / (max - min)  # Normalize to 0-1
```

**Example Results:**
- **Highest Risk**: West Humber-Clairville (normalized: 1.0)
- **Lowest Risk**: Lambton Baby Point (normalized: 0.0)

### 2. **Intersection (Node) Weight Calculation**

Each of the **11,495 intersections** gets a weight based on **4 key features**:

#### **Feature Extraction Per Intersection**

```python
# 1. Neighborhood Crime Risk (via spatial join)
# Uses point-in-polygon to find which neighborhood contains this intersection
for neighborhood_polygon in neighborhoods:
    if neighborhood_polygon.contains(intersection_point):
        risk_score = neighborhood_risk[neighborhood_name]  # 0-1 normalized
        break

# 2. POI Density (Points of Interest within 100m)
# Counts restaurants, shops, bars, etc. using spatial grid optimization
buffer_radius = 0.001  # ~100 meters in degrees
num_pois = count_pois_within_radius(intersection, buffer_radius)
poi_density = min(num_pois / 50.0, 1.0)  # Normalized, capped at 50

# 3. Street Type Importance (average of connected streets)
# Different street types have different priority values:
highway_priorities = {
    'motorway': 1.0,      # Highest exposure
    'trunk': 0.9,
    'primary': 0.8,
    'secondary': 0.7,
    'tertiary': 0.6,
    'residential': 0.4,
    'service': 0.2,
    'footway': 0.1        # Lowest exposure
}
avg_street_priority = mean([priority for street in connected_streets])

# 4. Intersection Degree (complexity)
# Number of streets meeting at this intersection
degree = len(connected_streets)
degree_normalized = min(degree / 8.0, 1.0)  # Normalized, capped at 8
```

#### **Weight Formula**

```python
# Weighted combination of all features:
weight_components = {
    'crime_rate': risk_score × 40%,              # Neighborhood crime (most important)
    'poi_density': poi_density × 20%,            # Local activity level
    'street_importance': avg_street_priority × 20%,  # Road exposure
    'degree': degree_normalized × 20%            # Intersection complexity
}

total_weight = sum(weight_components.values())

# Scale to meaningful range (0-100)
final_weight = total_weight × 100
```

#### **Weight Categorization**

| Range | Category | Color | Count | Description |
|-------|----------|-------|-------|-------------|
| 0-30 | Low | 🟢 Green | 4,772 | Safe residential areas, low crime |
| 30-60 | Medium | 🟡 Yellow | 5,339 | Mixed areas, moderate activity |
| 60-100 | High | 🔴 Red | 1,384 | High crime areas, busy intersections |

#### **Real Examples**

**Example 1: High-Risk Intersection**
- **Location**: Yonge & Dundas (Downtown Core)
- **Neighborhood**: Yonge-Bay Corridor (risk: 0.95)
- **POIs nearby**: 73 (bars, restaurants, shops)
- **Streets**: 4-way intersection (primary roads)
- **Calculation**:
  ```
  crime:     0.95 × 40% = 38.0
  poi:       1.00 × 20% = 20.0  (73/50 capped at 1.0)
  street:    0.80 × 20% = 16.0  (primary road)
  degree:    0.50 × 20% = 10.0  (4 streets / 8)
  -----------------------------------
  Total:     84.0 → 🔴 High Risk
  ```

**Example 2: Low-Risk Intersection**
- **Location**: Quiet residential corner in North Riverdale
- **Neighborhood**: North Riverdale (risk: 0.12)
- **POIs nearby**: 0
- **Streets**: Simple 2-way (residential)
- **Calculation**:
  ```
  crime:     0.12 × 40% = 4.8
  poi:       0.00 × 20% = 0.0
  street:    0.40 × 20% = 8.0   (residential)
  degree:    0.25 × 20% = 5.0   (2 streets / 8)
  -----------------------------------
  Total:     17.8 → 🟢 Low Risk
  ```

### 3. **Edge (Street) Weight Calculation**

Each of the **13,195 street segments** (edges) connects two intersections (nodes). The edge inherits the average weight of its endpoints.

```python
# Get the two nodes connected by this street
start_node = nodes[edge_start_id]
end_node = nodes[edge_end_id]

# Average their weights
edge_weight = (start_node['weight'] + end_node['weight']) / 2

# Store with street metadata
edge = {
    'source': edge_start_id,
    'target': edge_end_id,
    'weight': edge_weight,
    'length_m': street_length_meters,
    'name': street_name,
    'highway_type': street_type
}
```

#### **Why Average the Endpoints?**

Streets represent **transitions** between two points:
- Starting at Node A (weight 60)
- Ending at Node B (weight 80)
- Walking this street exposes you to **both risk levels**
- Average (70) represents the **overall exposure** along the route

#### **Edge Distribution**

| Weight Range | Risk Level | Count | Percentage |
|--------------|------------|-------|------------|
| 12-30 | Low 🟢 | 9,571 | 72.5% |
| 30-70 | Medium 🟡 | 3,614 | 27.4% |
| 70-129 | High 🔴 | 10 | 0.1% |

#### **Real Examples**

**Example 1: High-Risk Street**
- **Street**: Dundas St E segment near Yonge
- **Start Node**: Weight 84.0 (Yonge & Dundas intersection)
- **End Node**: Weight 78.5 (Next intersection east)
- **Edge Weight**: (84.0 + 78.5) / 2 = **81.25** 🔴
- **Length**: 127 meters
- **Visualization**: Bright red line on map

**Example 2: Safe Street**
- **Street**: Residential side street in North Riverdale
- **Start Node**: Weight 17.8 (quiet corner)
- **End Node**: Weight 19.2 (another quiet corner)
- **Edge Weight**: (17.8 + 19.2) / 2 = **18.5** 🟢
- **Length**: 89 meters
- **Visualization**: Green line on map

#### **Routing Implications**

When calculating the **safest route** using A* algorithm:

```python
# For each edge in the path:
route_cost = distance_cost × (1 - safety_weight) + safety_cost × safety_weight

# With safety_weight = 0.9 (90% safety priority):
# - Edge with weight 18.5 → LOW cost (preferred)
# - Edge with weight 81.25 → HIGH cost (avoided)

# The algorithm will choose longer but safer routes
# avoiding high-weight edges even if they're shorter
```

## 📁 Project Structure

```
├── index.html                    # Web interface
├── app.js                        # Leaflet map + visualization logic
├── style.css                     # Dark theme styling
├── server.js                     # Node.js static file server
├── package.json                  # Project configuration
│
├── Data Files:
│   ├── Neighbourhood_Crime_Rates_*.csv        # Crime statistics (158 neighborhoods)
│   ├── Neighbourhood_Crime_Rates_*.geojson    # Neighborhood boundaries
│   ├── planet_*.osm.geojson.xz               # OpenStreetMap data (compressed)
│   ├── downtown_streets.geojson              # 22,448 street segments
│   ├── downtown_pois.geojson                 # 19,487 points of interest
│   ├── intersection_weights.csv              # 11,495 weighted nodes
│   ├── intersection_weights.geojson          # Nodes for visualization
│   ├── routing_edges.csv                     # 13,195 weighted edges
│   ├── routing_edges.geojson                 # Edges for visualization
│   └── routing_graph.json                    # Complete graph structure
│
├── Python Scripts:
│   ├── process_downtown_osm.py               # Extract streets/POIs from OSM
│   ├── calculate_intersection_weights.py     # Calculate node weights
│   └── create_routing_graph.py               # Build routing graph
│
└── ML Notebooks:
    └── ML_Weight_Prediction.ipynb            # Train ML models (future work)
```

## 🛠️ Setup

### Prerequisites
- **Node.js** v14+ (JavaScript runtime)
- **Python** 3.8+ (for data processing)
- Python packages: `pandas`, `numpy`, `shapely`, `scikit-learn`

### Installation

```bash
# 1. Install Python dependencies
pip install pandas numpy shapely scikit-learn

# 2. Start the web server
node server.js

# 3. Open browser
# Navigate to http://localhost:3000
```

## 📍 Coverage Area

**Downtown Toronto** - optimized for dense urban routing:
- **Bounds**: 43.629°N to 43.675°N, -79.429°W to -79.347°W
- **Key areas**: Financial District, Entertainment District, Yonge-Bay Corridor
- **Size**: ~5km × 5km area with high intersection density

## 🎨 Visualization

The map shows **routing edges** color-coded by weight:

| Color | Weight Range | Risk Level | Count |
|-------|-------------|------------|-------|
| 🟢 Green | 12-30 | Safe | 9,571 edges |
| 🟡 Yellow | 30-70 | Medium | 3,614 edges |
| 🔴 Red | 70-129 | High Risk | 10 edges |

**Click any street** to see:
- Weight value
- Length (meters)
- Street name
- Highway type
- Risk category

## 🧮 Technical Details

### Graph Statistics
- **Nodes**: 11,495 intersections
- **Edges**: 13,195 street segments (bidirectional)
- **Average degree**: 2.3 edges per node
- **Weight range**: 12.0 - 128.8
- **Graph type**: Weighted, undirected

### Data Sources
1. **Toronto Open Data**: Crime rates by neighborhood (2014-2024)
2. **OpenStreetMap**: Street network, buildings, POIs
3. **Spatial Analysis**: Point-in-polygon for neighborhood assignment

### Calculation Pipeline

```
1. Load Crime Data (158 neighborhoods)
   ↓
2. Calculate Risk Scores (weighted sum of crime rates)
   ↓
3. Load OSM Data (22,448 streets + 19,487 POIs)
   ↓
4. Extract Intersections (11,495 nodes)
   ↓
5. Calculate Intersection Weights
   - Spatial join with neighborhoods
   - Count nearby POIs (100m radius)
   - Analyze street types
   ↓
6. Build Graph Edges (13,195 connections)
   - Match street endpoints to intersections
   - Calculate edge weights
   - Create bidirectional graph
   ↓
7. Export for Visualization & Routing
```

## 🤖 Machine Learning (Future Work)

The system is prepared for ML-based weight prediction:

**Approach**: Train models to predict weights based on features
- **Features**: Street type, POI density, building density, neighborhood risk
- **Target**: Weight value or category (Low/Medium/High)
- **Models**: RandomForest Regressor/Classifier, GradientBoosting
- **Use case**: Predict weights for new areas without manual calculation

See `ML_Weight_Prediction.ipynb` for implementation details.

## 🔬 Technical Deep Dive: Spatial Join Methodology

### **The Challenge: Area-Level Data → Point-Level Weights**

Crime data comes aggregated by **neighborhood areas** (158 polygons), but we need weights for **individual intersections** (11,495 points). How do we map area data to specific locations?

### **Solution: Point-in-Polygon Spatial Join**

#### **Step 1: Load Neighborhood Polygons**
```python
# From GeoJSON - each neighborhood is a polygon
neighborhoods = {
    "Yonge-Bay Corridor": Polygon([
        (-79.40, 43.65),  # SW corner
        (-79.36, 43.65),  # SE corner
        (-79.36, 43.68),  # NE corner
        (-79.40, 43.68)   # NW corner
    ]),
    "North Riverdale": Polygon([...]),
    ...
}
```

#### **Step 2: Load Risk Scores by Name**
```python
# From CSV - risk score per neighborhood
neighborhood_risk = {
    "Yonge-Bay Corridor": 0.95,  # High crime
    "North Riverdale": 0.12,     # Low crime
    ...
}
```

#### **Step 3: Spatial Join - The Core Algorithm**
```python
# For each intersection extracted from OSM:
intersection = Point(-79.3857, 43.6608)  # Just lat/lon coordinates

# Find which neighborhood contains this point
for name, polygon in neighborhoods.items():
    if polygon.contains(intersection):  # ← Point-in-Polygon test
        risk_score = neighborhood_risk[name]
        break

# Result: Point (-79.3857, 43.6608) is inside "Yonge-Bay Corridor"
# → Inherits risk score: 0.95
```

### **How `.contains()` Works: Ray Casting Algorithm**

The Shapely library uses computational geometry to test if a point is inside a polygon:

1. **Cast a ray** from the point to infinity (→)
2. **Count crossings** with polygon boundary
3. **Odd crossings** = INSIDE ✅ | **Even crossings** = OUTSIDE ❌

```
Visual Example:

Inside:
    ┌─────────────┐
    │ Polygon     │
    │   • P ─────→│─→  (crosses 1 time = ODD = INSIDE)
    │             │
    └─────────────┘

Outside:
• P ─────→┌──────┐─→  (crosses 2 times = EVEN = OUTSIDE)
          │      │
          └──────┘
```

### **Coordinate System Accuracy**

Both datasets use **WGS84 (EPSG:4326)** - geographic coordinates in decimal degrees:

| Source | Format | Example | Precision |
|--------|--------|---------|-----------|
| Crime GeoJSON | Lon, Lat (degrees) | -79.3857, 43.6608 | 6 decimals ≈ 0.1m |
| OSM Streets | Lon, Lat (degrees) | -79.3857, 43.6608 | 6 decimals ≈ 0.1m |

✅ **Same projection → Accurate spatial relationships**

### **Complete Workflow Example**

```python
# 1. Intersection from OSM
intersection = Point(-79.3857, 43.6608)

# 2. Find neighborhood via spatial join
yonge_bay_polygon = Polygon([(-79.40, 43.65), (-79.36, 43.68), ...])
yonge_bay_polygon.contains(intersection)  # → True

# 3. Get risk score
risk = 0.95  # From CSV for "Yonge-Bay Corridor"

# 4. Count nearby POIs
pois_within_100m = 73  # Spatial query

# 5. Calculate weight
weight = (
    risk * 0.40 +              # Crime risk (40%)
    (73/50) * 0.20 +           # POI density (20%)
    0.8 * 0.20 +               # Street importance (20%)
    (4/8) * 0.20               # Degree (20%)
) * 100 = 84.0
```

### **Why This Approach Works**

✅ **Mathematically sound**: Point-in-polygon is a proven computational geometry algorithm  
✅ **Consistent CRS**: Both datasets use WGS84  
✅ **High precision**: 6 decimal places = ~10cm accuracy  
✅ **Efficient**: Spatial indexing for fast lookups  
✅ **Validated**: Shapely is industry-standard geospatial library  

---

## 💬 Plain English Explanation (For Pitch)

### **The Problem We Solved**

Toronto publishes crime data by **neighborhood** - but people walk **street by street**. How do you tell someone which exact intersection is safe or dangerous?

### **Our Solution: Smart Data Mapping**

Think of it like this:

1. **Crime Data = Big Zones** 🗺️
   - Toronto is divided into 158 neighborhoods
   - Each neighborhood has a crime rate (like a "danger score")
   - Example: "Yonge-Bay Corridor" = High Crime (95/100)

2. **Street Network = Tiny Points** 📍
   - We have 11,495 street intersections from OpenStreetMap
   - Each intersection is just a GPS coordinate (latitude, longitude)
   - Example: Yonge & Dundas intersection = (43.6608°N, -79.3857°W)

3. **The Magic: Connecting the Dots** ✨
   - Our algorithm asks: "Is this intersection GPS point **inside** the Yonge-Bay neighborhood zone?"
   - Computer draws a line from the point and counts how many times it crosses the neighborhood boundary
   - Odd crossings = inside, even crossings = outside
   - Once we know the neighborhood, we assign that area's crime score to the intersection

4. **Make It Smarter** 🧠
   - We add local factors:
     - How many bars/stores nearby? (More activity = more risk)
     - How busy is the intersection? (4-way vs 2-way)
     - What type of street? (Highway vs residential)
   
5. **Final Result: Every Street Has a Safety Score** 🎯
   - Yonge & Dundas: Weight 84 (High Crime area + 73 bars nearby + busy 4-way) = 🔴 Red
   - Quiet Riverdale street: Weight 12 (Low Crime area + 0 bars + simple 2-way) = 🟢 Green

### **Why This Matters**

- **Accurate**: Uses real Toronto crime statistics (2024 data)
- **Precise**: Down to individual street corners, not just neighborhoods
- **Smart**: Considers multiple safety factors, not just crime
- **Visual**: Color-coded map shows safe (green) vs dangerous (red) streets
- **Actionable**: Powers safe route navigation - avoid red, prefer green

### **The Technical Win**

We bridged two incompatible datasets:
- **Crime data**: Area-level (neighborhoods)
- **Street data**: Point-level (GPS coordinates)

Using proven geospatial algorithms, we accurately mapped area statistics to individual locations - enabling street-by-street safety analysis for the first time.

---

## 🗺️ Dependencies

### Runtime
- **Node.js** v14+ (built-in `http`, `fs`, `path` modules)

### Frontend (CDN)
- **Leaflet.js** v1.9.4 - Interactive maps
  - https://unpkg.com/leaflet@1.9.4/dist/leaflet.css
  - https://unpkg.com/leaflet@1.9.4/dist/leaflet.js

### Map Tiles
- **CartoDB Dark Matter** basemap
  - https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png

### Python Libraries
```bash
pandas      # Data manipulation
numpy       # Numerical operations
shapely     # Geospatial analysis
scikit-learn # ML models (optional)
lzma        # Decompress .xz files
```

## 🚧 Next Steps

- [ ] Implement A* pathfinding algorithm
- [ ] Add start/end point selection UI
- [ ] Calculate and display safest route
- [ ] Compare safe route vs shortest route
- [ ] Add route distance/time estimates
- [ ] Train ML model for dynamic weight updates
- [ ] Add real-time crime data integration

## 📝 License

MIT License - Toronto Open Data is licensed under the Open Government Licence - Toronto

## 🙏 Acknowledgments

- **Toronto Open Data** - Crime statistics
- **OpenStreetMap** contributors - Street network data
- **CartoDB** - Dark Matter basemap tiles
- **Leaflet.js** - Open-source mapping library
