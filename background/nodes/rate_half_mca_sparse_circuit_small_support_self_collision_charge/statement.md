# Small-support same-source collision charge

- **status:** PROVED
- **support range:** `2<=c<=5`

Let `q=K-10`, and let `M_c=q-s` be the maximum number of support-`c`
circuit completions of an independent `(c-1)`-deletion.  Use `M_c=0`, hence
`s=q`, when the support-`c` circuit stratum is empty.

If the stratum is nonempty, choose an attaining source deletion and let `B`
be its completion carrier.  Then

```text
b=|B|=q+c-1-s.
```

For every independent support-`c` deletion `A`, its carrier has at most
`s+c-1` points outside `B`.  Consequently, writing `N=m-b`, the number of
support-`c` circuit supports is at most

```text
C(b,c),                                                       s=0,

C(b,c)+sum_(j=1)^c floor(
  C(b,c-j) C(N,j-1) (s+c-j) / j
),                                                            0<s<q,

0,                                                            s=q.    (SC1)
```

Their selected eleven-set incidence is at most `(SC1) C(m-c,11-c)`.

## Falsifier

A nonempty stratum with `M_c=0`; an intersection dimension below `12-2c`;
an independent deletion carrier with more than `s+c-1` points outside the
source carrier; or a circuit omitted from the inside stratum and all exact
outside strata.
