
## BALANCED-PENCIL ANCHOR DETERMINANT ATLAS (2026-07-29)

`l1_balanced_pencil_anchor_determinant_atlas` supplies an exact global bridge
from the primitive balanced split-pencil residual to Przemek's BC hierarchy.
After fixing one exact anchor, the coefficient determinant

```text
Delta_0=A_0B-B_0A
```

is an affine coordinate on the complete degree-capped coefficient body. For
every neighbor it satisfies

```text
Delta_0=(gcd(W_0,W)/gamma)((P-P_0)/G),
gcd(Delta_0,W_0)=gcd(W_0,W),
```

where `G` is the common agreement locator. At common-agreement deficiency
`j`, fixing the recovered common complement puts every neighbor in a split
linear system of projective dimension at most `j+1`. A root-matroid basis
injection gives the exact per-owner ceiling

```text
floor(binom(m,r)/(w+j-r+2)),       1<=r<=j+1.
```

Exact codeword distance gives the independent rank-free per-owner ceiling

```text
floor(binom(m,j+1)/binom(w+1+j,j+1)).
```

Every owner uses the better of the two bounds.

A Bezout-dual module vector gives the stronger global interface

```text
W(P-P_0)=gamma Delta_0L_0,
W=Delta_0J mod W_0,       gcd(J,W_0)=1.
```

Thus all common-complement owners are exact gcd strata inside one
received-word Pade family, and every fixed-owner quotient is the explicit
remainder graph `Y=X+rem_X((R/gamma)J)`.

More globally, if

```text
Delta_0J=Q_Delta W_0+R_Delta,
```

then the complete exact shell is bijective to

```text
{Delta_0 in F[Z]_(<=s-1):
 W_0+R_Delta divides Omega,
 gcd(Delta_0,1-Q_Delta)=1}.
```

Split numerator divisibility is automatic. The gcd is exactly the
complete-agreement/content guard.

The `j=0` chamber is precisely a paid one-parameter moving-root pencil. This
does not promote L1: the possible common-complement owners can be
exponentially numerous, and growing `j` remains unaggregated. The missing
theorem is now an owner coalescence/priority map across these determinant
charts, not a fixed-chart split count.
