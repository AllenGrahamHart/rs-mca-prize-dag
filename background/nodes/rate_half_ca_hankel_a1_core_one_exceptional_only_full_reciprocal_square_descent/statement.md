# `A=1` core-one exceptional-only full reciprocal square descent

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_exceptional_only_full_reciprocal_complement`

Put `n_X=D_0-1`, `N=n_X+r-1`, and reverse the remaining corrected forms at
their fixed degree bounds:

```text
V_vee=Y^(n_X-1)V(t,1/Y),
W_vee=Y^(r-1)W(t,1/Y),
K_vee=Y^n_X K_1(t,1/Y).                             (FRS1)
```

The infinity chain makes the constant term of `j_infW_vee+EK_vee` vanish.
Define

```text
S=(j_infW_vee+EK_vee)/Y.                            (FRS2)
```

Then the unit equation and first complement are exactly reduced to

```text
L W_vee-F S=E Y^N,                                  (FRS3)
V_vee+U W_vee+P_cl S=0.                             (FRS4)
```

Together with `(FRC3)`, the reciprocal corrected square therefore has the
triangular reconstruction ledger

```text
L=(R_X-FU)/P_cl,
G=(YL-j_infF)/E,
K_vee=(YS-j_infW_vee)/E,
V_vee=-UW_vee-P_clS.                               (FRS5)
```

A classifier should allocate only `F,U,W_vee,S`, recover `L,G,K_vee,V_vee`
in that order, and reject on any failed exact divisibility in `(FRS5)` or on
`(FRS3)`. There is one division by `P_cl` and two divisions by `E`. The
original second complement is algebraically redundant once the first
complement and unit equation hold, as in the proved factor descent.

This normal form does not supply the Hankel chain, splitting, or degree-box
reconstruction automatically, and it does not exclude the corrected square.
