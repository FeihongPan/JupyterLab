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

n_ZP = 52
p = np.zeros(n_ZP)
T = np.zeros(n_ZP)

# Die maxmale Temperatur eingeben
t_list = [46.61, 46.37, 46.31, 46.49, 46.63, 47.18, 44.12, 44.39, 54.30,
          55.84, 55.74, 56.59, 62.32, 62.32, 62.81, 62.80, 63.06, 63.06,
          64.26, 64.31, 53.75, 56.29, 56.37, 56.51, 62.28, 63.65, 63.78,
          64.26, 44.07, 44.07, 46.59, 46.90, 47.72, 47.87, 48.81, 47.97,
          54.20, 54.14, 57.21, 57.21, 57.16, 60.89, 61.08, 61.04, 62.19, 
          62.10, 62.72, 62.68, 62.79, 62.79, 64.00, 64.24]
T_list = []

for i in range(n_ZP):
    T_list.append(t_list[i] + T_0)

T = np.array(T_list)

# Sättigungsdruck berechnen
p_sat = PropsSI('P', 'T', T, 'Q', 1, fluid)  


# Darstellung der Zustandspunkte in einer Tabelle
df = pd.DataFrame(
    {
        'p in Pa': p_sat,
        'p in mbar': p_sat/100,
        'T in K': T,
        't in °C': T - T_0,
    },
    index = np.arange(n_ZP)
)