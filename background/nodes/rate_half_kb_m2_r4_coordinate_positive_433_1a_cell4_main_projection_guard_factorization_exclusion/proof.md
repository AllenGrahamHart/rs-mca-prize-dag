# Proof

Work in `F_p[w0,b,t]/(P)` with `p=2130706433`.  The compact kernel theorem
gives `ell=lc_b(P)=(t^2+1)^2`, `rd=ell`, and the normalized quadratic
evaluations `N0=A0(w0)` and `D0=A2(w0)`.  The signed-pair projection theorem
proves that every guarded pair on this chart lies on the irreducible factor
`F=0` of degrees `(13,3,284)`.

Construct `D0^5` one multiplication at a time and pseudo-reduce by the
quartic `P` after every multiplication.  Reduce `G=rd^2w0-rn^2` separately,
then reduce `N0D0^5` and the final product.  Each of the seven reductions
takes three steps.  A degree-lowering pseudo-step multiplies the represented
quotient-ring element by `ell`, so the resulting 11,088-term polynomial is

```text
C congruent ell^21 N0D0^5G (mod P).               (1)
```

No division has occurred in `(1)`.

The two degree-13 polynomials need not be ambient scalar multiples because
their proportionality scalar is a function on the plane curve.  Instead,
take their leading `w0` coefficients.  Exact cross multiplication followed
by three further plane pseudo-reductions gives zero:

```text
c13F-f13C congruent 0 (mod P).                    (2)
```

To justify inversion of `f13`, compute its norm from the quartic plane.  Up
to the recorded nonzero scalar, exact FLINT factorization gives

```text
Res_b(P,f13) =
 Q2^6 Q3a^6 Q3b^24
 (t+1)^36 (t-1)^68 (t+i)^98
 Q3c^144 (t-i)^388,                               (3)
```

where `i=16711679`, `i^2=-1`, and

```text
Q2  =t^2+1457968268t+1019305654,
Q3a =t^3+622603126t^2+1463338870t+1228312035,
Q3b =t^3+2097283074t^2+2097283076t+2130706432,
Q3c =t^3+2097283076t^2+33423359t+1.
```

The displayed quadratic and cubics are irreducible over `F_p`.  The only
base-field roots of `(3)` are therefore `+/-1,+/-i`, all excluded by the
main guard `t(1-t^2)(1+t^2)!=0`.  Consequently `P=0` and the admissible
guards imply `f13!=0`.

Suppose a guarded signed pair existed.  Then `F=0`; evaluating `(2)` gives
`f13C=0`, hence `C=0`.  The factor `ell` in `(1)` is invertible on the same
chart, so `N0D0G=0`.  But the compiled outside record is nonzero, giving
`N0!=0`; the rational map is defined, giving `D0!=0`; and the two source
deck pairs are disjoint, giving `G=rd^2(w0-r^2)!=0`.  This contradiction
excludes the main plane chart using only the necessary signed pair.

The exceptional-scale dependency proves that every scale omitted in the
compact model is empty.  The exact source projectivities carry the cell-4
row to all four sign rows and to duplicate-role cell 7, preserving all
equations and guards.  Thus all eight rows of orbit `[4,7]` are excluded.
QED.
