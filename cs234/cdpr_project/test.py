#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 23:23:49 2023

@author: waris
"""

import mujoco
import mediapy as media

model = mujoco.MjModel.from_xml_path("/home/waris/Desktop/desktop/robotics/courses/cs234/cdpr_project/model/sphereCDPR_2D.xml")

data = mujoco.MjData(model)

renderer = mujoco.Renderer(model)

duration = 3.8  # (seconds)
framerate = 60
frames = []
mujoco.mj_resetData(model, data)  # Reset state and time.
while data.time < duration:
  mujoco.mj_step(model, data)
  if len(frames) < data.time * framerate:
    renderer.update_scene(data)
    pixels = renderer.render()
    frames.append(pixels)
media.show_video(frames, fps=framerate)