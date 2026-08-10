# Audit

The parity-check weights are `1/L_C'(x)`, not the FPC5 touched-petal
barycentric weights. They are connected by the explicit rescaling
`e_x=w_x/v_x`; all weights are nonzero on the distinct-point core.

The syndrome length is `D=d+c`, because `d` initial moments recover the
amplitudes and exactly `c` recurrence rows extend them. No infinite moment
representation is used.

When `D>=N`, only a per-chart singleton is proved. A first-background-set
partition can still have many charts, so this does not by itself pay the
large-source target.

When `D<N`, the theorem exposes an ordinary GRS exact-shell problem. Calling
that identification a list-size bound would be circular; the background and
chronology filters may only reduce the shell and remain explicit.
