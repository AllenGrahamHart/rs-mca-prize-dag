# acl_count

- **status:** PROVED
- **closure:** proof
- **source:** `archived/slackMCA_v3.tex#thm:exactcount`
- **citation correction:** canonical Fable commit `3cca68b7` (2026-07-27)

## Statement

Put `N'=n/sigma`, `n_1=N'/2`, and `l'=rho N'+1`. The number of
antipodal-rearrangement classes of `l'`-subsets of `mu_(N')` is

```text
A(N',l')=sum_(u>=0, t=l'-2u>=0, u<=n_1-t) binom(n_1,t)2^t.
```

For every prime in the stable range, the canonical line has exactly
`B(p)=A(N',l')` bad slopes. At `rho=1/2`,

```text
B(p)=(3^(n/(2sigma))-1)/2.
```

Consequently the safe-slack exponent is

```text
beta(rho)=(1/2) max_(0<=theta<=2min(rho,1-rho))
                    (H(theta)+theta).
```

## Scope fence

Exactness requires the quotient norm threshold

```text
p>(2l')^(N'/2).
```

At `log_2(q)=256` and `rho=1/2`, this is the proved zone `N'<=80`. The range
`80<N'<approximately 512` is the separate conditional `zone_b`; this node
makes no exact-count claim there. The former Conjecture-F sketch citation did
not state this theorem.
