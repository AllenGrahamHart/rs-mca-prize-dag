# `A=1` core-one active-partition incidence reconstruction

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_active_core_two_sided_partition`

Retain either live active system and the notation of the two-sided partition
theorem. Let

```text
X_sat={x:P_X(x)=0},       Z_cl={gamma:P_cl(gamma)=0},
n_X=D_0-c,                n_Z=T-D_*.
```

For `gamma in Z_cl`, let `R_gamma` be the `r` roots of `Q(gamma;X)`
and put

```text
F_gamma(X)=product_(y in R_gamma)(X-y).
```

For `x in X_sat`, let `S_x` be the `e_*` supported roots of
`Q(t;x)` and put

```text
G_x(t)=product_(beta in S_x)(t-beta).
```

All supported slopes are finite in the official convention. Define the
bipartite nonincidence graph `H` on `X_sat` and `Z_cl` by

```text
x--gamma  iff  x notin R_gamma  iff  gamma notin S_x. (AIR1)
```

Then `H` is connected. More precisely,

```text
deg_H(x)>=n_Z-e_*,       deg_H(gamma)>=n_X-r,
n_Z>2e_*,                n_X>2r.                       (AIR2)
```

On every edge define the nonzero label

```text
theta_(x,gamma)=F_gamma(x)/G_x(gamma).                 (AIR3)
```

There are nonzero potentials `a_gamma,b_x`, unique up to one common scalar,
such that

```text
theta_(x,gamma)=b_x/a_gamma.                           (AIR4)
```

Equivalently, every alternating cycle

```text
x_1-gamma_1-x_2-gamma_2-...-x_k-gamma_k-x_1
```

satisfies

```text
product_(i=1)^k theta_(x_i,gamma_i)
                    /theta_(x_(i+1),gamma_i)=1,        (AIR5)
```

with `x_(k+1)=x_1`.

This gives an exact reconstruction criterion from proposed partition data.
Assume the incidence consistency in `(AIR1)` and the cycle identities
`(AIR5)`, recover potentials by `(AIR4)`, and write

```text
F_gamma(X)=sum_(j=0)^r f_(j,gamma)X^j.
```

A biform of bidegree `(r,e_*)` having exactly the proposed clean and
saturated fibers exists if and only if, for every `0<=j<=r`,

```text
(a_gamma f_(j,gamma))_(gamma in Z_cl)
       lies in RS[Z_cl,e_*+1].                         (AIR6)
```

When `(AIR6)` holds, coefficientwise interpolation reconstructs the biform
uniquely up to the common scalar, and its saturated fibers are automatically

```text
Q(t;x)=b_xG_x(t)       for every x in X_sat.           (AIR7)
```

The same data gives an exact rank certificate. Let `C_cl` have rows equal to
the coefficient vectors of `a_gamma F_gamma`, let `C_sat` have rows equal to
the coefficient vectors of `b_xG_x`, and let

```text
W_sat,cl=(Q(gamma;x))_(x in X_sat,gamma in Z_cl).
```

Then

```text
rank C_cl=rank C_sat=rank W_sat,cl=sr(Q),               (AIR8)
```

where `sr(Q)` is the separation rank of the dominant biform. Consequently

```text
rank W_sat,cl>=ceil((e+1)/(b+1))>=5,                    (AIR9)
```

and when `b=0` all three ranks are exactly `e+1`.

Thus an active partition packet can be tested by incidence consistency,
one connected-graph potential pass, and `r+1` Reed--Solomon membership
tests, with `(AIR8)--(AIR9)` as an immediate rank gate. This theorem does not
impose the Hankel chain, the adjugate identity, or irreducibility, and does
not exclude either live system.
