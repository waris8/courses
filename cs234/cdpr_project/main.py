#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 20:55:58 2023

@author: waris
"""

import gymnasium as gym

import numpy as np
from imitation.util.util import make_vec_env
from imitation.data.wrappers import RolloutInfoWrapper
from imitation.algorithms import bc
from imitation.data.types import Trajectory

manipulator = gym.make("env/sphereCDPR-v0")

venv = make_vec_env(manipulator,
                    rng=np.random.default_rng(),
                    post_wrappers=[lambda manipulator, _ : RolloutInfoWrapper(manipulator)])

rng = np.random.default_rng()

# Load expert trajectories
trajectories = np.load('expert_trajectories.npy')

# Separate observations and actions
observations, actions = zip(*trajectories)

# Convert to NumPy arrays
observations = np.array(observations)
actions = np.array(actions)
transitions = Trajectory(obs=observations, acts= actions, infos=None, terminal=True)

bc_trainer = bc.BC(observation_space=manipulator.observation_space, action_space=manipulator.action_space, demonstrations=transitions, rng=rng)
bc_trainer.train(n_epochs=1)








