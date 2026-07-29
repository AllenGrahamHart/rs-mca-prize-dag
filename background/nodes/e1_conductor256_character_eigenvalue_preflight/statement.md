# Conductor-256 character eigenvalue preflight

- **status:** PROVED
- **closure:** directed interval arithmetic and exact finite dynamic programming
- **dependency:** `e1_conductor256_character_diagonal_exponent_router`
- **consumer:** `e1_official_low_square_mass_pair_budget` (evidence)

Use the notation `kappa_j`, `D`, `R`, and `xi` from the character-diagonal
router.  A self-contained directed-decimal computation certifies all 63
nontrivial eigenvalues.  If each magnitude interval is rounded outward at
30 decimal places, the complete table has digest

```text
6ee33c37477a58c92a087cd7dcf3c128d148a2c8d08887141ff79367aa9efb8d.
```

In particular,

```text
min_(1<=j<=63)|kappa_j| > 1.7627       (attained at j=32),
max_(1<=j<=63)|kappa_j| < 24.292       (upper maximum at j=11,53),
sum_j |kappa_j|^(-1) < 6.556,
sum_j |kappa_j|^(-2) < 1.090.             (CEP1)
```

On every prize-envelope branch, `p>2^255` and `mu>=1`, so

```text
D < log(18^64/2^256) < 7.539,
R < 77.202.                                (CEP2)
```

The integer bounds `(CER8)--(CER9)` therefore sharpen uniformly to

```text
max_t |xi(g_t)| <= 7,
sum_t xi(g_t)^2 <= 101.                    (CEP3)
```

These bounds make the search finite but not affordable.  The exact number of
zero-sum integer 64-vectors satisfying the coarse box and Euclidean bounds in
`(CEP3)` is

```text
16616854517524950208619690062355423946568371 > 2^143.   (CEP4)
```

Nor does the weighted ellipsoid alone provide the missing pruning.  In the
universal radius-`77.202` enclosing ellipsoid, every vector with `k` entries
`+1`, `k` entries `-1`, and all other entries zero lies inside for `0<=k<=5`.
These already give

```text
sum_(k=0)^5 binom(64,k)binom(64-k,k)
  =38482585013041                                      (CEP5)
```

distinct unit exponent vectors modulo torsion.

Consequently a generic coordinate, Euclidean, or character-ellipsoid
enumeration is rejected as the successor to the router.  Any viable count
must impose the exact sparse profile product and the coefficient bounds for
both `u` and `u^(-1)` before generating this ambient lattice body, or prove a
new algebraic classification of sparse unit associates.  This preflight
does not count surviving associates, prove the 367-orbit cap, pay lower
profiles, or close E1.

## Falsifier

An exact eigenvalue outside its certified interval, an exponent vector from a
live same-cofactor associate family violating `(CEP3)`, or a disagreement
with the exact dynamic-program count `(CEP4)`.
