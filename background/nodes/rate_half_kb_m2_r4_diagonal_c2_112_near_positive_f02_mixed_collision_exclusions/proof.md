# Proof

The q-slice gate defines `q=P_(J_1)`. Its two roots are the coordinates
`c,d` of two distinct source labels, so `c-d` is an ambient named-open
factor. The affine reconstruction also works on the Laurent torus
`bcd!=0`.

For either cell in `(KBF2M-1)`, reconstruct the positive source form over
`QQ(b,c,d)`. At both roots of `q`, divide `U(r,W)^2-WV(r,W)^2` by the forced
`(W-1/c)^2` and compare the remaining quadratic projectively with

```text
(W-1/xi)(W-1/d),
```

where `xi=2` for `A` and `xi=b` for `OB`. This gives the four equations in
the pinned direct registry.

Reduce modulo `p=2130706433`. Sequentially saturate by the ten
reconstruction-generated nonmonomial factors and by `b,c,d`. The resulting
degrevlex bases have sizes

```text
F02-A-RM       6       SHA-256 31bb6f848859550aae71774f255ad7b58163e88d7a484902355809626448021a
F02-OB-RM      7       SHA-256 a0683962d17548fa21fbd1b081ff98120158c40bb4dedf6aa5ee0de9c5cb3c89.
```

Exact normal-form reduction gives `NF(c-d)=0` in both quotients. Thus each
scheme is supported on the forbidden repeated-root divisor. Localizing by
`c-d` returns `[1]` in both cells.

For an independent formulation, multiply the fourteen complete chart
factors to obtain `L`. It has total degree `18`, `132` terms, and SHA-256

```text
2810dcb8ddd37f7c87082bcc957d85dbe117697890ad674eea68546fac5bb51a.
```

A fresh four-variable computation forms `(KBF2M-2)` directly from the
original four equations. Both Groebner bases are `[1]`. By the
Rabinowitsch criterion, neither original variety has a point with `L!=0`
over the algebraic closure. This proves both exclusions. QED.
