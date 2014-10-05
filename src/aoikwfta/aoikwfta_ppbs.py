# coding: utf-8
"""
File ID: 3imh4G6

|ppbs| in the module name means PYTHONPATH bootstrap.
This module is intended to be imported by sibling module |aoikwfta.cmd|.
It will add package dir |aoikwfta|'s parent dir path to PYTHONPATH.
As a result, users can run module |aoikwfta.cmd| without configuring PYTHONPATH.
"""
import os
import sys

my_pp_dir_path = os.path.dirname(os.path.dirname(__file__))
## pp means PYTHONPATH

if my_pp_dir_path not in sys.path:
    sys.path.insert(0, my_pp_dir_path)
    