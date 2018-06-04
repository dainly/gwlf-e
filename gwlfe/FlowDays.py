import numpy as np
from Timer import time_function
from Memoization import memoize

@memoize
def FlowDays(AttenFlowDist, AttenFlowVel):
    if AttenFlowDist > 0 and AttenFlowVel > 0:
        return AttenFlowDist / (AttenFlowVel * 24)
    else:
        return 0


# def FlowDays_2():
#     pass
