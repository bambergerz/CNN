class Pixel:
    def __init__(self, red=0, green=0, blue=0):
        self._red = red
        self._green = green
        self._blue = blue

    @property
    def red(self):
        return self._red

    @property
    def green(self):
        return self._green

    @property
    def blue(self):
        return self._blue

    def L1difference(self, other):
        """
        return the Manhattan difference between two pixels

        :param other: another Pixel instance
        :return: the Manhattan difference between the two pixels.
        I.e., return the sum of the differences between the R, G, and B values of the pixels.
        """
        assert isinstance(other, Pixel)
        return (abs(self.red - other.red) +
                abs(self.green - other.green) +
                abs(self.blue - other.blue))
