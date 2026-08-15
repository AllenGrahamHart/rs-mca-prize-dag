# Sparse-circuit near-saturation carrier

- **status:** PROVED
- **support range:** `2<=c<=4`

Use the correction-space setup of the sparse-circuit completion ladder.
Put `q=K-10`.  Assume no independent deletion has all `q` circuit
completions.  For each fixed support size `2<=c<=4`, one of the following
holds.

1. Every independent `(c-1)`-set has at most `q-2` completions.
2. Every support-`c` circuit lies in one carrier of size at most
   `q+2c-2`.

Consequently the support-`c` incidence cap is

```text
max{
  C(q+2c-2,c) C(m-c,11-c),
  floor(C(m,c-1)/c
        * max_(0<=b<=q-2) b C(m-c+1-b,11-c))
}.                                                    (NS)
```

At `K'=22`, this maximum occurs at `b=q-2=10`, and the second branch is
active for `c=2,3,4`, with caps

```text
c=2:  26976765544297626187032777583778108529876750
c=3:  80942289326850303820580142737960784746097750
c=4: 161908567951387946577119676170547680391323000
```

## Falsifier

`q-1` completions whose labels fail to span a quotient hyperplane; a
support-`c` circuit outside the enlarged carrier; failure of Vandermonde
uniqueness at union size `q+3c-2`; or an incidence count above `(NS)`.
