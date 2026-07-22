# XR agreement-raise quotient safe-sum fence

- **status:** PROVED
- **closure:** proof
- **consumer:** `xr_tangent_support_mismatch_bridge`
- **dependencies:** `census_bounded_scales`, `xr_target_budget_audit`,
  `xr_mismatch_terminal_tangent_agreement_raise`
- **upstream alignment:** Przemek's finite `quotient paid status cell` and
  `safe-sum validity` (`cap25_cap_v13_raw.tex`)

Let a domain of size `n` be partitioned into fibers of size `c|n`, and put
`N=n/c`. For an exact support size `B`, write

```text
B=m c+s,       0<=s<c.
```

The quotient-remainder support family consists of `m` complete fibers and
`s` residual points outside those fibers. At agreement `B`, the scale is
active only when `c>B-k`. Its standard active threshold-uniform safe sum is

```text
U_act(n,k,A)=sum_c sum_(B=A)^(min(n,k+c-1))
             C(n/c,floor(B/c))
             C(n-c floor(B/c),B-c floor(B/c)).              (QSF1)
```

For any received affine line, each fixed support witnesses at most one
support-wise noncontained bad slope. Consequently `(QSF1)` is a valid union
bound for active quotient-remainder slopes over every support size `B>=A`,
whenever the quotient packet declares coverage by this support family.

This valid bound cannot be inserted into the six clean-row prize ledgers. In
each row one active summand already exceeds `B*`. The three RowC witnesses
are `(c,B)=(8,261),(8,135),(16,79)` at rates `1/4,1/8,1/16`. The prize-row
witness is the initial agreement `B=A` at fiber size
`c=2^34,2^34,2^33`, respectively. Every witness satisfies `B-k<c`, and exact
integer arithmetic gives

```text
C(n/c,floor(B/c)) C(n-c floor(B/c),B mod c)>B*.          (QSF2)
```

Thus the fixed-threshold quotient envelope fitting below `B*` does not by
itself pay the quotient/profile cells encountered during agreement raising.
Even the active support-union repair is already too large. A closing induction
needs a sharper distinct-slope image/coalescing theorem, a threshold-coherent
first-match owner, or the alternate static global-pair-list route.

This theorem does not assert that the actual quotient slope union has size
`U_act`, that `(QSF2)` is attained, or that the mismatch bridge is false.
