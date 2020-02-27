#!/usr/bin/python3
import numpy as np
from scipy import interpolate as interp
import subprocess as sp
from multiprocessing import Pool

def send_to_lua(args, l_script='./advanced/py_grating.lua'):
	output = sp.check_output(f'S4 -a {args} {l_script}', shell=True).decode().split('\t')
	return np.asarray(output, dtype=float)

# Select output
n_harm = 11
wavs = np.arange(600,700,1)
eps_plot = 0		# 0 false, 1 = true
all_field_plot = 0	# 0 false, 1 = true

# Geometrical parameters
a = 450            # Period
radius = 75        # Radius
t_grating = 150    # Grating thickness 

# Material parameters
RI_cover = 1.33
RI_substrate = 1.45
# RI_grating = interpolated values below:

# Interpolate silicon nitride dispersion with a cubic spline
# Downloaded from refractiveindex.info
material_wavs, material_n = np.loadtxt('./advanced/SiN.csv',
	delimiter=',', unpack=True, skiprows=1)
cubic_spline = interp.splrep(material_wavs*1000, material_n)
RI_grating = interp.splev(wavs, cubic_spline)

# Create a list of parameters to simulate
args = [f"\"lambda={wl}; a={a}; radius={radius}; t_grating={t_grating}; "+\
	f"n_harm={n_harm}; RI_cover={RI_cover}; RI_grating={ri_grating}; "+\
	f"RI_substrate={RI_substrate}; eps_plot={eps_plot}; "+\
	f"all_field_plot={all_field_plot}\""
	for wl, ri_grating in zip(wavs, RI_grating)]

with Pool(processes=3) as pool:
	spectrum = pool.map(send_to_lua, args)

specname = 'spectrum.txt'
np.savetxt(specname, spectrum, fmt='%.10f', delimiter='\t',\
	header = 'wav\t\t\tinc\t\t\ttrn\t\t\tref')