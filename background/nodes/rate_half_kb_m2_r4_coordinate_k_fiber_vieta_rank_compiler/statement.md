# KoalaBear m2 r4 coordinate K-fiber Vieta-rank compiler

- **status:** PROVED
- **scope:** every actual coordinate-order-two component in the residual
  `(m,r,delta)=(2,4,2)` row
- **dependency:**
  `rate_half_kb_m2_r4_coordinate_colored_quotient_resultant_compiler`
- **consumer:** `rate_half_band_closure`

Work in the proved coordinates

```text
tau(T)=-T,       b(X)=-X,       W=X^2.
```
Write a quotient point as `kappa=[u:v]`, and choose a source lift
`x_kappa=[r:s]` with `[r^2:s^2]=[u:v]`. The endpoint coordinate may
be chosen so that all twelve labels are finite and nonzero because `tau`
acts fixed-point-freely on them. If the component star at `x_kappa` is
the unordered `J`-edge `{a_kappa,b_kappa}`, define

```text
p_kappa=a_kappa b_kappa,
q_kappa=r*s*(a_kappa+b_kappa).                    (KBKV-1)
```
Star transport sends `(x,a,b)` to `(-x,-a,-b)`, so `(p_kappa,q_kappa)`
is independent of the chosen point above `kappa` and of the edge order.
Its homogeneous weight matches the equations below. This definition also
covers either ramified quotient value, where `r*s=q_kappa=0`.

For the positive coordinate form, the five edge records are realized
exactly when its coefficient vector lies in the kernel of the `10 x 8`
homogeneous system

```text
A_0(kappa)-p_kappa A_2(kappa)=0,
u*v B_1(kappa)+q_kappa A_2(kappa)=0,              (KBKV-2+)
```

and `A_2(kappa)!=0` for all five labels. For the negative form, the exact
`10 x 7` system is

```text
B_0(kappa)-p_kappa B_2(kappa)=0,
A_1(kappa)+q_kappa B_2(kappa)=0,                  (KBKV-2-)
```

with `r*s*B_2(kappa)!=0` for all five labels. In particular, the negative
branch cannot place a common-`K` label at a ramified quotient value. Thus
an actual positive packet has matrix rank at most seven and an actual
negative packet has rank at most six, with the stated leading-support
condition.

Two smaller determinant gates follow immediately. In the positive branch,

```text
det [q_kappa*v^2, q_kappa*u*v, q_kappa*u^2,
     u*v^2, u^2*v]_(kappa=[u:v] in K)=0.          (KBKV-3+)
```

In the negative branch,

```text
rank [-p_kappa*v, -p_kappa*u, v, u] <= 3,
det [q_kappa*v, q_kappa*u, v^2, u*v,
     u^2]_(kappa=[u:v] in K)=0.                  (KBKV-3-)
```

These gates must be imposed together with the colored quotient-resultant
system, exact bidegree, nonzero odd part, irreducibility, and outer-factor
divisibility. They do not prove that either parity branch is empty and do
not delete an orientation, type, owner, payment, row, or Prize result.

## Falsifier

An actual coordinate component whose deck-paired `K`-edge record is not
well defined by `(KBKV-1)`, does not satisfy its exact Vieta system, or
violates one of the rank consequences `(KBKV-3+)--(KBKV-3-)`.
