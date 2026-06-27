#-------------------------------------------------GCD aur LCM — Euclidean Algorithm---------------------------------------------------------
print("==================================================GCD aur LCM — Euclidean Algorithm================================================================")


def gcd(a, b):
    # Euclidean algorithm — O(log min(a,b))
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    # LCM aur GCD ka relation: a*b = gcd*lcm
    return (a * b) // gcd(a, b)

print(gcd(48, 18))  # 6
print(lcm(4, 6))     # 12

print("==================================================Modular Arithmetic — Fast Exponentiation=========================================================")
#-------------------------------------------------Modular Arithmetic — Fast Exponentiation---------------------------------------------------------

def power_mod(base, exp, mod):
    # Binary exponentiation — O(log exp)
    result = 1
    base = base % mod
    
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp // 2
        base = (base * base) % mod
    
    return result

print(power_mod(2, 10, 1000000007))  # 1024

print("===================================================Sieve of Eratosthenes — Prime Numbers Fast======================================================")
#-------------------------------------------------Sieve of Eratosthenes — Prime Numbers Fast---------------------------------------------------------

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    
    return [i for i in range(n + 1) if is_prime[i]]

print(sieve(30))