# KoalaBear m2 r4 positive 433-1a/O0b signed-edge atlas

- **status:** PROVED
- **scope:** the positive residual route `433-1a -> O0b`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_positive_residual_loop_workboard` and
  `rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler`
- **consumer:** `rate_half_band_closure`

Name the common target pairs `A,B,C`, with common degrees `(4,3,3)`,
common loop `C`, common multiplicities

```text
l=(0,0,1),             m_AB,m_AC,m_BC=(3,1,0),    (KBPSA-1)
```

and outside pairs `D,E,F`.  Normalize the two deficient colored
attachments to `B-E,C-F`.  The unique outside graph `O0b` has

```text
r=(0,1,1),             m_DE,m_DF,m_EF=(2,2,1).    (KBPSA-2)
```

The common loop and multiplicity-three `AB` pair spend the whole defect
budget three.  Hence the three `AB` records split `2+1` between their two
signed types, while each multiplicity-two outside pair uses its two
different signed types.

After target-representative sign gauge, put
`A=a,B=b,C=c,D=d,E=e,F=f`.  There are exactly two signed lanes,
indexed by `sigma in {+1,-1}`, with the twelve target-product records

```text
common:  -c^2;  ab,ab,-ab;  ac;
colored: be,cf;
outside: de,-de, df,-df, sigma ef.                 (KBPSA-3)
```

The sole invariant is the sign product around the five-cycle

```text
A-B-E-F-C-A.                                      (KBPSA-4)
```

For every nonloop product `p=epsilon uv`, the associated square-root-free
sum datum is `s^2=u^2+v^2+2p`; the loop has product `-c^2` and sum zero.
Thus `(KBPSA-3)` supplies all target data needed by the complete Vieta
rows once the twelve source quotient labels are assigned.

This theorem does not assign source fibers or quotient labels, impose the
coefficient kernel, prove either lane realizable or empty, delete positive
coordinate parity, close K3 or a Prize row, or prove either Prize result.

## Falsifier

An actual `433-1a -> O0b` packet with a signed target-edge multiset outside
the two lanes `(KBPSA-3)`, or a listed lane that fails target degree four
or total defect three.
