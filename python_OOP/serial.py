"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """
        Initialize the SerialGenerator with a starting value.

        Args:
            start (int): The initial serial number (default is 0).
        """
        self.start = start
        self.current = start

    def generate(self):
        """
        Generate the next serial number.

        Returns:
            int: The next serial number.
        """
        serial_number = self.current
        self.current += 1
        return serial_number

    def reset(self):
        """
        Reset the serial number to the initial value.
        """
        self.current = self.start


serial = SerialGenerator(start=100)
print(serial.generate())  # Output: 100
print(serial.generate())  # Output: 101
print(serial.generate())  # Output: 102
serial.reset()
print(serial.generate())  # Output: 100