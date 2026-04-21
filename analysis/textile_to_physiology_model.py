# Textile → Physiology → Wear Model
# This model connects textile design variables to physiological responses
# and ultimately to wear tolerance.

def textile_to_microclimate(moisture_wicking, breathability, coverage_fraction):
    """
    moisture_wicking: 0–1
    breathability: 0–1
    coverage_fraction: 0–1 (1 = full foot coverage, 0.3 = partial)
    """
    
    # More coverage traps more heat/moisture
    moisture_load = (1 - moisture_wicking) * coverage_fraction
    thermal_load = (1 - breathability) * coverage_fraction
    
    return moisture_load, thermal_load


def textile_to_mechanics(friction_coefficient, compression_level, seam_intensity):
    """
    friction_coefficient: 0–1 (higher = more friction)
    compression_level: 0–1 (moderate is optimal)
    seam_intensity: 0–1 (higher = more pressure points)
    """
    
    friction_load = friction_coefficient + seam_intensity
    
    # Compression has a non-linear effect (too low or too high is bad)
    compression_effect = -((compression_level - 0.5) ** 2) + 0.25
    
    return friction_load, compression_effect


def physiology_response(moisture_load, thermal_load, friction_load, compression_effect):
    """
    Combines microclimate + mechanical effects into physiological strain
    """
    
    discomfort = (
        0.4 * moisture_load +
        0.3 * thermal_load +
        0.3 * friction_load
    )
    
    circulation_support = compression_effect
    
    return discomfort, circulation_support


def compute_wear_tolerance(discomfort, circulation_support):
    """
    Converts physiological state into wear tolerance multiplier
    """
    
    base = 1.0
    
    # Higher discomfort reduces wear time
    base -= discomfort
    
    # Better circulation slightly improves tolerance
    base += 0.2 * circulation_support
    
    return max(base, 0.2)  # prevent negative values


# Example: comparing full vs partial coverage
if __name__ == "__main__":
    
    # Full sock
    m_load, t_load = textile_to_microclimate(0.6, 0.6, 1.0)
    f_load, c_eff = textile_to_mechanics(0.5, 0.5, 0.2)
    d, c = physiology_response(m_load, t_load, f_load, c_eff)
    wear_full = compute_wear_tolerance(d, c)
    
    # Partial coverage ("toe koozie")
    m_load2, t_load2 = textile_to_microclimate(0.6, 0.6, 0.4)
    f_load2, c_eff2 = textile_to_mechanics(0.5, 0.5, 0.2)
    d2, c2 = physiology_response(m_load2, t_load2, f_load2, c_eff2)
    wear_partial = compute_wear_tolerance(d2, c2)
    
    print("Full coverage wear factor:", wear_full)
    print("Partial coverage wear factor:", wear_partial)
