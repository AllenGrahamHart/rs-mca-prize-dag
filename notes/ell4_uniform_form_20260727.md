# The ell=4 lane is one combinatorial question (2026-07-27)

All three open `ell = 4` cells collapse to a single statement about subsets of a
cyclic 2-group. Verified against the banked `(4,9)` existence witness.

> **`(4,w)` holds iff there are `w` distinct `rho_i in mu_2048` with**
> ```text
> e_1 = e_3 = e_5 = e_7 = 0,
> ```
> **plus, for ODD `w` only, the dilation normalisation `e_w = 1`.**

| cell | subset size | conditions | normalisation |
|---|---|---|---|
| (4,9) | 9 | `e_1,e_3,e_5,e_7` + `e_9 = 1` | dilation exists (`gcd(9,2048)=1`) |
| (4,10) | 10 | `e_1,e_3,e_5,e_7` | **none exists, none needed** |
| (4,11) | 11 | `e_1,e_3,e_5,e_7` + `e_11 = 1` | dilation exists (`gcd(11,2048)=1`) |

The four vanishing conditions are just the window `p_1=p_3=p_5=p_7=0` transported
by Newton (valid for `char > w`).

## The polynomials were never unknowns

Every quartic/quintic and every divisor polynomial in these three nodes is a
*repackaging* of these symmetric functions:

```text
(4,9)   F = X A(X^2) - 1            A's coefficients = the EVEN e_k of the rho
(4,10)  F = E(X^2) - e_9 X          E's coefficients = the even e_k, plus e_10
(4,11)  F = X B(X^2) - (e_9X^2+1)   B's coefficients = the even e_k
```

Confirmed on the witness: its `rho` have `e_2 = 58`, `e_4 = 240`, `e_6 = 133`,
`e_8 = 86`, which are exactly `A = Y^4 + 58Y^3 + 240Y^2 + 133Y + 86` read backwards.
**`A`, `E`, `B` are outputs, never unknowns**, and the `G`-divisibility is automatic
once the `rho_i` lie in `mu_2048`. That is why every attempt to attack the cells
through the polynomial (elimination ideal, `Delta` certificate, resultants) was
fighting a reparametrisation rather than the problem.

## What this buys

1. **One target for three cells.** Bound the number of `w`-subsets of `mu_2048` with
   four vanishing odd symmetric functions (and product one, for odd `w`).
2. **The even/odd asymmetry is now cosmetic** — it is only whether a fifth condition
   `e_w = 1` is present. The parity dichotomy's obstruction (`gcd(w,2048)`) governs
   whether that condition can be *imposed*, not whether the cell is harder.
3. **It composes with the existence witness.** The witness proved no structural
   argument can close a WCL cell; this says exactly what the quantitative argument
   must count.

Likely generalises to `(ell,w)` as `w` distinct `rho_i in mu_{512*ell}` with
`e_1 = e_3 = ... = e_{2*ell-1} = 0` — `ell` conditions — but that is checked here
only for `ell = 4`; the closed `ell = 2` cells state their window as
`P(omega) = P(omega^3) = 0` rather than as power sums, and the equivalence has not
been verified.
