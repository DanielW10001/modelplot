# PRJDIR/src/modelplot2p.py

import numpy
import matplotlib.pyplot

NFROM = 0.25
NTO = 10
NSTEP = 0.0001

nlist = numpy.arange(NFROM, NTO, NSTEP)
plist = [1/n for n in nlist]

matplotlib.pyplot.title(r"$P(N)-N$ when $P(N) \equiv \frac {1} {N}$")
matplotlib.pyplot.xlabel(r"N")
matplotlib.pyplot.ylabel(r"P(N)")
matplotlib.pyplot.plot(nlist, plist,
                       label=r"$P(N) \equiv \frac {1} {N}$")
matplotlib.pyplot.legend()

matplotlib.pyplot.show()
