import matplotlib.pyplot as plt
import numpy as np

P=np.array([[5.09, 1.69], [5.38, 3.14], [3.54, 3.87], [2.42, 4.92], [0.69, 4.37], [-0.56, 2.96]])

# (x − 4)^2 + (y + 1)^2 = 8

T = np.linspace(0, 2*np.pi,5000) #задаем окружность параметрически
X = 4 + 8**0.5*np.cos(T)
Y = -1 + 8**0.5*np.sin(T)

plt.scatter(P[:,0], P[:,1])
plt.plot(X, Y)
plt.grid()
plt.show()


avgRadius=np.zeros(len(T))  #средний радиус до точек в конкретной точке окружности      
squareSum=np.zeros(len(T))  #сумма квадратов радиусов до точек в конкретной точке окружности
for i in range(len(T)):
    x=X[i]
    y =Y[i]
    sum=0
    distance=[]
    for j in range(len(P)):
        tempDistance=((x-P[j][0])**2+(y-P[j][1])**2)**0.5   #расстояние от точки до окружности
        sum+=tempDistance   
        distance.append(tempDistance)
    avg=sum/len(P)                                          #среднее расстояние до точек в конкретной точке окружности
    avgRadius[i]=avg
    for j in range(len(P)):
        squareSum[i]+=(distance[j]-avg)**2                  #считаем сумму квадратов расстояний до окружности




def golden_ratio_search(s,a,b):     #метод золотого сечения для массива 
    g=(5**0.5-1)/2
    n=44
    for i in range(n):
        b1=int(a+(b-a)*g)
        a1=int(b-(b-a)*g)
        if s[a1]<s[b1]:
            b=b1
            best=a1
        else:
            a=a1
            best=b1
    return best

plt.plot(T, squareSum)
plt.grid()
plt.show()


t=golden_ratio_search(squareSum,0,len(squareSum)-1)

newX=X[t]+avgRadius[t]*np.cos(T)   #подставляем средний радиус, координаты x и y для полученной точки и находим формулу окружности
newY=Y[t]+avgRadius[t]*np.sin(T)
plt.scatter(P[:,0], P[:,1])
plt.plot(newX, newY)
plt.plot(X, Y)
plt.grid()
plt.show()


