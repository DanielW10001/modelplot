# PRJDIR/src/modelplot2f.py

import numpy
import matplotlib.pyplot

NFROM = 0
NTO = 50
NSTEP = 0.0001

nlist = numpy.arange(NFROM, NTO, NSTEP)
flist = [(1-((n-1)**n)/(n**n)) for n in nlist]

matplotlib.pyplot.title(r"$F(N)-N$ when $P(N) \equiv \frac {1} {N}$")
matplotlib.pyplot.xlabel(r"N")
matplotlib.pyplot.ylabel(r"F(N)")
matplotlib.pyplot.plot(nlist, flist,
                       label=r"$F(N) \equiv 1 - \frac {(N-1)^N} {N^N}$")
matplotlib.pyplot.ylim(0.6, 1.05)
matplotlib.pyplot.legend()

matplotlib.pyplot.show()
