import os
import numpy as np
import mne
from noise import SNR_Set


def add_noise(i,ma, snr, param):
    v=ma-i.shape[1]
    if i.shape[1]<ma:
        if v>i.shape[1]:
            while v>i.shape[1]:
                ii=[]
                for j in range(len(i)):
                    ii.append(SNR_Set(i[j] ,snr, param))
                ii=np.array(ii)
                i=np.append(i,    ii   , axis=1 )
                
        else:
            ii=[]
            for j in range(len(i)):
                ii.append(SNR_Set(i[j][:v] ,snr, param))
            ii=np.array(ii)
            i=np.append(i,  ii , axis=1)

    return i





def data_augment_sleep(recording, hypnogram, snr, param):

    raw=mne.io.read_raw_edf(recording)
    hypno=mne.read_annotations(hypnogram)
    aa=raw.set_annotations(hypno, emit_warning=False)

    data, times= raw[:]

    for ann in raw.annotations:
        descr = ann['description']
        start = ann['onset']
        end = ann['onset'] + ann['duration']

    st1=np.array([[],[],[],[],[],[],[]])
    st2=np.array([[],[],[],[],[],[],[]])
    st3=np.array([[],[],[],[],[],[],[]])
    st4=np.array([[],[],[],[],[],[],[]])
    strem=np.array([[],[],[],[],[],[],[]])
    stw=np.array([[],[],[],[],[],[],[]])

    for stage in raw.annotations:
        start = stage['onset']
        end = stage['onset'] + stage['duration']
        if stage['description']=='Sleep stage 1':
            st1=np.append(st1, data[:,int(start*100):int(end*100)], axis=1)
        elif stage['description']=='Sleep stage 2':
            st2=np.append(st2, data[:,int(start*100):int(end*100)], axis=1)
        elif stage['description']=='Sleep stage 3':
            st3=np.append(st3, data[:,int(start*100):int(end*100)], axis=1)
        elif stage['description']=='Sleep stage 4':
            st4=np.append(st4, data[:,int(start*100):int(end*100)], axis=1)
        elif stage['description']=='Sleep stage R':
            strem=np.append(strem, data[:,int(start*100):int(end*100)], axis=1)
        elif stage['description']=='Sleep stage W':
            stw=np.append(stw, data[:,int(start*100):int(end*100)], axis=1)
    m=[]
    for i in [st1,st2,st3,st4,strem,stw]:
        m.append(i.shape[1])
    maximum=max(m)

    st1=add_noise(st1,maximum,snr, param)
    st2=add_noise(st2,maximum,snr, param)
    st3=add_noise(st3,maximum,snr, param)
    st4=add_noise(st4,maximum,snr, param)
    strem=add_noise(strem,maximum,snr, param)
    stw=add_noise(stw,maximum,snr, param)

    m=[]
    for i in [st1,st2,st3,st4,strem,stw]:
        m.append(i.shape[1])
    m=min(m)

    return st1[:,:m], st2[:,:m], st3[:,:m], st4[:,:m], strem[:,:m], stw[:,:m]


def data_augment_motor(X, Y, snr, param):
    x1=[]
    x2=[]
    x3=[]
    for i in range(len(X)):
        if Y[i]==0:
            x1.append(X[i])
        elif Y[i]==1:
            x2.append(X[i])
        elif Y[i]==2:
            x3.append(X[i])

    x1=np.array(x1)
    x2=np.array(x2)
    x3=np.array(x3)

    x1=add_noise(x1 ,maximum,snr, param)
    x2=add_noise(x2 ,maximum,snr, param)
    x3=add_noise(x3 ,maximum,snr, param)

    m=[]
    for i in [st1,st2,st3,st4,strem,stw]:
        m.append(i.shape[1])
    m=min(m)

    return x1[:,:m], x2[:,:m], x3[:,:m]