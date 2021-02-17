n=3
nonprimes = [j for i in range(2, 8) for j in range(i*2, 10, i)]
primes = [x for x in range(2, 7) if x not in nonprimes]

a = [primes for i in range(n)]
print(a)
