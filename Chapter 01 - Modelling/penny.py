# The falling penny myth

a = 9.8 # g
h = 381 # s
u = 0

'''
    s = ut + (1/2)a(t**2)
    h = (1/2)a(t**2)
    t = sqrt(2h / a)
'''

t = (2 * h / a) ** 0.5
print(f"{round(t, 2)} s")

'''
    v = u + at
    v = at
'''

v = a * t
print(f"{round(v, 2)} m/s")

'''
We get a velocity on impact of 86ms, which is about 190 miles per hour. That sounds like it could hurt.

Once the penny gets to about 18ms, the upward force of air resistance equals the downward force of gravity, 
so the penny stops accelerating. After that, it doesnt matter how far the penny falls;
it hits the sidewalk (or your head) at about 18ms, much less than 86ms, as the simple model predicts.
'''