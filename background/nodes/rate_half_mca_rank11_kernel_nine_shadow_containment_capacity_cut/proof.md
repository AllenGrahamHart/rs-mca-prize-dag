# Proof

Let `R=R_actual>=N_min`. As in the hybrid theorem, each normalized stratum
satisfies

```text
0<=x_d=I_d/R<=min(A_d/N_min,P_d)=u_d.               (1)
```

Summing each per-record shadow theorem over all records gives the two
constraints (LP). Increasing `R` only decreases the ambient terms in (1),
so optimization at `N_min` is uniform in the unknown actual record count.

For a fixed `x_1`, the containment constraint gives an upper bound
`L_C(x_1)` on `sum_(d>=2)x_d`. The first shadow constraint gives a second
bound `L_Q(x_1)`, obtained by filling coranks `2,3,...,9` in increasing
weight order. Thus the exact objective is

```text
x_1+min(L_C(x_1),L_Q(x_1)).                         (2)
```

On each linear piece, the `L_Q` branch has positive total slope because
`w_1<w_d`, while the `L_C` branch has negative total slope because its
corank-one coefficient exceeds 55. Therefore (2) is maximized at an
endpoint, a lower-corank cap breakpoint, or an intersection of the two
linear bounds. The primary verifier enumerates exactly these rational
candidates.

The independent verifier uses a different certificate. Let

```text
v_1=52+3E_0/E_1,
D=v_1 w_2-55w_1,
lambda=(v_1-55)/D,
mu=(w_2-w_1)/D.
```

Then `lambda,mu>=0`,

```text
lambda w_1+mu v_1=1,
lambda w_2+55mu=1,
lambda w_d+55mu>=1        for d>=3.
```

Hence every feasible point satisfies the dual bound

```text
sum_d x_d <= lambda C(m',9)+mu E_0 C(m',9).         (3)
```

At the boundary, only `x_1,x_2` are positive and both resource constraints
are equalities, so (3) is exact. For earlier rows the audit takes the
better of (3) and the sum of the independently reconstructed individual
caps.

The exact scan covers all 15,661 rows through `K'=15670`. At that endpoint,

```text
demand =
4475537178738548139330981218648452557243318003039175890361321166,

floor(N_min Phi) =
4475476933994360491615442893294277488243572130730662704491466634.
```

At `K'=15671`, the corresponding values are

```text
demand =
4476129380405368666077993690300826287914174911305949586829516020,

floor(N_min Phi) =
4476420485966832013665477959285495307950685280544721446642561655.
```

The unrounded rational differences have the same signs.
