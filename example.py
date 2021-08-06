import os
import mne
from Chua import chua
from noise import SNR_Set
from DA_alg import data_augment


st1,st2,st3,st4,strem,stw = data_augment('sleep.edf', 'hypno.edf', 9, 'g')

for i in [st1,st2,st3,st4,strem,stw]:
    print(i.shape[1])