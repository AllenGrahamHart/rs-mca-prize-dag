# Proof

For one owner point `p`, let `q_p` count the independent coordinate pairs
outside `B` that determine it and let `t_p` count its selected records. The
owner-pair capacity proof gives the exact marked decomposition and resource

```text
W_B <=sum_p t_p q_p,
sum_p q_p <=Q(K')=C(n'-9,2).                        (1)
```

The weighted concentrator gives `W_B>=ceil(L(K'))`. Exact arithmetic at
`K'=22526` yields

```text
ceil(L)=115097583282647783,
Q       =573619571778,
ceil(L)-200631*Q=11714977255865.                    (2)
```

If every `t_p<=200631`, then (1) contradicts (2). Hence some owner has

```text
t_p>=200632.                                        (3)
```

The unrounded average satisfies

```text
L(K')/Q(K')
 =constant*C(m',11)/C(n',11),                      (4)
```

because `C(n',9)C(n'-9,2)=55C(n',11)`. Each of the eleven factors in (4)
strictly increases with `K'`, so (3) persists. At `K'=22525`, the rounded
comparison is instead

```text
ceil(L)-200631*Q=-1170919108090,
```

recording the honest method wall.

It remains to identify the terminal type. If the fixed owner's complete
pair core has deficiency `delta`, exception disjointness gives

```text
t_p <=floor((981104+delta)/delta)
     =1+floor(981104/delta).                        (5)
```

For `delta>=5`, the right side is at most `196221`, contradicting (3).
Therefore `delta<=4`. This is precisely the record-count and deficiency
interface of the imported dense-owner chronology terminal.
