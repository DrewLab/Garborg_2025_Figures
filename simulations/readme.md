Computations were carried out using COMSOL Multiphysics (www.comsol.com), Version 6.2.

# Folder "Main COMSOL Files"
---------------------------
	This folder contains three COMSOL Multiphysics files:
		* main_Fig6_ExtendedDataFig7_SuppFigs7_and_12.mph: Use this file to generate the data reported in Figure 6, Extended Data Figure 7, and Supplementary Figures 7 and 12.

		* Extended_Data_Fig8.mph: Use this file to generate the data reported in Extended Data Figure 8

		* Extended_Data_Fig9.mph: Use this file to generate the data reported in Extended Data Figure 9

NOTE ON Extended Data Figure 10: The data in this plot are of the same type as those in Figure 6e. The data in question can be generated using the file "main_Fig6_ExtendedDataFig7_SuppFigs7_and_12.mph" and setting the parameter "brn.ks" to the values indicated in the figure.


# Folder "MeshSensitivityStudyFiles"
-----------------------------------
	This folder contain three subfolders:
		- COMSOLFile
		- NastranMeshes
		- PythonScript
		
	The COMSOL Multiphysics file used in the mesh sensitivity study is
		./COMSOLFile/main_test_MeshStudy.mph

	The meshes used in the study have also been provided in Nastran format. These meshes are in the files
		/.NastranMeshes/Mesh1.nas
		/.NastranMeshes/Mesh2.nas
		/.NastranMeshes/Mesh3.nas
		/.NastranMeshes/Mesh4.nas
		/.NastranMeshes/Mesh5.nas
		/.NastranMeshes/Mesh6.nas

	The Python script used to generate Supplementary Figure 11 and the data reported in Supplementary Table 2 can be found in the folder named "PythonScript".
	The script's name is "mesh_study.py" and it requires the library "matplotlib".
	Input data for the script (described in the section "Mesh Sensitivity Analysis" of the Supplementary Materials) in the following files:
		./PythonScript/data_new/bdp9_mesh1.txt
		./PythonScript/data_new/bdp9_mesh2.txt
		./PythonScript/data_new/bdp9_mesh3.txt
		./PythonScript/data_new/bdp9_mesh4.txt
		./PythonScript/data_new/bdp9_mesh5_production.txt
		./PythonScript/data_new/bdp9_mesh6.txt

	Running the script outputs (at the prompt) the L2-error sequence reported in Supplementary Table 2. In addition, the scripts results in the following figures:
		Output Files: Supplementary Figure 11
			Supplementary_Figure_11.eps
			Supplementary_Figure_11.pdf
			Supplementary_Figure_11.png
			


# NOTE ON MESHES in the COMSOL Multiphysics files
------------------------------------------------
The COMSOL Multiphysics files were created using version 6.2. Opening these files with newer versions of COMSOL Multiphysics and then rebuilding the meshes according to the steps that were originally used to generate said meshes, may introduce subtle changes in the meshes. To prevent such an occurrence, i.e., to preserve the meshes in the form used in our calculations, the meshes the COMSOL Multiphysics files have been locked.
