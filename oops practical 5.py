# Creating a class as Celsius
class Celsius:

    # Initialising or defining a function as init
    def __init__(self, temperature=0):
        self.set_temperature = temperature
        print("given Temperature = ", self.set_temperature)

    # Initialising or defining a function as converting celsius to fahrenheit
    def to_fahrenheit(self):
        return (self.temperature * 1.8)+32

    # It reads temperature from above function init
    def get_temperature(self):
        return self.temperature

    # Using setter for temperature
    def set_temperature(self, value):

        # Comparing a temparatur to kelvin
        if value < -273:
            raise ValueError("Temperature below -273 not possible")
        self.temperature = value
        temperature = property(get_temperature, self.set_temperature)

# Calling a above functions
c = Celsius()
c.temperature = 37
print(c.get_temperature())
print("after converting from celsius to fahrenheit:", c.to_fahrenheit())
