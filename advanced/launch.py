#!/usr/bin/python3
import numpy as np
from scipy import interpolate as interp
import subprocess as sp
from multiprocessing import Pool

def send_to_lua(args, l_script='./py_grating.lua'):
	output = sp.check_output(f'S4 -a \"{args}\" {l_script}', shell=True).decode().split('\t')
	return np.asarray(output, dtype=float)

def dict_to_args(indict, newitems={}):
	'''Returns dictionary keys and values as formatted parameters for S4'''
	params = (f'{key}={item}; ' for key, item in {**indict, **newitems}.items())
	return ' '.join(params)

# Geometrical parameters
default_parameters = {
	"n_harm":11, 
	"lambda":600, 
	"a":450, 
	"radius":75, 
	"t_grating":150,
	"RI_cover":1.33, 
	"RI_grating":2.0,
	"RI_substrate":1.45,
	"eps_plot":0,
	"all_field_plot":0}

# Interpolate silicon nitride dispersion with a cubic spline
# Downloaded from refractiveindex.info
wavs = np.arange(600,700,1)
material_wavs, material_n = np.loadtxt('./SiN.csv',
	delimiter=',', unpack=True, skiprows=1)
cubic_spline = interp.splrep(material_wavs*1000, material_n)
RI_grating = interp.splev(wavs, cubic_spline)

# Create a list of parameters to simulate
updated_parameters = ({"lambda": wl, "RI_grating": rig} for wl, rig in zip(wavs, RI_grating))
args = (dict_to_args(default_parameters, u) for u in updated_parameters)

# Send the parameters to S4
spectrum = [send_to_lua(arg) for arg in args]

# Save the output spectrum
specname = "spectrum.txt"
np.savetxt(specname, spectrum, fmt='%.10f', delimiter='\t',\
	header = 'wav\t\t\tinc\t\t\ttrn\t\t\tref')