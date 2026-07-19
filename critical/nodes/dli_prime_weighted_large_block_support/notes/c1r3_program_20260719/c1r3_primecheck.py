# find three primes just under 2^60 (deterministic MR for < 2^64) + sanity MR tests
def is_prime(n):
    if n < 2: return False
    for p in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n % p == 0: return n == p
    d, s = n-1, 0
    while d % 2 == 0: d //= 2; s += 1
    for a in (2,3,5,7,11,13,17,19,23,29,31,37):
        x = pow(a, d, n)
        if x in (1, n-1): continue
        for _ in range(s-1):
            x = x*x % n
            if x == n-1: break
        else: return False
    return True
found = []
n = (1 << 60) - 1
while len(found) < 3:
    if is_prime(n): found.append(n)
    n -= 2
print("primes:", [f"(1<<60)-{(1<<60)-p}" for p in found], found)
# MR sanity: known primes/composites
assert is_prime(7340033) and is_prime(13631489) and is_prime(23068673) and is_prime(104857601) and is_prime(167772161)
assert is_prime(63361) and is_prime(65921) and is_prime(204353) and is_prime(65537)
assert not is_prime(1048577) and not is_prime(16777217)
print("MR sanity PASS (7*2^20+1, 13*2^20+1, 11*2^21+1, 25*2^22+1, 5*2^25+1 all prime; 2^20+1, 2^24+1 composite)")
