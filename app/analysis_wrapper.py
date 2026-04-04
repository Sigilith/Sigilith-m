def normalize_risk(risk_value):
    # Implement the logic to normalize the risk value
    normalized_value = risk_value / 100  # Example normalization
    return normalized_value


def normalize_regime(regime_value):
    # Implement the logic to normalize the regime value
    normalized_value = (regime_value - 1) / 2  # Example normalization
    return normalized_value


def wrap_analysis(analysis_data, config):
    # Implement the logic for wrapping analysis with standardized object structure
    standardized_structure = {
        'normalized_risk': normalize_risk(analysis_data['risk']),
        'normalized_regime': normalize_regime(analysis_data['regime']),
        'analysis_result': analysis_data['result'],
        'config': config
    }
    return standardized_structure
