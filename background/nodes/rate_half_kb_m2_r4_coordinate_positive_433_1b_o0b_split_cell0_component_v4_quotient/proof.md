# Proof

Write `u=s*i` and `alpha_s=(1+u)/2`. The cell-`0` source normalization under
the B/C involution has `s'=-s`, `x'=-x`, and target coordinate `b'=c`.

On `A_s`, `c=u*b`, so `b'=u*b`. Substitution in the `A_-s` relation gives
`-u` times the `A_s` relation; moreover `r'=(-u)r=1/b'`. On `B_s`,
`c=-u*b`, so `b'=-u*b`. Substitution in the `B_-s` relation gives `u` times
the `B_s` relation and `r'=(-u)r=b'`. Thus component type is preserved and
the source sign flips. The parent involution already proves covariance of
the complete equations and guards.

The secondary actions touch only outside labels and therefore preserve
component and source state. Their proved commutation with B/C remains valid
after adjoining the component label. The executable enumerates both actions
on every tuple

```text
(component, lane, outside sign, source sign, missing record, matching),
```

covering `2*6*2*7*15=2,520` cases. Exact orbit construction gives the stated
profiles and 708 canonical representatives. QED.
