# how long will you have to wait if busses come every m1, m2, ... , mn minutes
# X be r.v. time to wait for first bus

# 1 bus
# X uniformly random from [0,m]
# E(X) = m/2


# 2 bus
#
import random

N = 1000000
M1 = 10

# 1 bus
E = 0
for repeat in range(N):
    E += M1 * random.random()

print(E / N)
