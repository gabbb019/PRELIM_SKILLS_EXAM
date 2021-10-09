from temperature import Temperature
import unittest

celsiusValue1 = Temperature(celsius=50)
celsiusValue2 = Temperature(celsius=25)
fahrenheitValue1 = Temperature(fahrenheit=50)
fahrenheitValue2 = Temperature(fahrenheit=25)

class TestTemperature(unittest.TestCase):
    def test_celsius1(self):
        self.assertEqual(celsiusValue1.kelvin,323.15) #Success
    
    def test_celsius2(self):
        self.assertEqual(celsiusValue2.kelvin, 323.15) #Fail
    
    def test_fahrenheit1(self):
        self.assertEqual(fahrenheitValue1.kelvin, 283.15) #Success
    
    def test_fahrenheit2(self):
        self.assertEqual(fahrenheitValue2.kelvin, 283.15) #Fail

if __name__ == "__main__":
    unittest.main()