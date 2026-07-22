# L1 official split-pencil value capacity

- **status:** PROVED
- **role:** remove the split-value axis from the surviving first-checkpoint
  Frobenius-pencil census
- **consumer:** `l1_mixed_petal_amplification`

Let `H` be an official multiplicative coset of size `n` in characteristic
`p`, so

```text
p>n/24.                                                   (SPV1)
```

Fix `Q in F[Z]` with `Q(0)=0` and `deg Q<p`, and put

```text
P(Z)=Z^p+Q(Z).
```

Let `V_H(P)` be the set of values `beta` for which `P(Z)-beta` has exactly
`p` distinct roots and all of them lie in `H`. Then

```text
|V_H(P)|<=floor(n/p)<=23.                                (SPV2)
```

Consequently the number of unordered pairs of distinct fully `H`-split
fibers in this pencil is at most

```text
binom(|V_H(P)|,2)<=binom(floor(n/p),2)<=253.              (SPV3)
```

## Exact split-value eliminant

Write the domain polynomial as `Omega(Z)=Z^n-alpha` and divide over
`F[T][Z]`:

```text
Omega(Z)=A_Q(Z,T)(P(Z)-T)+Rem_Q(Z,T),
Rem_Q(Z,T)=sum_(i=0)^(p-1) R_(Q,i)(T) Z^i.               (SPV4)
```

Put `m=floor(n/p)`. Weighted division gives

```text
deg_T R_(Q,i)<=floor((n-i)/p)<=m.                         (SPV5)
```

The monic gcd of the nonzero coefficient polynomials,

```text
G_Q(T)=gcd_i R_(Q,i)(T),                                 (SPV6)
```

is squarefree, splits over `F`, and satisfies

```text
G_Q(T)=product_(beta in V_H(P)) (T-beta).                 (SPV7)
```

In particular, a minimum-width pair exists for this `Q` exactly when
`deg G_Q>=2`. If `M_Q` is the `p` by `(m+1)` matrix whose rows are the padded
coefficient vectors of the `R_(Q,i)`, then

```text
rank M_Q<=m-deg(G_Q)+1.                                  (SPV8)
```

Thus `rank M_Q>=m` rejects a collision before the gcd calculation. The
eliminant has at most 23 degrees in `T`, independently of the size of the
ambient field.

## Low-complement closure

The capacity bound immediately gives

```text
2p>n  =>  no pair of fully H-split fibers.                (SPV9)
```

Suppose instead `2p<=n<3p`, put `s=n-2p`, and let `r=deg Q` (with `r=0`
when `Q=0`). If a pair exists, then `m=2`, `G_Q` is quadratic, and

```text
G_Q(P(Z)) divides Z^n-alpha.
```

Comparing the leading gap with the monic complement of degree `s` gives

```text
r+s>=p,       equivalently r>=3p-n.                      (SPV10)
```

For a first-checkpoint collision, `r<=r_d=2p-d-1`. Hence

```text
2p<=n<3p and d>=n-p  =>  t>=p+1.                         (SPV11)
```

At the control `(n,p)=(8192,3583)`, this closes every `t=p` depth
`d>=4609`; the row-sharp ratio endpoint alone began at `d=5599`.

In the surviving `m=2` band, a collision pair is also uniquely compiled by
its complement. Let `C_S` be the monic locator of

```text
S=H minus (X union Y),       |S|=s=n-2p,
```

and put `D_S=Omega/C_S`. There is at most one monic degree-`p` polynomial
`R` and one constant `c` such that

```text
D_S(Z)=R(Z)^2+c.                                      (SPV12)
```

When they exist for a genuine pair, `c` is a nonzero negative square and
the two tail locators are `R-delta` and `R+delta`, where `delta^2=-c`.
Consequently

```text
# unordered t=p pairs <=binom(n,n-2p)                  (SPV13)
```

in the `m=2` band, with an injective certificate `(C_S,R,c,delta)`. This is
a structural compiler, not permission to enumerate all complements.

## Exact `m=2` classification

In fact the square-quotient complement exists only at the two-point
remainder:

```text
2p<n<3p and a pair exists  =>  n=2p+2.                 (SPV14)
```

Write `Omega=Z^n-alpha`. Every pair is then uniquely indexed by an
antipodal complement `{x,-x} subset H`. Put

```text
b=x^2,                 C_S=Z^2-b,
c=b^p,                 R=Z(C_S)^((p-1)/2),
delta^2=-c.                                               (SPV15)
```

Then

```text
(R-delta)(R+delta)=(Z^n-alpha)/C_S,                      (SPV16)
```

and both degree-`p` factors split completely in `H`. Conversely every pair
has this form. Therefore the exact number of unordered minimum-width tail
pairs is

```text
n/2.                                                      (SPV17)
```

Their normalized perturbation has `deg Q=p-2`, so they occur at
first-checkpoint depths `d=p` and `d=p+1` and at no deeper depth. Thus all
`m=2` rows with `n-2p>2` have an empty `t=p` stratum; no complement
computation remains there.

Every minimum-width collision supplied by
`l1_official_first_checkpoint_split_pencil_reduction` is one such pair after
the constant term of `Q` is normalized to zero. Therefore, for each fixed
normalized perturbation `Q`, the `t=p` collision ledger has at most `253`
unordered records. A census or contributor computation should enumerate or
bound the surviving `Q` axis, use `(SPV4)--(SPV8)` to recover and certify the
split values inside each `Q` record, and must not shard independently over
`(b,c)`. In the `m=2` band, prefer the unique complement-square compiler
`(SPV12)` and its exact classification `(SPV14)--(SPV17)` over an independent
`Q` search.

This is the one-parameter moving-root bound specialized to the affine pencil
`P-beta`, with an exact disjoint-fiber proof. It does not bound how many
normalized `Q` occur in the surviving higher-complement band, higher tail
widths, or the complete L1 fiber.
