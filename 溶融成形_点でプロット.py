import matplotlib.pyplot as plt
import japanize_matplotlib
import numpy as np

T0 = 0  # 初期温度 [K]
TA = 1000  # 表面温度 [K]
density = 1600  # 密度 [kg/m^3]
Cp = 1050  # 比熱 [J/kg*K]
th = 1.26  # 熱伝導率 [W/m*K]  thermal conductivity
x_min = 0  # xの最小値 [mm]
x_max = 200  # xの最大値 [mm]
n_points = 200  # 分割数

heat_capacity = Cp * density # 熱容量 = 比熱 x 密度 どう温度に反映？
cell = (x_max - x_min) / n_points # 表面(x_min)からの距離(x_max)の長さを分割数で割り、プロットする数を出す

temperature_list = [] # グラフにプロットする温度の収納用リスト

for i in range(n_points): # 分割[数]回ループを繰り返す
    q = -th * (TA - T0) / (x_max - x_min)  # 熱流束
    f = (cell * q) * (10^3) / th # cell [mm] 変化後の温度変化
    temperature = TA + f # 前のcellの温度から変化分の温度を足す
    temperature_list.append(temperature) # 温度をリストに追加
    TA = temperature # 前のcellの温度を現在の変化後の温度とする

temperature_list.pop() # 最後の要素を削除
temperature_list.insert(0, 1000) # 新しい温度を先頭に追加

x = np.linspace(x_min, x_max, n_points)

# グラフの作成
plt.scatter(x, temperature_list, marker='o', s=10)  # 点でプロットし、サイズを10に設定
plt.xlabel("距離 x [mm]")
plt.ylabel("温度 T [K]")
plt.title("熱源からの距離と温度の関係")
plt.grid(True)
plt.ylim(0, 1000)  # y軸の範囲を0Kから1000Kに設定
plt.show()
