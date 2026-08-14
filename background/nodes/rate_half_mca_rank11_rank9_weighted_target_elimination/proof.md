# Proof

Put

```text
n'=1048576+K',       m'=67472+K',       D=n'-m'=981104.
```

The fixed target has at least `2578110` records. In its rank-nine branch,
the nine-cell pair-core dichotomy applies, and

```text
2578110>1434405
```

forces a common owner-plane core `J` with `|J|>=134944`.

Every owner point on a nonempty record line owns an actual support-wise
pair-noncontained record. Its complete pair core has size below `m'`.
Since `J` lies in every owner core,

```text
134944<=|J|<m'.                                      (1)
```

If `K'<=67472`, then `m'<=134944`, contradicting (1).

Now assume `K'>=67473`. The weighted concentrator and weighted rank-nine
cap give, in the same `(record,T)` unit,

```text
L(K') = (495405467/10^9) N_min
        *C(m',9)*C(m'-9,2)/C(n',9),
W_B>=ceil(L(K')),
W_B<=U(K')=981105*(m'-10)n'.                         (2)
```

At `K'=67473`, exact integer cross-multiplication gives

```text
L(67473)>147748596828055575=U(67473),
ceil(L(67473))=6849288576200976639.                  (3)
```

It remains to make (3) uniform. Since

```text
C(m'-9,2)=(m'-9)(m'-10)/2,
```

the ratio in (2) simplifies to

```text
L(K')/U(K')
 =constant * C(m',9)/C(n',9) * (m'-9)/n'.           (4)
```

Each factor `(m'-i)/(n'-i)`, `0<=i<=8`, strictly increases with `K'`
because `n'-m'=D>0`. The final factor `(m'-9)/n'` also strictly increases.
Thus (4) increases, so (3) implies `L(K')>U(K')` for every larger `K'`.
This contradicts (2) and eliminates the rank-nine branch on the complete
residual interval.
