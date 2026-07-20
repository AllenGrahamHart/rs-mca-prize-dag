# Audit - L1 cross-quotient split-descent obstruction

## Checked axes

1. The witness has `ell=2`, five complete two-point petals, and the maximal
   one-point background.
2. Petal labels are pairwise distinct.
3. Both pairs have the same exact singleton petal supports; filler points are
   explicitly excluded.
4. Exact missed-core and saturation guards are checked.
5. Total agreement is exactly `k+ell-1`, not below threshold.
6. The quotient includes its forced background factor before the remaining
   quadratic is tested.
7. The quadratic cofactor is irreducible over the base field.
8. The witness lies on the nonpositive-Johnson side.

## Route effect

Do not build a recursive L1 descent whose only splitting premise is that the
cross quotient vanishes on fixed support or background points. A viable
recursion must first isolate and prove a split quotient subclass.
