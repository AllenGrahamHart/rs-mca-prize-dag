# Proof

The clean fiber `f` is squarefree, `F_t` is nonzero at every root of `f`,
and the complementary factor `U` has no common root with `f`. Therefore
`F_Y`, `F_t`, and `U` are units modulo `f`. Equations `(QRC1)--(QRC2)` are
the implicit first- and second-derivative formulas from the two jet theorems.

The polynomial `f` divides the reciprocal domain locator `R_X`, which in
turn divides `Y^M-1`. Hence `Y^M=1` in `K_gamma`. Since
`N_sq=M+r-3`, this proves `(QRC4)`. Reducing the first-jet identity

```text
F_t U W_vee=-p_1e_0Y^N_sq
```

modulo `f` now gives `(QRC3)`. Its canonical representative has degree below
`r`; the actual specialization `W_vee(gamma,Y)` has degree at most `r-1` and
has the same class, proving the first equality in `(QRC7)`.

The domain locator is squarefree, so `R_X'` is a unit modulo `f`. The
transversality theorem says `v` is nonzero at every root, making it a unit as
well. Reduce the second-jet identity modulo `f` and use `(QRC4)`. Division by
`2R_X'v` gives `(QRC5)`. The total derivative decomposes as

```text
dot w=W_vee,t+W_vee,Yv.
```

Because the canonical representative `w` is the actual degree-`<r` fiber
polynomial, its formal derivative is `W_vee,Y(gamma,Y)`. Thus `(QRC6)` is the
class of `W_vee,t(gamma,Y)`. That derivative also has degree at most `r-1`,
so its canonical representative is the actual polynomial, proving the
second equality in `(QRC7)`. QED.
