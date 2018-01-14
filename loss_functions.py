import picture


class L1Distance:

    def __init__(self, p1, p2):
        """

        :param p1: the first picture. Consist of a two dimensional array of pixels.
        Each entry in this 2D array is a 3-tuple RGB value representing the color of that pixel.
        :param p2: the second picture. We compute the distance of this picture with respect to the first
        pioture. It is of the same datatype as p1
        """

        assert isinstance(p1, picture.Picture), "p1 parameter is not a picture"
        assert isinstance(p2, picture.Picture), "p2 parameter is not a picture"
        assert len(p1) == len(p2) and len(p1[0]) == len(p2[0]), "non-matching dimensions between pictures"

        self._p1 = p1
        self._p2 = p2
        self._dist = self._get_dst()

    def _get_dst(self):
        """
        Calculate the sum of the L1 (Manhattan) differences between pixels in the two images (i.e., p1 and p2).

        :return: the Manhattan distance between p1 and p2. An integer.
        """
        flat_p1 = self.p1.flatten()
        flat_p2 = self.p2.flatten()

        val = 0

        for x in range(len(flat_p1)):
            pixel1 = flat_p1[x]
            pixel2 = flat_p2[x]
            val += pixel1.L1difference(pixel2)

        return val

    @property
    def p1(self):
        return self._p1

    @property
    def p2(self):
        return self._p2







