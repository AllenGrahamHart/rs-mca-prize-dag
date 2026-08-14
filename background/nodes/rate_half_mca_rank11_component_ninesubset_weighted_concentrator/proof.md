# Proof

The predecessor fixes a component lane with at least

```text
I >=lambda*N_min*C(m',11),       lambda=495405467/10^9
```

incidences `(gamma,T)`. Mark all `C(11,9)=55` nine-subsets `B` of every
incidence. Averaging the resulting `55I` marked incidences over all
`C(n',9)` domain nine-subsets gives one `B` with

```text
W_B >=ceil(55*lambda*N_min*C(m',11)/C(n',9)).        (1)
```

The exact identity

```text
55*C(m',11)=C(m',9)*C(m'-9,2)
```

turns (1) into (WC1). No division by the extension multiplicity has been
made.

For comparison, a fixed record and `B` admit at most `C(m'-9,2)` choices
of `T`. Therefore

```text
number of distinct records
 >=ceil(W_B/C(m'-9,2))
 >=ceil(lambda*N_min*C(m',9)/C(n',9)).
```

Every factor `(67472+K'-i)/(1048576+K'-i)`, `0<=i<=8`, increases with
`K'`, so the uniform distinct-record endpoint is `K'=10`, where exact
integer arithmetic gives `2578110`. Direct evaluation of (WC1) there gives
`5868470021012020`.
