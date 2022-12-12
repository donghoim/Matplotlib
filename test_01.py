#%%
import matplotlib.pyplot as plt
import numpy as np


# 기본 그래프 그리기
# y축만 지정
plt.plot([1,2,3,4])
plt.show()

# x, y 축 지정
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()


# 스타일 지정하기
# ro = 원형 마커
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.show()
# b- 파란색 실선
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'b-')
plt.show()

# xmin, xmax, ymin, ymax 지정
plt.axis([0, 6, 0, 20])
plt.show()

# 여러개의 그래프로 그리기

# 200ms 간격으로 균일하게 샘플된 시간
t = np.arange(0., 5., 0.2)

# 빨간 대쉬, 파란 사각형, 녹색 삼각형
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
