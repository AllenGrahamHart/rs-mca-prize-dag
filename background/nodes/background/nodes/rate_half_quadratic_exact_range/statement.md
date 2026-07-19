# Rate-half exact quadratic range

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`

For the official rate-half parameters

```text
n=2^41,                         k=2^40,
s=floor(sqrt(7k^2)),            r_Q=3k-s-1=389,500,552,608,
B_Q=r_Q+1=389,500,552,609.
```

Let `q` be any admissible field order and put `B=floor(q/2^128)`. If
`1<=B<=B_Q`, then the exact adjacent MCA certificate is

```text
a_RH(q)=n-B+1,
B_mca(a_RH(q))=B<B_mca(a_RH(q)-1),
B_mca(a_RH(q)-1)>=B+1.                              (RQ1)
```

Consequently every admissible rate-half field in

```text
2^128<q<(B_Q+1)2^128
       =132540169959144315698788704090115531231543332700160
```

is completely determined. The unresolved rate-half field range begins at
the displayed exclusive endpoint, approximately `2^166.502834419`.

The same theorem gives a post-cutoff bracket. For every `1<=B<=k-1`, put

```text
r_safe(B)=min(B-1,r_Q).
```

Then

```text
B_mca(n-r_safe(B))=r_safe(B)+1<=B,
B_mca(n-B)>=B+1.                                      (RQ2)
```

Hence

```text
n-B+1<=a_RH(q)<=n-r_safe(B).                          (RQ3)
```

For `B<=B_Q` the endpoints coincide and recover `(RQ1)`. For
`B_Q<B<=2^39+1`, the lower candidate `a_0=n-B+1` has radius
`B-1<=2^39=(n-k)/2`; its sparse mutual numerator is at most `B-1`. In this
range the adjacent certificate is therefore equivalent to the single
far-CA assertion

```text
B_ca^far(a_0)<=B.                                     (RQ4)
```
