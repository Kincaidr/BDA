PYXIS_ROOT_NAMESPACE=True

import os
import sys
from casacore.tables import table
import numpy as np

#tdlconfig.profiles

def max_min_b(ms):
        
    tab=table(ms)
    uv = tab.getcol("UVW")[:,:2]
    print('max baseline is', np.sqrt((uv**2).sum(1)).max())
    print('min baseline is', np.sqrt((uv**2).sum(1)).min())

def wsclean():
    os.system("wsclean -name wsclean/Abell3376_sim -mem 60 -weight briggs 0.0 -size 6075 6075 -scale 1.5asec -pol I -intervals-out 1 -data-column DATA -fit-spectral-pol 2 -channels-out 4 -join-channels -niter 10000 -gain 0.1 -mgain 0.99 -auto-threshold 0.2 %s"%ms_set)


#/bin/bash -c 'source ....; xova ....'
def xova_bda():
    for k in range(len(z)):
        os.system(f"xova bda {ms_set} -fov 1.0 -d {z[k]} -dc DATA -mc 4096 --force -o xova_bda/Abell3376_bda_{z[k]}.ms -rc 2000000")
 
def bda_wsclean():
    for k in range(len(z)):
        os.system(f"wsclean -name xova_bda/Abell3376_bda_{z[k]} -mem 60 -weight briggs 0.0 -size 6075 6075 -scale 1.5asec -pol I -intervals-out 1 -data-column DATA -fit-spectral-pol 2 -channels-out 4 -join-channels -niter 10000 -auto-threshold 0.2 -gain 0.1 -mgain 0.99 xova_bda/Abell3376_bda_{z[k]}.ms")
    
def bda_wsclean_uvcut():
    for i in range(len(uv)):
        os.system(f"wsclean -name xova_bda/Abell3376_bda_0.83_{uv[i]} -mem 60 -weight briggs 0.0 -size 6075 6075 -maxuvw-m {uv[i]} -scale 1.5asec -pol I -intervals-out 1 -data-column DATA -fit-spectral-pol 2 -channels-out 4 -join-channels -niter 10000 -auto-threshold 0.2 -gain 0.1 -mgain 0.99 xova_bda/Abell3376_bda_0.83.ms")
    
    
def xova_timechannel():
    for i in range(len(x)):
        for j in range(len(y)):
            os.system(f"xova timechannel {ms_set} -dc DATA -c {y[j]} -t {x[i]} --force -o xova_timechannel/Abell3376_timechannel_t{x[i]}_c{y[j]}.ms -rc 2000000" )
            
            
def timechannel_wsclean_uvcut():
    for i in range(len(uv)):
            os.system(f"wsclean -name xova_timechannel/Abell3376_timechannel_t11_c4_{uv[i]} -mem 60 -weight briggs 0.0 -size 6075 6075 -maxuvw-m {uv[i]} -scale 1.5asec -pol I -intervals-out 1 -data-column DATA -fit-spectral-pol 2 -channels-out 4 -join-channels -niter 10000 -auto-threshold 0.2 -gain 0.1 -mgain 0.99 xova_timechannel/Abell3376_timechannel_t11_c4.ms")
            
     
def timechannel_wsclean():
    for i in range(len(x)):
        for j in range(len(y)):
            os.system(f"wsclean -name xova_timechannel/Abell3376_timechannel_t{x[i]}_c{y[j]} -mem 60 -weight briggs 0.0 -size 6075 6075 -scale 1.5asec -pol I -intervals-out 1 -data-column DATA -fit-spectral-pol 2 -channels-out 4 -join-channels -niter 10000 -auto-threshold 0.2 -gain 0.1 -mgain 0.99 xova_timechannel/Abell3376_timechannel_t{x[i]}_c{y[j]}.ms")

#sys.system(f"chgcentre {scans[i]} {coordinates_ra[i]} {coordinates_dec[i]}")


if __name__ == '__main__':
    ms_set='Abell3376_raw-Abell3376East-corr.ms' 
    ms_bda= '/net/ike/vault-ike/kincaid/xova_analysis/xova_bda/abell3376_bda.ms'
    x=[14,16]
    y=[1,2,3,4,5]
    z=[0.88,0.87,0.89]
    uv=[500,1000,2000,3000,4000,5000,6000,7000]
    #xova_timechannel()
    #sim()
    #wsclean()
    #max_min_b(ms_xova)
    #xova_bda()
    timechannel_wsclean_uvcut()
    #tnubda_wsclean_uvcut()
    #timechannel_wsclean()


#    for i in 9 11; do for j in 1 3; do echo Abell3376_timechannel_t${i%%*()}_c$j-MFS-image.fits; casa -c imfit_flux.py xova_timechannel/Abell3376_timechannel_t${i%%*()}_c$j-MFS-image.fits 1Jy_source.crtf; done; done
