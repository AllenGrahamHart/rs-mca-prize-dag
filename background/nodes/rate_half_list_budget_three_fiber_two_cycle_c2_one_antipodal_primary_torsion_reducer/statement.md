# Budget-three fiber-two c=2 one-antipodal primary/torsion reducer

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependencies:**
  `rate_half_list_budget_three_fiber_two_cycle_c2_normalized_gap_span_compiler`,
  `rate_half_list_budget_three_fiber_two_cycle_c2_torsion_field_router`

Retain the maximal official normalized `c=2` chamber and suppose its four
denominator roots contain an antipodal pair. Common subgroup scaling puts

```text
Omega={1,-1,c,d},       c,d in mu_N,
N=2^40,                 H=2^37+1,       M=2H-2=N/4.       (OAR1)
```

Set

```text
S=c+d,       P=cd,       X=S^2,
E(z)=(1-z^2)(1-Sz+Pz^2),
A(z)=E(z)^(-1/4)=sum_(n>=0)a_nz^n.                       (OAR2)
```

Generate the coefficients by the existing four-term recurrence. There are
unique polynomials `F_H,G_H in F[X,P]` such that

```text
a_M=F_H(X,P),       a_(M+1)=S G_H(X,P).                  (OAR3)
```

The complementary pair is antipodal exactly when `X=0`. On the
exactly-one-antipodal stratum `X!=0`, the primary double gap is therefore
exactly

```text
F_H(X,P)=G_H(X,P)=0.                                     (OAR4)
```

Root torsion also has a sign-free two-scalar circuit. Put

```text
U_0=X-2P,       V_0=P^2,
U_(j+1)=U_j^2-2V_j,       V_(j+1)=V_j^2,       0<=j<39. (OAR5)
```

Then

```text
c,d in mu_N       iff       U_39=2,       V_39=1.        (OAR6)
```

Consequently, modulo the sign `S -> -S`, exactly-one-antipodal primary
packets are represented without root labels by

```text
F_H=G_H=0,       U_39=2,       V_39=1,
X P (X-4P)((1+P)^2-X)!=0,       X is a square in F_q.    (OAR7)
```

Conversely every `(X,P)` satisfying `(OAR7)` reconstructs the two signs for
`S`, and the roots of `Y^2-SY+P` lie in `mu_N`; the two signs exchange
`{c,d}` with `{-c,-d}`. Thus `(OAR7)` is an exact circuit for this stratum.

As a first rejection gate, every packet must make

```text
R_H(P)=Res_X(F_H(X,P),G_H(X,P))
```

vanish at an `N`-torsion value of `P`. A nontrivial resultant intersection
is not sufficient: the joint `U_39=2` trace condition must still be imposed.

This theorem does not prove that `(OAR7)` is empty, use the secondary gap, or
prove C2-PAR. It splits C2-PAR into an exact one-antipodal cyclotomic
exclusion and the genuinely antipodal-free stratum.
