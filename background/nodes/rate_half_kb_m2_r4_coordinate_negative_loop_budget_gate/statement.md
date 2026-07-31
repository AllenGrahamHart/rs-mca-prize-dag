# KoalaBear m2 r4 coordinate negative loop-budget gate

- **status:** PROVED
- **scope:** every negative-parity coordinate-order-two component in the
  residual `(m,r,delta)=(2,4,2)` row
- **dependency:**
  `rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler`
- **consumer:** `rate_half_band_closure`

Among the five common-`K` edge orbits, let `ell_K` be the number of
antipodal `J` edges `{j,-j}`.  Every actual negative packet satisfies

```text
ell_K<=2.                                           (KBNL-1)
```

Consequently the seven injective pair-multiplicity skeletons in `(KBCV-6)`
reduce to exactly five:

```text
(4,4,2): (0,1,0;2,2,0), (1,1,0;1,1,1),
(4,3,3): (0,0,0;2,2,1), (1,0,0;1,1,2),
           (1,0,1;2,0,1).                         (KBNL-2)
```

The tuple notation is `(l_0,l_1,l_2;m_01,m_02,m_12)` as in the parent.
In the two-loop stratum, the quadratic `A_1` is projectively fixed by the
two loop-fiber roots.  In the one-loop stratum it has the corresponding
linear factor.

This gate does not exclude the five remaining skeletons, positive parity,
the coordinate orientation, any owner/payment, a row, or either Prize
result.

## Falsifier

An actual negative packet with three common-`K` antipodal edge orbits, or a
pair-multiplicity skeleton surviving the parent injectivity cut but outside
the five rows in `(KBNL-2)`.
