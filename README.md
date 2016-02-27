#PandaFalls

## Waterfall Charts
A waterfall chart is a data visualization that is used to present cumulative effects of variables introduced in an equation. Therefore, an abstraction of a waterfall chart is simply an equation, such as the one below:
```
Profit = Revenue - Costs
```

Currently, waterfall charts are created with stacked bar charts. An invisible "placeholder bar" is calculated and placed beneath the next bar. For example,
```
Revenue = $500
Costs = $200
```
There would be three stacked bars: Revenue, Costs, Profit
Revenue is easy to plot, just a single bar with value of $500
Cost is a bit more difficult, we have to plot $200 on top of a $300 "invisible" bar 
Profit would simply be the difference between $500 and $200 = $300 bar.

## Goal
I wanted to create a simple function to use a pandas dataset and output a waterfall chart.
