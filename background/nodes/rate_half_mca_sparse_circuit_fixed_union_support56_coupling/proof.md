# Proof

Fix `i in {0,1,2,3}` and an independent `i`-set `S subset D`.  Contract
`S` in the evaluation matroid and restrict to the `N` points outside `D`.
For a rank-`r` flat in this contracted restriction, choose a basis `A`.
Because `W` already vanishes on `S`, imposing the `r` outside evaluations
leaves a subspace of dimension at least `g-r`.  It vanishes on all of `D`
and on the complete contracted flat.  The polynomial common-root bound gives

```text
flat size <= K-u-(g-r)=R+r.                         (1)
```

For `r=4-i`, both `r` and `r+1` are at most `g-1`.  Thus rank-`r` flats
have size at most `B=R+r` and rank-`(r+1)` flats at most `B+1`.  Apply the
adjacent-flat circuit coupling in the contraction; its size hypothesis holds
because `N>=R+4>=B`.  Every original circuit
whose intersection with `D` is exactly `S` becomes a circuit after
contracting `S`; retaining all other contracted circuits is conservative.
Summing over the `C(u,i)` choices of `S` yields

```text
(6-i) C_(6,i) + (N-R-4+i) C_(5,i)
 <= C(u,i) R C(N,5-i),
```

which is `(S56)`.

Expose each support-five circuit in this stratum by deleting one of its
`5-i` outside points.  The remaining outside points cut `W` by at most
`4-i`, so the completion-stratified fixed-union charge gives budget `R`.
Division by `5-i` proves `(S5)`.

For fixed `i`, maximize `w5 C_(5,i)+w6 C_(6,i)` over the nonnegative region
defined by `(S56)` and `(S5)`.  Its slope in `C_(5,i)` has numerator
`lambda_i`.  If this is nonnegative, use `C_(5,i)=L_i`; if it is negative,
use the conservative lower endpoint zero.  Integer flooring gives `J_i`.

The remaining strata use direct completion exposure:

```text
C_(5,4)<=C(u,4)R,                  C_(5,5)<=C(u,5),
C_(6,4)<=floor(C(u,4)RN/2),        C_(6,5)<=C(u,5)R,
C_(6,6)<=C(u,6).
```

Adding them proves `(WS56)`.  Exact substitution gives the printed K'=83
value. QED.
