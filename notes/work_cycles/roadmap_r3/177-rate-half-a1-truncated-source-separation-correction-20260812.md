# Cycle 177: rate-half `A=1` truncated-source separation correction (2026-08-12)

An adversarial premise audit refuted the inference

```text
x_* outside U_0  =>  P_tau(x_*)!=0
```

for the compressed minimal recurrence of a truncated Hankel sequence. Over
`F_101` at the exact small core-one ratios `(e,p,d,n_0)=(5,7,13,19)`,
all-nonzero weights on `U_0={1,...,19}` share all 27 relevant moments with
all-nonzero weights on disjoint compressed supports of sizes 12 and 11.
The resulting `14 x 14` Hankel matrices have regular coranks one and two,
and their minimal recurrence contains `x_*=30`.

The affected claims were repaired rather than discarded:

```text
separated corank one: jets vanish, Smith [4];
collision, a(0) unit: corank one, Smith [4];
collision, ord(a)=1: corank two, Smith [1,3];
collision, ord(a)>=2: corank two, Smith [2,2].
```

```text
result:                  1 REFUTED fence; 3 PROVED routers repaired
DAG delta:               +1 REFUTED leaf; invalid dependency edges removed
critical status delta:   none
compute:                 64 exact finite-field checks; no Modal spend
new assumptions:         compressed-recurrence separation is explicit only
```

The Pade-Bezout contact-module presentation and normalization valuation
dichotomy remain valid. The remaining unshared nonreduced obstruction has
three exact local profiles, not two.
