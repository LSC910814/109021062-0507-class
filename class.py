import numpy 

numpy.zeros((2, 3)) #建立一個2*3全為0的陣列
numpy.ones((2, 3, 4)) #建立一個2*3*4全為1的陣列
numpy.arange(1, 10, 2) #建立一個由1開始，不超過10，間格值為2的均勻數
numpy.linspace(0, 10, 5)

a = numpy.array([1, 3, 5, 7, 9]) #一維陣列建立

print(a)

b = numpy.array([(1, 2, 3, 4, 5.01),  (1, 5, 9, 7, 3.01)], dtype = float) #二維陣列

print(b)

c = numpy.array([[(1, 3, 5, 7, 9), (1, 6, 8.3)],[(1, 2, 3, 4, 5), (1, 5, 9, 7.3)]], dtype = float) #三維陣列

print(c)