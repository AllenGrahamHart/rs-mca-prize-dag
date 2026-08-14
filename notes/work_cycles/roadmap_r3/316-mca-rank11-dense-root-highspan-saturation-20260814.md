# Cycle 316: MCA rank-11 dense-root high-span saturation (2026-08-14)

The new PROVED node
`rate_half_mca_rank11_dense_root_highspan_saturation` deletes the apparent
range of absorbing correction dimensions.

For the fixed relative core, subtract the descended dense pair line:

```text
D_H(X,Z)=H(X,Z)-a_0'(X)-Zb_0'(X).
```

The eighteen dense-pair anchor records give eighteen distinct roots of
`D_H`. The ten deviation-basis anchor records give values spanning `V'`.
Writing

```text
D_H=q_18 G,       deg_Z G<=13,
```

monicity of `q_18` makes coefficients `18..31` a triangular invertible
image of all fourteen coefficient vectors of `G`. Their span is therefore
the complete ten-dimensional `V'`. These coefficients are also high
coefficients of `H`.

Every unsafe survivor already satisfies `W<=V'` and absorbs every high
coefficient. It follows that

```text
W=V',       dim W=10.
```

Thus absorbing dimensions `2..9` are impossible. All clone and rank-flat
components are now components inside one fixed ten-dimensional correction
space. Their aggregate mass remains unpaid.

Focused verification:

```text
RATE_HALF_MCA_RANK11_DENSE_ROOT_HIGHSPAN_SATURATION_PASS
  roots=18 rank=10 controls=6/6
RATE_HALF_MCA_RANK11_DENSE_ROOT_HIGHSPAN_SATURATION_AUDIT_PASS
  factor=18+13 dimension=10 controls=5/5
```

No numerical experiment or Modal computation was used.

```text
start:                   31f2797af
DAG delta:               +1 PROVED high-span saturation node,
                         +2 requirement edges, +1 evidence edge
critical status delta:   none
upstream terminal delta: one common correction ten-space for every
                         rank-eleven H_C survivor
delta-star movement:     none
compute:                 exact polynomial factorization and rank only
next route action:       exploit the common ten-space to aggregate
                         rank-flat kernels and affine owner components
```
