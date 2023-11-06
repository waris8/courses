#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 20:49:28 2023

@author: waris
"""

import gymnasium as gym
from gymnasium import spaces
import mujoco
import numpy as np


class cdpr_env(gym.Env()):
    
    def __init__():
        super(cdpr_env, self).__init__()
        self.model = mujoco.MjModel.from_xml_path("/model/sphereCDPR_2D.xml")
        self.sim = mujoco_py.MjSim(self.model)
        self.data = self.sim.data
        
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(8,),dtype=np.float64)
        
        bounds = self.model.actuator_ctrlrange.copy().astype(np.float32)
        low, high = bounds.T
        self.action_space = spaces.Box(low=low, high=high, dtype=np.float32)
        
    def step():
        
    def reset():
        
    def render():
        
    def close():
        
        

