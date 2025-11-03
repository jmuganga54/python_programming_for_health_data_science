def calculate_bmi(weight, height):
    """Compute BMI given weight (kg) and height (m)."""
    return weight / (height ** 2)

def is_healthy_bmi(bmi):
    """Return True if BMI is within [18.5, 24.9], else False."""
    return 18.5 <= bmi <= 24.9
