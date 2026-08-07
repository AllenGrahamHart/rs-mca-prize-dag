# Audit - PMA rate-half core triple-excess reduction

## Load-bearing inputs

| input | use | guard |
|---|---|---|
| three full touched petals | supplies the fixed degree-`3ell` divisor of every codeword difference | partial petals require a separate reduction |
| normalized zero core | turns core agreement into `P(x)=0` | subtracting a planted codeword preserves list size |
| exact rate-half source equation | gives `N=4ell+b-2` and `K_0=ell+b-1` | no rounded-rate substitution |
| three distinct contributors | creates two nonzero differences and the `0/1/infinity` witness | a two-element list is already polynomially paid |
| PMA CRT word | retains the source coupling after the core reduction | arbitrary core-list counterexamples are not PMA counterexamples |

## Nonclaims

- Smooth multiplicative cores are not asserted to be order-three MDS.
- The smooth order-100 `J=0` fixture is not asserted to lift to a PMA source
  word.
- Positive three-fiber excess is not automatically a quotient or periodic
  profile; an owner bridge must be proved.
- The result does not cover `M=4,t=2`, larger `M`, or partial petals.
- The result does not promote `petal_mixed_amplification`.

## Mutations

The verifier rejects:

1. the wrong reduced dimension `K_0=ell+b`;
2. omission of the minus sign in the core received word;
3. the shifted baseline `2K_0` in place of `2(K_0-1)`;
4. deletion of the exact `3a` excess;
5. the claim that a smooth subgroup core automatically has no excess;
6. treating the arbitrary core fixture as a source-coupled PMA example.
7. allowing the scope fixture to sit outside the printed `J<=0` tail.
