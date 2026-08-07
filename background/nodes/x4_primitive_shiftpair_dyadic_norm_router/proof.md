# Proof

Write the two monic locators as products over their roots.  Equality of the
first `t` sub-leading coefficients is equality of the first `t` elementary
symmetric functions.  Newton's identities, used in the direction

```text
s_m-e_1 s_(m-1)+...+(-1)^(m-1)e_(m-1)s_1+(-1)^m m e_m=0,
```

therefore give equality of the two power sums for every `1<=m<=t`.  This
direction uses no division.  The common factor `alpha^m` is nonzero, so

```text
sum_(a=0)^(N-1) c_a zeta^(am)=0 in F.                 (1)
```

Fix an allowed `j`, put `n=n_j`, `h=h_j`, and
`xi=zeta^(2^j)`, a primitive `n`-th root.  For odd `u` with `2^j u<=t`,
grouping (1) first modulo `n` and then pairing residues `r,r+h` gives

```text
0=sum_(r=0)^(n-1) A_(j,r) xi^(ru)
 =sum_(r=0)^(h-1)(A_(j,r)-A_(j,r+h))xi^(ru)
 =beta_j(xi^u),                                       (2)
```

because `xi^(hu)=-1`.  This proves the vanishing assertion.

The odd residue classes modulo `n` index the roots of the cyclotomic
polynomial `Phi_n=X^h+1`.  Frobenius acts on them by multiplication by `p`.
Every orbit has length `f=ord_n(p)`; each orbit is one irreducible factor of
`Phi_n` over `F_p`, and hence one prime ideal of residue degree `f` above
`p` in `Z[zeta_n]`.  Equation (2) says that every Frobenius orbit meeting
`U_j` supplies a distinct prime ideal dividing `(beta_j)`.  If `beta_j` is
nonzero, multiplicativity of ideal norms therefore gives

```text
p^(f o_j) | |Norm_(Q(zeta_n)/Q)(beta_j)|.             (3)
```

This is also why counting tested powers separately would be wrong when the
root of unity generates a nontrivial extension of the base field.  The
members of `U_j` reduce to distinct odd residues: indeed
`u<=t/2^j<=e/2^j<=n/2`.  Each Frobenius orbit contains exactly `f` residues,
so `f o_j>=|U_j|=ceil(floor(t/2^j)/2)`.  This gives the stated field-uniform
weaker divisor `p^M_j` as well.

For the energy estimate, each `b_(j,r)` is a signed sum over a block of
`2^(j+1)` entries of `c`.  These blocks partition the `N` coordinates.
Cauchy-Schwarz and `sum_a c_a^2=2e` give

```text
E_j<=2^(j+1) sum_a c_a^2=2^(j+2)e.                   (4)
```

The proved DLI energy ceiling for an arbitrary nonzero integer coefficient
vector in `Z[zeta_n]` gives

```text
1<=|Norm(beta_j)|<=E_j^(h/2)=E_j^(n/4).              (5)
```

Combining (3)--(5), and using `n=N/2^j`, proves the norm gate.

It remains to identify the zero branch at the root level.  At `j=0`, the
powers `1,zeta,...,zeta^(N/2-1)` are a rational basis, so

```text
beta_0=0  iff  c_a=c_(a+N/2) for every a.
```

Since the supports are disjoint and `c_a` is `1`, `-1`, or `0`, this holds
exactly when membership in each of `P` and `Q` is invariant under the
antipodal involution.  Their locators are then products of factors
`X^2-x^2`, so both have common coefficient scale at least two.  Conversely,
unions of antipodal pairs plainly give `beta_0=0`.  The maximal
coefficient-scale quotient sieve removes this branch; consequently a
coefficient-primitive pair has `beta_0!=0` and is norm-gated. QED.
