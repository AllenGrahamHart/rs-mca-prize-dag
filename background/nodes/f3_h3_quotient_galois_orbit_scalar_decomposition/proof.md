# Proof

Fix `(u,v)` and put `m=min(v_2(u),v_2(v))`. An odd residue `r` fixes the
ordered pair exactly when

```text
(r-1)u=(r-1)v=0 mod 2^s.                           (1)
```

The two congruences in `(1)` are jointly equivalent to
`r=1 mod 2^(s-m)`. There are `2^m` such odd residues modulo `2^s`. Since
`|G|=2^(s-1)`, orbit-stabilizer proves `(QOD2)`.

To count the orbits with minimum valuation `m`, put `L=2^(s-m)`. There are
`L-1` nonzero residues divisible by `2^m` and `L/2-1` nonzero residues
divisible by `2^(m+1)`. Hence the number of ordered distinct pairs whose
minimum valuation is exactly `m` is

```text
(L-1)(L-2)-(L/2-1)(L/2-2)
  =(3/4)L(L-2).                                    (2)
```

Their common orbit size is `L/2`. Dividing `(2)` by `L/2` gives

```text
(3/2)(L-2)=3(2^(s-m-1)-1).                        (3)
```

Set `j=s-m-1`. Distinctness makes `0<=m<=s-2`, so `1<=j<=s-1`, and `(3)`
is `(QOD3)`. Summing gives

```text
sum_(j=1)^(s-1)3(2^j-1)=3(2^s-s-1).              (4)
```

Weighting by the orbit degree gives

```text
sum_(j=1)^(s-1)3(2^j-1)2^j
 =2^(2s)-3*2^s+2=(n-1)(n-2),                     (5)
```

proving `(QOD4)` and the printed official-order values.

Now work over `R=Z[1/2]`. Every denominator `1-zeta^u` has 2-power norm and
is therefore a unit over `R`, so `gamma_(u,v)` is integral over `R`. Odd
Galois dilation sends `gamma_(u,v)` to `gamma_(ru,rv)`. The quotient
consequence of shifted-product Sidonicity makes all `gamma_(u,v)` distinct.
Thus `(QOD5)` is the full Galois-orbit polynomial of one root: it is monic,
irreducible over `Q`, has coefficients in the integrally closed ring `R`, and
has degree `|O|`. Partitioning all quotient roots by their Galois orbits proves
`(QOD6)`.

Let `M_35` be the global cutoff-35 quotient-algebra module and `M_O` the
module obtained by replacing `Qhat_n` with `q_O` in its presentation. All are
finite by the proved Fitting-support compiler. For an odd prime `ell`,

```text
M_35 tensor F_ell !=0
```

exactly when `Qhat_n` and all first thirty-six product Hasse derivatives have
a common root over an algebraic closure of `F_ell`. By `(QOD6)`, this holds
exactly when the same is true with `q_O` for at least one orbit `O`, exactly
when `M_O tensor F_ell !=0` for at least one `O`.

A finite module over `R` has nonzero reduction modulo `ell` exactly when
`ell` divides its positive odd scalar annihilator. Therefore

```text
ell divides s_(n,35)^X
 iff ell divides s_O,35 for some O.                (6)
```

Equation `(6)` for every odd prime is precisely the radical identity
`(QOD8)`. At an official split prime, the cutoff-35 support theorem identifies
the left side with `P>=36,R>=1`, and the single-quotient candidate compressor
identifies that event with positive `Dbar_17`. QED.
