# CV Probe Data Analysis

## Setup

## Files
- `Data/` Folder. Raw and Parsed/Aggregated Data

  - `Raw`: Export a PROJECT from the tool software, then copy the folder  
    containing the desired runs into `Raw`. Child directories should be  
    formatted `Run1`, `Run2`, etc. and contain the following:  
    - An excel `*.xls` file containing the Voltage VS Capacitance Sweep  
    - A markup `.xml` file containing the name (aka "username") given to the run  
    - **NOTE:** Owing to large file size, `Data/Raw` is git-ignored.  

  - `Parse_Data.ipynb`:
    1. Parses File Names. Auto-detects and parses most naming conventions; <u>_see file for docs._</u>
    2. Aggregates Cp and Gp data from only **Named Runs** into CSVs.

  - `Selected_Measurements.csv`
    - Indicies: Run Numbers
    - Columns: `username`, `wafer_num`, `pos`, `cap_diam` (um), `cap_ind`, `flags`
  - `Cp_by_Measurement.csv`
    - Indicies: Run Numbers
    - Columns: The same as `Selected_Measurements` plus each point of the voltage sweep.
    - Data: Same as `Selected_Measurements` plus the <u>**capacitance**</u> at each voltage.
  - `Gp_by_Measurement.csv`
    - Indicies: Run Numbers
    - Columns: The same as `Selected_Measurements` plus each point of the voltage sweep.
    - Data: Same as `Selected_Measurements` plus the <u>**conductance**</u> at each voltage.

  - _My convention: `X_by_Y` means `X` Columns (predictors, dimensions) by `Y` Indicies (datapoints)._

- `Analysis/` Folder. Plotting, regression, correlation finding.

  - `Estimate_Eps_r.ipynb`
    - estimates the true dielectric constant $\epsilon_{r}$ at the measurement  
      frequency via minimizing MSE between theoretical and measured capacitances $C_{p}$ across  
      all measurements and voltages. Use same frequency for all CV measurements.  
    - Also finds the $\tan(\delta)$ that minimizes the MSE between theoretical and measured  
      conductances $G_{p}$.  
    - Also calculates the median derived $\epsilon_{r}$ and $\tan(\delta)$   
      **Note:** Requires parallel plate assumption!!!
  - `Expected_Cp_Gp_by_Diameter.ipynb`
    - After putting either the min-MSE or median $\epsilon_{r}$ and $\tan(\delta)$ into  
      `_Constants.py`, calculates the expected $C_{p}$ and $G_{p}$ values for each dimaeter  
      capcitor specified in `_Constants.py`.
  - `Selected_Graphs.ipynb`
    - Line plots of expected capcitance by area and measured capacitance by area:
      - Divided by wafer, then group
      - Divided by wafer only

- `Figures/` Folder. Where figures and tables are saved.