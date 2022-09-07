import os
import sys
import k3d
import os.path
import pathlib
import mag2exp
import numpy as np
import matplotlib as mpl
import discretisedfield as df
import matplotlib.pyplot as plt

for n in range(0, 11, 1):
    m_field = df.Field.fromfile(r'F:\ICMM\tube_hyst2.out/'+str(n)+'.ovf')
    mfm_field = m_field.pad({'x': (0,0)}, mode='constant')
    plane=mfm_field.plane('y')
    field_rotator = df.FieldRotator(mfm_field)
    field_rotator.rotate("from_euler", seq="y", angles=90, degrees=True)
    new_mfm_field = field_rotator.field.pad({'x': (0,2)}, mode='constant')#padding
    new_plane=new_mfm_field.plane('y')
    new_mfm_field.mesh.region=df.Region(p1=(0,0,-1.6e-7),p2=(4.05e-6,1.6e-7,0))
    new_plane=new_mfm_field.plane('y')
   
    line = new_mfm_field.mesh.line(p1=(0, 0.8e-7,-0.8e-7), p2=(4.05e-6, 0.8e-7, -0.8e-7), n=60)
    field_values = []
    parameter = []
    vortex_field = new_mfm_field
    for point in line:
        x, y, z = point
        parameter.append(x)  
        field_values.append(vortex_field(point))

    mx, my, mz = zip(*field_values)
    plt.figure(figsize=(9, 5))
    plt.plot(parameter, mx, "o-", linewidth=1, label="m_x")
    plt.plot(parameter, my, "o-", linewidth=1, label="m_y")
    plt.plot(parameter, mz, "o-", linewidth=1, label="m_z")
    plt.xlabel("x (nm)")
    plt.ylabel("reduced-magnetisation-component")
    plt.grid()
    plt.legend()
    plt.savefig('PLOT'+str(n)+'.svg')
