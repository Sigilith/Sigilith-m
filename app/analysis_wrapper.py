import datetime


def analyze_sequence_wrapper(sequence):
    # Assuming analyze_sequence_core is the function that processes the sequence
    analysis_output = analyze_sequence_core(sequence)

    # Enrich the output with additional information
    enriched_output = {
        'id': sequence.id,
        'timestamp': datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
        'entropy': analysis_output['entropy'],
        'transition_density': analysis_output['transition_density'],
        'risk_score': analysis_output['risk_score'],
        'regime_class': analysis_output['regime_class'],
        'analysis_result': analysis_output
    }
    return enriched_output
