# Claim contract

- **Claim:** the displayed rate-dependent lower and upper near-tail layers
  contain fewer than `2^122` `t_XR`-null sets in total.
- **Scope:** all four prize rates, `N=2^41`, and every official field with
  `128<=log2(q)<256`.
- **Counted object:** all `t_XR`-null sets in those layers, before structural
  strips; this is stronger than an extras-only bound there.
- **Inputs:** the banked interpolation lemma, complement duality, and the
  exact corridor definition.
- **Nonclaim:** no bound on the middle layers beginning at
  `t_XR+w_rho+1`.
