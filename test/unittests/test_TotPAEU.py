import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import TotPAEU


class TestTotPAEU(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_TotPAEU(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            TotPAEU.TotPAEU_2(z.NumAnimals, z.AvgAnimalWt),
            TotPAEU.TotPAEU(z.NumAnimals, z.AvgAnimalWt), decimal=7)
