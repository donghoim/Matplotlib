#%%

import matplotlib.pyplot as plt

## 기본 사용하기
plt.plot([1, 2, 3, 4], [2, 3, 5, 10], label='Price ($)')
plt.xlabel('X-Axis')        # x축 레이블명
plt.ylabel('Y-Axis')        # y축 레이블명
plt.legend()

plt.show()


## 위치 지정하기
plt.plot([1, 2, 3, 4], [2, 3, 5, 10], label='Price ($)')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
# plt.legend(loc=(0.0, 0.0))    # 그래프 좌측 모서리
# plt.legend(loc=(0.5, 0.5))    # 그래프 중간에
# plt.legend(loc=(1.0, 1.0))    # 그래프 우측 모서리 밖
plt.legend(loc=('lower right'))
plt.show()



# 열 개수 지정하기
# ncol = 범례 텍스트의 열 개수 표시 (1: 열 1개, 2: 열 2개)
plt.plot([1, 2, 3, 4], [2, 3, 5, 10], label='Price ($)')
plt.plot([1, 2, 3, 4], [3, 5, 9, 7], label='Demand (#)')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.legend(loc='best')          # ncol = 1
# plt.legend(loc='best', ncol=2)    # ncol = 2
plt.show()


# 범례 폰트 지정하기
plt.plot([1, 2, 3, 4], [2, 3, 5, 10], label='Price ($)')
plt.plot([1, 2, 3, 4], [3, 5, 9, 7], label='Demand (#)')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
# plt.legend(loc='best')
plt.legend(loc='best', ncol=2, fontsize=14)
plt.show()

# 범례 테두리 꾸미기
plt.plot([1, 2, 3, 4], [2, 3, 5, 10], label='Price ($)')
plt.plot([1, 2, 3, 4], [3, 5, 9, 7], label='Demand (#)')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
# frameon = 범례 텍스트 상자의 테투리 표시할지 여부 선택
plt.legend(loc='best', ncol=2, fontsize=14, frameon=True, shadow=True)
plt.show()
