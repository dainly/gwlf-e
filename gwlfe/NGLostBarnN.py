import numpy as np
from Timer import time_function
from LossFactAdj import LossFactAdj
from NGInitBarnN import NGInitBarnN


def NGLostBarnN(NYrs, NGPctManApp, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN, NGBarnNRate, Prec,
                DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct, RunConCoeffN):
    result = np.zeros((NYrs, 12))
    loss_fact_adj = LossFactAdj(NYrs, Prec, DaysMonth)
    ng_init_barn_n = NGInitBarnN(NGPctManApp, GrazingAnimal, NumAnimals, AvgAnimalWt, AnimalDailyN)
    for Y in range(NYrs):
        for i in range(12):
            result[Y][i] = (ng_init_barn_n[i] * NGBarnNRate[i] * loss_fact_adj[Y][i]
                            - ng_init_barn_n[i] * NGBarnNRate[i] * loss_fact_adj[Y][i] * AWMSNgPct * NgAWMSCoeffN
                            + ng_init_barn_n[i] * NGBarnNRate[i] * loss_fact_adj[Y][i] * RunContPct * RunConCoeffN)
            if result[Y][i] > ng_init_barn_n[i]:
                result[Y][i] = ng_init_barn_n[i]
            if result[Y][i] < 0:
                result[Y][i] = 0
    return result


def NGLostBarnN_2(NYrs, NGInitBarnN, NGBarnNRate, Precipitation, DaysMonth, AWMSNgPct, NgAWMSCoeffN, RunContPct,
                  RunConCoeffN):
    lossFactAdj = LossFactAdj.LossFactAdj(NYrs, Precipitation, DaysMonth)
    result = (np.tile(NGInitBarnN, NYrs) * np.tile(NGBarnNRate, NYrs) * np.ndarray.flatten(lossFactAdj) * (
                1 - (AWMSNgPct * NgAWMSCoeffN) + (RunContPct * RunConCoeffN)))
    result = np.minimum(result, np.tile(NGInitBarnN, NYrs))
    result = np.maximum(result, 0)
    return np.reshape(result, (NYrs, 12))
