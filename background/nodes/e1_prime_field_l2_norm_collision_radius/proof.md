# Proof

Put `N=2h`. For raw representatives `B,B'`, let

```text
a_x=1_(B\B')(x)-1_(B'\B)(x).
```

Exactly `2s` coefficients `a_x` are nonzero. Since
`zeta^(i+h)=-zeta^i`, folding gives

```text
alpha=sum_(i=0)^(h-1) c_i zeta^i,
c_i=a_i-a_(i+h).
```

The `h` embeddings of `Q(zeta)` are indexed by the odd residues `u mod N`.
For `0<=i,j<h`, character orthogonality gives

```text
sum_(u mod N, u odd) zeta^(u(i-j)) = h if i=j, and 0 otherwise.
```

Therefore

```text
sum_(u odd) |sum_i c_i zeta^(ui)|^2 = h sum_i c_i^2 = hS.
```

Apply AM-GM to those `h` squared absolute values. Because `alpha` is nonzero
in characteristic zero for distinct E1 classes,

```text
|Norm(alpha)|^(2/h)
 <= (1/h) sum_(u odd) |sigma_u(alpha)|^2
 = S,
```

which proves `|Norm(alpha)|<=S^(h/2)`.

It remains to control `S`. At one antipodal coordinate, the raw coefficient
profile is one of:

```text
opposite pair: two terms, c_i=+-2, contribution 4;
singleton:     one term,  c_i=+-1, contribution 1;
same-sign pair: two terms, c_i=0,  contribution 0.
```

Let their counts be `a,b,c`. Then

```text
2a+b+2c=2s,       S=4a+b.
```

The integer `b` is even. Unless `b=c=0`, one has
`4s-S=b+4c>=2`, hence `S<=4s-2`. If `b=c=0`, all folded
coefficients are even: `alpha=2 beta`, where `beta` has exactly `s`
coefficients in `{+1,-1}`. The same Parseval argument gives
`|Norm(beta)|<=s^(h/2)`. An odd row prime divides `Norm(alpha)` iff it
divides `Norm(beta)`.

By `e1_pair_feasible_prime_field_reduction`, all live rows are prime-field and
their two exact intervals have lower endpoint at least `2^250`. For `N=256`,
`h/2=64`; monotonicity in `s<=4` reduces the two cases to

```text
14^64<2^250,       4^64=2^128<2^250.
```

For `N=512` and `s=1`, `h/2=128`; the non-even case has `S<=2`, while
the even case has `|Norm(beta)|<=1`. Hence its nonzero norm is also too small
to be divisible by `p`. The collision-norm criterion completes both
exclusions.
