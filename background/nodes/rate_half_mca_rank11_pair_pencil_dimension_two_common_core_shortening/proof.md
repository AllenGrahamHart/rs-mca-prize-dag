# Proof

Assume the scalar polynomial span `W` has dimension two. Choose a basis and
factor its monic polynomial gcd:

```text
W=C span_F{P,Q},       gcd(P,Q)=1.                  (1)
```

Two distinct projective members `aP+bQ` and `a'P+b'Q` are coprime. Indeed,
their coefficient matrix is invertible, so a common root would be a common
root of `P,Q`, contrary to `(1)`. Therefore two distinct projective members
of the original space `W` have no common domain root outside `Z_D(C)`.

Every selected scalar polynomial has the form `R_p=C S_p`. At a root of
`C`, all quotient pair codewords

```text
(a_p,b_p)=(a_0,b_0)+R_p(U,V)
```

equal `(a_0,b_0)`. Define

```text
J={x in Z_D(C):(r_0,r_1)(x)=(a_0,b_0)(x)}.          (2)
```

Because the selected scalar points span `W`, a coordinate belongs to every
complete pair core exactly when it belongs to `J`.

Choose 38 represented projective secant directions from the direction
router. For each direction `l`, choose endpoints `p_l,q_l` and put

```text
I_l=H_(p_l) intersection H_(q_l).
```

The coprime-direction theorem gives `|I_l|>=134940`. If a coordinate lies
in `I_l intersection I_r` for distinct projective directions, both direction
polynomials vanish there. The primitive members are coprime, so the
coordinate lies in `Z_D(C)`; because it lies in one pair-core intersection,
the received pair equals the common pair value and it lies in `J`. Conversely
`J` lies in every complete pair core. Hence

```text
I_l intersection I_r=J.                            (3)
```

The petals `I_l\J` are pairwise disjoint in the `n`-point domain. Therefore,
with `j=|J|`,

```text
n>=j+sum_l(|I_l|-j)>=38*134940-37j.                 (4)
```

Exact ceiling division in `(4)` gives

```text
j>=ceil((5127720-2097152)/37)=81908.                (5)
```

## Reversible shortening

Every selected quotient core contains `J`. On `J`, the received pair and
every pair codeword equal `(a_0,b_0)`. For a record of type `p` and slope
`gamma`, both

```text
(r_0-a_0)+gamma(r_1-b_0)
```

and its explaining codeword `h-(a_0+gamma b_0)` vanish on the selected
support coordinates in `J`. The latter polynomial has degree below `K`, so
it is divisible by the squarefree locator `L_J`; its quotient has degree
below `K-j`.

On `D\J`, define the shortened received pair coordinatewise by

```text
r'_0=(r_0-a_0)/L_J,       r'_1=(r_1-b_0)/L_J,
```

where every denominator is nonzero. Divide every explanation difference by
the polynomial `L_J` and retain the same slope and first-owner label. Thus an
agreement outside `J` holds before shortening exactly when it holds after
shortening. Exact supports lose precisely `j` points, so their size becomes
`m-j`; each complete quotient core has size `m-2-j=(m-j)-2`. The inverse
multiplies received values and explanations by `L_J`, restores the common
pair, and reinserts `J`, so the transport is reversible. Finally

```text
(m-j)-(K-j)=m-K=67472.
```

If the scalar dimension is not two, the preceding direction router already
restricts it to three or four. QED.
