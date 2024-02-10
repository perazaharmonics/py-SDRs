- 10 ** (-A_ca_b / 10))
print(f'Sky noise temperature under rain T_sky_k: {T_skyrains_k:.2f} K')
print(f'Sky noise temperature under clear skies: {T_sca_k:.2f} K')

# Calculate the antenna noise temperature under rain conditions
T_sys_rain_k = T_skyrains_k + T_LNA
print(f'Antenna noise temperature T_Ant_k under rain: {T_sys_rain_k:.2f} K')

# Calculate the increase in noise power due to rain
deltaN_dB = 10 * np.log10(T_sys_rain_k / T_sys)
print(f'Increase in noise power deltaN_dB due to rain: {deltaN_dB:.2f} dB')

# Calculate the effect on the downlink C/N ratio due to rain attenuation
linkM_dB = A_rain_dB2 + deltaN_dB
print(f'Total link margin degradation due to rain: {linkM_dB:.2f} dB')

# Calculate the downlink C/N ratio with rain attenuation
CNdn_rain_dB = CNdn_dB - linkM_dB
CNdn_rain_lin = 10 ** (CNdn_rain_dB / 10)

# Calculate the overall C/N ratio with rain attenuation
CNo_rain_lin = 1 / ((1 / CNup_lin) + (1 / CNdn_rain_lin))
CNo_rain_dB = 10 * np.log10(CNo_rain_lin)
print(f'Overall C/N with 2-dB of rain attenuation is: {CNo_rain_dB:.2f} dB')

# Check if the link is beyond repair
if CNdn_rain_dB < minCNo_dB:
    print(f'The link has faded beyond repair: {CNdn_rain_dB:.2f} dB is below the required overall C/N ratio {minCNo_dB:.2f} dB')

    # Calculate the C/N minimum for each UL and DL with FEC margin
    CNdn_rain_dB_FEC = CNdn_rain_dB + FEC_dB
    print(f'C/N down in rain in 2.0-dB of rain attenuation is: {CNdn_rain_dB:.2f} dB which is smaller than {minCNo_dB:.2f} dB but {CNdn_rain_dB_FEC:.2f} dB with the margin provided by FEC')
