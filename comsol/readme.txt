Comsol files *.mph allow to reproduce the three simulation tests included in the paper along with the mesh sensitivity study.

- main_test.mph for the simulation test in the main manuscript (Fig. 6 & Suppl. Sim. Fig. 2). This same file can be used to generate Suppl. Sim. Fig. 16 provided the values of the permeability of the brain are set to those indicated in Suppl. Sim. Fig. 16.
- suppl_test_1.mph for the first test in the supplementary material (Suppl. Sim. Fig. 3).
- suppl_test_2.mph for the second test in the supplementary material (Suppl. Sim. Fig. 4).
- main_test_mesh_sensitivity_study.mph for the mesh sensitivity study (Suppl. Sim Fig. 20).
- Mesh1.nas through Mesh6.nas for the meshes used for the mesh sensitivity study in Nastran format.
- plot_data_brn_ks.py for the python script used to generate the plot with the comparison of the solutions of the main simulation test obtained for different values of brain permeability.
- data_brn_ks for the subfolder containing the output files of the relevant solution (interface volumetric fluid exchanges) for the different values of brain permeability exported from the COMSOL simulations (performed using the file main_test.mph changing the value of brn.ks) and imported in Python to make the plot.

Each Comsol file allows to generate all the figures included in the paper for the corresponding simulation test.

The files main_test.mph, suppl_test_1.mph, and suppl_test_2.mph in this repository were created and run in COMSOL Multiphysics v6.1. In all streamline plots of the filtration velocity, the arrowheads are not scaled proportionally to the velocity vector field. Instead, they are manually rescaled using different scaling factors for better visualization.

The file main_test_mesh_sensitivity_study.mph was created and run with COMSOL Multiphysics v6.2. 
