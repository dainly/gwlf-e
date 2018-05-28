# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division

import sys
import importlib
import unittest
import json
import numpy as np
from unittest import skip
from ddt import ddt, data
from mock import patch
import threading
from test_output import TestOutput

from StringIO import StringIO


class gms6_TestOutput(TestOutput):
    """
    Tests model generated output versus known
    static output.
    """
    __test__ = True
    def setUp(self):
        super(gms6_TestOutput, self).setUp('GMS6.gms','GMS6_output.json')