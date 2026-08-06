# Attack surface

## Plus-branch generating rows

When `p=1 mod 4` and `k=ord_n(p)=e`, the proved direct-sum theorem reduces
each open moving window to one explicit prime-field `[S,S-R,R+1]_p` GRS kernel and
`Z(L)=Z_1^C`, `C<=4`. The exact target is the deployed ternary-mass bound
`Z_1<=2^o(S)` with the finite tolerance printed by the consumer. A dimension
bound alone is not sufficient.

## Minus-branch rows

When `p=3 mod 4`, the bounded-class reduction is unavailable even on
generating rows. The official witness `p=2^61-1`, `q=p^2` has `C=2^40`
singleton proportionality classes. The coupled kernel and exact weighted
collision identity are now proved: each top window is the `F_p` coefficient
code divisible by an explicit Frobenius-closed negacyclic root polynomial,
with rank `hR`, pointwise floor, and ternary distance `2R+1`. Prove a
subexponential upper bound for this coupled mass, or pay the final extras
directly. Do not factor it as independent singleton kernels.

## Ambient extensions

When `k<e`, `(O1)` is false by `2^Theta(n)`. Do not attempt to repair it by
assuming generation. The final combinatorial and kernel objects nevertheless
descend exactly by `f2_generated_field_ambient_invariance`: five plus
order-one extensions map to `e=1`, and the plus/minus order-two degree-four
extensions map to `e=2`. No F1 bad-slope trichotomy is needed. A mass theorem
for the five signed generating types therefore covers all 12 official types.

## Seams

- Freeze the PP5.0 average-to-sum normalization. `log2|K1|=n/2` exactly;
  it cannot be hidden in `o(n)`.
- Any use of the Frobenius antipodal-descent identity must handle a domain
  coset representative outside the intermediate subfield. The K1 kernel
  itself is coset-invariant, so avoid this seam when possible.
- Growing-order Myerson remains evidence on matching sectors, not an
  all-row premise.

The preferred next attacks are the explicit GRS ternary mass on plus-branch
generating rows and the explicit coupled negacyclic mass on minus-branch
generating rows, formulated uniformly enough to cover the generated-field
images of official extensions.

The proved `f2_fixed_weight_flatness_mass_bridge` permits a sharper common
attack. For each branch map, prove on a central weight band

```text
max_v N_b(v) <= L(1+binom(S,b)/p^d),
```

with `log L=o(S)` and omitted binomial tails at most `2^(S/2+o(S))`.
This implies the required full-cube mass even though cross-weight collisions
are present. The shape matches upstream split-locator flatness, but the F2
map has weighted odd-power columns and is not the pruned first-match family;
those two transports remain mandatory.
