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
# import os


fold = "./data_new/"
file_prefix = "bdp9_mesh"

nM = 6

errorsL2 = np.zeros(nM-1)
errorsL1 = np.zeros(nM-1)
errorsLinf = np.zeros(nM-1)

fig, ax = plt.subplots(1, 1) # , figsize=(14,7))
# ax.ticklabel_format(axis='y', style='sci', scilimits=(0,0), useMathText=True)

for i in range(nM):
    if i+1==5:
        data = np.genfromtxt(fold+file_prefix+str(i+1)+"_production.txt")
    else:
        data = np.genfromtxt(fold+file_prefix+str(i+1)+".txt")
    time = data[:,0]
    Qex = data[:,1]
    
    if i+1==5:
        ax.plot(time, Qex, '-', marker='o', markevery=10, fillstyle='none', label = 'Mesh '+str(i+1))
    else:
        ax.plot(time, Qex, '-', label = 'Mesh '+str(i+1))

    if i==0:
        Qex_0 = np.copy(Qex)
    else:
        errorsL2[i-1] = 100.*np.linalg.norm(Qex-Qex_0, ord=2)/np.linalg.norm(Qex, ord=2)
        # errorsL2[i-1] = 100.*np.sqrt(np.sum((Qex-Qex_0)**2)/np.sum((Qex)**2))
        Qex_0 = np.copy(Qex)

print(f"L2-error sequence: {errorsL2}")

# ax.set_xticks(())
# ax.set_xticklabels(())
# ax.set_yticks(())

ax.set_xlabel(r'Time (s)')
ax.set_ylabel(r'$\text{Q}_{\text{flt}}$ on $\Gamma_{\text{SC}}$ (nl/s)')
# ax.set_title()
ax.grid(True)
ax.legend(loc='upper left')

fig.tight_layout()  
plt.savefig('./Supplementary_Figure_11.eps')
plt.savefig('./Supplementary_Figure_11.png')
plt.savefig('./Supplementary_Figure_11.pdf')
# plt.show(block=False)
plt.show()
plt.close(fig)
