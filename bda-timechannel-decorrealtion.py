
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as constants

uvcut=[500,1000,2000,3000,4000,5000,6000,7000]
bda_final_flux=np.array([920.336031417,913.780426532,904.846099895,913.125924905,934.011238502,905.334584172,858.452557473,858.505067912])
timechannel_final_flux=np.array([983.599807005,979.07436482,966.393026917,958.76961889,941.001190771,904.977583204, 863.694076408,861.561710166])

uvcut_lambda=np.array(uvcut)*(1/constants.c)*1283*10**3

decorrealtion_bda=np.array(1-((1000-bda_final_flux)/1000))
decorrealtion_timechannel=np.array(1-((1000-timechannel_final_flux)/1000))

plt.plot( uvcut_lambda,decorrealtion_bda,label='bda -dc 0.83')
plt.plot( uvcut_lambda,decorrealtion_timechannel,label='timechannel -t 11 -c 4')
plt.xlabel("baseline length (kilolambda)")
plt.ylabel("decorrealtion")
plt.title("decorrealton 1 Degree vs uvcut")
plt.ylim(0.75,1.05)
plt.legend()
plt.show()