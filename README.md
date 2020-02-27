# S4 grating

A 1D grating in [S<sup>4</sup>](https://web.stanford.edu/group/fan/S4/)

### Standard
* Run the grating simulation with `S4 grating.lua`
* `grating.lua` saves incident, transmitted and reflected intensity to `spectrum.txt`
* Plot `spectrum.txt` with your favourite plotting software 
    * or `python plot_spectrum.py`

### Notes
* On windows, place S4.exe in the same folder as you run `S4 grating.lua` from

## Advanced

### Python launch
* Run the grating simulation with `python launch.py`
* `python launch.py` calculates a cubic spline from `SiN.csv` to more accurately model a silicon nitride grating
* The simulation saves incident, transmitted and reflected intensity to `spectrum.txt`
* Plot the spectrum as above

### Field plots
* Under `# select output`, change `eps_plot` and/or `all_field_plot` from 0 to 1
* Run the grating simulation with `python launch.py`
* Plot the fields by running `plot_all_fields.py`

### Parallel python launch
* Relavent for machines with 2+ cores and models with a high (~50+) number of harmonics
* Run the grating simulation with `python parallel_launch.py`
* The simulation saves incident, transmitted and reflected intensity to `spectrum.txt`
* Plot the spectrum as above

