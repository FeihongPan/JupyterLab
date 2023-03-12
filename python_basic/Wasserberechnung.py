# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 15:23:41 2022

@author: Pan
"""

from CoolProp.CoolProp import PropsSI
import numpy as np 
import pandas as pd
import warnings
warnings.filterwarnings('ignore') # deaktiviert Warnungen (nicht für normale Arbeiten machen!)

fluid = 'Water'
T_0 = 273.15 #K

n_ZP = 11
d = np.zeros(n_ZP) 
cp = np.zeros(n_ZP)
p = np.zeros(n_ZP)
T = np.zeros(n_ZP)

# =============================================================================
# Druck und Tempeartur
# =============================================================================

p_list = [990e2,1000e2,504e2,550e2,522e2,496e2,497e2,
          500e2,501e2,504e2,484e2]

T_list = [T_0 + 40.00, T_0 + 40.08, T_0 + 50.09, T_0 + 58.19, T_0 + 57.99, T_0 + 58.12, 
          T_0 + 58.11, T_0 + 58.05, T_0 + 58.01, T_0 + 58.03, T_0 + 58.04]

p = np.array(p_list)
T = np.array(T_list)

# =============================================================================
# Dicht d berechnen [Pa] [K]
# =============================================================================
d = PropsSI('D', 'T', T, 'P', p, fluid)  

# =============================================================================
# die spezifische kapazität cp [kj/kg]
# =============================================================================
cp = PropsSI('C', 'T', T, 'P', p, fluid)  

# Darstellung der Zustandspunkte in einer Tabelle
df = pd.DataFrame(
    {
        'p in Pa': p,
        'p in mbar': p/100,
        'T in K': T,
        'T in °C': T - T_0,
        'd in kg/m3': d,
        'cp in kj/kg': cp/1000,
    },
    index = np.arange(n_ZP)
)