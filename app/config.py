# Sigilith-M Configuration

## Storage Paths
- **Data Path**: `/path/to/data`
- **Model Path**: `/path/to/models`

## Risk and Regime Classification Thresholds
- **Risk Threshold**: 0.75
- **Regime Classification Levels**:
  - Low: 0.0 - 0.3
  - Medium: 0.3 - 0.6
  - High: 0.6 - 1.0

## Dashboard Defaults
- **Default View**: Dashboard 1
- **Refresh Interval**: 5 minutes

## Terrain Engine Parameters
- **Resolution**: 30m
- **Analysis Type**: Global

## Utility Functions

### Classify Risk
```python
def classify_risk(value):
    if value < 0.3:
        return "Low"
    elif value < 0.6:
        return "Medium"
    else:
        return "High"
```

### Classify Regime
```python
def classify_regime(value):
    if value < 0.3:
        return "Stable"
    elif value < 0.6:
        return "Unstable"
    else:
        return "Critical"
```

# Notes
This configuration file provides the necessary settings for managing the Sigilith-M application, including essential storage paths, thresholds, and classifications.