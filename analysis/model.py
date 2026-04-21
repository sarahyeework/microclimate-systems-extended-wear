# Microclimate Systems Wear Model
# This is a conceptual model linking sock design to wear duration and mission impact.

def compute_wear_factor(moisture_control, friction_reduction, coverage_type):
    """
    moisture_control: 0–1 (higher = better moisture regulation)
    friction_reduction: 0–1 (higher = less friction)
    coverage_type: 'full', 'partial', 'optimized'
    """
    
    base = 1.0
    
    # Microclimate contributions
    base += 0.6 * moisture_control
    base += 0.4 * friction_reduction
    
    # Coverage adjustments
    if coverage_type == "partial":
        base += 0.2  # less overall heat/moisture load
    elif coverage_type == "optimized":
        base += 0.3  # engineered system
    
    return base


def compute_wear_days(baseline_wear_days, wear_factor):
    return baseline_wear_days * wear_factor


def compute_mission_impact(mission_days, crew_size, wear_days, mass_per_pair):
    total_pairs = (mission_days * crew_size) / wear_days
    total_mass = total_pairs * mass_per_pair
    
    return total_pairs, total_mass


# Example usage (for reference, not required to run)
if __name__ == "__main__":
    baseline = 2  # days
    
    wear_factor = compute_wear_factor(
        moisture_control=0.7,
        friction_reduction=0.5,
        coverage_type="optimized"
    )
    
    wear_days = compute_wear_days(baseline, wear_factor)
    
    pairs, mass = compute_mission_impact(
        mission_days=180,
        crew_size=3,
        wear_days=wear_days,
        mass_per_pair=0.06  # kg
    )
    
    print("Wear days:", wear_days)
    print("Total pairs:", pairs)
    print("Total mass (kg):", mass)
