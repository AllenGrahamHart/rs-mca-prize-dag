# Cycle 352: MCA rank-11 K'=13 sparse-circuit payment (2026-08-15)

Cycle 351 closed `K'=12` by controlling sparse circuits selected by a
projective quotient line.  At `K'=13`, the annihilator of the
ten-dimensional correction space is three-dimensional.  A direct
classification of its secant-plane intersection would be substantially
stronger than the row requires.

## Cycle pins

```text
our start:       8f1fb27314
canonical prize: 6ac775504a
upstream main:   93fba1be3f
open upstream:   #1170 in the rank-eleven dense-locator packet
```

## Codimension-three completion dichotomy

For a support-`c` circuit, delete one point and call the resulting
independent `(c-1)`-set `A`.  The common-zero space

```text
H_A={f in V:f|_A=0}
```

has dimension `11-c`.  Generalized MDS therefore permits at most three
circuit completions of `A`.

- If some `A` has three completions, their circuit labels are independent
  and span the three-dimensional quotient.  Vandermonde uniqueness then
  places every support-at-most-five quotient circuit in one carrier of size
  at most seven.
- Otherwise every `A` has at most two completions.  A full-rank eleven-set
  cannot contain both labels, so deletion double-counting gives an exact
  two-completion bound.

At `m'=67485`, the structured-carrier and two-completion caps are

```text
1679076702065233864778823429158845084750,
99254447944649683780146155758753837527116020.
```

The second is the uniform sparse-circuit cap per residual record.  No
classification of planes in secant varieties is used.

## Complete K'=13 payment

The shortening excess is three, so both corank-one and corank-two kernel
terms survive, with extension factors three and one.  Their exact combined
capacity is

```text
K_cap=206481189843433295842936213010503229833431068859362597823.
```

For full-rank components, circuits of size at least six create at least 45
rank-nine shadows.  The common-core offset cap over `j=9,10,11,12` is

```text
C_*=9278059895199813,
```

giving high-circuit capacity

```text
H_cap=870791924265139618716231673259817164224620222733319378834968170.
```

At the minimum residual-record count, kernel plus high plus low capacity is

```text
898085191110430398284744062896212914931984716650701254999384513,
```

against full component-incidence demand

```text
901702217989192688449626641411280218028664942551160634607759137.
```

The exact positive gap is

```text
3617026878762290164882578515067303096680225900459379608374624.
```

The demand-minus-low record coefficient is positive, so checking the
minimum record population is sufficient.

```text
result:                PROVED K'=13 component-row closure
newly closed row:      13
remaining rank nine:  14..15528
new nodes:             2 PROVED
new premise:           none
compute:               exact integer arithmetic and two small GF(17) audits
next route action:     determine whether the completion dichotomy scales to
                       quotient dimension four at K'=14, retaining all
                       kernel coranks and core offsets j=9..13
```
