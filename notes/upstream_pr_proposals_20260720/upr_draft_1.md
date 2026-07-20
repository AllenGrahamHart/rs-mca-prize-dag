# PR DRAFT 1 (RANK 1) — Independent exact-integer audit of the §0.4 four-pair crossings and constants

> Title: **Audit: independent exact-integer replay of the four §0.4 adjacent-pair crossings, margins, and field budgets**

Base: `origin/main@9908454995f3f195cfe748f35a1135211609d066` (towards-prize v13.2).
Cross-repo reference (SHA-pinned, read-only mirror):
`github.com/AllenGrahamHart/rs-mca-prize-dag@b8a169acb020f4a8cf990a552daf12b29127337b`,
node `notes/correspondence/REGIME_MAP.md` + replay `notes/correspondence/four_pairs_exact.py`,
node-local datum `critical/nodes/rate_half_band_closure/notes/upstream_determination_datum.md`.

## Scope

This is an **audit**, not a new bound. It independently re-derives, from a separate codebase and by
exact integer arithmetic (no floating point in the decision), the four §0.4 adjacent-agreement
crossings, their bit-margins, and the two field budgets, and it pins the exact exponent convention
that makes MCA "one factor of `p` easier" than list.

For `n = 2^21`, `K = k+1 = 2^20`, the single first-moment crossing family is:

```text
list row : unsafe(m)  <=>  C(n,m) >  p^(m-K)   * floor(q * eps*)
MCA  row : unsafe(m)  <=>  C(n,m) >  p^(m-K-1) * floor(q * eps*)   [pencil dof: identity witness at K=k+1]
```

Exact-integer replay (verifier reproduces every location and margin in `<row>` HISTORY §0.4):

| row | a0 (unsafe) | a0+1 (safe) | unsafe margin | safe margin | printed |
|---|---:|---:|---:|---:|---:|
| KoalaBear MCA  | 1,116,047 | 1,116,048 | +8.978  | −22.197 | 22.2 |
| KoalaBear list | 1,116,046 | 1,116,047 | +9.164  | −22.011 | 22.0 |
| Mersenne MCA   | 1,116,023 | 1,116,024 | +27.927 | −3.259  | 3.3  |
| Mersenne list  | 1,116,022 | 1,116,023 | +28.113 | −3.073  | 3.1  |

Field budgets independently recomputed and cross-checked:

```text
KoalaBear  q = (2^31-2^24+1)^6,  eps* = 2^-128
           B_* = floor(q/2^128) = 274,980,728,111,395,087
Mersenne   q = (2^31-1)^4,       eps* = 2^-100   (extra-official: circle domain, quartic field)
           B_* = floor(q/2^100)  = 16,777,215 = 2^24 - 1
```

The KoalaBear `B_*` agrees with the RF3'' KoalaBear safe-row budget printed in the tree at
`999b8f3a`; the Mersenne `B_*` agrees with the budget in open PR **#993**. The KoalaBear MCA radius
`n − a0 = 981,105` and `delta = 981105/2097152 = 0.46782732...` reproduce the §0.1 unsafe-edge row
exactly.

## Why this is worth banking

The Mersenne margins are only `3.259` / `3.073` bits. Your §0.4 note states that "an unspecified
poly(n) loss is not a finite certificate"; at 3-bit margins even a floating-point audit is unsafe.
This replay decides every crossing by exact big-integer comparison, so the margins are certified, and
the MCA-vs-list `−1` exponent (the pencil degree of freedom / identity-witness at `K=k+1`) is pinned
as an exact constant rather than an asymptotic.

## Verification

- stdlib-only, fail-closed verifier; passes under `python3` and `python3 -O` with byte-identical
  output; `py_compile` clean.
- All four pairs decided by exact `math.comb` / `pow` integer comparison (no float in the branch);
  floats only for the reported margin display.
- Semantic mutations (wrong exponent `m−K` on the MCA row, wrong `ε*`, off-by-one `a0`) are rejected.
- Cross-source constant checks: KoalaBear `B_*` vs `999b8f3a`; Mersenne `B_*` vs #993.

## Non-claims (fence)

This PR does **not**:

- prove or bound the **safe side** at `a0+1` — that is your conjecture (Q/extremality); we confirm
  only the crossing LOCATION arithmetic and the unsafe-side realization,
- close, move, or pin any threshold; official score is unchanged,
- import, re-derive, or independently re-verify your identity-prefix witnesses,
- claim any Grand MCA / Grand List / Proximity Prize result,
- assert anything about `B_ap`, the v12 Hankel band, or any near-capacity safe ledger,
- claim that our determined rate-1/2 family (see companion) transports to these `n=2^21` rows — it
  does not (different `n`, field, `δ`, and Mersenne `ε*`).

## Falsifiability note (your §0.5)

This audit is consistent with your envelope: it exhibits no super-polynomial primitive prefix fiber
and no super-polynomial primitive split-pencil family; it only replays the finite crossing arithmetic
your program already proves on the unsafe side.
