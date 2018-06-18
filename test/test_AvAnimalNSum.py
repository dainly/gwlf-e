import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.Outputs.AvAnimalNSum import AvAnimalNSum


class TestAvAnimalNSum(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    @skip("not ready")
    def test_AvAnimalNSum(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            AvAnimalNSum.AvAnimalNSum_f(),
            AvAnimalNSum.AvAnimalNSum(), decimal=7)