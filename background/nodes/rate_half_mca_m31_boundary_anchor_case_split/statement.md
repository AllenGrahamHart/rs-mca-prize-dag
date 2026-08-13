# Mersenne boundary-anchor case split

- **status:** PROVED
- **closure:** absorb one extra deficit layer when two high anchors exist
- **scope:** the pair-noncontained full-lift MCA branch

Retain the full-lift notation and put

```text
s=floor((e-K)/3),       q=e-K-3s,       H=e-s-1,
t=N-m.
```

Assume `H>=2`, `q>=1`, `2(s+1)<e`, `m-H>K-1`, and that every ordinary
Johnson/mean-centered cumulative cap `C_h` is defined through `H`. For
`0<=J<=H`, put

```text
B_0^(J)=0,       B_h^(J)=min_(h<=v<=J) C_v,
P_J=sum_(h=1)^J (B_h^(J)-B_(h-1)^(J))*floor(e/h),
P_0=0.
```

Then the full selected slope family satisfies the boundary-anchor bound

```text
|Z| <= max(P_H+1, P_(H-1)+(t+1)).                    (BA1)
```

For the Mersenne-31 MCA row at `e=98230`,

```text
s=32741, q=1, H=65488, t+1=981129,
P_H=16434744,       P_(H-1)=15506184.
```

Thus `(BA1)` gives

```text
|Z| <= max(16434745,16487313)=16487313
     < 16777215,
```

with exact slack `289902`. The paid Mersenne full-lift interval now extends
through `e=98230`; its residual interval starts at `e=98231`.

At `e=98231`, the same theorem is legal but gives `17492173`, exceeding the
budget by `714958`. This adjacent proof-method failure is not an unsafe
certificate.

## Nonclaims

This node does not pay KoalaBear, prove Mersenne safety at `e=98231`, or
claim that the first unpaid support is unsafe.
