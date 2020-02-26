#!/usr/bin/python3
import numpy as np
import subprocess as sp
from multiprocessing import Pool

def send_to_lua(args, l_script='py_grating.lua'):
	output = sp.check_output(f'S4 -a {args} {l_script}', shell=True).decode().split('\t')
	return np.asarray(output, dtype=float)

wavelengths = np.arange(600,700,1)

# Number of harmonics
n_harm = 11

# Geometrical parameters
a = 450            # Period
radius = 75        # Radius
t_grating = 150    # Grating thickness 

# Material parameters
RI_cover = 1.33
RI_grating = 2.0
RI_substrate = 1.45

# Select output
eps_plot = 0		# 0 false, 1 = true
all_field_plot = 0	# 0 false, 1 = true

# Create a list of parameters to simulate
args = [f"\"lambda={wl}; a={a}; radius={radius}; t_grating={t_grating}; \
	n_harm={n_harm}; RI_cover={RI_cover}; RI_grating={RI_grating}; \
	RI_substrate={RI_substrate}; eps_plot={eps_plot}; \
	all_field_plot={all_field_plot}\""
	for wl in wavelengths]

# Send the parameters to S4
spectrum = [send_to_lua(arg) for arg in args]

# Save the output spectrum
specname = "spectrum.txt"
np.savetxt(specname, spectrum, fmt='%.10f', delimiter='\t',\
	header = 'wav\t\t\tinc\t\t\ttrn\t\t\tref')