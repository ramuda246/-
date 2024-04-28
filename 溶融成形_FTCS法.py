import matplotlib.pyplot as plt
import numpy as np

# input parameter
den = 1600.0  # 密度
cp = 1050.0  # 比熱
cond = 1.26  # 熱伝導率
temp_bc = 1000.0  # 温度固定の境界条件
temp_init = 0.0  # 温度の初期値
lx = 0.2  # 横の長さ[m]
nx = 101  # 空間分割点数
tend = 3600.0  # 計算期間
dt = 0.5  # 時間刻み
tout = 600.0  # 結果出力の時間間隔

alpha = cond / (den * cp)  # 熱拡散率
dx = lx / (nx - 1)  # 空間分割の幅
nt = int(tend / dt)  # 時間のステップ数
nout = int(tout / dt)  # 結果出力のステップ間隔

# initial condition
temp = np.full(nx, temp_init)  # 離散化した各点の温度が入る配列
time = 0.0  # 初期時間は0.0秒

temp_new = np.zeros(nx)

# Boundary condition
temp[0] = temp_bc  # Dirichlet @ x=0
temp[nx - 1] = temp[nx - 2]  # Neumann @ x=Lx

# graph data array
fig, ax = plt.subplots(figsize=(10, 6))

# x軸を200mm単位で表示
gx = np.linspace(0, lx * 1000, nx)  # 0からlx * 1000まで200mm刻みで生成

# time loop
for n in range(1, nt + 1):
    # FTCS
    for i in range(1, nx - 1):
        temp_new[i] = temp[i] + dt * alpha * (temp[i + 1] - 2.0 * temp[i] + temp[i - 1]) / (dx * dx)

    # update
    for i in range(1, nx - 1):
        temp[i] = temp_new[i]

    # Boundary condition
    temp[0] = temp_bc  # Dirichlet @ x=0
    temp[nx - 1] = temp[nx - 2]  # Neumann @ x=Lx

    time += dt

    if n % nout == 0:
        ax.plot(gx, temp, label=f'Time = {time} [s]')

# graph plot
ax.set_xlabel('x [mm]')  # x軸ラベルをmm単位に変更
ax.set_ylabel('Temperature [C]')
ax.grid()
ax.legend()
plt.show()
