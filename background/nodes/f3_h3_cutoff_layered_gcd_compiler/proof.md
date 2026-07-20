# Proof

Fix a nonidentity target `t`, and write

```text
m=P(t),       r=R(t),       q=(m-c)_+.
```

The local factorizations of the row polynomials are

```text
Pcal(T)=(T-t)^m U(T),       Qcal(T)=(T-t)^r V(T),
U(t)V(t)!=0.                                           (1)
```

All relevant multiplicities and derivative orders are below `p`: indeed
`m,r<=d=n-1<p`, and `c,j<=d`. For a polynomial having a root of multiplicity
`a<p`, its `i`th Hasse derivative has multiplicity at least `a-i`, and the
coefficient of the first possible term is `binom(a,i)`, which is nonzero
when `0<=i<=a<p`. Therefore

```text
ord_t gcd(W^[0],...,W^[k])=(ord_t W-k)_+.             (2)
```

Applying `(2)` first to `Pcal` gives

```text
ord_t G=q.                                             (3)
```

Applying it again to `G` gives

```text
ord_t G_j=(q-j+1)_+.                                   (4)
```

Also, ordinary differentiation is the first Hasse derivative, so

```text
ord_t Qcal_+=(r-1)_+.                                  (5)
```

Since `r<=d`, equations `(4)` and `(5)` imply

```text
ord_t gcd(Qcal,G_j^d)
 = r        if q>=j, and 0 otherwise,

ord_t gcd(Qcal_+,G_j^d)
 = (r-1)_+  if q>=j, and 0 otherwise.                 (6)
```

Indeed, when `q>=j`, `G_j^d` has multiplicity at least `d`, which saturates
the complete quotient multiplicity; otherwise it has no root at `t`.
Summing `(6)` over `j=1,...,d-c` gives respectively

```text
sum_j ord_t gcd(Qcal,G_j^d)=rq,
sum_j ord_t gcd(Qcal_+,G_j^d)=q(r-1)_+.
```

Every root of `Qcal` is a nonidentity target, and polynomial degree is the
sum of root multiplicities over a splitting field. Summing over all targets
proves `(LGC3)`. Taking only `j=1` in `(6)` proves `(LGC4)`, showing why the
remaining layers cannot be omitted when some `q>1`.

The resultant statement follows from the proved global resultant compression
and reduction at the selected embedding `zeta_n -> g`. Its cleared quotient
polynomial differs from the monic `Qcal` only by a nonzero scalar, because
every shifted factor is nonzero modulo `p`; this does not change any gcd.

For an official nonidentity target, the proved uniform theorem gives

```text
P(t)<33n^(2/3).
```

Since `P(t)` is integral, its cutoff-18 excess is at most
`ceil(33n^(2/3))-19`, and the elementary cap `P(t)<=n-1` gives `n-19`.
Thus every `G_j` above `(LGC5)` is constant, proving the truncated range.

Finally, over a field the nullity of the Sylvester matrix of two nonzero
polynomials is the degree of their gcd. If `H` is a proposed monic gcd,
exact divisions `A=HA_0`, `B=HB_0` and a Bezout identity
`SA_0+TB_0=1` prove both divisibility and coprimality, hence certify the gcd
and its degree. Applying this sequentially to the defining derivative gcds
certifies `G` and every `G_j`; applying it once more to each terminal
intersection proves the stated certificate interface.
QED.
