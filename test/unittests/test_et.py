import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.MultiUse_Fxns import ET


class TestET(unittest.TestCase):
    def setUp(self):
        input_file = open('unittests/input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_DailyETPart1(self):
        z = self.z
        np.testing.assert_array_almost_equal(ET.DailyET_f(z.Temp, z.KV, z.PcntET, z.DayHrs),
                                             ET.DailyET(z.NYrs, z.DaysMonth, z.Temp, z.DayHrs, z.KV, z.PcntET,
                                                        z.ETFlag), decimal=7)

