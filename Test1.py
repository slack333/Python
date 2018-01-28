import random
import os
#d1 = 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9'.split()
deck = '3 K f A z D n W r m C Q A e X 5 m 9 S K 2 3 M J N x x k u s n B A o'.split()


#os.system ('clear')
random.shuffle(deck)
print (random.uniform(1.5, 10))
print (deck)

weighted_choices = [('Red', 3), ('Blue', 2), ('Yellow', 1), ('Green', 4)]
population = [val for val, cnt in weighted_choices for i in range(cnt)]
print (random.choice(population))
