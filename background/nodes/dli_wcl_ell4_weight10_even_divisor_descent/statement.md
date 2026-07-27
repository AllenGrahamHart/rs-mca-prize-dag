# WCL `(4,10)` even-weight divisor descent

- **status:** PROVED
- **closure:** proof
- **consumer:** `dli_wcl_slot_4_10_emptiness`
- **dependencies:** `dli_wcl_ell4_weight9_quartic_divisor_descent` (the odd-weight
  template), `dli_wcl_newton_short_window_exclusion`

Let `char K = 0` or `> 10`, with `omega` of exact order `2048`. For a reduced signed
weight-ten relation `rho_i = s_i omega^{e_i}` assume the `ell = 4` window

```text
p_1 = p_3 = p_5 = p_7 = 0.                                        (EDD1)
```

## The parity obstruction is sidestepped, not routed around

`gcd(10, 2048) = 2`, so the global dilation `lambda = a_w^{-(w^{-1})}` used at
`(4,9)` and `(4,11)` **does not exist** here
(`verify_descent_parity_dichotomy.py`). The resolution is not a sub-tuple router:
**the even case needs no normalisation at all.**

By Newton, `(EDD1)` gives `e_1 = e_3 = e_5 = e_7 = 0`. At `w = 10` the odd indices
are `{1,3,5,7,9}` — four are killed, `e_9` survives, and `e_10 = prod rho_i` is
simply *free*, there being no dilation to fix it and no need for one. Hence

```text
F(X) = prod_i (X - rho_i)
     = X^10 + e_2X^8 + e_4X^6 + e_6X^4 + e_8X^2 - e_9 X + e_10
     = E(X^2) - e_9 X,                                            (EDD2)
E(T) = T^5 + e_2T^4 + e_4T^3 + e_6T^2 + e_8T + e_10   monic quintic.
```

**`e_9 != 0` is automatic:** `e_9 = 0` makes `F` even, so its roots fall into
antipodal pairs, which reducedness forbids.

## Square locator and reconstruction

At a root, `E(rho^2) = e_9 rho`; putting `y = rho^2` and squaring,

```text
G(Y) = E(Y)^2 - e_9^2 Y      monic of degree 10,                  (EDD3)
G(Y) = prod_i (Y - rho_i^2),      rho = E(y)/e_9.                 (EDD4)
```

Each `rho_i^2 = omega^{2e_i}` lies in `mu_1024` and reducedness makes the squares
distinct, so

```text
G(Y) divides Y^1024 - 1.                                          (EDD5)
```

Verified: for 294 reconstruction instances over `F_10007` from a fixed seed, every
root `y` of `G` gives `rho = E(y)/e_9` with `rho^2 = y` and `F(rho) = 0`.

## Shape comparison across the ell=4 cells

```text
(4,9)   F = X A(X^2) - 1               A monic quartic   4 params  [dilation used]
(4,10)  F = E(X^2) - e_9 X             E monic quintic   6 params  [NO dilation]
(4,11)  F = X B(X^2) - (e_9X^2 + 1)    B monic quintic   6 params  [dilation used]
```

The odd cells put `X` outside the even part; the even cell puts the single odd term
*inside*, as `-e_9X`. That is the whole structural difference, and it is why the
missing dilation costs nothing.

## What remains

The `Delta` certificate: `(Y^1024 - 1) mod G` gives ten relations
`R_j in Z[e_2,e_4,e_6,e_8,e_9,e_10]` — **ten relations in six unknowns**. Show the
ideal has no characteristic-zero point and extract `Delta`. The same feasibility
caveat recorded on `(4,9)` and `(4,11)` applies: symbolic `Y^1024 mod G` blows up,
so the clean form (see `(4,9)`) is the better target.

Closes no cell. `dli_wcl_slot_4_10_emptiness` stays TARGET.
