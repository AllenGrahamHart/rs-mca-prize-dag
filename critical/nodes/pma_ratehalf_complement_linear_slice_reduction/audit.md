# Audit - PMA rate-half complement linear-slice reduction

## Load-bearing inputs

| input | use | guard |
|---|---|---|
| normalized label triple `(0,1,lambda)` | factor `E_c=L_1Etilde` | `lambda` must be nonzero |
| pairwise-disjoint core and petals | invertibility modulo `L_2L_3` | no denominator root lies in the core |
| exact support size `m=N-(2ell-a)` | complement degree `2ell-a` | lower-defect supports are not included |
| predecessor degree guard | low slice `deg V<=ell-a` | raising the cutoff changes the cell |
| predecessor exactness guard | `gcd(V,D)=1` | omitted roots cannot be recounted |
| three-petal mu-basis theorem | exact truncated-slice dimension | dimension uses the printed saturation alternative |
| fixed generated field | split-divisor interpretation | no challenge-field normalization is inferred |

## Consumer-backward check

The PMA consumer needs exact codewords in one fixed normalized three-petal
cell. The proof reconstructs the degree-`<K_0` polynomial and preserves the
exact core root set. Fourth-petal and first-match predicates remain external
deletions, so (LS6) is a conservative exact-cell envelope.

## Nonclaims

- The codimension does not by itself imply max-to-mean flatness.
- An arbitrary linear automorphism of the quotient is not an ordinary prefix
  map on the moment curve.
- `shared_census_kernel` is not assumed and is not a new requirement edge.
- No quotient, extension, or natural-scale owner has been assigned.
- The mu-basis reconciliation recovers the already-known `e+1` coefficient
  freedom; it is not a second reduction in dimension.
