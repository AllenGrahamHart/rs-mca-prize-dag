# Mersenne two-boundary-layer case split

- **status:** PROVED
- **closure:** absorb the second boundary layer at residue two
- **scope:** the pair-noncontained full-lift MCA branch

Retain the full-lift notation and put

```text
s=floor((e-K)/3),       q=e-K-3s,       H=e-s-1,
n=N-e,                  c=K-1,           t=N-m.
```

Assume the prefix hypotheses of the one-boundary-layer theorem through
`H`, together with

```text
q=2,       2(s+2)<e,       m-H>c.
```

Let `P_J` be the independently truncated suffix-minimum prefix profile
through `J`.  Define

```text
Q=floor((n-c)/(m-H-c)),       D=floor(e/(s+1)).
```

Then the complete selected slope family satisfies

```text
|Z| <= max{
  P_(H-2)+(t+1),
  P_(H-1)+Q+1,
  P_(H-1)+2,
  P_(H-1)+Q,
  P_(H-1)+D
}.                                                       (BA2)
```

For the Mersenne-31 MCA row at `e=98231`,

```text
s=32741, q=2, H=65489,
P_(H-2)=15505282,       P_(H-1)=16433719,
t+1=981129,             Q=484,             D=3.
```

The five cases in `(BA2)` are

```text
16486411, 16434204, 16433721, 16434203, 16433722.
```

Therefore

```text
|Z| <= 16486411 < 16777215
```

with exact slack `290804`.  The paid Mersenne full-lift interval now extends
through `e=98231`; its residual interval starts at `e=98232`.

At `e=98232`, the residue resets to `q=0`, so `(BA2)` is inapplicable.  This
is a theorem-scope wall, not an unsafe certificate.

## Nonclaims

This node does not pay KoalaBear, prove safety at `e=98232`, or assert that
the residue-zero support is unsafe.
