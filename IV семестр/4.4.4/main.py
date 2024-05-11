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
# data = pd.read_csv('data/Hg_green.csv', comment='#')
# x = data['m']
# xerr = 0
# y = (data['h2'] - data['h1']) ** 2
# yerr = 2 * 0.25 * (y ** 0.5)

data = pd.read_csv('data/Na.csv', comment='#')
data = data.query('m != 4')
x = data['m']
xerr = 0
y = (data['h2_light'] - data['h1_light']) ** 2 - (data['h2_dark'] - data['h1_dark']) ** 2
yerr = 4 * 0.1* (y ** 0.5)

# Plot
popt, pcov = curve_fit(lambda x, a, b: a * x + b, x, y, sigma=yerr)

plt.grid()
plt.xlabel(r'$m$')
plt.ylabel(r'$D_1^2 - D_2^2$, mm$^2$')
plt.errorbar(x, y, yerr, xerr, ls='',marker='s', ms=2, capsize=3, label='exp')
plt.plot(np.linspace(x.min(), x.max(), 10),
         (lambda x, a, b: a * x + b)(np.linspace(x.min(), x.max(), 10), *popt),
         label=f'y={round(popt[0], 2)}x+{round(popt[1], 2)}', alpha=0.5)
plt.legend()
# plt.show()
print('a, b, chisq_exp, chisq_th')
print(np.sqrt(np.diag(pcov)), sum(((y - (lambda x, a, b: a * x + b)(x, *popt)) / yerr) ** 2),
      len(x) + (8 * len(x)) ** 0.5)

data['D12 + D22'] = (data['h2_light'] - data['h1_light']) ** 2 + (data['h2_dark'] - data['h1_dark']) ** 2
data['D12 - D22'] = y
data['sigma D2'] = yerr
# print(np.round(data, 3).to_latex())
# plt.savefig('pic/Na(1)', dpi=300)
