# PRJDIR/src/modelplot1f.py

import numpy
import matplotlib.pyplot

NFROM = 0
NTO = 5
NSTEP = 0.0001

nlist = numpy.arange(NFROM, NTO, NSTEP)
flist = [(1-1/n**n) for n in nlist]

matplotlib.pyplot.title(r"$F(N)-N$ when $P(N) \equiv 1 - \frac {1} {N}$")
matplotlib.pyplot.xlabel(r"N")
matplotlib.pyplot.ylabel(r"F(N)")
matplotlib.pyplot.plot(nlist, flist,
                       label=r"$F(N) \equiv 1 - \frac {1} {N^N}$")
matplotlib.pyplot.legend()

matplotlib.pyplot.show()
