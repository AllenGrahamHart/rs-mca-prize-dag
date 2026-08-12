# Proof

## 1. The floor and its range

`(C2)` charges each type-2 slope a per-slope floor of `(R+1) - w*`, where
`w* = |W| = |S_g u S_h|`. Since `|S_g| = |S_h| = r`,

```text
w* = 2r - |S_g ^ S_h|,     so     r <= w* <= 2r,
```

the lower end being total overlap and the upper end disjointness. An
adversary choosing the configuration takes `w*` as LARGE as possible, i.e.
`w* = 2r`.

## 2. The equivalence

`floor(W) > 0` for every admissible `W` iff it is positive at `w* = 2r`, i.e.
iff `2r <= R`. At rate one half, `k = n/2` so `R = n - k = n/2`, and
`r = n - a`. Then

```text
2r <= R  <=>  2(n-a) <= n/2  <=>  2n - 2a <= n/2  <=>  a >= 3n/4.
```

The two conditions are literally the same condition. The verifier checks the
equivalence exhaustively for every `(n, a)` with `n <= 398` even.

## 3. The razor evaluation

At `n = 2^41`, `k = R = 2^40`, `rho = 2^34`, `a = k + 2^34`:

```text
r = n - a = R - rho = 63*rho = 1082331758592,
2r = 2164663517184,
floor = (R+1) - 2r = 1099511627777 - 2164663517184 = -1065151889407.
```

Positivity would require

```text
|S_g ^ S_h| >= 2r - R = 126*rho - 64*rho = 62*rho = 62r/63,
```

that is, an overlap of `98.412698%` of each support. Nothing in the problem
forces such an overlap, so the requirement is adversary-free and the floor is
negative for the configurations that matter.

## 4. The bracket

For any `a` in `[k+2^34, 3n/4)` we have `r = n-a > n/4 = R/2`, hence
`2r > R` and the floor at `w* = 2r` is negative. At the excluded top
`a = 3n/4 = k + 2^39` one gets `r = 2^39`, `2r = R`, and the floor is exactly
`(R+1) - R = +1`: **the sign flips precisely at the boundary**. The verifier
confirms both halves.

Therefore the ledger cannot bind anywhere on the open bracket, and it is
vacuous by SIGN before any question of counting slack arises. Any instrument
derived from `(C2)` — `(C3)`, `(C4)`, the `X_gamma` bookkeeping, or the
layer-A transports built on them — inherits the vacuity.

## 5. What this does NOT say

It says nothing about the true value of `B_ca^far` on the bracket. It only
removes a family of instruments from consideration there. The value question
is Statement U's, and U's cap is supplied by an independent pigeonhole for
exactly this reason.
