# KoalaBear m2 r4 coordinate negative one-loop 442 S1 forced-loop deployed product exclusion

- **status:** PROVED
- **scope:** common root-sign row `(epsilon_1,epsilon_2)=(1,1)`, outside
  skeleton `S1`, both parity cells, and forced loop record `DD` in the live
  sextic common orbit `[9,10,12,13]`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_s1_forced_ef_tau_minus_guarded_product_exclusion`
  and
  `rate_half_kb_m2_r4_coordinate_negative_one_loop_442_nonloop_singleton_sextic_mate_coordinate_compiler`
- **consumer:** `rate_half_band_closure`

Forcing the loop record gives

```text
-d^2=m.                                             (KB41FL-1)
```

In each of the two irreducible cubic common components, `-m` is a nonsquare.
Adjoin a root `theta` with `theta^2=-m`; this gives a genuine quadratic field
extension.  With canonical signs `alpha=beta=gamma=-1` and
`delta in {+1,-1}`, the residual binary sextic is

```text
J_delta=(X+ceZ)(X+cfZ)(X+theta*eZ)(X-delta*theta*fZ)
        (X^2-e^2f^2Z^2).                          (KB41FL-2)
```

For either parity, the three uniform equations have 17 monomials in `(e,f)`.
Exact Buchberger reduction in both degree-six tower fields reaches the raw
unit ideal:

```text
delta=-1: 57 S-pairs;
delta=+1: 55 S-pairs.                              (KB41FL-3)
```

Thus both forced-loop cells are empty.  Combined with the preceding eight
deletions, all ten `S1` product cells in common sign row `(1,1)` are empty.
The accepted four-row invariant-cell frontier falls from 72 to 70.

This theorem does not transport the `S1` deletion to another common
root-sign row, delete any `S0` or `S2` cell, impose outside `q` or full
interpolation, close the coordinate orientation or a row, or prove either
Prize result.

## Falsifier

A square root of `-m` inside a cubic component, a root of the three equations
in either quadratic extension and parity, or failure to reach the pair counts
in `(KB41FL-3)`.
