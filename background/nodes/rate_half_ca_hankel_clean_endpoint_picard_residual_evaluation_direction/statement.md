# Clean-endpoint Picard residual-evaluation direction

- **status:** PROVED
- **closure:** exact fibre-socle and Serre-dual identification
- **consumer:** `rate_half_band_crossing_location`

Retain the clean Picard point

```text
P_*=(x_0,S),       Q(z;x_0)=A_0(z)S(z),       deg A_0=m-1,              (PED1)
```

where `S` is linear, with multiplicity retained when `S` also divides
`A_0`. For the degree-`m` projection `pi:C->P^1_X`, the canonical fibre
sequence is

```text
0 -> F -> H^0(O_(C_x0)) -> H^1(P^1_z,O(-m)) -> 0.                    (PED2)
```

The positive elementary-modification direction of

```text
pi_*O_C(P_*) / pi_*O_C = k_(x_0)                                    (PED3)
```

is represented in `H^0(O_(C_x0))` by the fibre-socle class of `A_0`.
Under Serre duality

```text
H^1(O(-m)) = H^0(O(m-2))^*,                                         (PED4)
```

its image is, up to a nonzero scalar, the evaluation functional

```text
ev_S:p |-> p(S).                                                      (PED5)
```

This remains true in the repeated-supported branch: if `S` has fibre
multiplicity `e`, then `A_0` contains `S^(e-1)` and is the local socle
generator.

For `m>1`, `ev_S` is nonzero. Thus the modification direction has nonzero
projection to the canonical negative block

```text
O(-rho) tensor H^0(O(m-2))^*,
```

and cannot raise the trivial `O` summand. Consequently the clean kernel has
the unique-section splitting

```text
K_Q=O direct_sum O(1-rho) direct_sum O(-rho)^(m-2),
h^0(K_Q)=1.                                                          (PED6)
```

## Scope

The theorem supplies an explicit, coordinate-natural direction for the sole
clean Picard branch. It does not yet prove that the rational-normal
evaluation direction `(PED5)` is incompatible with the four-Hankel frame.
