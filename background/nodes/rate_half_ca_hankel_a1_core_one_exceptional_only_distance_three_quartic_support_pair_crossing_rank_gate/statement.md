# `A=1` distance-three quartic support pair-crossing rank gate

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quartic_internal_slice_lambda_cube_kernel`

Retain the support partition and matching. For each omitted pair index `l`,
put

```text
G_l(X)=X(X-s)(X-x_0)B(X)^4A'(X)^4D_l(X)^2.           (QPC1)
```

If `D_k=(X-a_k)(X-b_k)` with `k!=l`, define one row in `F^5` by

```text
R_l(k,d)=G_l(b_k)a_k^d+G_l(a_k)b_k^d,
                                      0<=d<=4.        (QPC2)
```

Thus `R_l` is an `(e-1) x 5` matrix depending only on the exceptional and
triple support, the omitted domain points `s,x_0`, and the pair matching. It
is independent of all internal slopes, `lambda_i`, `P_Z`, first jets, and
external cofactors.

Every exact external design supplies, for every `l`, a nonzero quartic

```text
P_l(X)=sum_(d=0)^4 p_ld X^d                         (QPC3)
```

such that

```text
R_l p_l=0,                                           (QPC4)
P_l(a)P_l(b)!=0       for every pair D_k, k!=l.      (QPC5)
```

Consequently either condition below excludes the support/matching packet
before any internal-slope work:

1. `rank R_l=5` for at least one `l`; or
2. for at least one `l`, every polynomial in `ker R_l` vanishes at one
   fixed root of `A/D_l`.

The first possible rank-five case is `e=6`. Deterministic smooth-subgroup
controls give, for every `l`,

```text
e=4: rank 3,       e=5: rank 4,
e=6: rank 5,       e=7: rank 5.                     (QPC6)
```

On the fixed `e=6,F_113` support used by the verifier, a complete census of
all `11!!=10,395` perfect matchings finds no matching for which every
omitted-pair matrix has rank at most four. The exact sorted rank-pattern
histogram is

```text
(5,5,5,5,5,5): 9811,       (4,5,5,5,5,5): 574,
(4,4,5,5,5,5):    9,       (4,4,4,5,5,5):   1.      (QPC7)
```

These controls show the threshold and nonvacuity only. They do not vary the
support/triple partition, so no universal rank-five theorem is asserted. A
packet passing `(QPC4)--(QPC5)` still owes one common coordinatewise-cube
vector across all `l`, the internal-slope and torus-kernel gates, and the
external perfect-power/source conditions.

Distinctness and matching combinatorics alone cannot prove rank five. If the
fixed smooth weight

```text
H(X)=X(X-s)(X-x_0)B(X)^4A'(X)^4
```

is replaced by arbitrary nonzero values satisfying
`H(b_k)=-H(a_k)` on every pair, then `P_l=D_l^2` satisfies all crossing
equations for every `l`. A uniform exclusion must use the actual
smooth-domain weight and support partition to rule out this antiweight
mechanism or its rank-deficient generalizations.
