# -*- coding:utf-8 -*-
#
# bar4.py
#
# 縦棒と折れ線の二軸グラフサンプル
#
# 参照：bar2.py, bar3.py
#
# A sample code of Matplotlib
# This was created from the Matplotlib sample codes and other documents.
#
# original
# lines_bars_and_markers example code: barh_demo.py — Matplotlib 1.5.1 documentation : http://matplotlib.org/examples/lines_bars_and_markers/barh_demo.html
#
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

"""
font = {'family' : 'monospace',
        'weight' : 'bold',
        'size'   : 'larger'}

mpl.rc('font', **font) 
"""
# タイトルや軸，凡例など全体のフォントサイズを変更する
# ただ，問題もあって，フォントを大きくすると，右のY軸のラベルが表示されなかった。ウィンドウを拡大すると見えてくる。saveFigでは，最初に表示される領域しか保存されない。つまりウィンドウを拡大しないと見えてこない部分は表示されない。
plt.rcParams['font.size'] = 18

people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
x_pos = np.arange(len(people))
performance = [10, 20, 50, 80, 100]
performance2 = [1000, 2000, 5000, 8000, 10000]
color = [[0.4, 0.4, 1] for x in people]
color2 = [[1, 0.4, 0.4] for x in people]

fig, ax1 = plt.subplots()

b1 = ax1.bar(x_pos, performance, align='center', color=color, edgecolor='none')
ax1.set_xlabel('performance')
ax1.set_ylabel('val1')
ax1.spines['top'].set_color('none')
# このtick_paramsはax1.twinx()より前に置くことで，X軸topの目盛り線を消せた
# しかし，X軸bottomの目盛り線は残る
#plt.tick_params(axis='x', top='off')
# top='off'でなく，length=0とすると，X軸はtopもbottomも目盛線を消せた
plt.tick_params(axis='x', length=0)

ax2 = ax1.twinx()
# plotにlabel='val2'とすればlegend引数に指定しなくても凡例にそのラベルが書かれる
p1 = ax2.plot(x_pos, performance2, '-o', color=[1, 0.4, 0.4], linewidth=5, markersize=20, markeredgecolor='none')
ax2.set_ylabel('val2')
plt.xticks(x_pos, people)
# これで縦棒と折れ線の両方の凡例を作ろうとしたのだが，縦棒の凡例しか表示されない。pltに指定するのは不可能なのか？
# b1[0]としてもだめ。
# 但し，pltを使うと，最上位に表示されることが分かった。
# b1[0], p1[0]としなければならないことが分かった。
# loc=2は'upper right'
# frameon=Falseは凡例の枠なし
# markerscale=0は凡例ではマーカなし
plt.legend((b1[0], p1[0]), ('val1', 'val2'), loc=2, frameon=False, markerscale=0)
# ax1を使うと，凡例よりもax2の方が最上位に来る。
#ax1.legend([b1[0], p1[0]], ['val1', 'val2'])

# グラフの最高点がちょうど境界になって切れるので，上下にスペースを開けようとしたが，plt.ylim([0, 120])では，右のY軸が0-120の範囲となって，折れ線グラフが表示されなくなってしまう。
# かと言って，ax1.ylim()は使えない。
# plt.ylim([0, 120])
# ax1及びax2のset_ylimを使えばよかった。
ax1.set_ylim([0, 120])
ax2.set_ylim([0, 12000])

plt.gcf().set_facecolor('w')

# dict(y=0)では，X軸のすぐ上に書かれた。
# dict(y=1)では，topのX軸のすぐ上に書かれた。
# dict(y=1.05)では，そのちょっと上に書かれた。PNGファイルに出力しても軸目盛りとかぶらず，ちょうどよい具合になった。
t = dict(y=1.05)
ax1.set_title('How fast do you want to go today?', **t)
# フォントを大きくすると，右が欠けてしまった。
# 次のようにsubplots_adjustすることによって，全体が表示されるようになった。
# 引数なしのsubplots_adjust()ではだめだった。
# 画面の表示とPNGファイルはまた微妙に位置やサイズが変わるので注意
# 画面の表示では問題なくとも，PNGファイルではタイトルと軸の文字が重なることがあった。
plt.subplots_adjust(left=0.2, right=0.8, top=0.8, bottom=0.2)
plt.savefig('bar4.png')
plt.show()
