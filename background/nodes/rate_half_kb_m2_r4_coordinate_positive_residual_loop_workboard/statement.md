# KoalaBear m2 r4 positive residual loop workboard

- **status:** PROVED
- **scope:** positive-parity coordinate-order-two packets in the residual
  `(m,r,delta)=(2,4,2)` row
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_positive_loop_ramification_gate`,
  `rate_half_kb_m2_r4_coordinate_positive_ramified_loop_multiplicity_exclusion`,
  and `rate_half_kb_m2_r4_order2_coordinate_source_facet_signature`
- **consumer:** `rate_half_band_closure`

Write a common skeleton as `(l_A,l_B,l_C;m_AB,m_AC,m_BC)`.  The global
positive loop cap and defect budget reduce the parent's ten common orbits
to exactly five live orbits and seven labeled skeletons:

```text
profile  name     common skeleton   orbit  defect  verdict
442      442-0a   (000;311)           1      2     live
442      442-1a   (001;400)           1      5     delete by defect
442      442-1b   (010;220)           2      1     live
442      442-2    (110;111)           1      2     delete by loop cap
442      442-3    (111;200)           1      3     delete by loop cap
433      433-0    (000;221)           1      0     live
433      433-1a   (001;310)           2      3     live
433      433-1b   (100;112)           1      1     live
433      433-2    (101;201)           2      2     delete by loop cap
433      433-3    (111;110)           1      3     delete by loop cap.       (KBPRW-1)
```

For the outside signed pairs `D,E,F`, let `r_i` count the two colored
`I-J` edge orbits, `l_i` count outside loops, and
`m=(m_DE,m_DF,m_EF)` count the remaining internal `I-I` edge orbits.  Up
to permuting `D,E,F`, all solutions of

```text
sum r_i=2,  sum l_i+sum m_ij=5,
r_i+2l_i+sum_(j!=i)m_ij=4                         (KBPRW-2)
```

with `sum l_i<=1` are the following six orbits:

```text
name  (r;l;m)             orbit  defect
O0a   (002;000;311)         3      2
O0b   (011;000;221)         3      0
O1a   (002;001;400)         3      5
O1b   (002;010;220)         6      1
O1c   (011;001;310)         6      3
O1d   (011;100;112)         3      1.             (KBPRW-3)
```

Adding common and outside defect, imposing total defect at most three,
and using that a common loop forbids an outside loop gives the exact
necessary route table:

```text
442-0a -> O0b, O1b, O1d
442-1b -> O0a, O0b
433-0  -> O0a, O0b, O1b, O1c, O1d
433-1a -> O0b
433-1b -> O0a, O0b.                              (KBPRW-4)
```

Thus thirteen representative route records remain.  The table pairs
common and outside orbit representatives; it is not a count of fully
labeled packets.  This theorem does not assert that any route is
algebraically realizable, impose its complete Vieta equations, close
positive coordinate parity, close K3 or a Prize row, or prove either Prize
result.

## Falsifier

An actual positive coordinate packet whose common/outside skeleton is
absent from `(KBPRW-4)`, or a listed integer row that fails the degree,
global-loop, or defect equations.
