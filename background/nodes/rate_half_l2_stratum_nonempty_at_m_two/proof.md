# Proof

## 1. Existence is witness-checkable

The claim "the `e = m = 2` stratum is nonempty" is existential, so a single
certified object proves it. The certificate is the pair
`((y_0, y_1), (Q_0, Q_1, Q_2))` displayed in `statement.md`, and the
certification is a finite list of exact finite-field computations, each of
which the verifier redoes from scratch:

1. `deg Q_j = 7` for `j = 0,1,2`, and `gcd(Q_0,Q_1,Q_2) = 1`, i.e. `s = 0`
   — required by (SAT1).
2. The three curves are linearly independent (separation rank `3 = m+1`) —
   required by (RNC2).
3. `M(Z) Q_Z = 0` holds entrywise, where `M(Z) = M_r(y_0) + Z M_r(y_1)` with
   `M_r(y)[a][b] = y[a+b]` of shape `9 x 8`, and `Q_Z = Q_0 + ZQ_1 + Z^2Q_2`.
   Expanding in `Z` gives four `9`-row blocks; all `36` entries vanish.
4. The `36 x 32` system `M(Z)Q_Z = 0`, read as linear in `(y_0,y_1)`, has
   nullity exactly `1`, and `(y_0, y_1)` spans that kernel — so the pencil is
   determined by the curve up to scale.
5. The generic rank of `M(Z)` is `7 = 4m-1`, there is exactly one finite
   rank-drop parameter (`z = 10`, to rank `6`), and `rank M_r(y_1) = 7` so
   there is no drop at infinity. Hence `delta = m-1 = 1`.
6. **The minimal index is exactly `2`.** Kernel vectors of parameter degree
   `e` are solutions of the `(e+2)*9 x (e+1)*8` system obtained by expanding
   `(M_0 + zM_1)(P_0 + ... + z^e P_e) = 0` in `z`. That system has nullity
   `0` at `e = 0` and at `e = 1`, and nullity `1` at `e = 2`. So `e = m = 2`,
   which is the target.

Nothing in this chain is statistical.

## 2. The (D-B) congruence criterion

For pairwise-coprime squarefree curves the `36 x 32` nullity equals
`10 - rank(Phi)`, where `Phi` is the `14 x 10` matrix of
`(f,g) |-> (Q_2 f - Q_1 g mod Q_0, Q_1 f - Q_0 g mod Q_2)` on degree-`<= 4`
pairs. The verifier confirms the identity on the witness and on `60` fresh
random curves over two fields. This is the practical membership test; it is
what makes a `24x24` determinant, rather than a `36x32` rank, the object to
compute.

## 3. Why the `+4` reading was wrong

The system `M(Z)Q_Z = 0` has `(m+2)(4m+1)` equations on `16m` unknowns, an
excess of `4m^2-7m+2` which is `-1, +4, +17, +38` at `m = 1,2,3,4`. Reading
that excess as an existence codimension predicts emptiness from `m = 2`. It
is not one. The solvability locus is determinantal: the `36 x 32` matrix must
drop rank to `31`, and the generic determinantal codimension of a rank-`<= 31`
locus in `36 x 32` matrices is `(36-31)(32-31) = 5`. In the `23`-dimensional
projective space of curves this leaves expected dimension `18`, and in
general `11m - 4`, which is **positive at every `m >= 1`**. The measured
dimension at `m = 2` is `18`, matching.

The round-34 incidence count `19` was contaminated by an excess component:
curves with a common root have `nullity 2` (the verifier plants a common root
and observes nullity `2` on `24/24` draws), and that family has dimension
`3*7 - 1 + 1 = 21 > 18`. Removing it leaves the good component at exactly
`18`, on which the codimension-`5` condition is transverse and the `B`-fibre
is a point.

## 4. What the witnesses do NOT buy

Every witness has `T = 0`: no member splits completely over `mu_32`. The
maximum number of roots of any member inside `mu_32` is `4`, and the maximum
number of roots shared by two members is `1`. The splitting statistics match
those of random degree-7 polynomials. The difficulty therefore moves intact
to the splitting layer, which is why the gate of record became
(SAT3)-on-(L2).

## 5. Convention note on `a*`

Reading each member as a degree-`rho = 7` form on `P^1` (so that a member of
affine degree `7-t` has `t` roots at infinity), the minimum of
`|S_g u S_g'|` over ordered pairs of distinct slopes is `13 = 7m-1`. Reading
`S_g` as the finite root multiset gives `12` on the same witness, because the
leading coefficient `22 + 62z + z^2` of the affine pencil vanishes at two
parameters. The verifier computes both and asserts the projective value,
which is the one the source bank records.
