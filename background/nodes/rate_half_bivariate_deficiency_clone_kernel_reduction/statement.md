# Deficiency-aware bivariate kernel reduction

- **status:** PROVED
- **closure:** exact polynomial factorization and coefficient extraction
- **consumer:** `rate_half_band_crossing_location`

Retain the strict rate-half endpoint

```text
N=16m,       rho=4m-1,       e=m,       T=4m+1,
sum_(x in D)(m-d_x)=1+O<=m.                            (DCK1)
```

Let `Q_Y(x)` be the nonzero parameter polynomial at coordinate `x`, of
degree at most `m`, and let

```text
A_x={gamma: Q_gamma(x)=0},       d_x=|A_x|,
Delta_x=m-d_x,
A_x(Y)=product_(gamma in A_x)(Y-gamma).                (DCK2)
```

For a joint support `W` with representation pair `(c_0,c_1)`, put

```text
L_x(Y)=c_(0,x)+Y c_(1,x).
```

Every coordinate factors exactly as

```text
Q_Y(x)=A_x(Y) R_x(Y),
0<=deg R_x<=Delta_x,       R_x!=0.                     (DCK3)
```

For `x in W`, write `R_x(Y)=sum_(t=0)^Delta_x r_(x,t)Y^t`. Define the
matrix `M_W` with rows `(i,j)`, `0<=i<=4m`, `0<=j<=m+1`, columns `(x,t)`,
`x in W`, `0<=t<=Delta_x`, and entries

```text
M_W[(i,j),(x,t)]
 =x^i [Y^j](L_x(Y) A_x(Y) Y^t).                       (DCK4)
```

The coefficient vector `r=(r_(x,t))` is a nonzero kernel vector:

```text
M_W r=0.                                               (DCK5)
```

Moreover every coordinate block `(r_(x,0),...,r_(x,Delta_x))` is nonzero.
The exact number of unknowns is

```text
U_W=sum_(x in W)(Delta_x+1)
   =|W|+Delta_W,
Delta_W=sum_(x in W)Delta_x<=1+O<=m.                  (DCK6)
```

Thus `rank(M_W)<=U_W-1`. Full column rank for every admissible endpoint
pattern would exclude the failing pencil. In the clean case `O=0`, there is
one deficiency unit in the entire domain, so

```text
U_W=|W|       if the deficient point is outside W,
U_W=|W|+1     if it is inside W.                       (DCK7)
```

## Scope

At a saturated coordinate `Delta_x=0`, `(DCK3)` has one scalar unknown and
recovers the previously printed product formula. That one-scalar formula is
not valid at a deficient coordinate. The matrix reduction is necessary, not
sufficient: a nonzero kernel vector must also have every coordinate block
nonzero and arise from the remaining pencil data.
