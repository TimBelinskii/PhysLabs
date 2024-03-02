import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


def fit(x, y, sy):
    D = np.sum(1 / sy ** 2) * np.sum(x ** 2 / sy ** 2) - np.sum(x / sy ** 2) ** 2
    B = np.vstack([[np.sum(x ** 2 / sy ** 2), - np.sum(x / sy ** 2)], [-np.sum(x / sy ** 2), np.sum(1 / sy ** 2)]]) / D
    b = np.vstack([np.sum(y / sy ** 2), np.sum(y * x / sy ** 2)])
    return (np.hstack(np.dot(B, b)), B.diagonal() ** 0.5)


def chi2(y_th, y_exp, y_err):
    return y_th.shape[0] - 1, np.sum((y_th - y_exp) ** 2 / y_err ** 2)


# Settings
# A = 6  # Want figures to be A6
# plt.rc('figure', figsize=[46.82 * .5 ** (.5 * A), 33.11 * .5 ** (.5 * A)])
# plt.rc('text', usetex=True)
# plt.rc('font', family='serif')
# # plt.rcParams.update({'text.latex.unicode': True})
data = pd.read_csv('data/e1t1.csv')

# Processing
data['$\Delta h$'] = 0.2
data['$\Delta \alpha$'] = 1

data['$\mathcal{V}$'] = (data['h4'] - data['h3']) / (data['h4'] + data['h3'])
data['$\delta$'] = data['h1'] / data['h2']
data['$\mathcal{V}_1$'] = 2 * data['$\delta$'] ** 0.5 / (1 + data['$\delta$'])
data['$\mathcal{V}_3$'] = data['$\mathcal{V}$'] / data['$\mathcal{V}_1$']

data['$\Delta\mathcal{V}$'] = data['$\mathcal{V}$'] * (
        data['$\Delta h$'] / (data['h4'] - data['h3']) + data['$\Delta h$'] / (data['h4'] + data['h3']))
data['$\Delta \mathcal{V}_3$'] = data['$\Delta\mathcal{V}$'] / data['$\mathcal{V}$'] * data['$\mathcal{V}_3$']

# Plot
plt.minorticks_on()
plt.grid()
plt.errorbar(data['alpha'], data['$\mathcal{V}_3$'], data['$\Delta \mathcal{V}_3$'], 0.5, ls='',
             label=r'Экспериментальные данные')
# plt.plot(np.linspace(0, 180, 300), np.cos(0.024 * (np.linspace(0, 180, 300) - 25)) ** 2, ls='--', c='r')
plt.xlabel(r'$\alpha,\ ^{\circ}$')
plt.ylabel(r'$\mathcal{V}_3$')
print(fit(np.abs(np.cos(data['alpha'])), data['$\mathcal{V}_3$'], data['$\Delta \mathcal{V}_3$']))
a, d = fit(np.cos(data['alpha']) ** 2, data['$\mathcal{V}_3$'], data['$\Delta \mathcal{V}_3$'])
print(chi2(data['$\mathcal{V}_3$'], a[1] * np.cos(data['alpha']) + a[0], data['$\Delta \mathcal{V}_3$']))
plt.savefig('pic/V(a).png', dpi=300)
#
# data = pd.read_csv('data/e2t1.csv')
# data['$\mathcal{V}$'] = (data['h4'] - data['h3']) / (data['h4'] + data['h3'])
# data['$\delta$'] = data['h1'] / data['h2']
# data['$\mathcal{V}_1$'] = 2 * data['$\delta$'] ** 0.5 / (1 + data['$\delta$'])
# data['$\mathcal{V}_2$'] = data['$\mathcal{V}$'] / data['$\mathcal{V}_1$']
# plt.grid()
# plt.errorbar(data['x'], data['$\mathcal{V}_2$'], 0.1, 0.5, ls='',
#              label=r'Экспериментальные данные')
# plt.xlabel(r'$x,\ см$')
# plt.ylabel(r'$\mathcal{V}_2$')
#
# plt.savefig('pic/V(x).png', dpi=300)
# plt.show()
