# Proof

The heavy-template theorem supplies an antipodal heavy pair and a third heavy
position which is not a quarter point. Translate the pair to `{0,64}`.
Reflection sends the third coordinate `u` to `-u`, while exchanging the two
antipodal endpoints sends it to `u+64`. These symmetries give the unique
representative `t` with `1<=t<=31`; the excluded representative `t=32` is
the quarter template.

For `H={0,64,t}`, the two non-diameter heavy-heavy lengths are `t` and
`64-t`. A light position that forms a chord of length `t` with a heavy
position must lie in

```text
W_t^(1)={128-t,64-t,64+t,2t}.
```

The analogous set for length `64-t` is

```text
W_t^(2)={64-t,64+t,128-t,64+2t}.
```

Their intersection is `C_t={64-t,64+t,128-t}` and their two exceptional
positions are `2t` and `64+2t`. Consequently both singleton heavy-heavy
classes contain a heavy-light chord exactly when a common position is light,
or, in the absence of every common position, both exceptional positions are
light. This is `(W_t)`.

For `1<=t<=31`, the five positions occupy the ranges

```text
64-t in [33,63],       64+t in [65,95],
128-t in [97,127],     2t in [2,62],
64+2t in [66,126].
```

The only possible cross-range coincidences reduce to `3t=64`; this has no
integer solution. Direct endpoint equations also show that none belongs to
`{0,64,t}`. Thus the five positions are distinct and nonheavy.

There are 125 available nonheavy positions. Supports meeting `C_t` number
`binom(125,4)-binom(122,4)`. If `C_t` is avoided and `U_t` is included, the
two remaining positions can be chosen from the other 120 positions, giving
`binom(120,2)`. The cases are disjoint and sum to 915,125.

The heavy antipodal pair contributes 16 to `D_64`. The light-Sidon theorem
forbids a light-light diameter, and the only possible additional heavy-light
diameter joins `t` to `64+t`, contributing four. This proves the diameter
claim. Finally global sign fixes the coefficient at zero; the other two
heavy signs give four choices and the four light signs give sixteen. The
displayed signed-vector count follows. QED.
