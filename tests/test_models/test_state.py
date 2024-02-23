#!/user/bin/python3
"""Defines unittests for models/state.py.

Unittest classes:
    TestState_instantiation
    TestState_save
    TestState_to_dict
"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import state
