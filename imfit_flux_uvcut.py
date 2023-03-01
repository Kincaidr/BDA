import sys
from matplotlib.pyplot import plot, show
import matplotlib.pyplot as plt
import numpy as np

region=sys.argv[3]

uvcut=[500,1000,2000,3000,4000,5000,6000,7000]
final_flux=[]

for i in range(len(uvcut)):
    image='xova_bda/Abell3376_bda_0.83_' + str(uvcut[i]) + '-MFS-image.fits'

    print(region,'region is')
    print(image,'image is')
    lines = open(region).readlines()
    flux=[]


    for i in range(len(lines)):
        f = open("uvcut_fluxes", "a")
        fit=imfit(imagename=image,region=lines[i])
        comp=fit['results']['component0']
        flux.append(comp['peak']['value']*1000)
        print(comp['peak']['value']*1000, comp['peak']['error']*1000)
        outputname=image.replace('xova_bda/','')
        final_flux.append(comp['peak']['value']*1000)
        f.write(str(image)+' '+str(flux[i])+'\n')
        
decorrealtion=np.array(1-((1000-final_flux)/1000))

plt.scatter( uvcut,decorrealtion, color='black', alpha=0.5)
plt.xlabel("uvcut in meters")
plt.ylabel("flux in Mjy")
plt.title("decorrealton 1 Degree flux vs uvcut")
plt.show()

 
# f.close()

# words=[] 
# with open('Bright_sources_fluxes_ddcal.txt', 'r') as r:
#     for line in r:
#         temp=line.split()
#         for i in temp:
#             words.append(temp)
#             words.sort()
#     r.close()

	
   
 
 
 
 


