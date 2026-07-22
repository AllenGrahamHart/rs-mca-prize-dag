# Distance-three saturated cyclic-design residue route fence

- **status:** PROVED
- **closure:** explicit finite-field construction
- **consumer:** `rate_half_band_closure`
- **dependencies:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_quadratic_locator_rank_gate`,
  `rate_half_ca_hankel_a1_core_one_exceptional_only_distance_three_complement_residue_rank_three_gate`

Over `F_151`, let `zeta=38` have order `15` and put

```text
e=5,       Z=mu_15={zeta^j:0<=j<15},       P(z)=z^15-1.
```

In `Z/15Z`, define

```text
S={0,1,5,6,10},       T={0,1,5,6,11},
U={0,3,6,9,12}.                                      (SCRF1)
```

Take all `15` translates of `S`, all `15` translates of `T`, and the three
distinct translates of `U`. For each resulting block `E`, put

```text
G_E(z)=product_(j in E)(z-zeta^j),
H_E(z)=P(z)/G_E(z).                                  (SCRF2)
```

The `33=6e+3` blocks are distinct and form an exact simple design:

```text
|E|=e,       every point of Z occurs in 11=2e+1 blocks. (SCRF3)
```

Their locator and complement ranks are exactly

```text
rank (coeff(G_E) coeff(G_E)^T)_E =16=3e+1,          (SCRF4)
dim span{H_E:E}=9=e+4.                              (SCRF5)
```

Thus exact biregularity, saturated quadratic locator rank, and the full
complement coefficient-span bound can all hold simultaneously. Those three
conditions alone do not exclude a distance-three packet.

The calibrated residue condition does reject this construction. For every
degree-five polynomial `I` with `I(0)!=0`,

```text
dim span{H_E mod I:E}>=4.                            (SCRF6)
```

In particular no internal locator with five nonzero roots can make the
residue rank at most three. The rank-three modulo-`I` gate, not merely its
unreduced `e+4` shadow, is therefore load-bearing in the remaining saturated
generic branch.
