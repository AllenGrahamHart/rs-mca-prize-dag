# L1 FPC5 rate-half `M=4,t=3` split-slice payment

- **status:** TARGET
- **consumer:** `l1_full_petal_fpc5_payment`

At rate `1/2`, after the projective Johnson-positive cells are paid, the
three-touched-petal tail has

```text
N=4ell+b-2,       d=2ell-a,
b>=7,              1<=a<=floor((b-3)/4),
J=ell(4a-b+2)+a^2+2ab-4a<=0.
```

First-layout domination leaves four planted anchors and at most four touched
triples in one fixed maximal source layout. Each triple's three source labels
determine one normalized cross-ratio `lambda`; it is not a field-wide
summation parameter. For one fixed triple and defect, the cell is exactly

```text
{D monic : D|L_C, deg D=2ell-a,
            deg rem_(L_2L_3)(D Etilde)<=ell-a,
            gcd(D,rem_(L_2L_3)(D Etilde))=1}.       (LS6)
```

There are fewer than `4n` such `(triple,a)` cells. The target is therefore a
uniform polynomial/profile payment for one fixed guarded LS6 atom, strong
enough that its sum over these polynomially many cells is admissible. There
is no remaining source-layout or free-`lambda` composition problem. Bounding
the dimension of the ambient linear slice is not the conclusion.

For every nonempty atom, the proved master-flat descriptor injects its
candidates into an unpunctured full-domain split flat with

```text
j=2ell-a,       r=ell-2a+1,       j-2r=3a-2>=1,
gcd(P)=1,       binom(n,j)/Q^(j-r)<2^(-3ell-4),
```

where `Q` is the generated-field size of the descriptor.

Thus the live primitive issue is a sub-balance maximum-versus-average
split-flat bound. Pure multiplicative pullbacks are absent for odd `a`; the
even-`a` quotient and all dihedral strata still require owner-safe treatment.
Every nonempty atom also satisfies `deg Etilde>=a`. The exactly aligned
common-pencil source has constant `Etilde` and is therefore empty, so the
remaining structured branch is necessarily misaligned or non-pencil.
