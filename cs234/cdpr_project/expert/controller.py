#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 12:43:16 2023

@author: waris
"""
import numpy as np
import math
from scipy.optimize import lsq_linear

class pid_controller():
    
    def __init__(self, kp, kd, m, l):
        self.kp = kp
        self.kd = kd
        self.m = m     #mass of the end_effector
        self.l = l     # length of wireframe
        
    def calc_input_sig(self, ad, xd, vd, xr, vr):
        return self.m*(ad + self.kp*(xd-xr) + self.kd*(vd-vr))
    
    def build_wrench_mat(self, x, y):
        l = []
        lt0 = math.sqrt(x**2 + y**2)
        lt1 = math.sqrt(y**2 + (self.l-x)**2)
        lt2 = math.sqrt((self.l-y)**2 + (self.l-x)**2)
        lt3 = math.sqrt(x**2 + (self.l-y)**2)
        l.append([lt1*lt2*lt3*x, -lt0*lt1*lt3*(self.l-x), -lt0*lt2*lt3*(self.l-x), lt0*lt1*lt2*x])
        l.append([lt1*lt2*lt3*y, lt0*lt2*lt3*y, -lt0*lt1*lt3*(self.l-y), -lt0*lt2*lt3*(self.l-y)])
        return np.array(l)
    
    def scale(self, array):
        min_val = np.min(array)
        max_val = np.max(array)
        scaled_array = -1 + (array - min_val) / (max_val - min_val)
        return scaled_array
    
    def find_tensions(self, w, fnet):
        # print("w")
        # print(w)
        # print("fnat")
        # print(fnet)
        x, residuals, rank, s = np.linalg.lstsq(w, fnet, rcond=None)
        # x = lsq_linear(w, fnet, bounds=(-1, 0)).x
        np.clip(x, -1, 0)
        return x

# p = pid_controller(0.1, 0.3, 0.5, 1.5)

# w = p.build_wrench_mat(1.5, 0.85, 1, lt1, lt2, lt3)