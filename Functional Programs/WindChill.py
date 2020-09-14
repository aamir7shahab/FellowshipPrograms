"""Programs that takes two double command-line arguments temperature
and velocity and prints the wind chill"""

import sys


class WindChill:

    @staticmethod
    def checkValid(temp, speed):
        """
        This function checks whether the give input is according to given conditions.
        :param temp:
        :param speed:
        :return: Forward
        """
        if (-50 <= temp <= 50) and (3 <= speed <= 120):
            result = WindChill.effectiveTemperature(temp, speed)
            return result
        else:
            return 0

    @staticmethod
    def effectiveTemperature(temp, speed):
        """
        This function takes two argument temp and speed and return effective temperature.
        :param temp:
        :param speed:
        :return:
        """
        result = 35.74 + 0.6215 * temp + ((0.4275 * temp) - 35.75) * pow(speed, 0.16)
        return result


if __name__ == "__main__":
    try:
        temperature = int(sys.argv[1])
        speed = int(sys.argv[2])
    except ValueError:
        print("Enter two integer values.")

if WindChill.checkValid(temperature, speed):
    print(f"Effective temperature: {WindChill.checkValid(temperature, speed)}")
else:
    print('Invalid input.')
