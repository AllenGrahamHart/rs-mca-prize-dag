# L1 official-reserve tame-refinement router

- **status:** PROVED
- **role:** remove wild fixed-petal refinements from the official L1 lower
  cutoff
- **consumers:** `l1_mixed_petal_amplification`

## Official generated-field setup

Let the generated evaluation field be `K_0=F_(p^f)`. Assume

```text
n=2^m>=2^13,       n | p^f-1,       p^f<2^256,
k<=n/2.                                                   (OR1)
```

Fix `epsilon>0`, put `eta=min(epsilon,1/4)`, and suppose some
`1<=sigma<=n-k` satisfies the corrected reserve

```text
sigma log_2(p^f)>=(1+epsilon) log_2 binom(n,k+sigma).     (OR2)
```

Let `sigma_0` be the least positive integer with `k+sigma_0<=n` and

```text
sigma_0 log_2(p^f)>=(1+eta) log_2 binom(n,k+sigma_0),
ell_0=sigma_0+1.                                         (OR3)
```

Then

```text
sigma_0<=sigma,       ell_0<p.                           (OR4)
```

The exact-shell identity therefore gives

```text
ImgFib_U(k+sigma) subset ImgFib_U(k+sigma_0)              (OR5)
```

for every received word `U`.

## Refinement consequence

For every divisor `s|ell_0`, put `r=ell_0/s`. Equation `(OR4)` gives

```text
1<=r<p,
```

so the characteristic never divides `r`. Every whole-petal degree-`s`
refinement at the canonical lower threshold is consequently in the tame
scope of `l1_tame_fixed_petal_refinement_census`. Across one fixed source,
all fixed-petal refinement-map classes number at most

```text
M_src tau(ell_0)<=n.                                    (OR6)
```

Thus wild fixed-petal decomposition is not an official L1 escape. The
remaining pullback obligations are role/support payment for tame maps,
partial-fiber loss, and maps with no whole-petal anchor.

## Scope

This theorem counts refinement maps only. It does not pay their fiber-role
assignments, prove a quotient-list bound, handle unanchored maps, or bound
arbitrary petal locators. The `F_9` wild decomposition fixture remains a valid
guard outside `(OR1)--(OR3)`.
