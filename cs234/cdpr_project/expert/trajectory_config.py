#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 16:41:45 2023

@author: waris
"""
import numpy as np

class Trajectory_config:
    
    # trajectory
    x0 = np.array([1.25, 0.75])
    x1 = np.array([1.7, 1.2])
    v0 = np.array([0, 0])
    v1 = np.array([0, 0])
    a0 = np.array([0, 0])
    a1 = np.array([0, 0])
    
    # control
    kp = 0.5
    kd = 0.5
    m = 0.5
    l = 1.5
