# XR uniform Maxwell first-core peeling owner

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_highcore_collision_count`
- **dependencies:** `xr_higher_rank_uniform_split_pencil_reduction`,
  `xr_rank_two_fundamental_circuit_owner`

Fix deterministic total orders on selected blocks, finite-field coordinates,
and normalized projective left relations. Let `F_0` be a one-per-slope
uniform split-pencil family on the `N`-point punctured domain. Define the
following peeling process.

While

```text
h|F_j|>=2N-2a,                                        (PO1)
```

choose the first inclusion-minimal subfamily `G_j subset F_j` satisfying

```text
h|G_j|>=2|union G_j|-2a.                              (PO2)
```

Choose the first normalized nonzero left relation of its split-pencil parity
stack, and let `Lambda_j` be the resulting trade. Trade rank one is impossible.

- If `rank Lambda_j=2`, choose its canonical coefficient basis and let `p_j`
  be the first active non-anchor block. Record its unique fundamental
  four/five-block circuit.
- If `rank Lambda_j>=3`, let `p_j` be the first active block and record the
  higher-rank relation.

In either case set

```text
F_(j+1)=F_j\{p_j}.                                    (PO3)
```

This process is deterministic and terminates. Every removed block has one
first-core pointed certificate

```text
(G_j,Lambda_j,p_j,local circuit when rank two),       (PO4)
```

and no two removed blocks have the same certificate. If `F_terminal` is the
unowned residual, then

```text
|F_terminal|<=B_0:=floor((2N-2a-1)/h).               (PO5)
```

Since `N<=n`, this residual is already below the P-A allocation:

```text
B_0<2N/h<=2n<=8n^3.                                  (PO6)
```

Consequently, for every uniform family,

```text
|F_0|<=B_0+(number of produced pointed certificates). (PO7)
```

Thus first Maxwell-core/trade selection and intratrade pivot ownership are
closed. The theorem does not bound the number of possible classified pointed
certificates, deduplicate them across collision components, classify the
rank-at-least-three records, extend to nonuniform cells, or prove the final
`8n^3` slope payment.
