import code
from scipy.misc import ascent
import numpy as N


ascent = ascent()
noisy_ascent = ascent + ascent.std()*0.5*N.random.standard_normal(ascent.shape)
# Convolution
Assignment3.convolution(ascent)
Assignment3.convolution(noisy_ascent)
print("Convolution: The robustness of the filter is relatively low to the presence of noise.")
print()
# Filter
Assignment3.filter(ascent)
Assignment3.filter(noisy_ascent)
print("Filtering: When applying the Gauss Filter, the images became blurrier as the value of variance increased.")
print("When applying the Gauss Laplace filter, the noise in the images and a same shade of gray become much more")
print("apparent as the value of variance increased. But when the value reached 7, the image became black.")
