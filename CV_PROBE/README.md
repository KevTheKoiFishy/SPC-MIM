# CV Probe Data Analysis

## Setup

## Files
- `Data/` Folder. Raw and Parsed/Aggregated Data

  - `Raw`: Export a PROJECT from the tool software, then copy the folder  
    containing the desired runs into `Raw`. Child directories should be  
    formatted `Run1`, `Run2`, etc. and contain the following:  
    - An excel `*.xls` file containing the Voltage VS Capacitance Sweep  
    - A markup `.xml` file containing the name (aka "username") given to the run  
    - **NOTE:** Owing to large file size, `Data/Raw` is not tracked by git.  

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

  - `Eps_R_Estimate.ipynb` estimates the true dielectric constant at the measurement  
    frequency via minimizing MSE between theoretical and measured capacitances across  
    all measurements and voltages. Use same frequency for all CV measurements.  
    Requires parallel plate assumption.

- `Figures/` Folder. Where figures and tables are saved.