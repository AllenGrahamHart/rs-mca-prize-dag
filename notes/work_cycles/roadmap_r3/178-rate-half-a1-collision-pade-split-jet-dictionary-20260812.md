# Cycle 178: rate-half `A=1` collision Pade/split-jet dictionary (2026-08-12)

The repaired three-profile collision now has an exact global dictionary.
For the second divided row `W` and local remainder `P_F=b+ay mod q`,

```text
a(0),[z]a = [z^0],[z^1] Phi_t(W)
           =-Lambda(tau)/L(x_*) times the matching jets of G_X(t,x_*).
```

The split-biform row derivative therefore selects the profiles:

```text
nonzero at tau:          [4];
simple parameter zero:   [1,3];
double parameter zero:   [2,2].
```

```text
result:                  PROVED Pade/moment/split-jet dictionary
DAG delta:               +1 PROVED leaf, 3 req edges, 1 evidence edge
critical status delta:   none
compute:                 48 low-order identity checks; no Modal spend
new assumptions:         none beyond unshared odd-characteristic collision
```

The audit also repairs an exact-evaluation shorthand in the parent Smith
router: for `P_F=b+ay+qR`, one has `F_0=b+c_0R(z,0)`, not literally
`F_0=b`. Since `ord c_0=6` and `ord F_0=2`, the router and all three
profiles are unchanged.

The next attack is global: constrain `G_X(t,x_*)` at the correction using
the two-directional split fibers and exact factor-degree trichotomy.
