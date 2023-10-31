# test_water_density.py
import unittest
from water_density import calculate_water_density

class TestWaterDensity(unittest.TestCase):

    def test_water_density_pass(self):
        result = calculate_water_density(20)
        self.assertAlmostEqual(result, 998.44, places=2)  # Expected value at 20°C

    def test_water_density_fail(self):
        result = calculate_water_density(10)
        self.assertAlmostEqual(result, 1000.00, places=2)  # Intentionally failing test

if __name__ == '__main__':
    unittest.main()
