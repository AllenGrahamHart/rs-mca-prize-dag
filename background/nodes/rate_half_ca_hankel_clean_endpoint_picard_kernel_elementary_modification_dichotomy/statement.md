# Clean-endpoint Picard-kernel elementary-modification dichotomy

- **status:** PROVED
- **closure:** exact finite-pushforward and bundle classification
- **consumer:** `rate_half_band_crossing_location`

Retain the Picard multiplication kernel bundle `K_Q` and the finite degree-`m`
projection

```text
pi:C -> P^1_X.
```

Then

```text
K_Q=pi_* O_C(N,-T)=pi_* O_C(P_*).                   (KED1)
```

The unmodified structure sheaf has the exact splitting

```text
pi_*O_C=O direct_sum O(-rho)^(m-1).                 (KED2)
```

Moreover `K_Q` is a length-one positive elementary modification at `x_0`:

```text
0 -> O direct_sum O(-rho)^(m-1)
  -> K_Q -> k_(x_0) -> 0.                            (KED3)
```

There are exactly two possible Birkhoff-Grothendieck splittings:

```text
K_Q=O(1) direct_sum O(-rho)^(m-1),                  (KED4a)
```

or

```text
K_Q=O direct_sum O(1-rho)
    direct_sum O(-rho)^(m-2).                        (KED4b)
```

Consequently

```text
h^0(K_Q)=2       in (KED4a),
h^0(K_Q)=1       in (KED4b).                         (KED5)
```

The first branch forces `C` to be isomorphic to `P^1`: the degree-one line
bundle `O_C(P_*)` has a basepoint-free pencil and defines a degree-one map to
`P^1`. The second branch has only the canonical point section.

## Route fence

The proposed injectivity or all-negative-splitting closure is impossible:
`K_Q` always contains a nonnegative summand. The clean endpoint is now the
two-branch problem `(KED4a)/(KED4b)` at this node. The proved child
`rate_half_ca_hankel_clean_endpoint_rational_elementary_branch_exclusion`
excludes `(KED4a)` by adjunction genus. The surviving clean branch is therefore
the unique-section elementary modification `(KED4b)`; it cannot be closed by
bare cohomological injectivity.
