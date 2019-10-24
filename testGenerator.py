def accel(n):
    while n>=1:
        yield int(n)
        n=n/2

def decel(n):
    i=1
    while i<=n:
        yield int(i)
        i=i*2

for i in accel(16):
    print(i)
    
for i in decel(16):
    print(i)
    
    