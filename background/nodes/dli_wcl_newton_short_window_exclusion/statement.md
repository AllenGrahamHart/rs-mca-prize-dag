# DLI Newton short-window exclusion

- **status:** PROVED
- **closure:** proof

## Statement

Let `F` be a field of characteristic zero or characteristic greater than
`w`. Let `omega in F` have exact order `2N`, and let

```text
P(X) = sum_(i=1)^w s_i X^e_i
```

be a reduced signed polynomial with distinct `e_i in {0,...,N-1}` and
`s_i in {+1,-1}`. If

```text
P(omega^(2j-1)) = 0  for j=1,...,ell
```

and `w<=2ell`, then no such polynomial exists.

Consequently, on the actual DLI production tower:

```text
level ell       WCL weight window       excluded here       residual
1               2,...,6                 2                   3,...,6
2               3,...,7                 3,4                 5,6,7
4               5,...,9                 5,6,7,8             9
ell>=8          ell+1,...,ell+5          every weight        empty
```

Combining the first row with the existing exact ambient exclusions at weights
3 and 4 leaves only six WCL weight slots across the entire tower:

```text
(ell,w) in {(1,5),(1,6),(2,5),(2,6),(2,7),(4,9)}.
```

## Nonclaims

This does not exclude any of those six residual slots or prove WCL-ZONE.
The cutoff `w<=2ell` is load-bearing. In unrestricted finite fields there are
non-antipodal examples at `w=2ell+1`, including the nonzero quadratic-residue
subgroups of `F_7`, `F_11`, and `F_19` for `ell=1,2,4` respectively. Those
examples do not have the official root-order or field-size parameters, but
they show that the Newton identities alone cannot cross the printed cutoff.

## Falsifier

A reduced signed relation of weight at most `2ell` satisfying the first
`ell` odd-power equations in characteristic zero or characteristic greater
than its weight.

## Display correction (2026-07-22, wcl seam audit)

Window displays of `L+5` / six-slot residuals in this note are PRE-EXTENSION
bookkeeping. The window of record is `L+1..L+7` (C1'-r3, L = dimension ell)
and the residual of record is the TEN slot cells; see
`critical/nodes/dli_wcl_zone_coverage/official_terminal_attack.md` (ten-slot
section) and `verify_slot_decomposition.py`. The theorem content of this
node is window-independent and unchanged.
