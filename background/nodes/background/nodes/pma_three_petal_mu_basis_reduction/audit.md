# Audit - PMA three-petal mu-basis reduction

## Hypothesis ledger

| hypothesis | use | failure mode if removed |
|---|---|---|
| one field `K` | PID and degree arithmetic in `K[X]` | no claim over a general coefficient ring |
| three distinct labels | all `alpha_i` are nonzero and the affine reconstruction is invertible | repeated labels merge fibers and destroy the dictionary |
| equal locator degree `ell` | gives complementary basis degrees summing to `ell` | unequal degrees require shifted row degrees |
| `gcd(L_1,L_2,L_3)=1` | makes the locator row unimodular and the cross-product factor a unit | a common locator factor lowers the basis-degree sum |
| `s<ell` | puts the contributor in the strict sub-`2ell` strip | no claim for `d>=2ell` |
| `deg F=d` | forces the syzygy to have vector degree exactly `s` | a lower-defect pair may occupy a lower syzygy rung |
| `gcd(F,W)=1` | forbids a nonconstant multiplier of the sole active basis vector | non-exact defect encodings violate (BAL) |

Pairwise coprimality of the locators is stronger than the module theorem
needs but is automatic for disjoint petals and is retained in the PMA
statement. It also keeps the three fiber products geometrically separated.

## Status boundary

The following are proved:

1. the exact linear dictionary between three-petal contributors and bounded
   syzygies;
2. a self-contained reduced-basis theorem with degrees `mu` and `ell-mu`;
3. the saturation balance law and exact Hilbert-function dimension;
4. the coefficient budget `e-1` for the upper-half strip;
5. pairwise coprimality of the three saturated fiber products;
6. the determinant identity and the primitive-coefficient characterization
   of saturation away from the petal product.

The following are not claimed:

- a polynomial count when `e` grows;
- a bound for split monic members of the two-generator family;
- a common-pencil or multiplicative-coset rechart;
- a theorem for partial petals, four touched petals, or `d>=2ell`;
- closure of `petal_mixed_amplification` or `imgfib`.

## Route consequence

The old search space "arbitrary triples of petal locators" is no longer the
right contributor-level object. Once a carried source and touched triple are
fixed, the locators are fixed and all contributors lie in one explicit
two-generator module. The remaining task is to count split exact-defect
members `uF_p+vF_q` with `gcd(u,v)=1`, preserving first-match ownership.
Source maximality does not determine `mu`; it only fixes the locator triple
from which `mu` is computed.

## Adversarial controls

The verifier checks the Hilbert-function formula exhaustively for small
pairwise-coprime monic triples and enumerates all bounded syzygies when testing
the balance law. It must also exhibit:

1. a common-factor locator triple for which the degree-sum formula changes;
2. an exact-degree but nonsaturated pair in the forbidden unbalanced range;
3. a saturated lower-degree pair showing why `deg F=d` is required;
4. a repeated-label failure of the affine dictionary.

It also checks the determinant-product identity on every exhausted locator
triple and rejects omitting any one of the three petal factors.
