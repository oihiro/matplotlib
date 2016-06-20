# -*- coding:utf-8 -*-
#
# bar1.py
#
# 横棒グラフサンプル
#
# original
# lines_bars_and_markers example code: barh_demo.py — Matplotlib 1.5.1 documentation : http://matplotlib.org/examples/lines_bars_and_markers/barh_demo.html
#
"""
 Simple demo of a horizontal bar chart.
"""
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

# Example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))
plt.barh(y_pos, performance, xerr=error, align='center', alpha=0.4)
plt.yticks(y_pos, people)
plt.xlabel('Performance')
plt.title('How fast do you want to go today?')
plt.show()
