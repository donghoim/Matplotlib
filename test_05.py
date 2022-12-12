#%%
import matplotlib.pyplot as plt


# 기본 사용 - xlim(), ylim()
plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.xlim([0, 5])      # X축의 범위: [xmin, xmax]
plt.ylim([0, 20])     # Y축의 범위: [ymin, ymax]

plt.show()



# 기본사용 - axis()
# axis() 함수에 [xmin, xmax, ymin, ymax]의 형태로 X, Y축의 범위를 지정할 수 있습니다.
# axis() 함수에 입력한 리스트는 반드시 네 개의 값 (xmin, xmax, ymin, ymax)이 있어야 합니다.
# 입력값이 없으면 데이터에 맞게 자동으로 범위를 지정합니다.

plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.axis([0, 5, 0, 20])  # X, Y축의 범위: [xmin, xmax, ymin, ymax]
plt.show()


#옵션 지정하기
plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
# 'on' | 'off' | 'equal' | 'scaled' | 'tight' | 'auto' | 'normal' | 'image' | 'square'

plt.axis('square')
# plt.axis('scaled')
plt.show()


# 축 범위 얻기
plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

x_range, y_range = plt.xlim(), plt.ylim()
print(x_range, y_range)             # (0.85, 4.15) (1.6, 10.4)
axis_range = plt.axis('scaled')
print(axis_range)                   # (0.85, 4.15, 1.6, 10.4)
plt.show()

