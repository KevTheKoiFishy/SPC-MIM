import numpy as np

EPS_0 = 8.854e-12
EPS_R = {
    "HfO2" : lambda f: 17.7028
}

SIGMA = {
    "HfO2" : lambda f: 3.550400e-6
}

LOSST = {
    "HfO2" : 9.5884e-03,
}

DIELECTRIC       = "HfO2"
MEASUREMENT_FREQ = 10e3
MEAS_FREQ_ANG    = MEASUREMENT_FREQ * np.pi * 2

D = np.linspace(100, 1000, 10) * 1e-6   # Diameters of circular parallel plate capacitors
A = np.pi * D * D * 0.25                # Surface area of overlapping plates

S = 20e-9                               # 20nm Plate Separation