# Fermat-factor adversary

Date: 2026-07-13.

## Construction

The first two prime factors of `F_12=2^4096+1` that satisfy the official
near-square condition for `n=8192` are

```text
p=190274191361,
p=1256132134125569.
```

For either row, `2^4096=-1 mod p`, so `2` has exact order `8192`. These are
deliberately hostile inputs for the norm-divisor route: the unique order-8192
subgroup has the low-height integer generator `2`, maximizing the chance that
lifted cyclotomic coincidences concentrate at one row prime.

The sparse exact audit in
`experiments/prize_resolution/f3_h3_fermat_factor_adversary_modal.py`:

1. certifies primality by deterministic 64-bit Miller--Rabin and verifies the
   exact order of `2`;
2. enumerates and sorts all `8191*8192/2=33,550,336` unordered products in
   `A=(1-H)\{0}`;
3. reconstructs the ordered product multiplicities `P(t)` using the diagonal;
4. frees that array, then enumerates and sorts all `8191^2=67,092,481`
   ordered quotients to obtain `R(t)`; and
5. accumulates `X_18`, the rich non-swap moment, and the rich fifth-orbit
   moment with exact integers.

The two workers ran in parallel on Modal with 4 GB each. Certified replay
`ap-MdlzVrunPKIxHe0OyZSWmb` returned:

| `p` | `max_t P(t)` | `P(1)` | rich targets `P(t)>=19` | `X_18` | `S_ns^rich` | `M_5^rich` |
|---:|---:|---:|---:|---:|---:|---:|
| 190274191361 | 5 | 3 | 0 | 0 | 0 | 0 |
| 1256132134125569 | 5 | 3 | 0 | 0 | 0 | 0 |

All mass checks passed. In particular, the exact C36' inequality and both
proved sufficient inequalities hold trivially on these rows because their
rich loci are empty.

## Verdict

No counterexample was found. More specifically, low-height subgroup
generation at order `8192` does not by itself create rich shifted-product
fibers, even at Fermat factors selected to concentrate the relevant
cyclotomic arithmetic. This removes a concrete threat to the norm-divisor
route.

This is two-row adversarial evidence, not a uniform bound over official rows.
It does not promote `f3_h3_mobius_excess_half` or any sufficient premise.
