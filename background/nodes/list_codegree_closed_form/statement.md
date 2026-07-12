# Arbitrary-arity closed form for the codegree recursion

- **status:** PROVED
- **consumer:** `list_large_m_scope_closure`

Fix a code of length `n`, dimension `k`, an agreement
`a_0=k+sigma` with `sigma>0`, and define

```text
a_j = k + 2^j sigma.
```

Let `B_j` be the worst ordinary-list size at agreement at least `a_j`, and let
`L_m(j)` be the worst `m`-interleaved common-support list size at that
agreement. Put

```text
d = max {j>=0 : a_j<=n}.
```

Then for every `m>=1`,

```text
L_m(0) <= sum_(r=0)^min(m-1,d)
             binom(m-1,r) product_(j=0)^r B_j.       (CF)
```

Thus the arbitrary-arity codegree tree has finite agreement depth `d` and is
polynomial in `m` of degree at most `d`. It does not by itself prove that the
right side fits the prize budget or meets a lower witness at an adjacent
agreement.
