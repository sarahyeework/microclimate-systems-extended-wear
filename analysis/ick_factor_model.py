# "Ick Factor" Model (Behavioral + Environmental Wear Limit)
# -----------------------------------------------------------
# Informally referred to as the "ick factor," this model captures
# the point at which users discontinue wear due to perceived
# contamination, odor, and discomfort.
#
# This is NOT a formal scientific construct. It is a conceptual
# variable representing real-world behavior: garments are often
# removed based on perception and environmental conditions,
# not material failure.
#
# This version incorporates additional factors observed in
# constrained environments (e.g., space):
# - sweat accumulation without drainage
# - biological debris (e.g., skin shedding)
# - mold and environmental contamination risk


def compute_ick_score(
    odor_level,
    moisture_level,
    contamination_level,
    sensory_irritation,
    debris_load,
    environmental_risk
):
    """
    odor_level: 0–1 (smell intensity)
    moisture_level: 0–1 (dampness / sweat accumulation)
    contamination_level: 0–1 (perceived dirtiness)
    sensory_irritation: 0–1 (itchiness, stickiness)
    debris_load: 0–1 (skin particles, buildup)
    environmental_risk: 0–1 (mold, system contamination risk)
    """
    
    ick_score = (
        0.25 * odor_level +
        0.20 * moisture_level +
        0.15 * contamination_level +
        0.15 * sensory_irritation +
        0.15 * debris_load +
        0.10 * environmental_risk
    )
    
    return ick_score


def compute_behavioral_wear_limit(ick_score, tolerance_threshold=0.6):
    """
    Determines whether a user continues wearing the garment.
    """
    
    return ick_score < tolerance_threshold


def adjust_wear_tolerance(base_wear_factor, ick_score):
    """
    Reduces effective wear time based on perception-driven limits.
    """
    
    behavioral_penalty = 1 - (ick_score ** 1.5)
    
    adjusted_wear = base_wear_factor * behavioral_penalty
    
    return max(adjusted_wear, 0.2)


def simulate_ick_event(debris_release_spike):
    """
    Models sudden increase in perceived contamination
    (e.g., removing socks releases accumulated skin particles).
    """
    
    return min(1.0, debris_release_spike + 0.3)


# Example
if __name__ == "__main__":
    
    ick = compute_ick_score(
        odor_level=0.6,
        moisture_level=0.8,
        contamination_level=0.5,
        sensory_irritation=0.6,
        debris_load=0.7,
        environmental_risk=0.5
    )
    
    print("Ick score:", ick)
