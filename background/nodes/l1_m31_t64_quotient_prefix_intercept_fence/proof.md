# Proof

Let `g=(1717986917,1288490189)` in `F_p[i]`, where `i^2=-1`. Exact
arithmetic gives

```text
g^(2^30)=-1,       g^(2^31)=1.
```

For odd `1<=r<=2047`, put

```text
q_r=2^(-2047) Re(g^(r 2^19)).                       (1)
```

The `1024` values are distinct. The replay also checks that the pinned eight
active roots fold four times to `q_1` and four times to `q_3`, which gives
the puncture in `(T64-1)`.

For odd `a` with `1<=a<=31`, define

```text
C_a={q_r:r congruent to a or -a mod 64}.            (2)
```

Every `C_a` has `64` elements. If `T_64` is normalized by
`T_2(X)=2X^2-1`, all members of `C_a` have the same `T_64(2q_r)` value.
Consequently their monic locators have the form

```text
P_a(Y)=2^(-127)(T_64(2Y)-tau_a),                    (3)
```

and `P_a-P_b` is constant. Only `C_1` and `C_3` meet the puncture, so the
other fourteen blocks are intact in `Q'`.

Take the common core to be the union of

```text
C_15,C_17,C_19,C_21,C_23,C_25
```

and the printed `31`-point subset of `C_27` in `verify.py`. It has size
`6*64+31=415`. Adjoin in turn the intact blocks

```text
C_5,C_7,C_9,C_11,C_13,C_29,C_31.                   (4)
```

This gives `A,B_1,...,B_6`, each of size `479`, and proves `(T64-3)`.
If `V_C` is the common-core locator, then replacing `C_5` by `C_a` changes
the full locator by

```text
V_C(P_5-P_a),                                       (5)
```

whose degree is at most `415`. The monic locators have degree `479`, so
their coefficients in degrees `478` through `416` agree. These are the
first `63` nonleading coefficients, proving `(T64-4)`.

Finally the exact binomial calculation in `verify.py` proves
`4H_64<p^32`. For `b=3,4,5`, equation `(T64-4)` makes the left side of
`(T64-5)` at least `3p^32`, `2p^32`, or `p^32`, respectively. Each is
strictly larger than `4H_64`. QED.
