# KoalaBear m2 r4 diagonal c2 (2,0,2) ramified-defect exclusion

- **status:** PROVED
- **scope:** the source-line branch of the diagonal `(a,b,c)=(2,0,2)` row
- **dependencies:**
  `rate_half_kb_m2_r4_diagonal_c2_square_fiber_linear_cut` and
  `rate_half_kb_m2_v4_outer_recurrence_router`
- **consumer:** `rate_half_band_closure`

The forced square fiber in `(KBDM-8)` cannot lie over the ramified source
orbit of `W=X^2`:

```text
w notin {0,infinity}.                              (KBRD-1)
```

Indeed, if `w` were ramified, the reciprocal source-line symmetry would
make both `w` and `tau(w)` ramified. Their square quartics contribute two
distinct star vertices of weight at least two, costing at least two units of
the complete-source defect

```text
Delta_star=sum_v binom(weight(v),2).
```

The four labels in `K_0=K intersect tau(K)` are then unramified. Their eight
reduced quadratic stars are all two-subsets of the four-label set `J_0`, so
they occupy at most `binom(4,2)=6` further star vertices. Eight units on six
vertices cost at least two more defect units. Thus

```text
Delta_star >= 2+2=4,                               (KBRD-2)
```

contradicting the proved complete-source budget `Delta_star<=3`.

Consequently every source-line `(2,0,2)` packet lies in the unramified case
of `(KBC2-2)--(KBC2-5)`: its reciprocal coefficient spaces have dimensions
exactly `4/3` before the open exact-degree conditions.

This deletes only the ramified source-line subcase. It does not delete the
unramified `(2,0,2)` row, the `(1,1,2)` row, the biquadratic source-cover
branch, the diagonal orientation, an owner, payment, row, or Prize result.

## Falsifier

An actual source-line `(2,0,2)` component with its forced square fiber at a
source branch value; eight reduced `J_0` stars occupying more than six
vertices; or a complete-source packet with `Delta_star>=4`.
