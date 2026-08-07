# Audit - PMA rate-half source-aligned gcd excess

## Load-bearing inputs

| input | use | guard |
|---|---|---|
| pairwise-coprime petal locators | CRT polynomial `E_c` and degree-`3ell` product | partial petals are not covered |
| core disjoint from the petals | invertibility of `L` on `C` and `gcd(L,L_C)=1` | no shared locator root may be cancelled silently |
| squarefree core locator | gcd degree equals a number of core points | multiplicity is not an agreement count |
| actual source numerator `P_*` | aligns equality points with the received word | ambient `0/1/infinity` fibers are only an upper superset |
| three actual list contributors | supplies the three root sets `S_i` | two contributors are already paid |

## Nonclaims

- The three-dimensional quotient code is not claimed to be an ordinary
  degree-two Reed-Solomon code.
- Its minimum-distance bound does not by itself bound the list size.
- The aligned gcd inequality is not yet excluded or profile-owned.
- The arbitrary smooth `J=0` fixture from the predecessor is not asserted to
  be source-coupled; no source lift is supplied.
- No result is claimed for `M=4,t=2`, larger `M`, or partial petals.

## Mutations

The verifier rejects a wrong quotient sign, loss of the CRT constant-on-petal
condition, a fourth independent source coordinate, omission of the triple
intersection subtraction, replacement of actual overlaps by ambient equality
fibers, dropping the source numerator from an overlap gcd, and an out-of-tail
arithmetic claim.
