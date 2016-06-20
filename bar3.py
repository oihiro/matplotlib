# -*- coding:utf-8 -*-
#
# bar3.py
#
# 縦棒グラフサンプル
#
# 参照：bar2.py
#
# A sample code of Matplotlib
# This was created from the Matplotlib sample codes and other documents.
#
# original
# lines_bars_and_markers example code: barh_demo.py — Matplotlib 1.5.1 documentation : http://matplotlib.org/examples/lines_bars_and_markers/barh_demo.html
#
import matplotlib.pyplot as plt
import numpy as np

people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
x_pos = np.arange(len(people))

performance = [10, 20, 50, 80, 100]

color = [[0.4, 0.4, 1] for x in people]

plt.bar(x_pos, performance, align='center', color=color, edgecolor='none')
plt.xticks(x_pos, people)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.tick_params(axis='x', length=0)
plt.tick_params(axis='y', right='off')

plt.gcf().set_facecolor('w')
plt.title('How fast do you want to go today?')
plt.show()
