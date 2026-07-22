# XR threshold quotient-image lcm normal form

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_tangent_support_mismatch_bridge`
- **dependency:** `xr_agreement_raise_quotient_safe_sum_fence`
- **upstream alignment:** Przemek's `fixed-support parameter gcd`, `exact
  finite-parameter quotient image ledger`, and affine-line lcm corollary

Let `C subseteq F^D` be a linear code and let `u+Zv` be a received affine
line. For a support `S subseteq D`, form the restriction quotient

```text
Q_S=F^S/C|_S
```

and let `a_S,b_S` be the classes of `u|_S,v|_S`. In any basis of `Q_S`, let
`L_(S,i)(Z)=a_(S,i)+Z b_(S,i)`. Define

```text
g_S(Z)=1                                      if a_S=b_S=0,
g_S(Z)=monic gcd of the nonzero L_(S,i)(Z)    otherwise.       (QIL1)
```

Then `g_S` is basis-independent, has degree at most one, and its roots in
`F` are exactly the finite slopes explained on `S` for which `(u,v)` is not
simultaneously explained on `S`.

For any finite support family `S`, put

```text
R_S(Z)=rad lcm_(S in S) g_S(Z).                         (QIL2)
```

The exact distinct support-wise noncontained slope image of `S` is the root
set of `R_S`; because every nonconstant factor is an `F`-linear factor,

```text
# distinct bad slopes witnessed by S = deg R_S.                (QIL3)
```

Taking `S` to be the quotient-remainder supports over every declared scale
and every agreement reached by the XR carry gives one exact threshold-union
quotient-image polynomial. This removes duplicate supports, agreement sizes,
and scales at the level of slope identity.

The theorem does not bound `deg R_S`, give a compressed official-row
construction of `R_S`, prove quotient/profile coverage, aggregate generic
charts, or close XR.
