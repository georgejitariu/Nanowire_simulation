import discretisedfield as df
import mag2exp
import k3d
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import os
import sys


#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

cont=0
for n in range(0, 11, 1):
    m_field = df.Field.fromfile(r'F:\ICMM\tube_hyst2.out/'+str(n)+'.ovf')
    mfm_field = m_field.pad({'x': (0,0)}, mode='constant')
    plane=mfm_field.plane('y')
    #m_field.plane('y').mpl()
    field_rotator = df.FieldRotator(mfm_field)
    field_rotator.rotate("from_euler", seq="y", angles=90, degrees=True)
    new_mfm_field = field_rotator.field.pad({'x': (0,2)}, mode='constant')#padding
    new_plane=new_mfm_field.plane('y')
    #new_plane.z.mpl.scalar(filter_field=new_mfm_field.norm,figsize=(10,2.5),symmetric_clim=True)
    new_mfm_field.mesh.region=df.Region(p1=(0,0,-1.6e-7),p2=(4.05e-6,1.6e-7,0))
    new_plane=new_mfm_field.plane('y')
    #new_plane.z.mpl.scalar(filter_field=new_mfm_field.norm,figsize=(10,2.5),symmetric_clim=True)
    
    list=[800]
    for i in list:
        ii=i*2.5e-9
        new_plane=new_mfm_field.plane(x=ii)
        new_plane.x.mpl.scalar(filter_field=new_mfm_field.norm,figsize=(6.5,6),symmetric_clim=True,colorbar_label='mx',cmap='seismic', clim=(-1, 1)) #x y z
        plt.xlabel('y (nm)')
        plt.ylabel('z (nm)')
        res = "{:.3e}".format(ii*10e5)
        plt.title('x='+ res+ '( $\mu m$)', fontdict=None, loc='center', pad=None)
        plt.savefig('PLOTx'+str(i)+'_'+str(cont)+'.svg')
        #print('x=',res)
    
    list=[800]
    for i in list:
        ii=i*2.5e-9
        new_plane=new_mfm_field.plane(x=ii) 
        new_plane.z.mpl.scalar(filter_field=new_mfm_field.norm,figsize=(6.5,6),symmetric_clim=True,colorbar_label='mz',cmap='seismic', clim=(-1, 1)) #x y z
        plt.xlabel('y (nm)')
        plt.ylabel('z (nm)')
        res = "{:.3e}".format(ii*10e5)
        plt.title('z='+ res+ ' ($\mu m$)', fontdict=None, loc='center', pad=None)
        plt.savefig('PLOTz'+str(i)+'_'+str(cont)+'.svg')
    cont=cont+1     
    
    #zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
cont=0
for n in range(0, 11, 1):
    m_field = df.Field.fromfile(r'F:\ICMM\tube_hyst2.out/'+str(n)+'.ovf')
    mfm_field = m_field.pad({'x': (0,0)}, mode='constant')
    plane=mfm_field.plane('y')
    #m_field.plane('y').mpl()
    field_rotator = df.FieldRotator(mfm_field)
    field_rotator.rotate("from_euler", seq="y", angles=90, degrees=True)
    new_mfm_field = field_rotator.field.pad({'x': (0,2)}, mode='constant')#padding
    new_plane=new_mfm_field.plane('y')
    #new_plane.z.mpl.scalar(filter_field=new_mfm_field.norm,figsize=(10,2.5),symmetric_clim=True)
    new_mfm_field.mesh.region=df.Region(p1=(0,0,-1.6e-7),p2=(4.05e-6,1.6e-7,0))
    new_plane=new_mfm_field.plane('y')
    #new_plane.z.mpl.scalar(filter_field=new_mfm_field.norm,figsize=(10,2.5),symmetric_clim=True)
    
    list=[-32]
    for i in list:
        ii=i*2.5e-9
        new_plane=new_mfm_field.plane(z=ii) 
        new_plane.x.mpl.scalar(filter_field=new_mfm_field.norm,figsize=(6.5,2),symmetric_clim=True,colorbar_label='mx',cmap='seismic', clim=(-1, 1)) #x y z
        plt.xlabel('x ($\mu m$)')
        plt.ylabel('y (nm)')
        res = "{:.3e}".format(ii*10e5)
        plt.title('z='+ res+ ' ($\mu m$)', fontdict=None, loc='center', pad=None)
        plt.savefig('PLOTx'+str(i)c
           
    
    list=[-32]
    for i in list:
        ii=i*2.5e-9
        new_plane=new_mfm_field.plane(z=ii) 
        new_plane.y.mpl.scalar(filter_field=new_mfm_field.norm,figsize=(6.5,2),symmetric_clim=True,colorbar_label='my',cmap='seismic', clim=(-1, 1)) #x y z
        plt.xlabel('x ($\mu m$)')
        plt.ylabel('y (nm)')
        res = "{:.3e}".format(ii*10e5)
        plt.title('z='+ res+ '($\mu m$)', fontdict=None, loc='center', pad=None)
        plt.savefig('PLOTz'+str(i)+'_'+str(cont)+'.svg')
        #print('y=',res)    
    
        
    list=[-32]
    for i in list:
        ii=i*2.5e-9
        new_plane=new_mfm_field.plane(z=ii) 
        new_plane.z.mpl.scalar(filter_field=new_mfm_field.norm,figsize=(6.5,2),symmetric_clim=True,colorbar_label='mz',cmap='seismic', clim=(-1,1)) #x y z
        plt.xlabel('x ($\mu m$)')
        plt.ylabel('y (nm)')
        res = "{:.3e}".format(ii*10e5)
        plt.title('z='+ res+ ' ($\mu m$)', fontdict=None, loc='center', pad=None)
        plt.savefig('PLOTz'+str(i)+'_'+str(cont)+'.svg')
     
    cont=cont+1
    
    
