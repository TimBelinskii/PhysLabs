import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import re

# Settings
A = 6  # Want figures to be A6
plt.rc('figure', figsize=[46.82 * .5 ** (.5 * A), 33.11 * .5 ** (.5 * A)])
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
# plt.rcParams.update({'text.latex.unicode': True})
data = pd.read_csv('data/2.csv', comment='#')


def sin(x):
    return np.sin(x * np.pi / 180)


def cos(x):
    return np.cos(x * np.pi / 180)


tmp = []
for row in data['phi']:
    deg, min, sec, empty = re.split('[*\'\"]', row)
    tmp.append(-float(deg) - float(min) / 60 - float(sec) / 3600 + 180 + 44 / 60 + 40 / 3600)
data['delta'] = tmp
data['n'] = sin((data['delta'] + 63 + 10 / 60 + 6 / 3600) / 2) / sin((63 + 10 / 60 + 6 / 3600) / 2)

dn_dd = cos((data['delta'] + 63 + 10 / 60 + 6 / 3600) / 2) / sin((63 + 10 / 60 + 6 / 3600) / 2) / 2
dn_da = (cos((data['delta'] + 63 + 10 / 60 + 6 / 3600) / 2) * sin((63 + 10 / 60 + 6 / 3600) / 2) - cos(
    (63 + 10 / 60 + 6 / 3600) / 2) * sin((data['delta'] + 63 + 10 / 60 + 6 / 3600) / 2)) / 2 / (
                sin((63 + 10 / 60 + 6 / 3600) / 2) ** 2)
data['sn'] = np.sqrt((dn_dd * 10 / 3600) ** 2 + (dn_da * 10 / 3600) ** 2)

x = data['lmbd'][:-2]
xerr = 0
y = data['n'][:-2]
yerr = data['sn'][:-2]

# Plot
popt, pcov = curve_fit(lambda x, a, b: a * x + b, x, y, sigma=yerr)

plt.grid()
plt.xlabel(r'wavelength $\lambda$,\ nm')
plt.ylabel(r'refractive index $n$')
plt.errorbar(data['lmbd'], data['n'], data['sn'], xerr, ls='', marker='s', ms=5, label='exp data')
plt.plot(np.linspace(x.min(), x.max(), 10),
         (lambda x, a, b: a * x + b)(np.linspace(x.min(), x.max(), 10), *popt),
         label=f'y={round(popt[0] * 10 ** 5, 2)}e-5 x+{round(popt[1], 2)}', alpha=0.5)
plt.legend()
# plt.show()
data = np.round(data, 3)
print(np.sqrt(np.diag(pcov)))
# plt.savefig('pic/n(lmbd)', dpi=300)
