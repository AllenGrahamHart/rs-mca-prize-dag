# Small-source cross-support collision charge

- **status:** PROVED
- **source supports:** `2<=c<=5`
- **target supports:** `2<=d<=9`, `c+d<=11`

Let `q=K-10`, and suppose the exact source-support completion maximum is
`M_c=q-s>0`.  Choose an attaining source deletion and let `B` be its
completion carrier, so

```text
b=|B|=q+c-1-s.
```

For every independent target-support deletion `A` of size `d-1`, its
carrier has at most `s+d-1` points outside `B`.  Consequently, writing
`N=m-b`, the number of target-support-`d` circuit supports is at most

```text
C(b,d),                                                       s=0,

C(b,d)+sum_(j=1)^d floor(
  C(b,d-j) C(N,j-1) (s+d-j) / j
),                                                            0<s<q.    (XC1)
```

Their selected eleven-set incidence is at most `(XC1) C(m-d,11-d)`.

## Falsifier

An admissible pair `c+d<=11` with intersection dimension below `12-c-d`;
a target deletion carrier with more than `s+d-1` points outside the source
carrier; or a target circuit omitted from the inside stratum and all exact
outside strata.
