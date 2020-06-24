# PRJDIR/src/modelplot3f.py

import numpy
import math
import matplotlib.pyplot

NFROM = 0
NTO = 50
NSTEP = 0.0001

nlist = numpy.arange(NFROM, NTO, NSTEP)
flist = [(1-(1-math.sin(n))**n) for n in nlist]

matplotlib.pyplot.title(r"$F(N)-N$ when $P(N) \equiv sin(N)$")
matplotlib.pyplot.xlabel(r"N")
matplotlib.pyplot.ylabel(r"F(N)")
matplotlib.pyplot.plot(nlist, flist,
                       label=r"$F(N) \equiv 1 - (1 - sin(N))^N$")
matplotlib.pyplot.ylim(0, 1.1)
matplotlib.pyplot.legend()

matplotlib.pyplot.show()
