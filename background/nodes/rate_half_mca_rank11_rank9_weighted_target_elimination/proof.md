# Proof

Put

```text
n'=1048576+K',       m'=67472+K',       D=n'-m'=981104.
```

The fixed-chart weighted concentrator and the rank-nine component cap are
in the same `(record,T)` unit:

```text
L(K')=(495405467/10^9) N_min
      *C(m',9)C(m'-9,2)/C(n',9),
W_B>=ceil(L(K')),
W_B<=U(K')=981105*(m'-10)n',
N_min=274980728111260126.                           (1)
```

Exact integer arithmetic at the adjacent rows gives

```text
K'=20617: ceil(L)=92386821615379573
           U       =92394042904582935,

K'=20618: ceil(L)=92397581841774591
           U       =92395178310909600.              (2)
```

At `K'=20618`, direct cross-multiplication before rounding has positive
numerator

```text
12094297975958500187163143893546997482199568008609448643893803356370400,
```

so `L(20618)>U(20618)`. The corresponding cross-product at `20617` is
negative. Thus `20618` is the honest first crossing of this method.

To propagate the strict inequality, cancel `m'-10` from the ratio in (1):

```text
L(K')/U(K')
 =constant * C(m',9)/C(n',9) * (m'-9)/n'.          (3)
```

The nine factors `(m'-i)/(n'-i)`, `0<=i<=8`, and the final factor
`(m'-9)/n'` all strictly increase with `K'`, because `n'-m'=D>0`.
Therefore (3) strictly increases, and the contradiction in (2) persists
for every `K'>=20618`.

## Why the former low-row proof does not propagate

The nine-cell pair-core theorem is an original-row statement. Reversing a
shortening from residual dimension `K'` multiplies by a locator on
`1048576-K'` deleted coordinates, and those coordinates lie in every
lifted owner core. Hence an original-row common core `J_lift` decomposes as

```text
J_lift = J_deleted disjoint_union J_res,
|J_deleted|=1048576-K'.                             (4)
```

The conclusion `|J_lift|>=134944` does not imply
`|J_res|>=134944`; for every `K'<=913632`, (4) already satisfies the
original-row lower bound with `J_res` empty. Comparing `|J_lift|` with the
residual support size `m'` mixes two rows. Same-support noncontainment gives
only `|C_res|<m'` in the residual row and `|C_lift|<1116048` after lifting.
Neither contradicts (4). Thus no row below the weighted crossing is closed
here.
