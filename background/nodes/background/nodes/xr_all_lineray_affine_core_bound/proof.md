# Proof

For `(gamma,e) in P`, write `S_e=supp(e)` and `T_e=D\S_e`. First observe

```text
H(A_P) subset <y_1>,                                      (1)
```

because the syndrome difference of two errors is a scalar multiple of
`y_1`.

We claim that restriction `A_P->F^(T_e)` is injective for every `e`. Let
`z in A_P` vanish on `T_e`. Then `z` is supported inside `S_e`, so
`wt(z)<=wt(e)<=t`. By `(1)`, write `Hz=beta y_1`.

If `beta=0`, then `z` is a kernel word of weight at most `t`; the distance
hypothesis forces `z=0`. If `beta!=0`, put `q=beta^(-1)z`. Both `q` and
`e-gamma q` are supported in `S_e`, while

```text
Hq=y_1,       H(e-gamma q)=y_0.
```

This contradicts transversality. Thus restriction is injective.

Fix a basis of `A_P` and let `B` be its coordinate matrix. Injectivity gives
an `s`-set `I_e subset T_e` on which `B` has full column rank. Express every
error uniquely as `e=e_*+Bx_e`. Since `e` vanishes on `I_e`, the invertible
system

```text
B|_(I_e) x_e = -e_*|_(I_e)                              (2)
```

recovers `e` from its zero minor `I_e`.

If a distinct error `f` also vanished on `I_e`, equation `(2)` would give
`f=e`; applying `H` and using `y_1!=0` would then force the slopes equal, so
the pairs would not be distinct. Consequently

```text
I_e intersect S_e = empty,
I_e intersect S_f != empty       for every distinct pair e,f.       (3)
```

The nonuniform Bollobas set-pair inequality applied to `(I_e,S_e)` gives

```text
sum_e 1/C(|I_e|+|S_e|,|I_e|) <=1.
```

Since `|I_e|=s`, this is the weighted claim in `(AC)`. Every denominator is
at most `C(s+w,s)`, proving `|P|<=C(s+w,s)`. For a maximum-weight error,
injectivity into its zero coordinates gives `s<=|D|-w`, and hence
`C(s+w,s)<=C(|D|,s)`.

For the RS application, map a retained pair `(gamma,c)` to

```text
e=u+gamma v-c.
```

This is injective when the syndrome direction is nonzero. Agreement at least
`A` gives `wt(e)<=n-A=r`, while RS distance `n-k+1` is greater than `r`.
If both endpoint syndromes had lifts on `supp(e)`, the received pair would
jointly agree with a codeword pair on the complementary `A`-set; this is the
common-support/tangent branch removed before the generic residual. Therefore
the theorem applies to every retained stratum. Projection from LineRay pairs
to slopes can only decrease cardinality.

More sharply, choose exactly one retained pair above every live slope and
apply the theorem to this selected family. Every selected error still has
weight at most `t`, so a selector of affine rank `sigma` gives

```text
#slopes <= C(sigma+t,sigma).
```

Minimizing over the finite set of selectors proves `(SEL)`. In particular,
the existence of one low-rank selector is enough; no rank bound on the full
LineRay pair family is required.

Finally, for either rank parameter `d<=3`, monotonicity gives

```text
C(r+d,d)<=C(n+3,3)<=8n^3
```

on the candidate lengths `n>=1024`. Direct exact arithmetic at the six pinned
rows shows that `d=4` already exceeds the allocation in every case; the
verifier records both sides. This proves precisely the stated low-rank
branches.

## Provenance

The set-pair proof was independently reconstructed from the theorem statement
in upstream PR `przchojecki/rs-mca#737`, whose Lean file is explicitly only an
unproved statement target. This packet relies on the written proof above and
its independent finite replay, not on the PR's status label. The local theorem
uses only the one-level all-pair bound; no upstream atlas or host-extraction
claim is imported.
