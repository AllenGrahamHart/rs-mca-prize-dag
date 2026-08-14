# Kernel multi-basis decoration compression

- **status:** PROVED
- **scope:** one rank-deficient eleven-subset in the residual correction
  matroid
- **units:** decorated `(record,T,B)` incidences

Let `W=V'` be the ten-dimensional residual correction space, and let `T`
be an eleven-subset with

```text
rank(ev_T:W->F^T)=r=10-d,       1<=d<=9.
```

The evaluation matroid on `T` is loopless. Consequently `T` has at least

```text
1+(11-r)=d+2
```

distinct rank bases `B` of size `r`.

Decorate every kernel-lane incidence `(record,T)` by every such basis.
For each fixed `B`, the common-quotient cancellation and support-local
rank-`d` cap used by the canonical-basis globalizer apply to all decorated
records over `B`. The fixed-basis decorated capacity is therefore still

```text
M_d C(K'-10,d+1).
```

Since every undecorated incidence has at least `d+2` decorations, the
rank-`d` capacity improves to

```text
floor(C(n',10-d) M_d C(K'-10,d+1)/(d+2)).
```

This is a multiplicity correction to the kernel capacity. It does not pay
the complete kernel lane or any affine-owner lane.

## Falsifier

A common-zero coordinate of `W`; a rank-`r` eleven-set with fewer than
`12-r=d+2` bases; failure of the fixed-basis quotient cancellation when
all basis decorations are retained; or a decorated incidence counted in
the numerator without a corresponding basis of `T`.
