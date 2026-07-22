# Audit

## Verdict

The theorem is a direct graph-counting consequence of two proved nodes. The
nodal graph is restricted to the same generic vertices and the same
signed-disjoint distance-six edge set counted by `D_6`; no edge type changes
during the subtraction.

## Boundary checks

- The antipodal-free threshold is sharp for this argument: at `m=14`, the
  available lower bound has `F_0(14)-2nu_0(14)=-6`.
- The antipodal threshold is sharp for this argument: at `m=15`, the
  available lower bound has `F_A(15)-2nu_A(15)=-8`.
- At `m=16` in the antipodal class, equality occurs:
  `F_A(16)=44=2nu_A(16)`.
- The quotient weight is preserved because the charge is targetwise. No
  averaging or class conversion is used.

## Limitations

The result does not show that smooth edges are sparse. It converts the nodal
high tail into an additional copy of the smooth high tail and leaves the
off-antipodal `25<=P<=32` and antipodal `25<=P<=34` bands untouched. Those
terms can still correlate adversarially with `R(t)`. Survival of the exact
integer checks is not evidence for a missing smooth elliptic-curve estimate.
