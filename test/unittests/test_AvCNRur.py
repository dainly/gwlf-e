import unittest
from unittest import skip
from mock import patch
import numpy as np
from gwlfe import Parser
from gwlfe import AvCNRur


class TestAvCNRur(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()


    def test_AvCNRur(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            AvCNRur.AvCNRur_f(z.NRur, z.Area, z.CN),
            AvCNRur.AvCNRur(z.NRur, z.Area, z.CN), decimal=7)