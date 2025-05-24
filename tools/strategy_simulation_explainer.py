# Phase 119 – Strategy Simulation Explainer

def explain_simulation_run(simulation_result):
    explanation = []
    for key, value in simulation_result.items():
        explanation.append(f"{key}: {value}")
    return "\n".join(explanation)