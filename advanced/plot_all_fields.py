import matplotlib.pyplot as plt
import numpy as np

## Load fields
Exr, Exi, Eyr, Eyi, Ezr, Ezi = np.loadtxt('fields.E', usecols=(3,4,5,6,7,8), unpack=True)
Hxr, Hxi, Hyr, Hyi, Hzr, Hzi = np.loadtxt('fields.H', usecols=(3,4,5,6,7,8), unpack=True)

eps = np.loadtxt('epsilon.txt')
field_list = ((Exr, Exi), (Eyr, Eyi), (Ezr, Ezi),
              (Hxr, Hxi), (Hyr, Hyi), (Hzr, Hzi))

[Ex, Ey, Ez, Hx, Hy, Hz] = (np.sqrt(np.add(real**2, imag**2))
                            for real, imag in field_list)
[Ex, Ey, Ez, Hx, Hy, Hz] = (np.reshape(F, (451, 450))
                            for F in (Ex, Ey, Ez, Hx, Hy, Hz))
                            
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
