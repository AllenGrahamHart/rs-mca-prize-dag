# XR deficient window: exact phi-fiber and split-pencil router

- **status:** PROVED
- **consumer:** `xr_band_forced_commonroot_syzygy_count` (evidence)

Use the active-defect notation

```text
N=n-e,       K=k-ell,       w=d+ell,       r=h-d,
phi=[P:Q],   gcd(P,Q)=1,    max(deg P,deg Q)=ell.
```

For a selected `r`-point block `B`, let its nonempty `phi`-fiber sizes be
`m_1,...,m_v`.  Put

```text
T_3(B)=sum_(i<j<k)m_i m_j m_k,
q=floor(r/ell),       u=r-q ell,
T_pack(r,ell)=binom(q,3)ell^3+binom(q,2)ell^2 u.     (FSP1)
```

Then `T_3(B)` is exactly the number of unordered triples in `B` with three
pairwise distinct `phi` values, and

```text
T_3(B)>=T_pack(r,ell).                               (FSP2)
```

If `v>=3`, the exact minimum is

```text
T_+(r,ell)=
  r-2,                    3<=r<=ell+2,
  ell(r-ell-1),           ell+2<r<=2ell,
  T_pack(r,ell),          r>2ell.                    (FSP3)
```

Let `M_B=product_(x in B)(X-x)`.  If the values of `phi` on `B` are
`[a_i:b_i]`, then

```text
M_B divides product_(i=1)^v (b_i P-a_i Q).           (FSP4)
```

Consequently, every block with `v<=2` is a one- or two-member
**split-pencil block**.  For `v=1`, necessarily `r<=ell`.  For `v=2`, if
one part has size `m`, then

```text
max(1,r-ell)<=m<=min(ell,r-1).                       (FSP5)
```

Let `Tau_3` be the parameters having at least one selected block with
`v>=3`, and choose the first such block under the fixed first-match order.
For affine dimension `s>=2`, the affine-plane component cap gives

```text
|Tau_3| B_(s-2) T_+(r,ell)
 <=3 binom(N,s-2)binom(e,3),                         (FSP6)

B_(s-2)=product_(j=3)^s(w+j)/(s-2)!.
```

When `r>2ell`, every selected block has at least three fibers and every
target has at least two selected blocks, so the stronger exact refinement is

```text
2|Tau| B_(s-2) T_pack(r,ell)
 <=3 binom(N,s-2)binom(e,3).                         (FSP7)
```

The complementary family `Tau_SP` has at least two disjoint selected block
locators, each dividing a product of at most two members of the primitive
pencil `{bP-aQ}`.  This is an exact structural endpoint, not its census.
The high-fiber upper tails also remain open, so no critical status changes.
