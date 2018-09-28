# -*- coding: utf8 -*-

import os
os.sys.path.append(os.path.realpath(os.path.dirname(__file__)+ "/.."))
from Program import FourWinsGame
import pytest

#def testAnnuDarlehen():
#	assert 21835.457140057595 == annuDarlehen.calcAnnuDarlehen(100000, 0.03, 5)

#def testInput(monkeypatch):
#	inputs = [10, 'y']
#    input_generator = (i for i in inputs)
#	monkeypatch.setattr('__builtin__.raw_input', lambda prompt: next(input_generator))
#	
#	try:
#		annuDarlehen.run()
#	except Exception:
#		print("\nFail")
#
#	assert out == "test"