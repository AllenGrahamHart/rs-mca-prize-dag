# Support-four external-carrier charge

- **status:** PROVED
- **component subset size:** `11`

Assume the joint support-four/support-five zero-carrier theorem.  Write
`b=K-t-delta`, `N=m-b`, and let `C_4(t,delta)` be

```text
C(b,4),                                                    delta=0,

C(b,4)+sum_(j=1)^4 floor(
  C(b,4-j) C(N,j-1) (delta+4-j) / j
),                                                        delta>0.   (EC1)
```

Then the number of support-four circuit supports is at most
`C_4(t,delta)`, and their selected eleven-set incidence is at most

```text
C_4(t,delta) C(m-4,7).                                  (EC2)
```

For terminal defects `s_4,s_5`, a branch-safe cap is the maximum of `(EC2)`
over

```text
4<=t<=6,       0<=delta<=min(s_4,s_5).                   (EC3)
```

At `K'=45`, `m=67517`, the five caps indexed by
`r=min(s_4,s_5)=0,1,2,3,4` are respectively

```text
128418333025617494219383854271189320
16309490987560221486803236111312261069715952
32578977236967057729773689331510654377703052
48847981285537255883023887048112197222518076
65116503154664572206800622437528709545004660.
```

## Falsifier

A support-four circuit omitted from the inside stratum and all four outside
strata; an outside completion count exceeding `delta+4-j`; a circuit charged
fewer than `j` times in outside stratum `j`; or an incidence above `(EC2)`.
