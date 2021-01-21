# get p and q
def rsa_moder(n):
    base = 2
    while base < n:
        if n % base == 0:
            return base, n // base
        base += 1




# solve Euler f(n)
def rsa_get_euler(prime1, prime2):
    return (prime1 - 1) * (prime2 - 1)


# get private key
def rsa_get_key(e, euler):
    k = 1
    while True:
        if (((euler * k) + 1) % e) == 0:
            return (euler * k + 1) // e
        k += 1


# we have n and e, need to calculate d(or have n,d to calculate e)
def get_rsa_e_d(n, e=None, d=None):
    if e is None and d is None:
        return

    arg = e
    if arg is None:
        arg = d

    primes = rsa_moder(n)
    p = primes[0]
    q = primes[1]

    d = rsa_get_key(arg, rsa_get_euler(p, q))
    print(p)
    print(q)

    return d

print(get_rsa_e_d(10539750919,49))

