def IsPrime(a):
  if(a<2):
    return False
  for i in range(2,a):
    if(a%i==0):
      return False
  return True

def prime_list(n):
    prime = []
    for i in range(n+1):
        if(IsPrime(i)):
            prime.append(i)
    return prime

print(prime_list(100))