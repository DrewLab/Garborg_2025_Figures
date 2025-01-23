# Garborg_2025_Figures
Contains code to generate figures for Garborg_2025 publication


# To generate matlab figures
1. Download folder titled "matlab" and add it to your path
2. Open file "figureScript.m"

Option 1:
3. Select "Run" to generate all figures for publication made with matlab

Option 2:
3. Run second section "Process data sets" individually to generate all data in the workspace
4. Run any individual section prior to "SUBFUNCTIONS" to generate only the plots for a specific figure, specified in the section title


# To generate comsol figures
Comsol files *.mph allow to reproduce the three simulation tests included in the paper

- main_test.mph for the simulation test in the main manuscript (Fig. 6 & Suppl. Sim. Fig. 2)
- suppl_test_1.mph for the first test in the supplementary material (Suppl. Sim. Fig. 3)
- suppl_test_2.mph for the second test in the supplementary material (Suppl. Sim. Fig. 4)

Each Comsol file allows to generate all the figures included in the paper for the corresponding simulation test

All the files in this repository were created and run in COMSOL Multiphysics v6.1
