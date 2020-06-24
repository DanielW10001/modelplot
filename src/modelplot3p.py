# PRJDIR/src/modelplot3p.py

import numpy
import math
import matplotlib.pyplot

NFROM = 0
NTO = 50
NSTEP = 0.0001

nlist = numpy.arange(NFROM, NTO, NSTEP)
plist = [math.sin(n) for n in nlist]

matplotlib.pyplot.title(r"$P(N)-N$ when $P(N) \equiv sin(N)$")
matplotlib.pyplot.xlabel(r"N")
matplotlib.pyplot.ylabel(r"P(N)")
matplotlib.pyplot.plot(nlist, plist,
                       label=r"$P(N) \equiv sin(N)$")
matplotlib.pyplot.legend()

matplotlib.pyplot.show()
