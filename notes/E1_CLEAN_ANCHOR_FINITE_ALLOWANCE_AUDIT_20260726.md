# E1 clean-anchor finite-allowance audit

## Ruling

The direct-E1 route was not yet posed at finite prize currency. Four defects
were repaired without promoting any open statement:

1. The characteristic-zero count is
   `A_2(N,ell)=sum binom(N/2,t)2^t` over feasible signed singleton supports.
   It is not divided by global sign. The paper's exact test is
   `A_2(16,9)=3280=(3^8-1)/2`.
2. The live clean-anchor quotient orders are `N=256,512`. The older
   `{128,256}` labels are folded dimensions `h=N/2`, not quotient orders.
3. `o(1)` or "negligible" collision density is not a finite `2^-128`
   certificate. If `K=A_2(N,ell)` and
   `P=sum_y binom(r_y,2)` counts colliding unordered class pairs, the exact
   sufficient row inequality is `P<=K-B*-1`.
4. The initial field gate `|F_p(Q)|>B*` was still too broad for a pair-loss
   proof. Balanced fibers can force `P>K-B*-1` even when the image could exceed
   `B*`.

The elementary fiber inequality `K-|image|<=P` then gives
`|image|>=B*+1`, and the canonical quotient locator realizes those values as
bad slopes at the candidate predecessor.

## Generated-field split

Let `Q` be the quotient root set and `B=F_p(Q)`. Every E1 value lies in `B`.
Therefore `|B|<=B*` rules out direct E1, independently of collision behavior.
For `b=|B|`, write `K=sb+r`. Convexity gives the exact unavoidable floor

```text
P_min(K,b)=b binom(s,2)+rs.
```

At the six anchors, `P_min<=K-B*-1` first becomes possible at
`b_pair_min=ceil((K+B*+1)/3)`, with bit lengths `188,134,170` at rates
`1/4,1/8,1/16`. The pointwise pair target is now posed only on
`b>=b_pair_min`. The intermediate range `B*<b<b_pair_min` may still admit a
direct image proof, but cannot use this pair ledger. The universal unsafe
router owns both lower field ranges.

## Exact output

`e1_clean_anchor_exact_collision_allowance` prints `K`, `B*`, and
`K-B*-1` at all six RowC/prize anchors. The smallest class-to-budget ratio is
`119` at the prize `1/8` row, so the exact target permits substantial value
loss. No collision-pair bound is inferred from this margin. The same packet
prints and verifies all six exact `b_pair_min` values.

Two independent bounded verifiers pass:

```text
E1_CLEAN_ANCHOR_EXACT_COLLISION_ALLOWANCE_PASS
  rows=6 small_checks=80 profile_checks=507
E1_CLEAN_ANCHOR_EXACT_COLLISION_ALLOWANCE_AUDIT_PASS
  rows=6 ternary_checks=80 map_checks=1272296
```

The first exhausts raw subsets through order sixteen and reconstructs their
signed classes. The second enumerates ternary class profiles and every labeled
finite map through seven classes. Both independently replay the six bignum
allowances.

## Provenance and concurrency

- starting local pin: `b5df49eac98d1480261378776deb3f81b57d34dd`
- ending proof pin: `1f56def3ea8a7863b1aaf38f95bcdd38ea523a4d`
- canonical prize pin: `cc979e4befcbc42e1cb2725661941c037e4662ab`
- upstream main pin: `b13de8113a03f06b6fc22bbd2f289a8abcdf7e95`
- upstream source: `tex/slackMCA_v4.tex`, SHA-256
  `810ac469b8a8a8ba4638d882ec8426be95ffddf0f8888b83315afb4d60e990b4`,
  labels `thm:exactcount` and `prop:qfloor`
- open upstream PRs at the pin: `#1087--#1108`; none advertises a competing
  direct-E1 or clean-anchor value-set result

## Burn-down

```text
node attacked: unsafe_crossing_family_instantiation, direct-E1 branch
result: NARROWED; exact finite compiler and two generated-field route cuts PROVED
DAG delta: +1 off-orbit PROVED node and typed req/ev edges; E1 target re-posed
critical delta: none; math orbit remains 242 = 180/38/24
upstream terminal delta: exactcount is upstream-proved; finite row compiler is local
delta-star bracket movement: none
new assumptions: none
compute spend: none; bounded local exact replays only
live compute requests: none
next route-deciding action: prove or falsify the pointwise P allowance on the
  |F_p(Q)|>=b_pair_min class; route both lower field ranges separately
```
