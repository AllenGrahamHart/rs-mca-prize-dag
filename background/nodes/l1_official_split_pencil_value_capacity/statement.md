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

Every minimum-width collision supplied by
`l1_official_first_checkpoint_split_pencil_reduction` is one such pair after
the constant term of `Q` is normalized to zero. Therefore, for each fixed
normalized perturbation `Q`, the `t=p` collision ledger has at most `253`
unordered records. A census or contributor computation should enumerate or
bound the surviving `Q` axis, use `(SPV4)--(SPV8)` to recover and certify the
split values inside each `Q` record, and must not shard independently over
`(b,c)`.

This is the one-parameter moving-root bound specialized to the affine pencil
`P-beta`, with an exact disjoint-fiber proof. It does not bound how many
normalized `Q` occur in the surviving higher-complement band, higher tail
widths, or the complete L1 fiber.
