# Proof

The node `e1_qzeta128_p257_j65_harbater_nonprincipality` proves

```text
J_65=q_1q_65
```

nonprincipal unconditionally.

For the other product, put

```text
beta=zeta_128-zeta_128^(-1),
E_63=Q(beta).
```

The automorphism `sigma_63` sends

```text
zeta_128 -> zeta_128^63 = -zeta_128^(-1),
```

and fixes `beta`. Since it is an involution, `E_63` is its degree-32 fixed
field. Exact reduction modulo 257 gives

```text
9-9^(-1)=66,
57-57^(-1)=66.
```

Consequently `q_1` and `q_63` lie above the same prime

```text
p_66=(257,beta-66)
```

and

```text
p_66 O_(Q(zeta_128))=q_1q_63=J_63.                 (1)
```

The quotient `(Z/128Z)^x/<63>` is cyclic of order 32, so `E_63/Q` is cyclic.
Only the finite prime 2 and the real place ramify, with ramification indices
32 and 2. The ambiguous class-number formula gives

```text
|Cl(E_63)^Gal(E_63/Q)|
  = h(Q) * (32*2)/32 / [ {+/-1} : {+/-1} intersect N(E_63^x) ]
  = 1 * 2/2
  = 1.                                                   (2)
```

The unit index is two because every norm from the totally imaginary field
`E_63` is positive at the real place. If `Cl(E_63)` had nontrivial
2-primary part, the cyclic 2-group `Gal(E_63/Q)` acting on its elements would
have a nonidentity fixed point: every finite 2-group action has a number of
fixed points congruent to the set size modulo two. This contradicts `(2)`.
Thus `h(E_63)` is odd.

If `(1)` were principal, ideal norm through the quadratic extension would
make `p_66^2` principal. Odd class number then makes `p_66` itself
principal.

The proved fixed-field certificate says exactly that `p_66` is
nonprincipal. Therefore `J_63` is nonprincipal, while the Harbater node
already proves `J_65` nonprincipal. This proves the conjunction. QED.
