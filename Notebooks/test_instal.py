import sys
print('System version: ', sys.version)

import IPython
print('IPython version: ', IPython.__version__)


try:
    import numpy as np
    print('Numpy version: ', np.__version__)
except:
    print('No numpy')

try:
    import matplotlib
    print('Matplotlib version: ', matplotlib.__version__)
except:
    print('no matplotlib')

try:
    import pyneb
    print('PyNeb version: ', pyneb.__version__)
except:
    print('no PyNeb')

try:
    import pyCloudy
    print('pyCloudy version: ', pyCloudy.__version__)
except:
    print('no pyCloudy')

try:
    import astropy
    print('Astropy version: ', astropy.__version__)
except:
    print('no astropy')

try:
    import scipy
    print('Scipy version: ', scipy.__version__)
except:
    print('no scipy')

import matplotlib.pyplot as plt

x = np.arange(100)
plt.plot(x, x**2)
plt.show()
