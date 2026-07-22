# Proof

Fix `B>A`, a support `S in S_c(B)`, and a slope `z in Q_c(B)` witnessed by a
codeword `p_z`. Write `B=mc+s`, `0<=s<c`.

First suppose `s=0`. Deleting any point `x in S` breaks one complete fiber
into a residual set of size `c-1`, so

```text
S\{x} in S_c(B-1).
```

At least one such deletion remains noncontained. Otherwise choose distinct
`x,y in S`. Let codeword pairs explain `(u,v)` on `S\{x}` and `S\{y}`.
Their two endpoint codewords agree on `S\{x,y}`, whose size is

```text
B-2>=A-1>=k.
```

Reed-Solomon uniqueness makes the two pairs equal. Their supports together
cover `S`, so that common pair explains `(u,v)` on `S`, contradicting the
chosen noncontained witness.

Next suppose `s>=2`. There are at least two residual points. Deleting any
residual point leaves `m` complete fibers and `s-1` residual points, hence a
member of `S_c(B-1)`. If every residual deletion were contained, the same
two-deletion argument on distinct residual points would force one codeword
pair to explain all of `S`, again a contradiction. Thus some profile-
preserving deletion remains noncontained.

It remains to consider `s=1`. Let `x` be the unique residual point and put
`S_0=S\{x}`. If `S_0` is noncontained, it belongs to `S_c(B-1)` and the
descent continues. If `S_0` is contained, then the slope is, by definition,
in `T_c(A)`.

Iterate these steps. Restricting the explaining codeword `p_z` preserves the
same slope at each deletion, and noncontainment is retained by construction.
The support size drops strictly, so the process reaches either size `A` or a
remainder-one contained predecessor. This proves

```text
Q_c(>=A) subseteq Q_c(A) union T_c(A).
```

The reverse inclusion is immediate from the definitions, proving `(QRD2)`.

For the tangent assertion, let `(c_0,c_1)` explain `(u,v)` on the pure-fiber
predecessor `S_0`. On `S_0`, both `p_z` and `c_0+z c_1` agree with `u+zv`.
Since `|S_0|=B-1>=A>=k`, RS uniqueness gives

```text
p_z=c_0+z c_1
```

as global codewords. At `x`, the line agrees with `p_z`. The pair cannot
agree endpoint-wise at `x`, or it would explain `(u,v)` on all of `S` and
contradict noncontainment. Hence `x` is a genuine discrepancy coordinate
where the affine error cancels at slope `z`. This is exactly the genuine
tangent branch.

Finally, the lcm normal form has one factor for each distinct slope in the
sets above. Set equality `(QRD2)` therefore gives the equivalent factor
localization. QED.
