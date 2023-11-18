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

DEFAULT_SIZE = 480

class cdpr_env(gym.Env):
    
    metadata = {
       "render_modes": [
           "human",
           "rgb_array",
           ],
       "render_fps": 20,
    }
    
    def __init__(self, frame_skip=None, render_mode=None, camera_id = None, camera_name = None):
        
        super(cdpr_env, self).__init__()
        self.model = mujoco.MjModel.from_xml_path("model/sphereCDPR_2D.xml")
        self.data = mujoco.MjData(self.model)
        
        self.observation_space = spaces.Box(low=-np.inf, high=np.inf, shape=(10,),dtype=np.float64)   #position, velocity, acceleration, cable length
        self._set_action_space()
        
        self.init_qpos = self.data.qpos.ravel().copy()
        self.init_qvel = self.data.qvel.ravel().copy()
        
        assert render_mode is None or render_mode in self.metadata["render_modes"]
        self.render_mode = render_mode
        self.width = DEFAULT_SIZE
        self.height = DEFAULT_SIZE
        self.frame_skip = frame_skip
        self._viewers = {}
        self.viewer = None
        self.camera_name = camera_name
        self.camera_id = camera_id
        
    def _set_action_space(self):
        bounds = self.model.actuator_ctrlrange.copy().astype(np.float32)
        low, high = bounds.T
        self.action_space = spaces.Box(low=low, high=high, dtype=np.float32)
        return self.action_space
    
    def _get_obs(self):
        return np.concatenate(
            [
                self.data.qpos[:2].flat[1:],
                self.data.qvel[:2].flat,
                self.data.ten_length.flat
            ]
        )
        
    def step(self, action):
        if np.array(action).shape != self.action_space.shape:
           raise ValueError("Action dimension mismatch")
        self._step_mujoco_simulation(action, self.frame_skip)
        
    def _step_mujoco_simulation(self, ctrl, n_frames):
        
        posbefore = self.data.qpos
        self.data.ctrl[:] = ctrl

        mujoco.mj_step(self.model, self.data, nstep=self.frame_skip)
        mujoco.mj_rnePostConstraint(self.model, self.data)
        
        ob = self._get_obs()
        terminated = False

        if self.render_mode == "human":
            self.render()
        return (
            ob,
            0,
            terminated,
            False,
            dict(action=ctrl, diff=self.data.qpos - ob)
        )
        
        
    def reset(self, *, seed = None, options = None):
        
        super().reset(seed=seed)

        self._reset_simulation()

        ob = self.reset_model()
        if self.render_mode == "human":
            self.render()
        return ob, {}
      
    def _reset_simulation(self):
        mujoco.mj_resetData(self.model, self.data)
       
    def reset_model(self):
        qpos = self.init_qpos
        
        qvel = self.init_qvel
        self.set_state(qpos, qvel)
        return self._get_obs()
        
    def set_state(self, qpos, qvel):
        
        self.data.qpos[:] = np.copy(qpos)
        self.data.qvel[:] = np.copy(qvel)
        if self.model.na == 0:
            self.data.act[:] = None
        mujoco.mj_forward(self.model, self.data)
        
        
    def render(self):
        
        if self.render_mode is None:
            gym.logger.warn(
                "You are calling render method without specifying any render mode. "
                "You can specify the render_mode at initialization, "
                f'e.g. gym("{self.spec.id}", render_mode="rgb_array")'
            )
            return
        
        if self.render_mode =="rgb_array":
            camera_id = self.camera_id
            camera_name = self.camera_name

            if camera_id is not None and camera_name is not None:
                raise ValueError(
                    "Both `camera_id` and `camera_name` cannot be"
                    " specified at the same time."
                )

            no_camera_specified = camera_name is None and camera_id is None
            if no_camera_specified:
                camera_name = "track"

            if camera_id is None:
                camera_id = mujoco.mj_name2id(
                    self.model,
                    mujoco.mjtObj.mjOBJ_CAMERA,
                    camera_name,
                )

                self._get_viewer(self.render_mode).render(camera_id=camera_id)

        if self.render_mode == "rgb_array":
            data = self._get_viewer(self.render_mode).read_pixels(depth=False)
            # original image is upside-down, so flip it
            return data[::-1, :, :]
        elif self.render_mode == "human":
            self._get_viewer(self.render_mode).render()
        
    def _get_viewer(self, mode):
        
        self.viewer = self._viewers.get(mode)
        if self.viewer is None:
            if mode == "human":
                from gym.envs.mujoco.mujoco_rendering import Viewer

                self.viewer = Viewer(self.model, self.data)
            elif mode in {"rgb_array", "depth_array"}:
                from gym.envs.mujoco.mujoco_rendering import RenderContextOffscreen

                self.viewer = RenderContextOffscreen(self.model, self.data)
            else:
                raise AttributeError(
                    f"Unexpected mode: {mode}, expected modes: {self.metadata['render_modes']}"
                )

            self.viewer_setup()
            self._viewers[mode] = self.viewer
        return self.viewer
    
    def viewer_setup(self):
        assert self.viewer is not None
        self.viewer.cam.distance = self.model.stat.extent * 0.5
        
    def close(self):
        if self.viewer is not None:
           self.viewer.close()
           self.viewer = None
           self._viewers = {}
        

