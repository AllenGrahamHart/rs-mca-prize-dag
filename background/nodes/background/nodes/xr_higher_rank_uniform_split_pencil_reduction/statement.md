# XR higher-rank uniform split-pencil reduction

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_highcore_collision_count`
- **dependencies:** `xr_rs_flat_nullity_basis_charge`,
  `xr_poststrip_affine_pencil_charge`

Fix the high-core P-A branch and a one-per-slope selector of affine error
rank `s=a+1`, where `a>=1`. In the flat-nullity notation, assume the uniform
cell

```text
u=v=0.
```

After puncturing the `k-a` common zero coordinates and applying the fixed
coordinate scaling, the selector is a coherent split-pencil family on

```text
N=R+a
```

coordinates. Its kernel is `GRS_a`, every chosen agreement block has size

```text
m=a+h,
```

distinct blocks have intersection at most `a`, and the extension direction
is non-`GRS_a` on every block. The last assertion follows from the generic
tangent-strip exclusion, not from a rank assumption.

Let `L` be the number of selected slopes. If

```text
hL >=2N-2a,                                           (HR1)
```

then the family contains an inclusion-minimal nonempty Maxwell core `G`.
Writing `V=union_(A in G) A`, `v_G=|V|`, and

```text
h|G|=2v_G-2a+e,
```

one has

```text
0<=e<=h-1,
h|J|<=2|union J|-(2a+1)       for nonempty proper J subset G,
|G|<=floor((2N+h-(2a+1))/h),                         (HR2)
e+2p_A<=h-1                    for every A in G,      (HR3)
```

where `p_A` is the number of coordinates private to `A` inside `G`.

For full-row-rank parity checks `H_A` of `GRS_a` on the blocks, put

```text
M_G=stack_(A in G)[H_A|-gamma_A H_A].
```

Then

```text
rank M_G<=2v_G-(2a+1),
dim leftker(M_G)>=e+1.                                (HR4)
```

Every nonzero left relation gives a dual-product-code trade
`Lambda=(lambda_A(x))` satisfying

```text
sum_A lambda_A=0,
sum_A gamma_A lambda_A=0,                             (HR5)
lambda_A(x)=P_A(x)/Lambda'_A(x),  deg P_A<h,          (HR6)
```

after the fixed normalization. Every active block row has weight at least
`a+1`, and every active coordinate has degree at least three.

Trade rank one is impossible. If a trade has matrix rank two, and `t` is its
number of active block rows while `rho` is its active-coordinate union size,
then necessarily `a>=2` and

```text
4<=t<=a+2,
a+2<=rho<=min{
  floor(a t/(t-2)),
  floor(t(a+h)/(t-1))
}<=2a.                                                (HR7)
```

Its row space is a two-dimensional subspace of dual `GRS_a` on the active
union. Hence it is represented by a polynomial pencil of degree at most

```text
rho-a-1<=a-1,                                         (HR8)
```

and the zero set of each active row is one fiber of that pencil. When `t=4`,
the pencil parameters are a projective change of the four slopes.

For an XR counterexample `L>8n^3`, `(HR1)` is automatic. Thus every uniform
higher-rank counterexample has a bounded Maxwell/trade certificate, and its
rank-two part is confined to at most `2(s-1)` active coordinates. This is a
structural reduction, not the missing aggregate slope payment.
