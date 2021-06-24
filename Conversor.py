class Conversor():

    def __init__(self):
        self.__value_in = 0

    def get_value(self):
        self.__value_in = input("Insert a value to convert: ")
        return True

    def set_extern_value(self,number):
        self.__value_in = number
        return True

    def nautic_miles_to_kilometers(self):
        formula = float(self.__value_in) * 1.852
        return formula

    def kilometers_to_nautic_miles(self):
        formula = float(self.__value_in) / 1.852
        return formula

    def miles_to_kilometers(self):
        formula = float(self.__value_in) * 1.60934
        return formula

    def kilometers_to_miles(self):
        formula = float(self.__value_in) / 1.60934
        return formula

    def meters_to_feet(self):
        formula = float(self.__value_in) * 3.28084
        return formula

    def feet_to_meters(self):
        formula = float(self.__value_in) / 3.28084
        return formula

    def celsius_to_kelvin(self):
        formula = float(self.__value_in) + 273.15
        return formula

    def kelvin_to_celsius(self):
        formula = float(self.__value_in) - 273.15
        return formula

    def celsius_to_farenheit(self):
        formula = (float(self.__value_in) *9 / 5) + 32
        return formula

    def farenheit_to_celsius(self):
        formula = (float(self.__value_in) - 32) *5 / 9
        return formula

    def farenheit_to_kelvin(self):
        formula = ((float(self.__value_in) - 32) *5 / 9) + 273.15
        return formula

    def kelvin_to_farenheit(self):
        formula = ((float(self.__value_in) - 273.15) * 9 / 5) + 32
        return formula

    def miles_to_nautic_miles():
        formula = ((float(self.__value_in)/1.151))
        return formula

    def nautic_miles_to_miles():
        formula = ((float(self.__value_in)*1.151))
        return formula

    def kilometers_to_meters(self):
        formula = (float(self.__value_in) * 1000)
        return formula

    def meters_to_kilometers(self):
        formula = (float(self.__value_in) / 1000)
        return formula
