# proof: aqb_average_member_transfer

Let `F` be the finite averaged quotient-box family, and let `L(w)` be the
list contribution of member `w`. Let `T` be the MCA trigger. Assume the
family-average contribution exceeds the trigger:

```text
(1/|F|) sum_{w in F} L(w) > T.
```

If every member satisfied `L(w) <= T`, then averaging those inequalities would
give

```text
(1/|F|) sum_{w in F} L(w) <= T,
```

contradicting the strict average excess. Therefore at least one member
`w_0 in F` has `L(w_0) > T`.

In the AQB application, `T` is the conservative MCA trigger at `sigma*`.
Thus once the averaged quotient-box packet proves average excess over that
trigger, this finite averaging argument produces an individual received word
whose list contribution exceeds the trigger. That member is the unsafe witness
used by `rate_half_band_closure`.
