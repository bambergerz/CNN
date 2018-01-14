import numpy as np
from pixel import Pixel


class Picture:
    def __init__(self, p):
        """

        :param p: A potential picture object
        """
        self.enforce_assertions(p)
        self._picture = self.create_pixels(p)
        self.numpy_rep = np.array(p)

    @staticmethod
    def enforce_assertions(p):
        """
        Enforce that the picture is a list of rows.
        Each row consists of a list of pixel.
        Each pixel is a 3-Tuple of RGB values.
        Each value must be between 0 and 255.
        All rows must contain the same number of pixels.

        :param p: the picture we are enforcing our assertions on
        :return: None
        """

        assert isinstance(p, list), "improper abstraction of a picture. Should be a list of rows of pixels"
        first_row_width = len(p[0])
        num_cols = len(p)
        assert isinstance(first_row_width, list), "the first row is not represented as a list of pixels"
        for col in range(1, num_cols):
            row = p[col]
            assert len(row) == first_row_width, "the picture does not have unifrom length rows"
            for pixel in row:
                assert isinstance(pixel, tuple), "found a pixel whose data type is not a tuple"
                assert len(pixel) == 3, "found a pixel that does not have appropriate RGB dimensions"
                for entry in pixel:
                    assert entry >= 0, "found a pixel with an R, G, or B value less than 0"
                    assert entry <= 255, "found a pixel with an R, G, or B value greater than 255"

    @staticmethod
    def create_pixels(self, picture):
        """

        :param picture: the inisital picture which consisted of a fundamental data types
        (i.e., represented pixels as 3-tuples)
        :return: a 2D array of Pixel objects.
        """
        rows = []
        for orig_row in picture:
            row = []
            for pixel in orig_row:
                row.append(Pixel(pixel[0], pixel[1], pixel[2]))
            rows.append(row)
        return rows

    def flatten(self):
        """

        :return: a flattened numpy array representation of the pixels
        """
        return self.numpy_rep.flatten()






