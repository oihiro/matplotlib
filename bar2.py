# -*- coding:utf-8 -*-
# 日本語コメントを書くのなら必須。でないと実行時エラーになる。
#
# bar2.py
#
# 横棒グラフサンプル
#
# A sample code of Matplotlib
# This was created from the Matplotlib sample codes and other documents.
#
# original
# lines_bars_and_markers example code: barh_demo.py — Matplotlib 1.5.1 documentation : http://matplotlib.org/examples/lines_bars_and_markers/barh_demo.html
#
"""
Simple demo of a horizontal bar chart.
"""
import matplotlib.pyplot as plt
# 効果はいまだ不明
plt.rcdefaults()
import numpy as np
from matplotlib.ticker import NullLocator

# Example data
# ここにひらがなを入れたら目盛りが表示されなくなった。
# 日本語を表示するならフォント設定が必要
#people = ('あいう', 'Dick', 'Harry', 'Slim', 'Jim')
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
# y_pos = array([0, 1, 2, 3, 4])
y_pos = np.arange(len(people))
"""
配列のスカラーとの演算は，配列の各要素に演算を施した結果の配列となる。
"""
#performance = 3 + 10 * np.random.rand(len(people))
performance = [10, 20, 50, 80, 100]
performance2 = [50, 20, 20, 10, 20]
error = np.random.rand(len(people))

# peopleの数だけ，RGB色のリストのリストを作成
# RGBの各色は0-1の範囲で表す。下記は朱色に近い赤となる。
color = [[1, 0.4, 0.4] for x in people]
color2 = [[0.4, 0.4, 1] for x in people]

"""
barh(bottom, width)
align='center' は横棒の上下に空白領域を設け，横棒自体はセンタリングするとともに，縦軸上の氏名をグラフ横棒の上下中央に配置
align='edge' は上下の空白領域がなくなる。縦軸上の氏名は，横棒の下の線にアラインされる。
alpha=0.x はグラフ横棒の透明度を示す。alpha指定なしは横棒色が青。alpha=0.1は非常に薄い青
height=0.5 heightは横棒の太さ（つまりy軸方向の幅）を示す。0.5は，横棒と空白部分（隣の横棒までの間）の太さが同じ
color=color 横棒の色
edgecolor=None としてもbar境界線の色は黒で変わらず。
edgecolor='w'とすると，境界線が白となり，見えないのと同じになった。
edgecolor='none'は色なしとなる。
facecolor='g' としたらcolor設定は無視され横棒の色が緑になった。
"""
plt.barh(y_pos, performance, height=0.5, align='center', color=color, edgecolor='none')

# 積み上げ横棒グラフ
# leftを指定する
plt.barh(y_pos, performance2, left=performance, height=0.5, align='center', color=color2, edgecolor='none')

# yticksを行わなかったら，-1 〜 5がy軸のテキストとして表示された。
plt.yticks(y_pos, people)
plt.xlabel('Performance')
ax = plt.gca() # gca stands for 'get current axis'
# 右と上の軸の線がなくなった。しかし，spines[].set_color('none')だけでは，内向きの短い線は残ってしまう。
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 下記のようにすると，X軸の目盛りの文字と線がどちらも表示されなくなる
#ax.xaxis.set_major_locator(NullLocator())
# Y軸の目盛りの線は表示させないようにすることができた。しかし，X軸方向は残る。しかも，上の境界には残るのが厄介
plt.tick_params(axis='y', length=0)
# X軸の上の目盛り線を消すことができた！ matplotlibのAPIを調べて分かった
plt.tick_params(axis='x', top='off')

# 周囲の余白の大きさ　0.1, 0.9がデフォルト
#plt.subplots_adjust(left=0.2, right=0.8, top=0.8, bottom=0.2)

# 余白は白になったが，グラフとy軸目盛りは表示されなくなってしまった
# と思ったら，Figure1とFigure2が生成され，Figure1の上にFigure2が載っていたのであった。
# これはFigure2を作ったに過ぎない
#plt.figure(facecolor='w')

# これで余白が白になった。
plt.gcf().set_facecolor('w')
# 余白は青
#plt.gcf().set_facecolor('b')


plt.title('How fast do you want to go today?')
plt.show()
