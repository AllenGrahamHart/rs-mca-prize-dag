# KoalaBear m2 r4 positive 433-1a quadratic paired-product resultant interface

- **status:** PROVED
- **scope:** every principal common survivor of the positive route
  `433-1a -> O0b`
- **dependencies:**
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_common_kernel_uniqueness`,
  `rate_half_kb_m2_r4_coordinate_positive_433_1a_o0b_signed_edge_atlas`,
  and `rate_half_kb_m2_r4_order2_coordinate_source_facet_signature`
- **consumer:** `rate_half_band_closure`

Let the five common quotient labels be two deck pairs and a singleton,

```text
K={lambda,-lambda,mu,-mu,M},       xi=-M.          (KBPQI-1)
```

For one of the fifteen matching cells, common-kernel uniqueness gives,
uniquely up to a common nonzero scalar,

```text
A_2(W)=d_0+d_1 W+d_2 W^2,
A_0(W)=e_0+e_1 W+e_2 W^2,
B_1(W)=beta_0+beta_1 W,
F(W)=A_0(W)/A_2(W).                                (KBPQI-2)
```

Every actual packet has `A_2(kappa)!=0` and product `F(kappa)` at each of
its twelve source labels.  In particular, the product `x` placed at the
missing mate `xi` obeys

```text
A_0(-M)-x A_2(-M)=0.                              (KBPQI-3)
```

For two proposed products `y,z`, write

```text
P_y(W)=A_0(W)-y A_2(W)=p_2 W^2+p_1 W+p_0,
Q_z(W)=A_0(-W)-z A_2(-W)=q_2 W^2+q_1 W+q_0
```

and define the explicit paired-product eliminant

```text
C_F(y,z)=(p_2 q_0-p_0 q_2)^2
          -(p_2 q_1-p_1 q_2)(p_1 q_0-p_0 q_1).   (KBPQI-4)
```

This is `Res_W(P_y,Q_z)`.  Hence products carried by a deck pair
`{kappa,-kappa}` necessarily satisfy `C_F(y,z)=0`.

The seven outside target products in cycle lane `sigma` are

```text
O_sigma={de,-de,df,-df,sigma ef,be,cf}.           (KBPQI-5)
```

Exactly one of the five internal records in `(KBPQI-5)` lies over `eta`.
The missing mate `xi` carries one record `x in O_sigma`; `xi=eta` is the
aligned case, while otherwise `xi in L^c`.  Removing `x`, the other six
records can be partitioned into three pairs, and every pair must satisfy
`(KBPQI-4)`.  Thus each fixed common row and cycle sign has the exhaustive
necessary case ledger

```text
5 eta choices * 7 xi-record choices * 15 perfect matchings = 525 cases.
                                                               (KBPQI-6)
```

If the target record `x=epsilon uv` at `xi` has squared target sum

```text
s_x^2=u^2+v^2+2x,
```

then the sum half of the Vieta equation supplies the square-root-free cut

```text
xi B_1(xi)^2-s_x^2 A_2(xi)^2=0.                   (KBPQI-7)
```

The ledger may be pruned by `(KBPQI-3)`, `(KBPQI-7)`, leading support,
source-label distinctness, and the three resultants before any of the six
remaining outside sum rows is constructed.

This theorem does not claim that a resultant survivor lifts to three
distinct unused source deck pairs, satisfies the six remaining outside sum
rows, is realizable, or deletes either alignment branch.  It does not close
`433-1a -> O0b`, positive coordinate parity, K3, a Prize row, or either
Prize result.

## Falsifier

An actual principal `433-1a -> O0b` packet whose common product map is not
`(KBPQI-2)`, whose missing mate violates `(KBPQI-3)`, whose residual
outside records admit no ledger case in `(KBPQI-6)`, or whose actual deck
pair violates `(KBPQI-4)` or missing-mate sum violates `(KBPQI-7)`.
