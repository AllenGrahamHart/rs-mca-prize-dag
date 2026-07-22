# Consumer-backward audit

- **verdict:** NO ISSUE
- **consumer:** `list_adjacency_closing`, rate-half unsafe edge
- **scope checked:** ordinary and constant common-support interleaved lists;
  no MCA/CA transfer

## Checks

1. On `D=gamma H_n`, the quotient value `Y=X^c` satisfies
   `Y^N=gamma^n`; reduction modulo `Y^N-delta` therefore preserves values on
   every evaluation point.
2. For `m=N/2+d`, rotation by `N-d` maps sources `j<d` to
   `N-d+j`, sources `d<=j<=m` to `j-d`, and wraps only once. The only wrapped
   index at least `N/2` is `j=m`, whose coefficient is fixed by monicity.
3. Since the tail degree is strictly below `c`, quotient blocks do not overlap
   or cross the code boundary. Thus the variable high part is exactly
   `(a_0,...,a_(d-1))`.
4. The constant coefficient is a product of `m` elements from one quotient
   coset. It lies in one coset of the order-`N` subgroup, so its range has size
   at most `N`; exclusion of the distinguished fiber cannot enlarge it.
5. With `E_A=L_A-U`, the codeword is `-E_A`, not `E_A`. Hence
   `U-(-E_A)=L_A`, and its agreement set is exactly the locator root set.
6. The cyclic multiplier is nonzero on the multiplicative domain. It neither
   creates nor deletes roots; the fixed tail is disjoint because its quotient
   fiber was excluded.
7. The optimized instance has `N=256,d=1,m=129`, so its exact lower bound is
   the field-independent integer `ceil(C(255,129)/256)>2^238`. At the
   artificial endpoint `q=2^256`, the equivalent cap comparison has
   `114.6503...` bits of margin. The earlier `N=2^19,d=2048` instance and its
   `75.0796...`-bit margin remain valid historical controls.
8. Diagonal repetition creates distinct interleaved tuples with the same
   common support and does not change the threshold denominator. No claim is
   made about MCA slopes.
9. With `a=k+2^34-1`, the exact inequality `a^2<n(k-1)` places the closed-ball
   radius strictly beyond the Reed--Solomon Johnson radius. This is a list
   lower construction, not a safe-side decoding bound.

The independent audit verifier enumerates the abstract support map over every
small even `N<=64`, separately enumerates quotient-coset constant terms, and
recomputes the historical and optimized cap inequalities, exact Johnson gate,
and 74 maximal-prefix extremality checks.
