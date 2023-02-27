import random

def estimate_pi(num):
    random.seed(2**32)
    #pi*r^2=surface of circle, according to law of large number for probabilities, number of bean scattered in a square is even distributed.
    total, hit=0,0
    pre_pi, cur_pi=0.0, 3.0
    while True:
        #total, hit = 0, 0
        for i in range(num):
            x,y=random.random(), random.random()
            if x**2+y**2 <=1.0:
                hit+=1
            total+=1
        pre_pi = cur_pi
        cur_pi = 4*hit/float(total)
        #print pre_pi, cur_pi
        if abs(3.151-cur_pi)<=0.005:
            return cur_pi

print estimate_pi(100)