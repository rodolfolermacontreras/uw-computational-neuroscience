"""
Created on Wed Apr 22 15:15:16 2015

@author: rkp

Quiz 2 code.
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

import pickle

from compute_sta import compute_sta


FILENAME = 'c1p8.pickle'

with open(FILENAME, 'rb') as f:
    data = pickle.load(f)
    
stim = data['stim']
rho = data['rho']
    

# Fill in these values
sampling_period = 2  # in ms (1000 ms / 500 Hz)
num_timesteps = 150  # 300 ms window / 2 ms sampling period

sta = compute_sta(stim, rho, num_timesteps)

spike_times = rho[num_timesteps:].nonzero()[0] + num_timesteps
num_spikes = len(spike_times)
print('num_spikes =', num_spikes)
print('sta[:5] =', sta[:5])
print('sta[-5:] =', sta[-5:])
print('sta min/max =', sta.min(), sta.max())

time = (np.arange(-num_timesteps, 0) + 1) * sampling_period

plt.plot(time, sta)
plt.xlabel('Time (ms)')
plt.ylabel('Stimulus')
plt.title('Spike-Triggered Average')
plt.savefig('sta_plot.png', dpi=150)
print('Saved plot to sta_plot.png')