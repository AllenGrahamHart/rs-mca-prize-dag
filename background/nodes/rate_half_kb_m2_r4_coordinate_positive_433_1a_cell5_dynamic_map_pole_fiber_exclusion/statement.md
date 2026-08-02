# KoalaBear positive 433-1a cell-5 dynamic map-pole fiber exclusion

- **status:** PROVED
- **scope:** the 38 map-only pole values in the proved cell-5 exceptional
  router, with signs `(-1,-1)`
- **consumer:** `rate_half_band_closure`

Let `L` be multiplication by the generic primitive coordinate

```text
s=x1+2*x0+3*b
```

on the proved 24-dimensional localized signed-pair algebra.  Although the
three polynomial coordinate maps `p_u(s)` have poles at these 38 values,
the exact rational matrices `p_u(L)` cancel every such pole.  They specialize
to commuting multiplication operators `M_x1,M_x0,M_b` at every routed value.

At each fiber an exact Krylov search chooses a new primitive form.  The form
`x1+2*x0+b` works at 33 values and `x1+3*x0+b` at the other five.  The
resulting squarefree minimal polynomials have total degree 24.  Factoring
them and freshly rebuilding the necessary `DE+` and colored `BE` equations
gives 804 irreducible component rows:

```text
220  common gcd 1;
584  common gcd e^2-1.
```

Thus every component is empty or violates target square distinctness, and
all 38 map-pole fibers contain no admissible packet in cell 5 and sign row
`(-1,-1)`.

This does not treat the eight basis-specialization hazards, another sign or
cell, delete cell 5 or route `433-1a -> O0b`, close K3, a Prize row, LIST, or
MCA.

## Falsifier

An uncancelled coordinate-operator pole, a noncommuting specialization, a
singular claimed Krylov basis, an omitted irreducible component, an outside
colored gcd, or an admissible packet at one of the 38 listed fibers.
