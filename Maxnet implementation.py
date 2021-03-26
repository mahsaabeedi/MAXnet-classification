import numpy as np

a = [1.2, 1.1 , 1 , 0.9 , 0.95 , 1.15]

# beta is negative 
#all values are added with beta
beta = -3

for i in range(6):
    a[i] = a[i] +( - (beta))


# print(a)


for i in range(len(a))   :
    a[i] = 1/a[i]
    
print(a)

e = 0.15
def MAXNet(data, e):
    print(data)
    print("*****")
    old_data = data
    while 1:
        sum_of_data = sum(old_data)
        new_data = np.subtract(old_data, e * sum_of_data) + np.multiply(old_data, e)
        for i in range(0, len(new_data)):
            if new_data[i] < 0.0:
                new_data[i] = 0.0
        old_data = new_data
        print(new_data)
        non_zero = np.count_nonzero(new_data)
        print("*****")
        if non_zero == 1:
            break


MAXNet(a, e)
