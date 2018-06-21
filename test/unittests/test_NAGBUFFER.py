import unittest
from unittest import skip
import numpy as np
from gwlfe import Parser
from gwlfe.BMPs.AgAnimal import NAGBUFFER


class TestNAGBUFFER(unittest.TestCase):
    def setUp(self):
        input_file = open('input_4.gms', 'r')
        self.z = Parser.GmsReader(input_file).read()

    def test_NAGBUFFER(self):
        z = self.z
        np.testing.assert_array_almost_equal(
            NAGBUFFER.NAGBUFFER_2(z.n42, z.n43, z.n64, z.NYrs, z.NGPctManApp, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN, z.NGBarnNRate,
              z.Prec, z.DaysMonth, z.AWMSNgPct, z.NgAWMSCoeffN, z.RunContPct, z.RunConCoeffN, z.GRPctManApp, z.PctGrazing, z.GRBarnNRate,
              z.AWMSGrPct, z.GrAWMSCoeffN, z.PctStreams, z.NGAppNRate, z.NGPctSoilIncRate, z.GRAppNRate, z.GRPctSoilIncRate,
              z.GrazingNRate),
            NAGBUFFER.NAGBUFFER(z.n42, z.n43, z.n64, z.NYrs, z.NGPctManApp, z.GrazingAnimal_0, z.NumAnimals, z.AvgAnimalWt, z.AnimalDailyN, z.NGBarnNRate,
              z.Prec, z.DaysMonth, z.AWMSNgPct, z.NgAWMSCoeffN, z.RunContPct, z.RunConCoeffN, z.GRPctManApp, z.PctGrazing, z.GRBarnNRate,
              z.AWMSGrPct, z.GrAWMSCoeffN, z.PctStreams, z.NGAppNRate, z.NGPctSoilIncRate, z.GRAppNRate, z.GRPctSoilIncRate,
              z.GrazingNRate), decimal=7)