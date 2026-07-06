# proof: sov_active_core_obstruction_vanishing

An active anchored `h`-core in this branch is counted only when it admits a
partner half: equivalently, there are disjoint `h`-subsets `P,Q` of the row
roots with equal elementary signatures `e_1,...,e_{h-1}` and unequal constant
term. This is the finite minimal `h`-trade object used by the midlarge/SOV
scans.

Let

```text
L_R(X) = prod_{x in P union Q} (X - x)
```

be the monic degree-`2h` locator of its split support. The proved node
`x83_uniform_square_shift_obstruction_gate` says that for any split
`2h`-support the top `h+1` locator coefficients force a unique square-root
candidate, and the support underlies a minimal `h`-trade exactly when the low
obstruction coefficients vanish. The proved node `a_universal_trade_variety`
records the same condition as the row-independent variety `W_h`: trades in
any row are precisely the `mu_n`-points satisfying those obstruction equations.

The proved recursion node `sov_forced_root_recursion_algebra` identifies this
forced square root with the SOV obstruction construction and defines the
obstruction coordinates as

```text
O_i = [X^i](S^2 - L_R),     1 <= i <= h-1.
```

Combining these facts, every active `h`-core in the intended `h>20` band gives
a finite `h`-trade support `R=P union Q`, hence a point of `W_h`, hence all
SOV obstruction coordinates vanish. This proves the bridge from active-core
equations to the forced-root obstruction system. The proof is structural and
does not assert any value-distribution or fiber-size bound.
