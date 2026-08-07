# Sharp FPC5 distance-only no-go fence

- **status:** PROVED
- **consumer:** `l1_fpc5_ratehalf_m4_t2_payment`

Put `L=ell-2` at the sharp rate-half cell. Then

```text
|C|=5L+5,       |D|=2L+1,
|B|=|R|=L-1,    s=L-1.                               (NG1)
```

There exist abstract families `F_L` of defect sets `D subset C` with

```text
|D intersect D'|<=L-1       for D!=D',               (NG2)
```

and

```text
|F_L|
 >= binom(5L+5,2L+1)
    / sum_(i=0)^(L+1) binom(2L+1,i)binom(3L+4,i).    (NG3)
```

In particular,

```text
log_2 |F_L|
 >= (5H(2/5)-2H(1/2)-3H(1/3)+o(1))L
 = (0.099865...+o(1))L.                              (NG4)
```

Adjoining the same fixed background block `B` to every member gives combined
supports `S=D union B` with the exact sharp weight and

```text
|S intersect S'|
 <=(L-1)+(L-1)=2L-2=2s.                              (NG5)
```

Thus the parameter, block, weight, and pairwise-overlap information proved by
the joint-support distance theorem is compatible with exponential abstract
families. No support-distance-only argument can yield the required fixed
polynomial bound.

## Scope

These are abstract set systems. The theorem does not place their locators in
the guarded cofactor flat, satisfy the numerator equations, or construct a
received word. It is a route-sufficiency refutation, not an FPC5
counterexample.
