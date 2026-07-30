# Claim contract

## Exact object

In the fixed field

```text
E_63=Q(zeta_128-zeta_128^(-1)),
```

certify that the degree-one prime

```text
p_66=(257,zeta_128-zeta_128^(-1)-66)
```

is nonprincipal.

The monic degree-32 defining polynomial `f_63` is pinned in `statement.md`.
It has 32 distinct roots modulo 257, including 66, as replayed by
`verify.py`.

## Exact certificate

The Jacobi-sum Stickelberger relation constructs `alpha` with

```text
(alpha)=(J_63/bar(J_63))^(2*21121).
```

An explicit residue character at `r=5406977` kills every global unit and
every `21121`st power but does not kill `alpha`. Hence `J_63`, and therefore
`p_66`, is nonprincipal.

## Equivalence to the original test

The ideals `q_1=(257,zeta-9)` and `q_63=(257,zeta-57)` contract to `p_66`
because

```text
9-9^(-1)=57-57^(-1)=66 mod 257.
```

Their product is `p_66 O_(Q(zeta_128))`. The cyclic degree-32 field `E_63`
is ramified over `Q` only at 2 and infinity; the ambiguous class-number
formula gives a trivial ambiguous class group and hence odd class number.
Extension to the quadratic field is therefore injective on ideal classes.
Thus `p_66` is nonprincipal if and only if `q_1q_63` is nonprincipal.

## Dependencies

- `e1_qzeta128_p257_j63_stickelberger_relation`.
- `e1_qzeta128_p257_j63_residue_obstruction`.

No GRH assumption, BNF computation, or predicted class coordinate is used.
