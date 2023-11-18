#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 12:10:41 2023

@author: waris
"""
import numpy as np
from sympy import symbols, Eq, solve

class polynomial_trajectory():
    
    def __init__(self, x0, v0, a0, x1, v1, a1, t0, tf):

        t = symbols('t')
        a, b, c, d, e, f = symbols('a b c d e f')
        
        # Define the quintic polynomial
        P = a * t**5 + b * t**4 + c * t**3 + d * t**2 + e * t + f
        
        # Define the boundary conditions
        conditions = [
            Eq(P.subs(t, t0), x0),
            Eq(P.subs(t, tf), x1),
            Eq(P.diff(t).subs(t, t0), v0),
            Eq(P.diff(t).subs(t, tf), v1),
            Eq(P.diff(t, 2).subs(t, t0), a0),
            Eq(P.diff(t, 2).subs(t, tf), a1),
        ]
        
        # Solve the system of equations
        coefficients = solve(conditions, (a, b, c, d, e, f))
        
        self.a = coefficients[a]
        self.b = coefficients[b]
        self.c = coefficients[c]
        self.d = coefficients[d]
        self.e = coefficients[e]
        self.f = coefficients[f]
        
    def calc_pos(self, t):
        
        return (self.a*(t**5)) + (self.b*(t**4)) + (self.c*(t**3)) + (self.d*(t**2)) + (self.e*t) + self.f  
        
    def calc_vel(self, t):
        return (5*self.a*(t**4)) + (4*self.b*(t**3)) + (3*self.c*(t**2)) + (2*self.d*t) + self.e
        
    def calc_acc(self, t):
        return (20*self.a*(t**3)) + (12*self.b*(t**2)) + (6*self.c*t) + (2*self.d)


# t = polynomial_trajectory(1.25, 0, 0, 1.7, 0, 0, 0, 3)

# pos = t.calc_pos(2)
# vel = t.calc_vel(2)
# acc = t.calc_acc(2)
# print(pos)
# print(vel)
# print(acc)