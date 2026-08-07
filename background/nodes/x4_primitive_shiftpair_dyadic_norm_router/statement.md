# Primitive shift-pair dyadic norm router

- **status:** PROVED
- **closure:** proof

Let `D=alpha mu_N` be a multiplicative-coset evaluation domain in a finite
field `F` of characteristic `p`, where `N=2^s>=4`.  Write
`mu_N=<zeta>`.  Let `P,Q` be disjoint `e`-subsets of `Z/NZ`, and assume, for
`1<=t<=e`, that the monic locators of

```text
alpha{zeta^a:a in P}  and  alpha{zeta^a:a in Q}
```

have the same first `t>=1` sub-leading coefficients.  Put

```text
c_a=1_P(a)-1_Q(a).
```

For every `j` such that `2^j<=t` and `n_j=N/2^j>=4`, put
`zeta_(n_j)=zeta^(2^j)` and define

```text
h_j=n_j/2,
A_(j,r)=sum_(a=r mod n_j) c_a,
b_(j,r)=A_(j,r)-A_(j,r+h_j)        (0<=r<h_j),
beta_j=sum_(r=0)^(h_j-1) b_(j,r) zeta_(n_j)^r in Z[zeta_(n_j)],
U_j={u odd: 1<=u and 2^j u<=t}.
```

Let `f_j=ord_(n_j)(p)`, and let `o_j` be the number of orbits under
`u -> pu (mod n_j)` on odd residue classes that meet the reduction of
`U_j`.  Put

```text
M_j=|U_j|=ceil(floor(t/2^j)/2).
```

Then:

1. `beta_j(zeta_(n_j)^u)=0` after reduction to `F` for every `u in U_j`.
2. If `beta_j!=0` as an algebraic integer and
   `E_j=sum_r b_(j,r)^2`, then

   ```text
   p^(f_j o_j) | |Norm(beta_j)|,
   f_j o_j>=M_j,
   p^M_j <= p^(f_j o_j) <= |Norm(beta_j)| <= E_j^(n_j/4)
                                      <= (2^(j+2)e)^(N/2^(j+2)).
   ```

3. At `j=0`, `beta_0=0` exactly when both `P` and `Q` are unions of
   antipodal pairs.  Hence every coefficient-primitive shift pair has
   `beta_0!=0` and obeys the displayed norm gate.

Thus every coefficient-primitive record in the residual X4/SP2 incidence
has a canonical, exact DLI norm-gate certificate.  The orbit count, rather
than the raw number of tested odd powers, is mandatory over generated
extension fields.

This theorem does not count the records satisfying the gate, compile the
first-owner map, pay the minimal stratum, or close X4, LIST, or MCA.
