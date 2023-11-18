#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 13:50:13 2023

@author: waris
"""

from setuptools import setup

setup(
    name="cdpr_rl",
    version="0.0.1",
    install_requires=["mujoco", "stable-baselines3", "imitation"],
)