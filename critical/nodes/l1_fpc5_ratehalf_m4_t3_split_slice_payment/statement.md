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
Every nonempty atom also satisfies `deg Etilde>=a`. If the three touched
petal locators lie in one common pencil, affine source alignment makes
`Etilde` constant and misalignment forces a nonconstant common factor in
`D` and its remainder. Both cases are empty. The remaining branch is
therefore genuinely non-common-pencil.

Writing `e=deg Etilde`, the range `a<=e<=ell-a` is an exact prefix ladder:
it is the disjoint union of `Q_0^(e-a)` ordinary prefix cells of depth
`ell+e-1`, with effective average depth `ell+a-1` after cancellation. The
high-multiplier range `e>ell-a` has exact Pade quotient coordinates:

```text
D=quo_E((L_2L_3)Q),       V=-rem_E((L_2L_3)Q),
deg Q=e-a,                gcd(D,Q)=1.
```

If `F=E^(-1) mod L_2L_3`, every candidate also has
`D=rem_(L_2L_3)(FV)` and necessarily `deg F>=ell+a`. Thus the high branch
is a two-sided primitive rational-approximation cell, not an unstructured BC
flat. More generally every nonempty atom satisfies the source-only gate

```text
deg rem_(L_3)(L_1L_2^(-1))>=a;
```

failure is exactly a short syzygy between the three petal locators. Its split
maximum and quotient/dihedral owner transport remain open.

For any two distinct candidates, their primitive Pade quotients satisfy

```text
0!=D_1Q_2-D_2Q_1,       deg(D_1Q_2-D_2Q_1)<=ell-2a.
```

This determinant contains `gcd(D_1,D_2)` and separates candidates relative
to a fixed base. The induced root-intersection cap has Johnson denominator
exactly `J<=0`, so pairwise distance alone cannot close the target; the
remaining theorem must use split-root or owner structure.

The fixed-base determinant is now an exact coordinate, not merely an
injection. For one primitive base `(D_0,Q_0,V_0)`, every polynomial
`H` of degree at most `ell-2a` gives exactly one point of the complete monic
unguarded slice by

```text
R_H=rem_(D_0)(-H Q_0^(-1)),       D_H=D_0+R_H,
Q_H=(H+D_HQ_0)/D_0,              V_H=(D_HV_0-MH)/D_0.
```

All formal multi-determinant and Plucker identities therefore already hold
on the whole ambient slice and cannot supply a maximum bound. The guarded
atom is exactly the `H` subset for which `D_H` splits on the core and the
root-local primitive inequalities hold. This explicit split-root chart,
not abstract collective compatibility, is the remaining high-branch object.

The base overlap is now an exact canonical owner. For every non-base guarded
point, put

```text
G=gcd(D_0,H)=gcd(D_0,D_H),
D_0=GA,       D_H=GB,       H=GK.
```

Then `G,A,B` are pairwise coprime,
`K=AQ_H-BQ_0`, and primitivity is exactly
`gcd(K,B)=gcd(G,Q_H)=1`. At fixed `g=deg G`, candidate-only root sets have
pairwise intersection at most `h-g`, giving

```text
|F_G| <= floor(
  binom(2ell+a+b-2,h-g+1) / binom(2ell-a-g,h-g+1)).
```

In particular, if `g=h-c`, this is less than `3^(c+1)` per owner. The
fixed-owner top-overlap chambers are therefore paid. The unresolved content
is aggregation or chronology-valid transport across the potentially many
different owners `G`, together with the low-ladder prefix theorem.
