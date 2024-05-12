import numpy as np

q0 = np.array([50,100,60,30,40])
p0 = np.array([6,2,4,10,8])

q1 = np.array([56,120,60,24,36])
p1 = np.array([10,2,6,12,12])

#p1q1
p1q0 = p1 * q0
print("p1q0 =",p1q0)
sum_p1q0 = sum(p1q0)
print("p1q0 =",sum_p1q0)
print()

#p0q0
p0q0 = p0 * q0
print("p0q0 =",p0q0)
sum_p0q0 = sum(p0q0)
print("p0q0 =",sum_p0q0)
print()

#p1q1
p1q1 = p1 * q1
print("p1q1 =", p1q1)
sum_p1q1 = sum(p1q1)
print("p1q1 =",sum_p1q1)
print()

# p0q1
p0q1 = p0 * q1
print("p0q1 =", p0q1)
sum_p0q1 = sum(p0q1)
print("p0q1 =",sum_p0q1)

# Laspeyre's Method
l = sum_p1q0 * 100 / sum_p0q0
print("Laspeyre =",l)
print()

# Paasche's Method
p = sum_p1q1 * 100 / sum_p0q1
print("Paasche =",p)
print()

# Dorbish and Bowley's Method
d = (l + p) / 2
print("Dorbish =",d)
print()

# Fisher's Ideal Index Number
f = np.sqrt(l * p)
print("Fisher =",f)