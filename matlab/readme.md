# 📊 How to Generate Experimental Figures

This guide explains how to reproduce the publication figures using MATLAB.

---

## 🔹 Option 1 — Generate All Figures

Use this option to generate **all figures** at once.

### Steps

1. Download the folder titled `experimental`.
2. Add the `experimental` folder to your MATLAB path.
3. Open the file `figureScript.m`.
4. Click **Run** to generate all publication figures.

---

## 🔹 Option 2 — Generate Selected Figures

Use this option to generate **specific figures only**.

### Steps

1. Download the folder titled `experimental`.
2. Add the `experimental` folder to your MATLAB path.
3. Open the file `figureScript.m`.
4. Run the section titled **Process data sets** to load and process all data into the workspace.
5. Run any individual section **before** the `SUBFUNCTIONS` section to generate the corresponding figure(s).  
   - Each section title specifies which figure it produces.

---

## ✅ Notes

- Ensure all required MATLAB toolboxes are installed.
- Make sure the `experimental` folder is correctly added to your MATLAB path before running any sections.

---
