import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

# Settings
A = 6  # Want figures to be A6
plt.rc('figure', figsize=[46.82 * .5 ** (.5 * A), 33.11 * .5 ** (.5 * A)])
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
# plt.rcParams.update({'text.latex.unicode': True})
data = pd.read_csv('data/3-5.csv', comment='#')
# x =
# xerr =
# y =
# yerr =

# Plot
popt, pcov = curve_fit(lambda x, a, b: a * x + b, data['z'], data['m'])

plt.grid()
plt.xlabel(r'')
plt.ylabel(r'')
plt.errorbar(x, y, yerr, xerr, ls='', label='Эксп. данные')
plt.plot(np.linspace(x.min(), x.max(), 10),
         (lambda x, a, b: a * x + b)(np.linspace(x.min(), x.max(), 10), *popt),
         label=f'y={round(popt[0], 2)}x+{round(popt[1], 2)}', alpha=0.5)
plt.legend()
plt.show()
# plt.savefig('pic/', dpi=300)
