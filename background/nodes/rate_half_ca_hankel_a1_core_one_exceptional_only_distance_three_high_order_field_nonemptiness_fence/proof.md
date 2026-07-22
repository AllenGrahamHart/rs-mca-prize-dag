# Proof

The verifier supplies a recursive Lucas certificate for each displayed
integer. At every certified integer `n`, it records the complete prime
factorization of `n-1`. For each distinct prime divisor `q` of `n-1`, it
records a witness `a_q` satisfying

```text
a_q^(n-1)=1 mod n,
gcd(a_q^((n-1)/q)-1,n)=1.                           (1)
```

Suppose a prime `l` divides `n`. Equation `(1)` implies that the order of
`a_q mod l` contains the full `q`-part of `n-1`. Applying this for every
`q | n-1` shows `n-1 | l-1`, hence `l>=n`. Therefore `n` is prime. The
certificate bottoms out at integers at most `1000`, checked by trial
division.

The top-level factorizations are

```text
p_(e/3)-1
 =2^42 * 13 * 174763 * 524287 * 21487
  *1661926226357084884519,

p_e-1
 =2^41 * 3^2 * 757 * 174763 * 9187 * 524287
  *14833675282790944213.
```

They prove `N | p_g-1`. Since

```text
e=3*174763*524287,
```

the same factorizations give the two gcd identities in `(HOF1)`. Direct
integer division places both primes between `B*2^128` and `(B+1)*2^128`.
Finally,

```text
r=7*79*8191*121369,
```

and none of these factors occurs in either displayed factorization of
`p_g-1`. Hence `gcd(r,p_g-1)=1` in both cases, completing `(HOF1)`. QED.
