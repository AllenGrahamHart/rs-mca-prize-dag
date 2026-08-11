# `A=1` constant-residual triple-tangency packets

- **status:** PROVED
- **closure:** local cube valuation and exact defect allocation
- **consumer:** `rate_half_band_crossing_location`

Retain a parameter-constant first-degree profile and write

```text
A_0=B R_a,       deg R_a=a,       G=B G_L,             (CTP1)
```

where `B` is the product of the heavy residual-domain rows.  Let `E` be
the heavy rows at which `R_a` vanishes.  Split the heavy supported
incidences into `I_E` incidences on `E` and `I_0` incidences off `E`, so
`I_H=I_E+I_0`.

At every incidence counted by `I_0`, the horizontal intersection
multiplicity of `C` with the supported fibre is a positive multiple of
three.  Equivalently, the specialized excess recurrence factor consumes at
least two degrees there.  Incidences on `E` consume at least one degree.
Consequently

```text
2 I_0+I_E<=sum_gamma c_gamma<=Delta.                   (CTP2)
```

This completely pins the two smallest constant residuals.

## Core-free residual degree two

For `s=0,a=2`, there are exactly two distinct heavy rows `x_1,x_2` at
which `R_2` vanishes, and

```text
Delta=2e-1,       I_H=2e-2,       O=Delta,
I_0 in {0,1}.                                           (CTP3)
```

Writing `c_i=e-d_(x_i)` for their row deficits, the only packets are

```text
I_0=0: {c_1,c_2}={1,1};
I_0=1: {c_1,c_2}={1,2}.                                (CTP4)
```

Thus `R_2` is split and squarefree on those two heavy domain rows.  In the
second packet there is exactly one ordinary heavy incidence; in the first
there is none.

## Core-one residual degree one

For `s=1,a=1`, the root `x_*` of `R_1` is a heavy residual-domain row.  Put

```text
u=Delta-I_H,       v=Delta-O,       Delta=e-2.
```

Then the complete packet list is

```text
(u,v,I_0,c_(x_*)) in
  {(0,2,0,2),
   (1,1,0,3), (1,1,1,4),
   (2,0,0,4), (2,0,1,5), (2,0,2,6)}.                  (CTP5)
```

In particular `A_0` has a double root at `x_*`, that row has at least
`e-6` supported slopes, and there are at most two ordinary heavy
incidences.

## Scope

The theorem classifies but does not exclude the packets in `(CTP4)` and
`(CTP5)`.  It makes no transversality or smoothness claim at an incidence;
the multiplicity statement is the local intersection length on the reduced
Cartier curve.
