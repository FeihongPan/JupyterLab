"""
Frequency Response Modell
+ Parameter:
    + delta: charakristische Funktion
    + eta: Parameter in der Frequency Response zur Substitution
    + omega: Winkelfrequenz [1/s]
    + f: Frequenz [1/s]
    + t_h, t_R: Zeitkonstante [s]
    + a: Kugelradius [m]
    + m: Probenmasse [kg]
    + L: Dicke von der ebenen Platte [m]
    + D: Diffusionskoeffizient [m^2/s]
    + R: Gaskonstante = 8.314 J/molK
    + T_0: Versuchstemperatur [K]
    + V_0: Ausgangsvolumen [m^3]

+ Index:
    + 0: Ausgangsdaten
    + 1: Platte, der Index „1“ steht für die 1-dimensionale Betrachtung
    + 3: Kugel, der Index „1“ steht für die 1-dimensionale Betrachtung
    + c: in-phase
    + s: out-of-phase
"""

import numpy as np
from Modell.m_single import Kugel, Platte

# Klasse von der Diffusionsmodell für hierarchischen Porensystemen
# (Sun und Bourdin 1993)
class m_hierarchisch():
    '''
        t_R: Zeitkonstante für den Massenaustausch zwischen den beiden Porensorten
        K_omega: relative Gleichgewichtskonstante der Konzentration in den Speicherporen im Verhältnis zu den Transportporen
        delta_c_i: charakteristische in-phase Komponente
        delta_s_i: charakteristische out-of-phase Komponente
        K_i: Frequency Response Parameter
    '''

    def __init__(self, f, list_delta_c, list_delta_s, list_K, t_R, K_omega):
        self.f = f
        self.list_delta_c = list_delta_c
        self.list_delta_s = list_delta_s
        self.list_K = list_K
        self.t_R = t_R
        self.K_omega = K_omega

    # Gibt die Kreisfrequenz der Volumenmodulation vom Modell
    @property
    def func_omega(self):
        return (2 * np.pi * self.f)

    # Charakteristiche Funktion für das hierarchischen Porensystemen(in-phase)
    # (Sun und Bourdin 1993)
    def func_chara_hierar_c(self):
        ans = 0
        n = len(self.list_K)

        def func_i(delta_c, delta_s):
            chara_c_i = delta_c + self.K_omega * ((delta_c - delta_s * self.func_omega * self.t_R) / (1 + self.func_omega ** 2 * self.t_R ** 2))
            return chara_c_i
        
        # ans = K * delta_in
        for i in range(n):
            ans += self.list_K[i] * func_i(self.list_delta_c[i], self.list_delta_s[i])
            return ans

    # Charakteristiche Funktion für das hierarchischen Porensystemen(out-of-phase)
    # (Sun und Bourdin 1993)
    def func_chara_hierar_s(self):
        ans = 0
        n = len(self.list_K)

        def func_i(delta_c, delta_s):
            chara_s_i = delta_s + self.K_omega * ((delta_s + delta_c * self.func_omega * self.t_R) / (1 + self.func_omega ** 2 * self.t_R ** 2))
            return chara_s_i
        
        # ans = K * delta_out
        for i in range(n):
            ans += self.list_K[i] * func_i(self.list_delta_c[i], self.list_delta_s[i])
        return ans
    
    

if __name__ == '__main__':
    np_f = np.linspace(start=0.001, stop=10, num=10000)
    m_1 = Kugel(a=1e-5, D=1e-11, f=np_f, K=1)
    m_2 = Platte(L=1e-5, D=1e-11, f=np_f, K=1)
    m_hier = m_hierarchisch(f=np_f, list_delta_c=[m_1.func_chara_3c(), m_2.func_chara_1c()],
                            list_delta_s=[m_1.func_chara_3s(), m_2.func_chara_1s()], list_K=[1, 1], t_R=2.5, K_omega=0.4)
    chara_s = m_hier.func_chara_hierar_c()
    dict = dict(zip(np_f, chara_s))
    print(dict)
