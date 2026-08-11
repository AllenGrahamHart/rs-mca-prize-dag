# Layer-A saturation-count route fence

- **status:** PROVED
- **closure:** exact algebraic counterexample family
- **consumer:** `rate_half_band_crossing_location`

Let `F` be an odd-characteristic field containing a primitive thirty-second
root `zeta`. Put

```text
D = <zeta> = mu_32,       U = <zeta^2> = mu_16,
H = <zeta^4> = mu_8.
```

Choose any thirteen-element set `W` contained in `U`, choose
`eta in F \ H`, and use the nine slopes

```text
Gamma = H union {eta}.
```

For the biform

```text
Q(Z,X)=Z^2-X^4                                             (LAW1)
```

define the incidence set

```text
I={(gamma,x) in Gamma x W : Q(gamma,x)=0}.
```

Then every `x in W` is saturated by exactly two slopes, so

```text
m=2,  rho=7,  T=9,  a=|W|=13=7m-1,
|I|=26,  (m+1)(rho+1)=24.                                 (LAW2)
```

Nevertheless, the `26 x 24` Layer-A evaluation matrix

```text
E_I[(gamma,x),(i,t)] = gamma^i x^t,
0<=i<=2, 0<=t<=7,
```

has

```text
ker E_I={A(X)(Z^2-X^4): deg A<=3},
nullity(E_I)=4,       rank(E_I)=20.                        (LAW3)
```

Thus the positive count excess

```text
(7m-1)m-4m(m+1)=3m^2-5m=2
```

does not imply full Layer-A rank, even when every point of `W` is saturated.

## Scope

This refutes only the bare `(LA-W COUNT)` promotion from row surplus and
pointwise saturation to full rank. It is not a counterexample to the endpoint
Hankel target: the construction does not make `W` the union of two
degree-seven slope supports, does not complete all nine slopes to the required
global blocks, and does not impose the split-biform, support-intersection, or
Hankel-source constraints. Any valid Layer-A theorem must use at least some of
that additional geometry rather than the count alone.
