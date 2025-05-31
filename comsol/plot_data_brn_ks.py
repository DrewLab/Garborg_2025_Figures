#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  3 10:39:14 2025

@author: beatriceghitti
"""

import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


fold = "data_brn_ks/"

data0 = np.genfromtxt(fold+"data_ksem15.txt")
data1 = np.genfromtxt(fold+"data_ksem16.txt")
data2 = np.genfromtxt(fold+"data_ksem17.txt")

time = data0[:,0]

fig, ax = plt.subplots(1, 2, figsize=(9.6,4.8))

ax[0].ticklabel_format(axis='y', style='sci', scilimits=(0,0), useMathText=True)
ax[1].ticklabel_format(axis='y', style='sci', scilimits=(0,0), useMathText=True)

ax[0].plot(time, data0[:,2]*1e-6, 'b-', linewidth=1.8, label = r'$\Gamma_{\text{SC}},\, \kappa_S=2\times 10^{-15}\,\text{m}^2$')
ax[0].plot(time, data1[:,2]*1e-6, 'g-', linewidth=1.8, label = r'$\Gamma_{\text{SC}},\, \kappa_S=2\times 10^{-16}\,\text{m}^2$')
ax[0].plot(time, data2[:,2]*1e-6, 'r-', linewidth=1.8, label = r'$\Gamma_{\text{SC}},\, \kappa_S=2\times 10^{-17}\,\text{m}^2$')
ax[0].set_yticks((-4e2,-3e2,-2e2,-1e2,0.,1e2,2e2,3e2,4e2,5e2))

ax[1].plot(time, data0[:,1]*1e-6, 'c-', linewidth=1.8, label = r'$\Gamma_{\text{BR}},\, \kappa_S=2\times 10^{-15}\,\text{m}^2$')
ax[1].plot(time, data1[:,1]*1e-6, 'm-', linewidth=1.8, label = r'$\Gamma_{\text{BR}},\, \kappa_S=2\times 10^{-16}\,\text{m}^2$')
ax[1].plot(time, data2[:,1]*1e-6, color='orange', linestyle='-', linewidth=1.8, label = r'$\Gamma_{\text{BR}},\, \kappa_S=2\times 10^{-17}\,\text{m}^2$')
ax[1].set_yticks((-6e1,-4e1,-2e1,0.,2e1,4e1,6e1,8e1))

ax[0].set_xlabel(r'Time (s)')
ax[0].set_ylabel(r'Fluid Exchange $\text{Q}_{\text{flt}}$ on $\Gamma_{\text{SC}}$ (nl/s)')

ax[1].set_xlabel(r'Time (s)')
ax[1].set_ylabel(r'Fluid Exchange $\text{Q}_{\text{flt}}$ on $\Gamma_{\text{BR}}$ (nl/s)')

ax[0].grid(True)
ax[1].grid(True)

ax[0].legend(loc='upper right')
ax[1].legend(loc='upper right')

fig.tight_layout()  
plt.savefig('./plot_comparison_brn_ks.pdf')
plt.show()
plt.close(fig)
