#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 14:09:12 2023

@author: waris
"""

from gymnasium.envs.registration import register

register(
     id="sphereCDPR-v0",
     entry_point="cdpr_env",
     max_episode_steps=300,
)