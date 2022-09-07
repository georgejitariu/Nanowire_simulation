#MFM only for samples alligned on OX Axes(Horizontally)

import discretisedfield as df
import mag2exp
import k3d
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import os
import sys
import matplotlib.colors

for n in range(0, 11, 1):# number of ovf files
    m_field = df.Field.fromfile(r'F:\Anaconda\envs\mfm\samples_j/'+str(n)+'.ovf')#path of the files
    field_rotator = df.FieldRotator(m_field)
    new_field=m_field
    new_field.mesh.region=df.Region(p1=(0,0,-1.6e-07),p2=(1.28e-06,1.6e-07,0)))# check the geometry of the samples and put xmax.ymax,zmax values
    new_plane=new_field.plane('y')
    new_plane.z.mpl.scalar(filter_field=new_field.norm,figsize=(30,2),symmetric_clim=True,cmap='seismic',clim=(-1,1))
    new_mfm_field_w_pad = field_rotator.field.pad({"z": (0, 20)}, mode="constant")
    #new_mfm_field_w_pad = new_mfm_field_w_pad.pad({"y": (40, 40)}, mode="constant")
    phase = mag2exp.mfm.phase_shift(new_mfm_field_w_pad, quality=650, k=100, tip_q=1e-9, tip_m=(0, 0, 1e-16))
    phase.plane(z=3e-8).mpl.scalar(figsize=(30,2) ,cmap='afmhot', colorbar_label='Phase shift (radians)')# z=where the counter lever tip should be
    plt.xticks(fontsize=15,weight='bold')
    plt.yticks(fontsize=15,weight='bold')
    plt.xlabel('x ($\mu m$)', fontsize=16,weight='bold')
    plt.ylabel('y (nm)', fontsize=16,weight='bold')
    plt.savefig('PLOT'+str(n)+'.png')
    #plt.savefig('PLOT'+str(n)+'.svg')
    
    
    #---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
