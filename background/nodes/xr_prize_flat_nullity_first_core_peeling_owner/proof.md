# Proof

After exceptional-slope deletion, every block has size

```text
m=kappa+h,       kappa=a+u+v,
```

on a ground set of size

```text
N=R+a+u.
```

The pair cap is `kappa`. Suppose the current family `F` satisfies

```text
h|F|>=2|union F|-2kappa.                              (1)
```

Then an inclusion-minimal nonempty subfamily satisfying `(1)` exists. The
general flat-nullity Maxwell compiler applies to that core and gives a left
kernel of dimension at least

```text
(u+v)(t-2)+e+1>=1.
```

Thus the canonical first nonzero trade exists and has an active block. The
algorithm deletes one block, so it terminates after finitely many steps.
Fixed total orders and row reduction make every choice deterministic, and a
block is deleted only once. Hence every deleted block receives exactly one
pointed certificate.

At termination the current family `F_term` fails `(1)`. Therefore

```text
h|F_term|<2|union F_term|-2kappa
          <=2N-2kappa
          =2(R-v).                                    (2)
```

All quantities are integral, so `(2)` gives `(PO1)`.

At most `v` slopes were deleted before normalization. Adding those slopes to
`(PO1)` gives the first expression in `(PO2)`. On a prize row, `v<=k` and
the function

```text
v+floor((2(R-v)-1)/h)
```

is increasing in `v` because `h>2`. Its value at `v=k` is below `n` on each
of rates `1/4,1/8,1/16`; exact substitution is replayed by the verifier.
This proves `(PO2)` and pays the unowned remainder.

The certificate records the deterministic core and trade before deletion.
The rank-metric, rank-one flat/basis, arbitrary-`W` Segre, and dual-plane
routers are deterministic after the same ambient orders are fixed, so their
first applicable owner can be attached without changing uniqueness. The
argument makes no count of the resulting nonterminal owner packets. QED.
