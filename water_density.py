# water_density.py
def calculate_water_density(temperature_Celsius):
    # Constants for the density of water
    density_0C = 999.84  # kg/m^3 at 0°C
    temperature_coefficient = 0.07  # kg/m^3 per degree Celsius

    # Calculate water density at the given temperature
    water_density = density_0C - temperature_coefficient * temperature_Celsius
    return water_density
