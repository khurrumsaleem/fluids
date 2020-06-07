#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 07:28:17 2020

@author: caleb
"""

import test_drag
import test_control_valve
import test_geometry
import test_two_phase
import test_two_phase_voidage
import test_separator
import test_piping
import test_packed_bed
import test_compressible

to_test = [test_drag, test_control_valve, test_geometry, test_two_phase, 
           test_two_phase_voidage, test_separator, test_piping, test_packed_bed,
           test_compressible]
for mod in to_test:
    for s in dir(mod):
        obj = getattr(mod, s)
        if callable(obj) and hasattr(obj, '__name__') and obj.__name__.startswith('test'):
#            print(s)
            try:
                obj()
            except Exception as e:
                print('FAILED TEST %s with error:' %s)
                print(e)