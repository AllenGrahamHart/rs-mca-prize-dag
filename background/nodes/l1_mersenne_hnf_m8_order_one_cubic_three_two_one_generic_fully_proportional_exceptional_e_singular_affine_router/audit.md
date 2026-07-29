# Audit

- The chart explicitly retains `a_2!=0`; roots on `A(z)=0` belong to the
  separately proved exceptional leading-chart exclusion and are not silently
  divided away here.
- The factors removed from `S_0` and `S_1` are fixed official units and the
  inherited `b!=0` saturation.
- Division by `z+27` is justified by `N(-27)=24948`, not by an unsupported
  genericity assertion.
- The forward implication uses `A!=0` to infer `R=0` from (FSA4). The reverse
  implication instead uses the reconstructed `R=0`, `K=0`, and the proved
  unit `z+27` to recover both normalized coefficient equations.
- Squaring introduces no branch: `b` is reconstructed first, and `H=0` is
  exactly the cleared equation `b^2=z` for that value.
- The quartic pair is only a coefficient endpoint. A common factor of degree
  one or two may produce an ambient `F_(p^2)` candidate; higher-degree common
  factors do not, and an `A` factor is outside this chart. None of those
  decisions is made here.
- Both checker sources are unexecuted under the Modal-only policy. The node's
  proof status rests on the displayed polynomial identity and reversible
  algebra.
