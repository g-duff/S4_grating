import matplotlib.pyplot as plt
import numpy as np

## Load fields
Exr, Exi, Eyr, Eyi, Ezr, Ezi = np.loadtxt('fields.E', usecols=(3,4,5,6,7,8), unpack=True)
Hxr, Hxi, Hyr, Hyi, Hzr, Hzi = np.loadtxt('fields.H', usecols=(3,4,5,6,7,8), unpack=True)

eps = np.loadtxt('epsilon.txt')

## Calculate components
Ex = np.sqrt(np.add(Exr**2, Exi**2))
Ey = np.sqrt(np.add(Eyr**2, Eyi**2))
Ez = np.sqrt(np.add(Ezr**2, Ezi**2))

Ex = np.reshape(Ex, (451, 450)) ## (period+1, period)
Ey = np.reshape(Ey, (451, 450))
Ez = np.reshape(Ez, (451, 450))

Hx = np.sqrt(np.add(Hxr**2, Hxi**2))
Hy = np.sqrt(np.add(Hyr**2, Hyi**2))
Hz = np.sqrt(np.add(Hzr**2, Hzi**2))

Hx = np.reshape(Hx, (451, 450))
Hy = np.reshape(Hy, (451, 450))
Hz = np.reshape(Hz, (451, 450))

Efields = [Ex, Ey, Ez]
Efield_names = ["$E_x$", "$E_y$", "$E_z$"]

Hfields = [Hx, Hy, Hz]
Hfield_names = ["$H_x$", "$H_y$", "$H_z$"]

Efig, Eaxes = plt.subplots(ncols=3)

for ax, field, field_name in zip(Eaxes, Efields, Efield_names):
    ax.set_title(field_name)
    ax.pcolormesh(field)
    ax.contour(eps, colors='white', levels=1)
    ax.set_xlabel('x (nm)')
    ax.set_ylabel('z (nm)')
    ax.set_aspect('equal')

Hfig, Haxes = plt.subplots(ncols=3)

for ax, field, field_name in zip(Haxes, Hfields, Hfield_names):
    ax.set_title(field_name)
    ax.pcolormesh(field)
    ax.contour(eps, colors='white', levels=1)
    ax.set_xlabel('x (nm)')
    ax.set_ylabel('z (nm)')
    ax.set_aspect('equal')

Efig.tight_layout()
Hfig.tight_layout()
plt.show()