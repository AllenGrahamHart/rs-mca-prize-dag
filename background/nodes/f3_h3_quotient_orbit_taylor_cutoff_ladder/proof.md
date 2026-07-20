# Proof

Fix `c>=2`. The proof of the cutoff-35 Taylor-content compiler applies with
`35` replaced by `c`. Over an algebraic closure of any odd residue field,
the monic resultant factors as

```text
C_O,c(X)
 =product_(q_O(alpha)=0)
    (sum_(i=0)^c Pcal_n^[i](alpha)X^i),              (1)
```

with roots counted with multiplicity. Since the polynomial ring in `X` is
an integral domain, `(1)` is zero exactly when one factor is zero, exactly
when one root `alpha` makes all first `c+1` Hasse derivatives vanish. The
orbitwise quotient-algebra support theorem identifies this event with
`p|s_O,c`. Divisibility of every coefficient is precisely divisibility of
the positive odd content, proving `(TCL2)--(TCL3)`.

In characteristic zero the same product is nonzero. Otherwise one quotient
root would be a product root of multiplicity at least `c+1>=3`, contrary to
dyadic shifted-product Sidonicity.

Now let `a<=b`. If an odd prime divides `c_O,b`, then `(TCL3)` gives one
block root with product multiplicity at least `b+1`, hence at least `a+1`.
Applying `(TCL3)` again shows that the prime divides `c_O,a`. This inclusion
of prime supports is equivalent to the squarefree divisibility `(TCL4)`.

Finally every factor in `(1)` has `X`-degree at most `c`, so

```text
deg_X(C_O,c)<=c deg(q_O).                            (2)
```

At the first official order, the maximum and total block degrees are
`4,096` and `67,084,290`. Substituting `c=2` into `(2)` gives `8,192` and
`134,168,580`. Since cutoff-35 support is contained in cutoff-2 support, the
cutoff-2 contents give a complete pre-screen; exact row evaluation safely
discards lower-multiplicity primes. QED.
