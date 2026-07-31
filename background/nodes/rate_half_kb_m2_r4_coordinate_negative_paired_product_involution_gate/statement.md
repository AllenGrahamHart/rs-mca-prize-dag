# KoalaBear m2 r4 coordinate negative paired-product involution gate

- **status:** PROVED
- **scope:** every negative-parity coordinate-order-two component in the
  residual `(m,r,delta)=(2,4,2)` row
- **dependency:**
  `rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler`
- **consumer:** `rate_half_band_closure`

Write the twelve source labels as six deck pairs `{+/-kappa_i}`.  Let

```text
y_i=p_(kappa_i),       z_i=p_(-kappa_i)
```

be the products of the two horizontal roots in their source stars.  Every
actual negative packet satisfies

```text
rank [y_i z_i, -(y_i+z_i), -1]_(i=1,...,6) <= 2. (KBNP-1)
```

More precisely, the matrix has a kernel vector `(c,a,b)` with

```text
a^2+bc != 0,       c y_i z_i-a(y_i+z_i)-b=0.      (KBNP-2)
```

Thus all six product pairs are free orbits of one nontrivial projective
involution.  Failure of any `3 x 3` minor deletes the negative packet before
choosing source square roots or evaluating edge sums.

There is a useful symbolic collapse.  If two product pairs are

```text
(u,-u),       (v,-v),       u^2!=v^2,
```

then `(KBNP-2)` forces `c=b=0` and `a!=0`.  Consequently every product pair
satisfies

```text
y_i+z_i=0.                                         (KBNP-3)
```

The exact defect-zero abstract source-facet fixture is therefore impossible
in negative parity over every odd field.  Its paired products include
`(AC,-AC)` and `(BC,-BC)` with `A^2!=B^2`, so `(KBNP-3)` applies.  But its
first pair is `(DE,DF)` and has nonzero sum `D(E+F)` because `E` and `F`
are distinct signed pairs.  As a regression, all `7P6=5040` assignments of
six distinct signed square-pairs from `F_29` fail `(KBNP-1)`; the printed
assignment has first-three-row determinant `12`.

No positive-parity packet, coordinate orientation, owner, payment, row, or
Prize result is deleted by this node.

## Falsifier

An actual negative coordinate packet whose six paired products violate
`(KBNP-1)--(KBNP-3)`, or a negative realization of the deleted fixture.
