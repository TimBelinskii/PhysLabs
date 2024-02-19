import pandas as pd
from matplotlib import pyplot as plt

# Settings
A = 6  # Want figures to be A6
plt.rc('figure', figsize=[46.82 * .5**(.5 * A), 33.11 * .5**(.5 * A)])
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
# plt.rcParams.update({'text.latex.unicode': True})
f4 = pd.read_csv('data/4.csv')


# Plot
plt.errorbar(f4['отр']/2, f4['преломл_обыкн'], 0.5, 0.5, label=r'dsf')
plt.errorbar(f4['отр']/2, f4['преломл_необыкн'], 0.5, 0.5, label=r'adsf')
plt.xlabel(r'Угол от $\varphi_1, ^{\circ}$')
plt.text(7, 70, r'$R = t^2$')
plt.legend(fontsize=8)
plt.show()
