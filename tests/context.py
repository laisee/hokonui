''' Module for handling imports '''
# -*- coding: utf-8 -*-

import sys
import hokonui
import hokonui.exchanges
import hokonui.utils

# avoid flake8, pylint messages about unused imports
__all__ = [sys, hokonui.exchanges, hokonui.utils]

if __package__ is None:
    from os import (path)
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
