import matplotlib.pyplot as plt
import pandas as pd

usd_df = pd.read_csv('usd.csv', delimiter=';')
eur_df = pd.read_csv('eur.csv', delimiter=';')

fig, axes = plt.subplots(2, 1, figsize=(12, 14), gridspec_kw={'height_ratios': [1, 2]})

usd_df.head(5).plot.barh(x='Bank', y=['Buy', 'Sale'], title='USD', ax=axes[0], rot=0, edgecolor = 'black')
axes[0].set_xlabel('Price')
axes[0].set_ylabel('Bank')
eur_df.plot.barh(x='Bank', y=['Buy', 'Sale'], title='EUR', ax=axes[1], edgecolor='black')
axes[1].set_xlabel('Price')
axes[1].set_ylabel('Bank')

plt.tight_layout()
plt.show()