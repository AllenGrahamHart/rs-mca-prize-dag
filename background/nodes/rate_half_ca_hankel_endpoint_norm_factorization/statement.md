# Endpoint norm-defect and complementary-factor identities

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`

Retain the notation and hypothetical failing profile of
`rate_half_ca_hankel_endpoint_saturation_rigidity`:

```text
rho=4m-1,       N=16m,       e=m,       T=4m+1,
O=sum_(gamma in Z)(rho-u_gamma)<=m-1.                 (ENF1)
```

Use homogeneous parameter coordinates `(U:V)`.  For each supported finite
slope `gamma`, let `L_gamma(U,V)` be a linear form vanishing at `gamma`, and
put

```text
H(U,V)=product_(gamma in Z)L_gamma(U,V).
```

Let `Q(U,V;X)` be the primitive generic apolar generator and define its
evaluation-domain norm

```text
R(U,V)=product_(x in D)Q(U,V;x).
```

If `o_gamma=rho-u_gamma` and

```text
J(U,V)=product_(gamma in Z)L_gamma(U,V)^o_gamma,
```

then there is a homogeneous parameter form `S(U,V)` such that

```text
J R=H^rho S,
deg J=O<=m-1,       deg S=1+O<=m.                    (ENF2)
```

Thus the degree-`16m^2` domain norm of `Q` is a `(4m-1)`st power of the
squarefree supported-slope polynomial up to numerator and denominator defects
that each have degree at most `m`.

There is also an exact complementary-factor identity.  Let

```text
D_sat={x in D: Q(U,V;x) has m distinct roots, all in Z},
b=N-|D_sat|.
```

Then

```text
1<=b<=1+O<=m,       |D_sat|=N-b>=15m.                (ENF3)
```

Writing

```text
P_sat(X)=product_(x in D_sat)(X-x),
```

there are biforms `Vbar(U,V;X)` and `W(U,V;X)` satisfying

```text
Q Vbar+P_sat W=H,                                      (ENF4)
deg_(U,V) Vbar=3m+1,       deg_X Vbar<N-b,
deg_(U,V) W<=4m+1,         deg_X W<=rho-1=4m-2.
```

At least

```text
3m+1-O>=2m+2                                            (ENF5)
```

supported slopes are simultaneously:

1. generic-rank slopes of the Hankel pencil;
2. squarefree `D`-split specializations of `Q` with exactly `rho` roots; and
3. parameter-transverse at every one of those roots.

Finally, evaluate `Q` on the grid `D x Z` and let `M` be the resulting
`N x T` matrix.  It is a nonzero-row, nonzero-column word of the product code

```text
RS[D,rho+1] tensor RS[Z,m+1].
```

Its Hamming weight has the two exact MDS-excess expressions

```text
wt(M)=T(N-rho)+O
     =N(T-m)+(1+O).                                    (ENF6)
```

Thus the total excess above the component-code minimum distance is at most
`m-1` when summed by columns and at most `m` when summed by rows.

The theorem does not exclude these identities.  It converts an endpoint
counterexample into a low-defect norm-power problem and, equivalently on at
least fifteen sixteenths of the domain, a bounded-bidegree complementary
factorization against a split polynomial of degree at least `15m`.  It also
poses the same obstruction as a simultaneous near-equality problem for two
MDS component codes; this is not the ordinary global minimum-weight problem
for their product code.
