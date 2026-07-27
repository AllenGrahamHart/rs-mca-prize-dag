# RS tangent flexible-budget unsafe floor

- **status:** PROVED
- **closure:** proof

Let `C=RS[F,D,k]`, `n=|D|`, `q=|F|`, and choose an integer agreement
`a` with `k<a<n`. Put

```text
delta = 1-a/n,
e = n-a,
B* = floor(q/2^t).
```

If `e<=q`, one received line has at least `e` pairwise-distinct support-wise
MCA-bad slopes at radius `delta`. In particular,

```text
n-a > floor(q/2^t)
```

is an exact direct-value unsafe certificate:

```text
epsilon_mca(C,delta) >= e/q > 2^-t.
```

Equivalently, the theorem's guaranteed `e`-slope payload clears the budget
exactly on the numerical range

```text
q<=e*2^t-1.
```

For an evaluation set `D subset F`, the premise `e<=q` is automatic because
`e<n<=q`. No subgroup, quotient, prime-field, generated-field, or norm
hypothesis is used.
