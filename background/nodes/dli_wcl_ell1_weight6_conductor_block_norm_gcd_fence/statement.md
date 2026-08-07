# WCL `(1,6)` conductor and block-norm gcd fence

- **status:** PROVED
- **closure:** proof
- **dependency:** `dli_wcl_ell1_weight6_parity_adapted_heron_descent`
- **consumer:** `dli_wcl_slot_1_6_emptiness`

Let `zeta=zeta_512`, let `K=Q(zeta)` and `K_0=Q(zeta^2)`, and fix six
distinct residues `x_i in Z/256`. For one global-sign class
`epsilon in {+/-1}^6/{+/-1}`, put

```text
S_epsilon=sum_i epsilon_i zeta^(x_i),
N_epsilon=|Norm_(K/Q)(S_epsilon)|.                    (CB1)
```

Every `S_epsilon` is nonzero. Let `sigma` be the nontrivial element of
`Gal(K/K_0)`, so

```text
sigma(S_epsilon)=S_(epsilon*eta),   eta_i=(-1)^(x_i). (CB2)
```

## Maximal conductor owner

There is a unique largest `d>=0` for which all `x_i` are congruent modulo
`2^d`. Distinctness gives `d<=5`. After absorbing harmless signs caused by
the choice of representatives,

```text
S_epsilon=zeta^c T_epsilon,
T_epsilon=sum_i epsilon'_i zeta_(512/2^d)^(z_i),       (CB3)
```

where the six `z_i` are distinct modulo `256/2^d` and are not all of one
parity. Moreover

```text
N_epsilon
  = |Norm_(Q(zeta_(512/2^d))/Q)(T_epsilon)|^(2^d).    (CB4)
```

Thus an all-one-parity order-512 support is not a primitive Heron stratum:
it belongs exactly to a lower-conductor signed relation. It is routed there,
not discarded.

## Mixed-parity block norms

At the maximal conductor the parity action `(CB2)` is fixed-point-free on
the 32 global-sign classes. Use any parity-adapted perfect pairing from the
parent theorem.

In the even-product sector, each base-field Heron block contains four sign
classes, arranged as two `sigma`-pairs. If `epsilon` and `theta` represent
the two pairs, then its exact absolute base-field norm is

```text
|Norm_(K_0/Q)(H)|=N_epsilon N_theta.                  (CB5)
```

In the odd-product sector, each descended quadratic block contains eight
sign classes, arranged as four `sigma`-pairs. For representatives
`epsilon_1,...,epsilon_4`,

```text
|Norm_(K_0/Q)(Q)|=product_(j=1)^4 N_(epsilon_j).      (CB6)
```

Consequently every parity-adapted block norm containing a fixed sign class
is divisible by that class's entire rational norm `N_epsilon`. The gcd of
any collection of such block norms that all contain the class is therefore
still divisible by `N_epsilon`.

This rules out the proposed cross-pairing block-norm gcd as a compression of
the individual `(1,6)` norm obstruction. It does not exclude a compatible
prime: the remaining route needs arithmetic control of an individual
minimal-conductor signed norm, or a genuinely independent equation.
