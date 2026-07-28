# Proof

The prime-field reduction gives the exact prize budget interval

```text
I_P=[B_P 2^128,(B_P+1)2^128-1]
```

and proves that every pair-feasible row in it has odd prime characteristic
`p=1 mod N`. Direct integer comparison gives `B_P>2^127`, hence

```text
p>2^255,                 2p>2^256.                    (1)
```

Represent two distinct classes by signed singleton vectors `x,y` and put
`d=x-y`. Their support sizes have the same parity as `ell`. Reducing modulo
two, signs disappear, so

```text
sum_i d_i = |supp(x)|-|supp(y)| = ell-ell = 0 (mod 2). (2)
```

Let `zeta` be the relevant 2-power root and `pi=1-zeta`, the unique prime
above two. Since `zeta=1 mod pi`, equation (2) gives

```text
alpha=sum_i d_i zeta^i = 0 (mod pi).
```

The difference polynomial is nonzero and has degree below the cyclotomic
degree, so `alpha` is nonzero. Divisibility by `pi` therefore implies that
the positive integer

```text
R=|Norm(alpha)|
```

is divisible by `Norm(pi)=2`. In particular `R` is even.

For `N=256`, the cyclotomic degree is 128 and the folded L2 theorem gives
`R<=S^64`. Thus `S<=16` implies

```text
R<=16^64=2^256.
```

For `N=512`, the degree is 256 and the same theorem gives `R<=S^128`.
Thus `S<=4` implies

```text
R<=4^128=2^256.
```

In either case, (1) gives `0<R<2p`. If a finite-field collision occurred,
the collision-norm criterion would give `p|R`, forcing `R=p`. This is
impossible because `R` is even while `p` is odd. The next possible square
mass is two larger because class-difference square mass is even.
