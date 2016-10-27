import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

#luminosity: L = K_L (M/Msun)^beta; mass-bins: m_0, m_1, m_2, ... in increasing order
#dN/dm = K (M/Msun)^-alpha; use common intervals

m_0=0.01; m_1=0.08; m_2=0.43; m_3=0.5; m_4=1.0; m_5=2.0; m_6=20.0; m_7=200.0

K_L1=K_L2=0.23; K_L3=K_L4=K_L5=1.0; K_L6=1.5; K_L7=3200.0
b1=b2=2.3; b3=b4=b5=4.0; b6=3.6; b7=1.0

K1=82.471; K2=K3=1.8661; K4=K5=K6=K7=1.0
a1=0.3; a2=a3=1.8; a4=2.7; a5=a6=a7=2.3

tot_num =  (m_1**(-a1+1.)-m_0**(-a1+1.))/(-a1+1.) + \
           (m_2**(-a2+1.)-m_1**(-a2+1.))/(-a2+1.) + \
           (m_3**(-a3+1.)-m_2**(-a3+1.))/(-a3+1.) + \
           (m_4**(-a4+1.)-m_3**(-a4+1.))/(-a4+1.) + \
           (m_5**(-a5+1.)-m_4**(-a5+1.))/(-a5+1.) + \
           (m_6**(-a6+1.)-m_5**(-a6+1.))/(-a6+1.) + \
           (m_7**(-a7+1.)-m_6**(-a7+1.))/(-a7+1.) #normalized to tot_num=1

norm=1./tot_num; tot_num=1.0

m_sn = 8.0
tot_sn =   norm*( (m_6**(-a6+1.)-m_sn**(-a6+1.))/(-a6+1.) + \
           (m_7**(-a7+1.)-m_6**(-a7+1.))/(-a7+1.) )

#1 supernova or 1.e51 erg for every SN or every (tot_num/tot_sn) stars

tot_mass = norm*( (m_1**(-a1+2.)-m_0**(-a1+2.))/(-a1+2.) + \
           (m_2**(-a2+2.)-m_1**(-a2+2.))/(-a2+2.) + \
           (m_3**(-a3+2.)-m_2**(-a3+2.))/(-a3+2.) + \
           (m_4**(-a4+2.)-m_3**(-a4+2.))/(-a4+2.) + \
           (m_5**(-a5+2.)-m_4**(-a5+2.))/(-a5+2.) + \
           (m_6**(-a6+2.)-m_5**(-a6+2.))/(-a6+2.) + \
           (m_7**(-a7+2.)-m_6**(-a7+2.))/(-a7+2.) )

mass_sn = norm*( (m_6**(-a6+2.)-m_sn**(-a6+2.))/(-a6+2.) + \
          (m_7**(-a7+2.)-m_6**(-a7+2.))/(-a7+2.) )

#mean_mass = total_mass/tot_num
#mass in SN/mass in stars = mass_sn/tot_mass ~ 4.4

tot_lum = norm*( K_L1*(m_1**(-a1+b1+1.)-m_0**(-a1+b1+1.))/(-a1+b1+1.) + \
           K_L2*(m_2**(-a2+b2+1.)-m_1**(-a2+b2+1.))/(-a2+b2+1.) + \
           K_L3*(m_3**(-a3+b3+1.)-m_2**(-a3+b3+1.))/(-a3+b3+1.) + \
           K_L4*(m_4**(-a4+b4+1.)-m_3**(-a4+b4+1.))/(-a4+b4+1.) + \
           K_L5*(m_5**(-a5+b5+1.)-m_4**(-a5+b5+1.))/(-a5+b5+1.) + \
           K_L6*(m_6**(-a6+b6+1.)-m_5**(-a6+b6+1.))/(-a6+b6+1.) + \
           K_L7*(m_7**(-a7+b7+1.)-m_6**(-a7+b7+1.))/(-a7+b7+1.) )

lum_ob = norm*( K_L6*(m_6**(-a6+b6+1.)-m_sn**(-a6+b6+1.))/(-a6+b6+1.) + \
           K_L7*(m_7**(-a7+b7+1.)-m_6**(-a7+b7+1.))/(-a7+b7+1.) )
