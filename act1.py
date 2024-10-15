def fun1(n):
  return n*(n+1)/2

print("\n Function1 result= ",fun1(4))

def fun2(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
        
    return sum
print("\n Function2 result= ",fun2(4))

def fun3(n):
    sum = 0
    for i in range(1, n+1):
      for j in range(i, i+1):
        sum += 1
    return sum
      
print("\n Function3 result= ",fun3(4))
