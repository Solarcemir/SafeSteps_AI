# SafeRoute AI - Toronto Risk Map

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Node.js](https://img.shields.io/badge/Node.js-v14+-green.svg)](https://nodejs.org/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Leaflet](https://img.shields.io/badge/Leaflet-1.9.4-green.svg)](https://leafletjs.com/)

**AI-powered safe route navigation system** using real Toronto crime data, live incident monitoring, OpenStreetMap infrastructure, and intelligent weight calculation for risk-aware pathfinding.

---

## 📋 Table of Contents

- [Quick Start](#-quick-start)
- [Project Overview](#-project-overview)
- [Features](#-features)
- [Demo](#-demo)
- [How It Works](#-how-it-works)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Technical Details](#-technical-details)
- [API Configuration](#-api-configuration)
- [Troubleshooting](#-troubleshooting)
- [FAQ](#-frequently-asked-questions-faq)
- [Future Roadmap](#-future-roadmap)
- [Tech Stack](#-tech-stack)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🚀 Quick Start

Get up and running in 3 minutes:

```bash
# 1. Clone the repository
git clone https://github.com/Solarcemir/SafeSteps_AI.git
cd SafeSteps_AI

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. (Optional) Set up Gemini API key for live crime monitoring
echo "GEMINI_API_KEY=your_api_key_here" > .env

# 4. Start the server
node server.js

# 5. Open your browser
# Navigate to http://localhost:3000
```

**That's it!** The map will load with historical crime data. Click "🤖 Fetch Live Crime Data" to see real-time incidents (requires API key).

---

## 🎯 Project Overview

SafeRoute AI is a comprehensive urban safety navigation system that analyzes Toronto's downtown area to create a **weighted routing graph** enabling safe path calculation between any two points. The system combines historical crime statistics, real-time incident monitoring, and advanced geospatial analysis to provide users with actionable safety intelligence.

### Key Capabilities:
- 🗺️ **Interactive Risk Visualization**: Dark-themed map with color-coded streets (🟢 safe → 🔴 dangerous)
- 🤖 **AI-Powered Live Incident Monitoring**: Gemini AI integration for real-time crime data analysis
- 📊 **Weighted Routing Graph**: 11,495 intersection nodes + 13,195 street edges with safety scores
- 🧠 **Smart Multi-Factor Analysis**: Crime rates, POI density, street characteristics, and intersection complexity
- 📍 **Real Toronto Data**: Crime rates from 2024 across 158 neighborhoods + live incident tracking
- 🚨 **Dynamic Danger Zones**: 100m radius circles around active incidents with detailed descriptions
- 🎯 **Ready for Pathfinding**: Complete graph structure for A* or Dijkstra safe routing algorithms

---

## 🚀 Features

### 1. **Historical Crime Analysis**
- Processes 158 Toronto neighborhoods with normalized crime rates (per capita)
- Analyzes 9 crime types: Homicide, Shooting, Robbery, Assault, Break & Enter, Auto Theft, Theft from MV, Theft Over, Bike Theft
- Severity-weighted scoring system prioritizing violent crimes
- Color-coded visualization: green (safe) → yellow → orange → red (dangerous)

### 2. **Live Crime Incident Monitoring** 🆕
- **AI-Powered Analysis**: Gemini 2.0 Flash integration for intelligent crime data extraction
- **Real-Time Updates**: Fetches latest incidents from Toronto crime feeds
- **Automatic Geocoding**: Converts location descriptions to precise GPS coordinates
- **Detailed Descriptions**: News-style summaries with location, type, severity, and full incident details
- **Visual Alerts**: Red danger zone circles (100m radius) with pulsing markers
- **Smart Popup Interface**: Consolidated view of all active incidents with severity indicators

### 3. **Intelligent Weight System**
Each street intersection receives a 0-100 safety score based on:
- **Crime Risk** (40%): Neighborhood crime statistics normalized by population
- **POI Density** (20%): Nearby bars, nightlife, and high-activity venues
- **Street Importance** (20%): Road type classification (highway vs residential)
- **Intersection Complexity** (20%): Number of converging streets (traffic exposure)

### 4. **Advanced Geospatial Analysis**
- **Point-in-Polygon Spatial Joins**: Maps street intersections to neighborhood crime zones
- **Coordinate System Accuracy**: WGS84 (EPSG:4326) with 6-decimal precision (~10cm accuracy)
- **Spatial Indexing**: Optimized POI lookups within 100m radius
- **Boundary Visualization**: 158 neighborhood polygons rendered as GeoJSON layers

### 5. **Interactive Web Interface**
- **Dark Theme Map**: Optimized for nighttime use with CartoDB Dark Matter tiles
- **Responsive Controls**: Easy layer toggling, route planning, and event reporting
- **Real-Time Updates**: Dynamic incident markers and danger zones
- **Detailed Popups**: Click any street or incident for comprehensive information

---

## 🎬 Demo

### What You'll See

When you first load SafeRoute AI at `http://localhost:3000`:

#### Main Map View
- **Dark-themed interactive map** centered on downtown Toronto
- **Color-coded streets** showing safety levels:
  - 🟢 **Green streets**: Safe areas (low crime) - e.g., residential neighborhoods
  - 🟡 **Yellow streets**: Moderate risk - mixed commercial/residential
  - 🟠 **Orange streets**: High risk - busy entertainment districts
  - 🔴 **Red streets**: Critical risk - areas with high crime rates
- **158 neighborhood boundaries** as transparent overlays
- **Control panel** on the left with layer toggles and features

#### Live Incident Demo
1. Click "🤖 Fetch Live Crime Data" button
2. Status message shows "Analyzing crime feeds with AI..."
3. After ~10 seconds, the map updates with:
   - **Red circular markers** at incident locations
   - **100m danger zone circles** around each incident
   - **Consolidated popup** listing all incidents by severity
4. Click individual markers to see:
   - Exact location (street intersection)
   - Crime type (shooting, robbery, assault, etc.)
   - Severity rating (60-95%)
   - Detailed 2-3 sentence description
   - Timestamp

#### Example Live Incidents (Real Data)
- **King St W & Spadina Ave**: Shooting incident, severity 95%
- **Yonge & Dundas Square**: Armed robbery, severity 80%
- **Front St & Jarvis St**: Aggravated assault, severity 75%

#### Interactive Features Demo
- **Click any street**: Popup shows weight, name, length, risk category
- **Zoom in/out**: Streets remain visible and color-coded at all zoom levels
- **Change crime filter**: Switch between "All Crimes", "Violent Crimes", "Property Crimes", etc.
- **Plan route** (coming soon): Click two points to see safest vs shortest path

### Screenshots

*Note: Screenshots would be displayed here showing:*
1. Main map with color-coded streets
2. Live incident markers with danger zones
3. Detailed popup for a crime incident
4. Control panel with all options
5. Route planning interface

### Data Visualization

The map displays **13,195 street segments** color-coded by safety score:

| Color | Weight Range | Count | % of Total | Example Areas |
|-------|--------------|-------|-----------|---------------|
| 🟢 Green | 0-30 | 9,571 | 72.5% | Residential neighborhoods, quiet streets |
| 🟡 Yellow | 30-60 | 3,614 | 27.4% | Mixed commercial/residential areas |
| 🟠 Orange | 60-80 | 9 | 0.07% | Entertainment districts, busy intersections |
| 🔴 Red | 80-100 | 1 | 0.01% | Yonge-Dundas area, high-crime zones |

**Key Insights:**
- **72.5%** of downtown Toronto streets are classified as "safe"
- Only **0.1%** of streets have critical risk levels
- Entertainment districts and major intersections tend to have higher weights
- Residential side streets consistently show low risk scores

---

## 🎯 Usage

Once the server is running at `http://localhost:3000`, you can:

### Basic Features

#### 1. **Explore the Crime Heat Map**
- **Pan/Zoom:** Click and drag to move around Toronto, scroll to zoom
- **Street Colors:** 
  - 🟢 **Green** = Safe streets (low crime rate)
  - 🟡 **Yellow** = Medium risk
  - 🟠 **Orange** = High risk
  - 🔴 **Red** = Critical risk (high crime area)
- **Click any street** to see:
  - Weight value (safety score)
  - Street name and type
  - Length in meters
  - Risk category

#### 2. **View Crime Data Layers**
Use the layer selector to focus on specific crime types:
- 🎯 **All Crimes (Weighted)** - Shows overall safety based on all crime types
- ⚠️ **Violent Crimes** - Focuses on assault, robbery, shooting, homicide
- 🏠 **Property Crimes** - Shows break & enter patterns
- 👤 **Personal Safety** - Assault and robbery data
- 🚗 **Vehicle Safety** - Auto theft zones
- 🚲 **Bike Safety** - Bicycle theft hotspots
- 🔴 **Critical** - Homicide and shooting incidents only

#### 3. **Fetch Live Crime Incidents** (Requires API Key)
1. Click the "🤖 Fetch Live Crime Data" button
2. Wait ~10 seconds while AI processes latest crime reports
3. View results:
   - **Red markers** appear at incident locations
   - **Danger zones** (100m radius circles) show impact area
   - **Consolidated popup** displays all active incidents
4. Click individual markers for detailed information:
   - Exact location and intersection
   - Crime type and severity (%)
   - Detailed description of what happened
   - Time of incident

#### 4. **Plan Safe Routes** (Future Feature)
1. Click "🗺️ Plan Safe Route" button
2. Click on map to set:
   - First click = **Start point (A)**
   - Second click = **End point (B)**
3. View route comparison:
   - Safest route (green) - Avoids high-risk areas
   - Shortest route (blue) - Direct path
   - Statistics showing distance, time, safety score

#### 5. **Report Crime Events** (Manual Markers)
1. Click "🚨 Report Crime Event" button
2. Select crime type from dropdown
3. Click on map to place marker
4. View all reported events
5. Clear events with "🗑️ Clear All Events" button

### Advanced Features

#### View Street Network Details
Click "🔍 Show Street Network" to see:
- All intersection nodes (11,495 points)
- Street edges (13,195 connections)
- Weight distribution across the network

#### Toggle Layers
Use checkboxes to show/hide:
- Crime data boundaries (158 neighborhoods)
- Street network overlay
- Live incident markers

---

## 📊 How It Works

### 1. **Crime Risk Calculation**
Uses **crime RATES** (normalized by population) from Toronto Open Data:

```python
# Crime type weights (based on severity)
CRIME_WEIGHTS = {
    'HOMICIDE': 10.0,    # Most severe
    'SHOOTING': 10.0,
    'ROBBERY': 5.0,
    'ASSAULT': 3.0,
    'BREAK_AND_ENTER': 2.0,
    'AUTO_THEFT': 2.0,
    'THEFT_FROM_MV': 1.0,
    'THEFT_OVER': 1.0,
    'BIKE_THEFT': 1.0
}

# Calculate neighborhood risk score
risk_score = Σ(crime_rate × weight) for all crime types
risk_normalized = (risk - min) / (max - min)  # Normalize to 0-1
```

**Example Results:**
- **Highest Risk**: West Humber-Clairville (normalized: 1.0)
- **Lowest Risk**: Lambton Baby Point (normalized: 0.0)

### 2. **Live Incident Processing Pipeline** 🆕

```
1. Data Fetching
   ↓
   Scrape Toronto crime feeds (gtaupdate.com, police reports)
   
2. AI Analysis (Gemini 2.0 Flash)
   ↓
   Extract structured data:
   - Location (street intersections, districts)
   - Crime type (shooting, robbery, assault, etc.)
   - Severity (1-100 scale)
   - Detailed description (2-3 sentence summary)
   
3. Geocoding
   ↓
   Convert locations to GPS coordinates:
   - Toronto Fire Service (TFS) district mapping
   - Nominatim OpenStreetMap API
   - Custom coordinate database
   
4. Visualization
   ↓
   Create map elements:
   - Red circular markers (20px, white border, pulsing shadow)
   - Danger zone circles (100m radius, 20% opacity)
   - Detailed popups (location, description, severity table)
   
5. User Interface
   ↓
   Display consolidated popup:
   - All incidents sorted by severity
   - Color-coded borders (red > 80%, orange 70-80%, yellow < 70%)
   - Timestamp and data source attribution
```

### 3. **Intersection (Node) Weight Calculation**

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
SafeSteps_AI/
│
├── Frontend (Web Interface)
│   ├── index.html                     # Main web interface with map and controls
│   ├── app.js                         # Leaflet map + visualization logic (2161 lines)
│   ├── pathfinding.js                 # A* routing algorithm implementation
│   ├── style.css                      # Dark theme styling
│   ├── chat.html                      # AI chat interface for safety queries
│   └── chat.js                        # Chat functionality
│
├── Backend (Server)
│   ├── server.js                      # Node.js HTTP server + API endpoints
│   └── package.json                   # Node.js project configuration
│
├── Data Processing Scripts (Python)
│   ├── process_downtown_osm.py        # Extract streets/POIs from OpenStreetMap data
│   ├── calculate_intersection_weights.py  # Calculate node weights with crime data
│   ├── create_routing_graph.py        # Build complete routing graph structure
│   ├── fetch_live_crimes.py           # Scrape and process live crime incidents
│   ├── gemini_api.py                  # Gemini AI integration for chat feature
│   ├── analyze_layers.py              # Analyze data layers and distributions
│   ├── check_nodes.py                 # Validate node data
│   └── explain_rates.py               # Crime rate calculation explanations
│
├── Data Files
│   ├── Crime Data
│   │   ├── Neighbourhood_Crime_Rates_Open_Data_*.csv      # 158 neighborhoods, 9 crime types
│   │   └── Neighbourhood_Crime_Rates_Open_Data_*.geojson  # Neighborhood boundary polygons
│   │
│   ├── OpenStreetMap Data
│   │   ├── planet_*.osm.geojson.xz    # Compressed OSM extract for Toronto
│   │   ├── downtown_streets.geojson   # 22,448 street segments (processed)
│   │   └── downtown_pois.geojson      # 19,487 points of interest (bars, shops, etc.)
│   │
│   └── Routing Graph Data
│       ├── intersection_weights.csv        # 11,495 nodes with computed weights
│       ├── intersection_weights.geojson    # Nodes in GeoJSON for visualization
│       ├── routing_edges.csv               # 13,195 street edges with weights
│       ├── routing_edges.geojson           # Edges in GeoJSON for visualization
│       └── routing_graph.json              # Complete graph structure (9.8 MB)
│
├── Configuration
│   ├── requirements.txt               # Python dependencies
│   ├── .env                          # API keys (not in git, create locally)
│   └── .gitignore                    # Git ignore rules
│
├── Documentation
│   ├── README.md                     # This file
│   └── test.ipynb                    # Jupyter notebook for testing/analysis
│
└── Cache
    └── __pycache__/                  # Python bytecode cache (auto-generated)
```

### Key Files Explained

#### Frontend Files
- **index.html** (140 lines): Main interface with map container, control panel, and UI elements
- **app.js** (2161 lines): Core application logic including:
  - Leaflet map initialization
  - GeoJSON layer loading and rendering
  - Color-coding algorithm for streets
  - Event handlers for user interactions
  - Live crime data fetching and display
  - Route planning interface (in progress)
- **style.css**: Dark theme optimized for nighttime use with high contrast

#### Backend Files
- **server.js** (161 lines): Simple Node.js HTTP server that:
  - Serves static files (HTML, JS, CSS)
  - Provides `/fetch-live-crimes` API endpoint
  - Handles `/chat` endpoint for AI safety queries
  - Returns JSON and GeoJSON data

#### Data Processing Pipeline
The Python scripts follow this workflow:

```
1. process_downtown_osm.py
   └─→ Extracts streets and POIs from OSM
       └─→ Outputs: downtown_streets.geojson, downtown_pois.geojson

2. calculate_intersection_weights.py
   └─→ Computes safety weights for each intersection
       └─→ Uses: Crime data + POIs + street types
       └─→ Outputs: intersection_weights.csv, intersection_weights.geojson

3. create_routing_graph.py
   └─→ Builds complete routing graph
       └─→ Connects intersections with edges
       └─→ Outputs: routing_graph.json, routing_edges.csv

4. fetch_live_crimes.py (runs on-demand)
   └─→ Scrapes live crime feeds
       └─→ Uses Gemini AI to extract structured data
       └─→ Geocodes locations
       └─→ Returns JSON to frontend
```

### Data Flow

```
User Browser (index.html)
    ↓
    ├─→ Loads routing_edges.geojson (street visualization)
    ├─→ Loads Neighbourhood_Crime_Rates.geojson (boundaries)
    ├─→ Loads routing_graph.json (for pathfinding)
    │
    └─→ Clicks "Fetch Live Crime Data"
         ↓
      server.js (/fetch-live-crimes endpoint)
         ↓
      fetch_live_crimes.py
         ├─→ Scrapes gtaupdate.com
         ├─→ Calls Gemini AI API
         └─→ Returns structured JSON
              ↓
         app.js displays incidents on map
```

## 💻 Installation

### Prerequisites
- **Node.js** v14+ (JavaScript runtime) - [Download here](https://nodejs.org/)
- **Python** 3.8+ (for data processing) - [Download here](https://www.python.org/)
- **Git** (for cloning the repository)

### Step-by-Step Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/Solarcemir/SafeSteps_AI.git
cd SafeSteps_AI
```

#### 2. Install Python Dependencies
```bash
# Using pip
pip install -r requirements.txt

# Or install packages individually
pip install pandas numpy shapely scikit-learn beautifulsoup4 requests google-generativeai python-dotenv playwright
```

#### 3. (Optional) Set up Gemini API Key
For live crime monitoring features, you'll need a Google Gemini API key:

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Create a `.env` file in the project root:
```bash
echo "GEMINI_API_KEY=your_api_key_here" > .env
```

**Note:** The app works without an API key using historical data. Live crime monitoring requires the API key.

#### 4. Install Playwright (if using live crime monitoring)
```bash
playwright install
```

#### 5. Start the Server
```bash
node server.js
```

You should see:
```
🚀 Server running at http://localhost:3000/
📍 SafeRoute AI - Toronto Risk Map
Press Ctrl+C to stop the server
```

#### 6. Open Your Browser
Navigate to **http://localhost:3000**

The map will load with Toronto crime data visualized on the street network!

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

### Data Files Included

The repository includes pre-processed data files totaling ~50MB:

| File | Size | Description |
|------|------|-------------|
| `routing_graph.json` | 5.4 MB | Complete graph structure with nodes, edges, weights |
| `routing_edges.geojson` | 4.7 MB | Visualizable street edges with safety colors |
| `intersection_weights.geojson` | 6.6 MB | All 11,495 intersections with computed weights |
| `downtown_streets.geojson` | 15 MB | Raw street network (22,448 segments) |
| `downtown_pois.geojson` | 11 MB | Points of interest (19,487 locations) |
| `Neighbourhood_Crime_Rates.geojson` | 2.5 MB | 158 neighborhood boundaries |
| `Neighbourhood_Crime_Rates.csv` | 285 KB | Crime statistics by neighborhood (2024) |
| `intersection_weights.csv` | 2.2 MB | Node weights in CSV format |
| `routing_edges.csv` | 1.1 MB | Edge weights in CSV format |

**Total Data Size**: ~49 MB (pre-processed, ready to use)

**Note**: The original OSM extract (`planet_*.osm.geojson.xz`) is compressed and not required for running the application.

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

5. **Live Crime Integration** 🚨
   - Gemini AI analyzes real-time Toronto crime feeds
   - Extracts location, type, severity from news-style reports
   - Geocodes to precise GPS coordinates
   - Creates 100m danger zones on map
   - Consolidated popup shows all active incidents
   
6. **Final Result: Every Street Has a Safety Score** 🎯
   - Yonge & Dundas: Weight 84 (High Crime area + 73 bars nearby + busy 4-way) = 🔴 Red
   - Quiet Riverdale street: Weight 12 (Low Crime area + 0 bars + simple 2-way) = 🟢 Green
   - Live incidents: Red markers with 100m radius danger circles

### **Why This Matters**

- **Accurate**: Uses real Toronto crime statistics (2024 data) + live incident monitoring
- **Precise**: Down to individual street corners, not just neighborhoods
- **Smart**: Considers multiple safety factors + AI-powered analysis
- **Visual**: Color-coded map shows safe (green) vs dangerous (red) streets
- **Real-Time**: Fresh incidents with detailed descriptions and severity ratings
- **Actionable**: Powers safe route navigation - avoid red zones, prefer green streets

### **The Technical Win**

We bridged three incompatible data sources:
- **Crime data**: Area-level (neighborhoods)
- **Street data**: Point-level (GPS coordinates)
- **Live incidents**: Text descriptions → structured data

Using proven geospatial algorithms and cutting-edge AI, we accurately mapped area statistics to individual locations and integrated real-time monitoring - enabling comprehensive street-by-street safety analysis.

---

## 💻 Tech Stack

### **Frontend**
- **JavaScript (ES6+)**: Core application logic and map interactions
- **Leaflet.js v1.9.4**: Interactive map rendering and layer management
- **HTML5/CSS3**: Responsive UI with dark theme styling
- **Fetch API**: Asynchronous data loading

### **Backend**
- **Node.js**: HTTP server for static files and API endpoints
- **Python 3.x**: Data processing pipeline and AI integration

### **AI & Data Processing**
- **Google Gemini 2.0 Flash**: Natural language processing for crime incident extraction
- **Beautiful Soup 4**: Web scraping for live crime feeds
- **Pandas**: Data manipulation and statistical analysis
- **NumPy**: Numerical computing for weight calculations
- **Shapely**: Computational geometry and spatial operations

### **Geospatial**
- **OpenStreetMap (OSM)**: Street network data (11,495 nodes, 13,195 edges)
- **Nominatim API**: Geocoding and reverse geocoding
- **GeoJSON**: Standard format for crime boundaries and routing graph
- **WGS84 (EPSG:4326)**: Coordinate reference system

### **Data Sources**
- **Toronto Open Data**: 2024 crime statistics (158 neighborhoods, 9 crime types)
- **Live Crime Feeds**: Real-time incident monitoring
- **Toronto Fire Service (TFS)**: District coordinate mapping

### **Map Visualization**
- **CartoDB Dark Matter**: Basemap tiles for night-mode aesthetic
- **Custom Markers**: SVG-based crime incident indicators
- **Dynamic Layers**: Crime boundaries, routing edges, danger zones

---

## 🔑 API Configuration

### Google Gemini API Setup

The live crime monitoring feature uses Google's Gemini AI to analyze real-time crime feeds. Here's how to set it up:

#### 1. Get Your API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated key

#### 2. Configure the Application
Create a `.env` file in the project root directory:

```bash
# .env file
GEMINI_API_KEY=your_actual_api_key_here
```

**Security Note:** Never commit the `.env` file to git. It's already included in `.gitignore`.

#### 3. Verify Configuration
The application will automatically load the API key from the `.env` file. If configured correctly:
- Click "🤖 Fetch Live Crime Data" button
- Wait ~10 seconds for AI processing
- Live incidents will appear on the map

#### Without API Key
The application works fully without an API key:
- ✅ Historical crime data visualization
- ✅ Street network with safety weights
- ✅ Route planning (when implemented)
- ❌ Live crime incident monitoring (requires API key)

---

## 🔧 Troubleshooting

### Common Issues

#### 1. Server won't start - "Cannot find module"
**Problem:** Node.js can't find required files.

**Solution:**
```bash
# Make sure you're in the correct directory
cd SafeSteps_AI
ls -la  # Should see server.js, index.html, etc.
node server.js
```

#### 2. Python errors - "Module not found"
**Problem:** Python dependencies not installed.

**Solution:**
```bash
# Install all dependencies
pip install -r requirements.txt

# Or install missing package individually
pip install pandas  # Replace with missing package name
```

#### 3. Map doesn't load - Blank screen
**Problem:** Browser can't access static files or data files are missing.

**Solution:**
- Check browser console (F12) for errors
- Verify all `.geojson` and `.json` files are present
- Try refreshing the page (Ctrl+F5)
- Check server logs for 404 errors

#### 4. Live crime data fails - "Failed to fetch incidents"
**Problem:** API key not configured or invalid.

**Solution:**
```bash
# Verify .env file exists
cat .env

# Should show: GEMINI_API_KEY=your_key_here

# Make sure there are no spaces around the = sign
# Correct:   GEMINI_API_KEY=abc123
# Incorrect: GEMINI_API_KEY = abc123
```

#### 5. Port 3000 already in use
**Problem:** Another application is using port 3000.

**Solution:**
```bash
# Option 1: Kill the process using port 3000 (Linux/Mac)
lsof -ti:3000 | xargs kill -9

# Option 2: Use a different port
# Edit server.js, change PORT = 3000 to PORT = 3001
```

#### 6. Playwright installation fails
**Problem:** Playwright browsers not installed.

**Solution:**
```bash
# Install Playwright and browsers
pip install playwright
playwright install

# Or install specific browser
playwright install chromium
```

#### 7. CORS errors in browser console
**Problem:** Browser blocking requests due to CORS policy.

**Solution:** This shouldn't happen with the included server. If it does:
- Make sure you're accessing `http://localhost:3000` (not opening `index.html` directly)
- Check that server.js is running
- Clear browser cache

### Need More Help?

If you encounter other issues:
1. Check the [GitHub Issues](https://github.com/Solarcemir/SafeSteps_AI/issues) page
2. Create a new issue with:
   - Error message (full text)
   - Operating system
   - Node.js version (`node --version`)
   - Python version (`python --version`)
   - Steps to reproduce

---

## 📊 Data Pipeline

### **1. Historical Crime Processing** (Python)

**Input Files:**
- `Neighbourhood_Crime_Rates_Open_Data.csv` - Crime statistics
- `Neighbourhood_Crime_Rates_Open_Data.geojson` - Neighborhood boundaries
- Toronto OSM extract (street network XML)

**Output Files:**
- `routing_graph.json` - 11,495 nodes with safety weights (9.8 MB)
- `routing_edges.geojson` - 13,195 edges for visualization (15 MB)

### **2. Live Crime Monitoring** (Python + Node.js)

```bash
# Server endpoint: GET /fetch-live-crimes
# Returns JSON with live incidents
```

**Pipeline:**
1. Scrape Toronto crime feeds
2. Gemini AI extracts structured data
3. Geocode locations to GPS coordinates
4. Return JSON to frontend
5. Frontend creates markers and danger zones

**Output Format:**
```json
{
  "success": true,
  "events": [
    {
      "lat": 43.6532,
      "lon": -79.3832,
      "type": "shooting",
      "impact": 95,
      "location": "King St W & Spadina Ave",
      "description": "Detailed incident description..."
    }
  ],
  "timestamp": "2024-11-23T12:34:56Z"
}
```

---

## 🗺️ Project Structure

```
Sheridan_Datathon/
│
├── index.html                 # Main web interface
├── style.css                  # Dark theme styling
├── app.js                     # Frontend logic (2100+ lines)
├── server.js                  # Node.js HTTP server
│
├── routing_graph.json         # 11,495 nodes with safety weights (9.8 MB)
├── routing_edges.geojson      # 13,195 edges for visualization (15 MB)
├── Neighbourhood_Crime_Rates_*.csv     # Crime statistics
├── Neighbourhood_Crime_Rates_*.geojson # Boundaries
│
├── fetch_live_crimes.py       # AI-powered live crime fetching
├── gemini_api.py             # Gemini AI integration
├── .env                       # API keys (not committed)
│
└── README.md                  # This file
```

---

## 🎯 Future Roadmap

### **Phase 1: Smart Routing** (Next Sprint)
- [ ] Implement A* pathfinding with safety weights
- [ ] Drag-and-drop start/end point selection
- [ ] Display safest route vs shortest route comparison
- [ ] Show route statistics (distance, time, safety score)
- [ ] Turn-by-turn navigation with safety alerts

### **Phase 2: Advanced AI** (Q1 2025)
- [ ] Train ML models to predict crime hotspots by time of day
- [ ] Dynamic weight adjustments based on real-time patterns
- [ ] Sentiment analysis of crime descriptions
- [ ] Integration with police dispatch data
- [ ] Predictive risk modeling using historical trends

### **Phase 3: Mobile App** (Q2 2025)
- [ ] Native iOS/Android apps
- [ ] GPS tracking with real-time rerouting
- [ ] Push notifications for nearby incidents
- [ ] Voice-guided safe navigation
- [ ] Community reporting features
- [ ] Offline mode with cached data

### **Phase 4: Scale to Other Cities** (Q3 2025)
- [ ] Template system for any city with open crime data
- [ ] Automated data pipeline for municipal integration
- [ ] Multi-city comparison and benchmarking
- [ ] Public API for researchers and civic tech developers

### **Phase 5: Social Impact** (Ongoing)
- [ ] Partner with local police departments
- [ ] Community safety workshops
- [ ] Academic research collaborations
- [ ] Open-source toolkit for developers

---

## 🏆 Achievements

✅ Built complete end-to-end system in 48 hours  
✅ Processed 158 neighborhoods, 11,495 intersections, 9 crime types  
✅ Integrated cutting-edge AI (Gemini 2.0 Flash) for live monitoring  
✅ Achieved 6-decimal GPS precision (~10cm accuracy)  
✅ Created intuitive dark-themed UI optimized for night safety  
✅ Generated production-ready weighted graph for pathfinding  
✅ Implemented robust fallback systems for API reliability  

---

## ❓ Frequently Asked Questions (FAQ)

### General Questions

**Q: Do I need an API key to use SafeRoute AI?**
A: No! The application works fully without an API key using historical crime data. The Gemini API key is only required for the live crime monitoring feature (the "🤖 Fetch Live Crime Data" button).

**Q: Is the crime data real?**
A: Yes! We use official Toronto Open Data crime statistics from 2024 for 158 neighborhoods. The live incident monitoring (when API key is configured) pulls real-time data from Toronto crime feeds.

**Q: How accurate are the safety scores?**
A: Safety scores are calculated using official crime RATES (normalized by population) with a multi-factor algorithm. They represent relative risk, not absolute danger. Always use common sense and local knowledge.

**Q: Can I use this for route navigation?**
A: The pathfinding feature is currently in development. The graph structure is complete and ready for A* algorithm implementation. For now, you can visualize safety scores and manually plan routes.

**Q: Does this work for areas outside downtown Toronto?**
A: Currently optimized for downtown Toronto (43.629°N to 43.675°N). The methodology can be adapted to any city with open crime data and OpenStreetMap coverage.

### Technical Questions

**Q: Why do some streets have different colors on each side?**
A: Streets are segments (edges) connecting intersections (nodes). Each intersection has its own safety weight. The street's color is the average of its two endpoints, so adjacent streets may differ.

**Q: What does "weight" mean?**
A: Weight is a 0-100 safety score for each intersection, where:
- **0-30**: Safe (low crime, quiet area)
- **30-60**: Moderate risk (mixed area)
- **60-100**: High risk (high crime, busy area)

**Q: How often is the data updated?**
A: Historical crime data is updated when Toronto Open Data releases new statistics (typically quarterly). Live incident monitoring fetches real-time data when you click the button.

**Q: Can I add my own crime data?**
A: Yes! The system accepts standard CSV files with crime rates by neighborhood. You'll need to modify `calculate_intersection_weights.py` to process your data format.

**Q: What's the difference between "crime count" and "crime rate"?**
A: We use crime RATES (crimes per 100,000 residents), not raw counts. This accounts for population differences—a neighborhood with 100 crimes and 1,000 residents is more dangerous than one with 100 crimes and 100,000 residents.

### Usage Questions

**Q: The map is loading slowly. What can I do?**
A: The initial load processes ~50MB of geospatial data. Tips:
- Use a modern browser (Chrome, Firefox, Edge)
- Disable browser extensions temporarily
- Clear browser cache
- Check your internet connection (map tiles load from CDN)

**Q: Can I download the map for offline use?**
A: The data files can work offline, but map tiles require internet. You could set up a local tile server for fully offline operation.

**Q: How do I report incorrect data?**
A: Open an issue on [GitHub Issues](https://github.com/Solarcemir/SafeSteps_AI/issues) with:
- Location (intersection or street name)
- What's incorrect (weight, crime data, etc.)
- Expected vs actual values

**Q: Can I use this data for research?**
A: Yes! The MIT license allows academic and commercial use. Please cite the project and acknowledge Toronto Open Data as the crime data source.

### Privacy & Safety Questions

**Q: Does this app track my location?**
A: No. SafeRoute AI runs entirely in your browser. We don't collect, store, or transmit any user data, including location.

**Q: Is my API key secure?**
A: Your Gemini API key is stored in the `.env` file on your local machine. It's never transmitted to anyone except Google's Gemini API. Never share your `.env` file or commit it to git.

**Q: Should I rely on this for personal safety decisions?**
A: SafeRoute AI is a visualization and research tool. It provides data-driven insights but should not be your only source of safety information. Always:
- Use common sense and situational awareness
- Follow local police recommendations
- Trust your instincts
- Consider time of day and other factors

---

## 🤝 Contributing

We welcome contributions to SafeRoute AI! Here's how you can help:

### Ways to Contribute

1. **Report Bugs**
   - Use the [GitHub Issues](https://github.com/Solarcemir/SafeSteps_AI/issues) page
   - Provide detailed description and steps to reproduce
   - Include system information and error messages

2. **Suggest Features**
   - Open an issue with the "enhancement" label
   - Describe the feature and its benefits
   - Explain use cases

3. **Improve Documentation**
   - Fix typos or unclear instructions
   - Add examples or tutorials
   - Translate documentation

4. **Submit Code**
   - Fork the repository
   - Create a feature branch (`git checkout -b feature/AmazingFeature`)
   - Make your changes
   - Test thoroughly
   - Commit with clear messages (`git commit -m 'Add AmazingFeature'`)
   - Push to your branch (`git push origin feature/AmazingFeature`)
   - Open a Pull Request

### Development Guidelines

#### Code Style
- **Python**: Follow PEP 8 style guide
- **JavaScript**: Use ES6+ features, meaningful variable names
- **Comments**: Explain "why", not "what"

#### Testing
- Test your changes locally before submitting
- Ensure existing features still work
- Add tests for new features when possible

#### Commit Messages
- Use clear, descriptive commit messages
- Start with a verb (Add, Fix, Update, Remove)
- Example: "Add geocoding fallback for missing locations"

### Development Setup

```bash
# 1. Fork and clone your fork
git clone https://github.com/YOUR_USERNAME/SafeSteps_AI.git
cd SafeSteps_AI

# 2. Create a new branch
git checkout -b feature/my-new-feature

# 3. Make changes and test
node server.js  # Test the application

# 4. Commit and push
git add .
git commit -m "Add my new feature"
git push origin feature/my-new-feature

# 5. Open a Pull Request on GitHub
```

### Areas Needing Contribution

- [ ] Implement A* pathfinding algorithm for route calculation
- [ ] Add mobile-responsive design
- [ ] Create unit tests for Python data processing
- [ ] Optimize map rendering for better performance
- [ ] Add more crime data sources
- [ ] Implement real-time traffic integration
- [ ] Create REST API for external applications
- [ ] Add multilingual support (French, Spanish, etc.)

### Questions?

Feel free to open an issue for questions or join our discussions!

---

## 📝 License

MIT License - Toronto Open Data is licensed under the Open Government Licence - Toronto

## 🙏 Acknowledgments

- **Toronto Open Data** - Crime statistics and neighborhood boundaries
- **OpenStreetMap** contributors - Street network data
- **Google Gemini AI** - Natural language processing
- **CartoDB** - Dark Matter basemap tiles
- **Leaflet.js** - Open-source mapping library
