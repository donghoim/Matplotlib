#%%

import matplotlib.pyplot as plt

#축 레이블 설정하기
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.xlabel('X-Label')
plt.ylabel('Y-Label')
plt.show()

# 여백 지정하기(padding 값)
plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
plt.xlabel('X-Axis', labelpad=15)
plt.ylabel('Y-Axis', labelpad=20)
plt.show()

# 폰트 설정하기
plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
# x축 폰트, 컬러, 굵기, 사이즈 지정
plt.xlabel('X-Axis', labelpad=15, fontdict={'family': 'serif', 
                                            'color': 'b', 
                                            'weight': 'bold', 
                                            'size': 14})
# y축 폰트, 컬러, 굵기, 사이즈 지정
plt.ylabel('Y-Axis', labelpad=20, fontdict={'family': 'fantasy', 
                                            'color': 'deeppink', 
                                            'weight': 'normal', 
                                            'size': 'xx-large'})
plt.show()


# 폰트를 정의하여 사용도 가능
font1 = {'family': 'serif',
         'color': 'r',
         'weight': 'bold',
         'size': 14
         }

font2 = {'family': 'fantasy',
         'color': 'b',
         'weight': 'normal',
         'size': 'xx-large'
         }

plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
plt.xlabel('X-Axis', labelpad=15, fontdict=font1)
plt.ylabel('Y-Axis', labelpad=20, fontdict=font2)
plt.show()



# 위치 지정하기
plt.plot([1, 2, 3, 4], [2, 3, 5, 10])

# x축 레이블 위치 지정
plt.xlabel('X-Axis', loc='right')

# y축 레이블 위치 지정
plt.ylabel('Y-Axis', loc='top')
plt.show()



