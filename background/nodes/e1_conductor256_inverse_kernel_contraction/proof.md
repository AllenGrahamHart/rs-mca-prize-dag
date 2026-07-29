# Proof

Write the discrete Fourier transform as

```text
xhat_j=sum_t x_t exp(-2 pi i jt/64).
```

The character-diagonal router proves

```text
lambdahat_j=kappa_j xihat_(-j),       kappa_j!=0 for j!=0.   (1)
```

Both `xi` and `lambda` have coordinate sum zero. Reindexing `j` by `-j` in
the inverse transform and substituting the transform of `lambda` therefore
gives

```text
xi_t
 = (1/64) sum_(j=1)^63 lambdahat_j kappa_j^(-1)
       exp(-2 pi i jt/64)
 = sum_s q_(t+s) lambda_s.                                (2)
```

Conjugacy of `kappa_j` and `kappa_(64-j)` makes every `q_r` real. Since
`sum_s lambda_s=0`, subtracting any real constant `c` from the kernel in
(2) changes nothing. Thus

```text
|xi_t| <= max_r |q_r-c| ||lambda||_1.                     (3)
```

Choose `c=(max q+min q)/2`. The maximum coefficient in (3) is half the
range of `q`, proving the first inequality in `(IKC4)`. Taking `c=0`, summing
(2) over `t`, and using cyclic invariance gives

```text
sum_t |xi_t|
 <= sum_s |lambda_s| sum_t |q_(t+s)|
 = ||lambda||_1 sum_r |q_r|,                              (4)
```

which is the second inequality.

The verifier imports the hash-pinned directed-Decimal spectrum construction.
For each nonzero `kappa_j` rectangle it encloses

```text
kappa_j^(-1)=conj(kappa_j)/|kappa_j|^2
```

using outward interval multiplication and division. It then evaluates all
64 sums in `(IKC1)` against the certified root-of-unity table. Conjugate
pairing is checked by requiring every imaginary interval to contain zero.
The printed real intervals prove `(IKC2)` without binary floating point.

Finally `(IKC5)` follows from the proved strict prize radius. Each coordinate
of `xi` is an integer, so the first strict bound gives `|xi_t|<=3`. If
`P=sum_{xi_t>0}xi_t`, zero sum gives

```text
sum_t |xi_t|=2P,
```

an even integer. The strict bound below `61.92` therefore gives at most 60.
QED.
