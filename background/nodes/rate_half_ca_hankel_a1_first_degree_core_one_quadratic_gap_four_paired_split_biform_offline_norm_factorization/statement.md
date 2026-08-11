# `A=1` quadratic paired split-biform off-line norm factorization

- **status:** PROVED
- **closure:** exact row-power divisor and residual-degree ledger
- **consumer:** `rate_half_band_crossing_location`

Let `G(t,X)` be either proved pair-boundary split biform. Let `Sigma_off`
be the off-line supported slopes, and let `M` be the classified fixed-domain
rows on which `G(-,x)` has its full parameter degree and all its roots in
`Sigma_off`. Put

```text
H_off(t)=product_(delta in Sigma_off)(t-delta),
L_M(X)=product_(x in M)(X-x),
N_G(X)=product_(delta in Sigma_off) G(delta,X).       (ONF1)
```

Every specialization `G(delta,X)` in `(ONF1)` is nonzero. If

```text
T_off=|Sigma_off|,       m=deg_t G,       n=deg_X G,
R=|M|,                                                (ONF2)
```

then

```text
N_G(X)=L_M(X)^m S_G(X),
deg S_G<=T_off*n-R*m.                                (ONF3)
```

More exactly, put

```text
q_delta=n-deg_X G(delta,X)>=0.
```

Then

```text
deg S_G=T_off*n-R*m-sum_delta q_delta.               (ONF3a)
```

At most `m` off-line slopes have `q_delta>0`, because they are distinct
roots of the nonzero top `X`-coefficient of `G`, whose parameter degree is
at most `m`. Every selected padded zero-excess fiber has `q_delta=0`.

The factorization is scheme-theoretic: repeated `X`-roots of a specialized
fiber contribute their full multiplicity to `S_G` after the one incidence
copy per row root has been removed.

## Extremal profile

For `d_A in {0,1}`,

```text
T_off=3e,       m=e-2,       n=p-3,
R=3p-3+d_A,     2p=3e-1.                            (ONF4)
```

Consequently

```text
deg S_G<=(3-d_A)e-9+2d_A
 =3e-9       if d_A=0,
 =2e-7       if d_A=1.                              (ONF5)
```

For the official `e=183251937963`, these two caps are

```text
549755813880,       366503875919.                   (ONF6)
```

Let `Z_0` be any guaranteed set of zero-excess fibers from the padded-fiber
theorem, and let

```text
J_delta(X)=product_(y in Z(F_delta)\M)(X-y),
F_delta=A_delta R_delta.                            (ONF7)
```

All roots are counted with multiplicity in the product over `delta`. Then

```text
product_(delta in Z_0) J_delta(X) divides S_G(X),
sum_(delta in Z_0) deg J_delta<=deg S_G.             (ONF8)
```

In particular every padded-heavy factor `R_delta` divides the residual
norm. When `d_A=1`, `M=U_0`, so `J_delta=R_delta` exactly.

The extremal residual is determined completely by local tangent data. For
`x in M`, let `A_x` be the `m=e-2` roots of `G(-,x)` and put

```text
D_x=
 product_(delta in A_x) partial_X G(delta,x)
 product_(delta in Sigma_off outside A_x) G(delta,x). (ONF9)
```

Then

```text
S_G(x)=D_x/L_M'(x)^m.                               (ONF10)
```

Both degree caps in `(ONF5)` are strictly below `R=|M|`. Hence

```text
S_G(X)=sum_(x in M)
 D_x L_M(X)/[(X-x)L_M'(x)^(m+1)].                   (ONF11)
```

This remains valid when an incident fiber is tangent to the row: then the
corresponding derivative and `S_G(x)` are both zero.

The extremal cap has no hidden counting slack. For every off-line slope let
`a_delta` be its triple-union excess and `r_delta` its padded-heavy degree.
When `d_A=0`, let `b_delta` be one if the exceptional row `x_circ` lies in
`S_delta` and zero otherwise; when `d_A=1`, put `b_delta=0`. Then

```text
sum_delta (r_delta+a_delta+b_delta)
 =(3-d_A)e-9+2d_A,                                  (ONF11a)

deg S_G=sum_delta
 (r_delta+a_delta+b_delta-q_delta).                 (ONF11b)
```

Thus the incidence excess and padding merely account for the complete norm
capacity. They cannot overfill it without a further source/Hankel
restriction; fiber degree drops reduce the residual instead.

## First strict profile

For `0<=r_A<=e-6`,

```text
T_off=3e+1,       m=e-1,       n=p-2,
R=2p+r_A,         2p=3e-1,                         (ONF12)
```

and the same factorization `(ONF3)` holds with

```text
deg S_G
 <=[3e^2-4e-7-2r_A(e-1)]/2.                       (ONF13)
```

The selected outside-`M` fiber factors again divide `S_G` as in `(ONF8)`.
The local value identity `(ONF10)` also holds, but the strict residual cap
need not be below `R`, so no strict interpolation claim is made.

## Scope

This theorem does not prove that the residual norm is too small or that it
has an incompatible root. It replaces the full product of all off-line
fibers by one explicit high-power classified-row factor and a bounded
residual. The next useful step must identify `S_G` from the retained
source/Hankel equations, now equivalently the tangent products `(ONF9)`, or
force more outside-`M` fiber degree than its cap.
