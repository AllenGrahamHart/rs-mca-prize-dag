# Cycle 224: Mersenne next-cell Delsarte route screen (2026-08-13)

The first unpaid mean-centered Mersenne support `e=65455` misses the MCA
budget by only `342908`.  Its punctured explanation blocks have

```text
n=983127,       A=1999,       pair intersection <=5.
```

A preregistered Johnson-scheme Delsarte LP used the six possible distances
`A-5,...,A`.  Exact dual-Hahn entries were built by integer term
recurrence; only the final ratios were converted to floating point.  Each
distance variable was bounded by the proved total list cap `16203700`.

The initial 60-second run completed 541 of 1999 eigenspaces and returned the
partial-relaxation optimum `16203700.200638048`, with no improvement.  One
staged completion rerun was authorized.  It completed all 1999 rows and
returned the same optimum:

```text
proved raw cap:       16203700
full LP optimum:      16203700.200638048
payment threshold:    15860792
verdict:              NO SIGNAL
```

Thus the ordinary support-only Delsarte LP is weaker than the proved
mean-centered cap and cannot pay the slope profile.  No exact dual is needed
for this negative route screen; no theorem or DAG status changes.

Modal runs:

- partial: `ap-7CJw55he3qUkakWZSfvCnn`;
- full: `ap-s1CgqT4b9VaKbStMrw8MHG`.

```text
start:                   67f22b780
result:                  ROUTE CUT; support-only Delsarte gives no saving
DAG delta:               none
critical status delta:   none
full-lift residuals:     unchanged
delta-star movement:     none
compute:                 two bounded Modal runs, 2 CPU / 1 GiB; no local
                         heavy computation
next route action:       retain information erased by binary support
                         projection: slope ownership, explanation amplitudes,
                         or the full-lift near-MDS extension
```
