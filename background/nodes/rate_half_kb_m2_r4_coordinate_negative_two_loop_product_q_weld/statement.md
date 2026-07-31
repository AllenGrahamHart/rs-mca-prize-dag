# KoalaBear m2 r4 coordinate negative two-loop product-to-q weld

- **status:** PROVED
- **scope:** every negative-parity coordinate packet in either two-loop
  skeleton retained by `(KBNL-2)`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_complete_fiber_vieta_compiler` and
  `rate_half_kb_m2_r4_coordinate_negative_loop_stratified_q_compiler`
- **consumer:** `rate_half_band_closure`

Let `lambda,mu in K` be the two loop labels, put

```text
R(W)=(W-lambda)(W-mu),
```

and let `N=B_0`, `D=B_2`.  At all five common fibers write

```text
p_s=N(s)/D(s).
```

The five product rows

```text
[-p_s,-p_s s,1,s]                                  (KBNW-1)
```

have rank exactly three.  Their one-dimensional kernel reconstructs
`(D_0,D_1,N_0,N_1)`, with `D(s)!=0` on `K`.

Fix either loop label `h in {lambda,mu}`.  For every two distinct nonloop
labels `i,j`, the packet satisfies the denominator-free weld

```text
q_i R(j)(h-i)(p_h-p_j)
 = q_j R(i)(h-j)(p_h-p_i).                         (KBNW-2)
```

After `(KBNW-1)` and leading support hold, choose one of the three nonloop
labels `i_0`.  The two instances of `(KBNW-2)` pairing `i_0` with the other
two labels are necessary and sufficient for the complete five-row
common-`K` sum system

```text
A_1(s)+q_s B_2(s)=0,       A_1=cR.                 (KBNW-3)
```

Thus a signed two-loop candidate is tested by the rank-three product gate
and two scalar welds, rather than an unrelated `3 x 3` determinant.  The
edge-orbit signs remain part of the `q_s` data.

This theorem does not prove either two-loop skeleton empty, classify its
signed assignments, impose the six complement fibers, delete positive
parity, move an owner/payment, close a row, or prove either Prize result.

## Falsifier

An actual negative two-loop packet whose product rows do not have rank
three, which violates `(KBNW-2)`, or for which the two welds do not exactly
reconstruct `(KBNW-3)`.
