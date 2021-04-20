from glassnode import GlassnodeClient
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker

gn = GlassnodeClient(api_key='...')

since = '2020-09-01'
interval = '24h'

usdt_btc = gn.get(
    'https://api.glassnode.com/v1/metrics/market/price_usd_close',
    a='BTC',
    s=since,
    i=interval
)

sopr = gn.get(
    'https://api.glassnode.com/v1/metrics/indicators/sopr',
    a='BTC',
    s=since,
    i=interval
)

sns.set_style("white")

fig, ax = plt.subplots()
fig.tight_layout()

# Format X Axis
date_fmt = mdates.DateFormatter('%-d. %b')
ax.xaxis.set_major_formatter(date_fmt)

ax.tick_params(axis=u'both', which=u'both',length=0)
ax.grid(axis='y')

ln1 = sns.lineplot(
    data=sopr, x="t", y="v", ax=ax, label="SOPR",
    estimator=None, color="goldenrod", linewidth=1, legend=False
).set(title="Bitcoin: SOPR", xlabel='', ylabel='')


ax2 = ax.twinx()
ax2.tick_params(axis=u'both', which=u'both',length=0)
ax2.xaxis.set_major_formatter(date_fmt)

sns.despine(left=True, bottom=True)

# Format Price Y Axis
thousands_fmt = ticker.FuncFormatter(lambda x, pos: '$%dK' % round(x/1000) )
ax2.yaxis.set_major_formatter(thousands_fmt)

ln2 = sns.lineplot(
    data=usdt_btc, x="t", y="v", ax=ax2, label="Price [USD]",
    estimator=None, color=".7", linewidth=1, legend=False
).set(xlabel='', ylabel='')

ax.axhline(1, ls='-', linewidth=1, color="black")

fig.legend(loc="upper right", frameon=False, ncol=2)

plt.show()
