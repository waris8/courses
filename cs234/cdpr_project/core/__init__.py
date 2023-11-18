#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 14:09:12 2023

@author: waris
"""

from gymnasium.envs.registration import register

register(
     id="envs/sphereCDPR-v0",
     entry_point="env.cdpr_env:cdpr_env",
     max_episode_steps=300,
)