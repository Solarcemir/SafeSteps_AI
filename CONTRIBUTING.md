# Contributing to SafeRoute AI

Thank you for your interest in contributing to SafeRoute AI! We welcome contributions from the community.

## 🤝 Ways to Contribute

### 1. Report Bugs
- Use the [GitHub Issues](https://github.com/Solarcemir/SafeSteps_AI/issues) page
- Provide detailed description and steps to reproduce
- Include system information and error messages

### 2. Suggest Features
- Open an issue with the "enhancement" label
- Describe the feature and its benefits
- Explain use cases

### 3. Improve Documentation
- Fix typos or unclear instructions
- Add examples or tutorials
- Translate documentation

### 4. Submit Code
Follow the process below for code contributions.

## 🚀 Getting Started

### Fork and Clone
```bash
# 1. Fork the repository on GitHub
# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/SafeSteps_AI.git
cd SafeSteps_AI

# 3. Add upstream remote
git remote add upstream https://github.com/Solarcemir/SafeSteps_AI.git
```

### Create a Branch
```bash
# Create a feature branch
git checkout -b feature/AmazingFeature

# Or a bugfix branch
git checkout -b bugfix/FixSomething
```

## 💻 Development Guidelines

### Code Style

#### Python
- Follow [PEP 8](https://pep8.org/) style guide
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep functions focused and small

```python
# Good
def calculate_safety_score(crime_rate, poi_density, street_type):
    """
    Calculate safety score for an intersection.
    
    Args:
        crime_rate (float): Normalized crime rate (0-1)
        poi_density (float): Nearby POI count normalized (0-1)
        street_type (str): Type of street (highway, residential, etc.)
    
    Returns:
        float: Safety score (0-100)
    """
    # Implementation
    pass

# Avoid
def calc(a, b, c):  # Unclear names, no documentation
    return a * 0.4 + b * 0.2 + c * 0.2
```

#### JavaScript
- Use ES6+ features (const/let, arrow functions, etc.)
- Use meaningful variable names
- Add comments for complex logic
- Keep functions focused and small

```javascript
// Good
const calculateRouteDistance = (coordinates) => {
    // Calculate total distance from coordinate array
    return coordinates.reduce((total, coord, i) => {
        if (i === 0) return 0;
        return total + getDistance(coordinates[i-1], coord);
    }, 0);
};

// Avoid
function calc(c) {  // Unclear name
    var t = 0;  // Use const/let
    for (var i = 1; i < c.length; i++) {
        t = t + d(c[i-1], c[i]);
    }
    return t;
}
```

### Testing
- Test your changes locally before submitting
- Ensure existing features still work
- Add tests for new features when possible

```bash
# Test the server
node server.js

# Test Python scripts
python calculate_intersection_weights.py

# Check for Python errors
python -m py_compile script_name.py
```

### Commit Messages
Use clear, descriptive commit messages:

```bash
# Good
git commit -m "Add geocoding fallback for missing locations"
git commit -m "Fix crash when crime data is missing"
git commit -m "Update README installation instructions"

# Avoid
git commit -m "fix"
git commit -m "updates"
git commit -m "changes"
```

### Commit Message Format
```
<type>: <subject>

<body (optional)>

<footer (optional)>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

**Example:**
```
feat: Add A* pathfinding algorithm

Implement A* algorithm for safe route calculation.
Uses Haversine distance for heuristic and safety
weights for edge costs.

Closes #42
```

## 🔄 Pull Request Process

### Before Submitting
1. **Update your branch** with latest upstream changes:
```bash
git fetch upstream
git rebase upstream/main
```

2. **Test thoroughly**:
- Start the server and verify it works
- Test all modified features
- Check browser console for errors

3. **Review your changes**:
```bash
git diff upstream/main
```

### Submitting
1. **Push to your fork**:
```bash
git push origin feature/AmazingFeature
```

2. **Create Pull Request**:
- Go to GitHub and click "New Pull Request"
- Select your branch
- Fill in the template with:
  - Description of changes
  - Related issue number (if any)
  - Testing steps
  - Screenshots (for UI changes)

3. **PR Title Format**:
```
[Type] Short description

Examples:
[Feature] Add A* pathfinding algorithm
[Fix] Correct weight calculation for edge cases
[Docs] Update installation instructions
```

### After Submitting
- Respond to review comments promptly
- Make requested changes in new commits
- Keep the PR focused—avoid unrelated changes
- Be patient—reviews may take time

## 🎯 Areas Needing Contribution

### High Priority
- [ ] Implement A* pathfinding algorithm for route calculation
- [ ] Add unit tests for Python data processing
- [ ] Improve mobile responsiveness
- [ ] Optimize map rendering performance

### Medium Priority
- [ ] Add more crime data sources
- [ ] Implement real-time traffic integration
- [ ] Create REST API for external applications
- [ ] Add multilingual support

### Documentation
- [ ] Create video tutorials
- [ ] Add more code examples
- [ ] Translate to other languages
- [ ] Write developer guides

## 📝 Code Review Process

All submissions require review. We look for:

1. **Functionality**: Does it work as intended?
2. **Code Quality**: Is it readable and maintainable?
3. **Testing**: Is it tested adequately?
4. **Documentation**: Are changes documented?
5. **Style**: Does it follow our guidelines?

## 🐛 Reporting Bugs

A good bug report includes:

### Required Information
- **Description**: Clear description of the bug
- **Steps to Reproduce**:
  1. Go to '...'
  2. Click on '...'
  3. See error
- **Expected Behavior**: What should happen
- **Actual Behavior**: What actually happens
- **Screenshots**: If applicable
- **Environment**:
  - OS: [e.g., Windows 10, macOS 13]
  - Browser: [e.g., Chrome 120, Firefox 121]
  - Node.js version: [e.g., v18.0.0]
  - Python version: [e.g., 3.10.5]

### Example Bug Report
```markdown
## Bug: Map doesn't load on Safari

**Description**
The map displays a blank screen on Safari 16.

**Steps to Reproduce**
1. Open http://localhost:3000 in Safari 16
2. Wait for page to load
3. Map container remains blank

**Expected Behavior**
Map should display with crime data layers

**Actual Behavior**
Blank screen, console shows CORS error

**Screenshots**
[Attach screenshot of blank map and console error]

**Environment**
- OS: macOS 13.0
- Browser: Safari 16.0
- Node.js: v18.0.0
```

## 💡 Suggesting Features

A good feature request includes:

1. **Use Case**: Why is this needed?
2. **Proposed Solution**: How would it work?
3. **Alternatives**: Other approaches considered
4. **Benefits**: Who benefits and how?
5. **Mockups**: UI sketches if applicable

## 📞 Questions?

- Open an issue with the "question" label
- Check [FAQ section](README.md#-frequently-asked-questions-faq) in README
- Review existing issues for similar questions

## 📜 Code of Conduct

- Be respectful and inclusive
- Accept constructive criticism gracefully
- Focus on what's best for the project
- Show empathy towards others

## 🙏 Thank You!

Your contributions make SafeRoute AI better for everyone. We appreciate your time and effort!
