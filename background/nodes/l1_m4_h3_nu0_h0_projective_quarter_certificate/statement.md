# L1 m=4, h=3, nu=0, h=0 projective quarter certificate

- **status:** PROVED
- **dependency:** `l1_m4_h3_nu0_h0_projective_branch_exclusion`
- **consumer:** `l1_mixed_petal_amplification`

Assume the surviving `nu=0`, `b!=0`, `deg H=0` endpoint. Put

```text
r=R(0),       A=a/r^2,       B=b/r^3.                 (PQC1)
```

Let `beta_1,beta_2,beta_3` be the roots of `Y^3+aY+b` and put
`lambda_i=beta_i-r`. After relabelling, normalize the three nonzero fiber
products as

```text
(lambda_1,lambda_2,lambda_3)=lambda_1(1,u,v),
u,v in K,       s=1+u+v!=0,       q=u+v+uv.           (PQC2)
```

Then

```text
A=9q/s^2-3,
B=27uv/s^3-A-1,
q(4q-s^2)=3uvs.                                      (PQC3)
```

For `N=p+1`, write

```text
epsilon=u^N,       eta=v^N in mu_4.
```

An exact certificate over all 16 pairs `(epsilon,eta)` proves the complete
necessary table

```text
p=8191,131071,524287:       (A,B)=(6,20);
p=2147483647:               (A,B)=(6,20), or
                             (844833809,2002167159).   (PQC4)
```

For the universal packet, the normalized shifted-value polynomial is

```text
X^3+3X^2+9X+27=(X+3)(X^2+9).                         (PQC5)
```

This is a necessary projective classification. It does not prove that either
packet lifts to a degree-`p` inner polynomial, construct a split pencil,
exclude the constant-eliminant endpoint, treat the cubic endpoint or any
other valuation, or close L1.
