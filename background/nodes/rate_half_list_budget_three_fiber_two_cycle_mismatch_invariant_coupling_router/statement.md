# Budget-three fiber-two mismatch invariant coupling router

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:**
  `rate_half_list_budget_three_fiber_two_cycle_boundary_transfer`

Retain a generic canonical survivor in one of the `c=1,2`
denominator-mismatch strata. Let

```text
D_*(Y)=product_(A in Omega)(Y-A),       |Omega|=4,      (MIC1)
```

where the four elements of `Omega` are distinct nonzero squares in the base
field. Let the split outer quartic be

```text
O(W)=W^4+alpha W^2+beta W+gamma.                       (MIC2)
```

For a binary quartic

```text
f(X,Z)=aX^4+bX^3Z+cX^2Z^2+dXZ^3+eZ^4,
```

define

```text
I(f)=12ae-3bd+c^2,
J(f)=72ace+9bcd-27ad^2-27b^2e-2c^3.                  (MIC3)
```

Thus

```text
I_O=alpha^2+12gamma,
J_O=72alpha gamma-27beta^2-2alpha^3.                 (MIC4)
```

There are two exact finite mismatch packets.

For `c=2`, choose an unordered two-subset `{A,B}` of `Omega`. The completion
roots have source quartic

```text
f_2=(X^2-AZ^2)(X^2-BZ^2),
I_2=A^2+14AB+B^2,
J_2=2(A+B)(A^2-34AB+B^2).                            (MIC5)
```

There are exactly `binom(4,2)=6` such candidates.

For `c=1`, choose an ordered pair `(A,C)` of distinct roots of `D_*`. Here
`A` is the repeated completion-root square and `C` is the residual
exceptional-pair square. Write

```text
{B,D}=Omega\{A,C},       u^2=BD.                     (MIC6)
```

For either of the two values of `u`, choose `s` with
`s^2=B+D+2u`. The source quartic and its invariants are

```text
f_1=(X^2-AZ^2)(X^2-sXZ+uZ^2),

I_1=A^2+BD+3A(B+D)-8Au,
J_1=2(A-u)(A^2+BD+16Au-9A(B+D)).                     (MIC7)
```

Changing `s` to `-s` applies `X |-> -X`, so it does not create another PGL
class. There are exactly `4*3*2=24` candidates.

For either stratum, the completion-root Mobius matching holds if and only if
at least one candidate in its packet satisfies

```text
I_O^3 J_*^2=I_*^3 J_O^2.                             (MIC8)
```

This is a root-permutation-free scalar coupling: `c=1` needs 24 indexed
tests, `c=2` needs six, and their union has 30 indexed tests (at most 30
distinct invariant classes). On a passing test, factoring the already split
constant-degree quartics and matching one cross ratio reconstructs a map in
`PGL_2(F)`.

The theorem closes the missing completion-root coupling derivation for the
two denominator-mismatch strata. It does not prove any equation `(MIC8)`
impossible, import the matched trace-Jacobi norm gates, cover an above-floor
or noncanonical branch, or authorize a large computation.
