import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

# data = pd.read_csv('data/3-5.csv', comment='#')
#
# popt, pcov = curve_fit(lambda x, a, b: a * x + b, data['z'], data['m'])
#
# plt.grid()
# plt.xlabel(r'Номер совмещенной полосы, $m$')
# plt.ylabel(r'Отсчет по компенсатору, $z$')
# plt.errorbar(data['m'], data['z'], 9, 0.2, ls='', label='Эксп. данные')
# plt.plot(np.linspace(-7, 10, 10), (lambda x, a, b: a * x + b)(np.linspace(-7, 10, 10), *popt),
#          label=f'y={round(popt[0], 2)}x+{round(popt[1], 2)}', alpha=0.5)
# plt.legend()
# # plt.show()
# plt.savefig('pic/3-5.png', dpi=300)

# data = pd.read_csv('data/6-7.csv', comment='#')
# lmbd, l = 670 * 1e-9, 0.1
#
# data['m'] = (lambda x, a, b: a * x + b)(data['z'], *popt)
# data['$\delta n$'] = data['m'] * lmbd / l
# np.round(data, 2)
#
# popt, pcov = curve_fit(lambda x, a, b: a * x + b, data['P'], data['$\delta n$'])
#
# plt.grid()
# plt.xlabel(r'Разность давлений $\Delta P$, мм. вод. ст.')
# plt.ylabel(r'Разность показателей преломления $\delta n$')
# plt.errorbar(data['P'], data['$\delta n$'], 0.1 * data['$\delta n$'].iloc[-1], 25, ls='', label='Эксп. данные')
# plt.plot(np.linspace(-600, 500, 10), (lambda x, a, b: a * x + b)(np.linspace(-600, 500, 10), *popt),
#          label=f'y=({round(popt[0] * 1e8, 2)}e-8)x {round(popt[1] * 1e6, 2)}e-6', alpha=0.5)
# # plt.show()
# plt.legend()
# plt.savefig('pic/6-7.png', dpi=300)

data = pd.read_csv('data/8-11.csv', comment='#')
print(data.to_latex())
