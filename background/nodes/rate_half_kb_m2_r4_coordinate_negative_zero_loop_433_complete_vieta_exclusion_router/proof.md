# Proof

## 1. Exact extension model

In the quotient `(KBZ433V-1)`, reduction uses `X^6=-X-6`.  Binary powering
gives

```text
X^(p^6-1)=1
```

and gives a nonidentity for division of the exponent by each prime in

```text
{2,3,7,67,127,283,1254833,
  9679978477096567,1513303300498959019}.
```

These are all prime divisors of `p^6-1`, so `X` has order `p^6-1`; in
particular the quotient is a field and `X` is primitive.  The same replay
gives `g^M=3` and full order for `g=X^1768759633`.  A base value `a` whose
discrete logarithm to base `3` is `e` is therefore exactly `g^(Me)`.  This
proves that the explicit arithmetic and the product-router Smith ledgers use
the same embedding.

## 2. Forced outside sum equation

For each common record, the first three rows

```text
[-p,-p kappa,1,kappa]
```

have rank three.  Their one-dimensional kernel gives
`(d_0,d_1,n_0,n_1)`, and all five common rows replay.  The denominator
`d_0+d_1 kappa` is the negative Vieta form `B_2` up to one common nonzero
scale.

The common-root representatives from the finite atlas give

```text
q_kappa=x_kappa(u+v),       kappa=x_kappa^2.
```

The five values `-q_kappa B_2(kappa)` interpolate one quadratic and replay
on all five rows.  By the complete-fiber Vieta compiler this quadratic is
`A_1` in the same scale.  Product injectivity makes the Mobius inverse
defined at every outside product and gives the first equation in
`(KBZ433V-2)`.  The sum equation is

```text
A_1(kappa)+q_kappa B_2(kappa)=0.
```

Squaring `q_kappa=x_kappa(u+v)` removes the harmless deck choice
`x_kappa -> -x_kappa` and proves the second equation in `(KBZ433V-2)`.
Hence failure of that equation is a necessary complete-packet exclusion.

## 3. Exhaustive routed census

The outside-skeleton compiler expands every signed edge as an explicit pair
of target labels.  Multiplying each expanded pair replays its product form.
The two product routers then supply every compatible Smith system.

For cells `[2,5,6,9]`, the only product-live types were `Z0,Z1,Z4` and no
type had a positive-dimensional system.  On the four distinct `(b,c)` rows
their distinct guarded product-assignment counts are respectively

```text
48,128,64.
```

Each row has two common q records, for `4*2*(48+128+64)=1920` exact tests.
Every first outside row fails `(KBZ433V-2)`.  Target sign/exchange is an
invertible change of the normalized target coordinate and transports the
complete Vieta equations, so the cell-2 calculation deletes the full
four-cell orbit.

In cell 12, the `Z4` counts on its eight distinct product rows are

```text
80,80,80,80,48,48,48,48.
```

With two common q records each, these give `1024` failures.  The 16 free
Smith systems on each product row all have an exact collision certificate.

In each of cells 13 and 14, every one of four product rows has 96 guarded
`Z1` assignments and 128 guarded `Z3` assignments.  Two common q records
give `1792` failures per cell.  `Z1` has no family; each product row has 32
`Z3` family systems and every one has a collision certificate.  The total
is therefore

```text
1920+1024+1792+1792=6528
```

isolated tests and `8*16+2*4*32=384` collision-forced family systems.
This proves `(KBZ433V-3)`.

The prior product deletions leave `Z2,Z3,Z4` in cell 12 and `Z1,Z2,Z3` in
cells 13 and 14.  Removing exactly the lanes in `(KBZ433V-3)` gives
`(KBZ433V-4)`.  The verifier records unresolved free systems in all four
remaining lanes and makes no claim about them. QED.
