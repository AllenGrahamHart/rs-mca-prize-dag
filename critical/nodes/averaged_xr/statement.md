# Exact slope-resolved support-pair moment

- **status:** PROVED
- **closure:** exact linear algebra
- **upstream source:** `rs-mca` commit `674503f72134eaed4a20f1944f1423b23744ce2c`

Let `F=F_q`, let `D subset F` contain `n` distinct points, and let
`1<=k<k+t<=n`. For every `(k+t)`-support `S`, let

```text
Pi_S : F^D -> F^t
```

send a word to the top `t` coefficients of its interpolant on `S`, and put
`K_S=ker(Pi_S)`. If two supports `S,T` have exchange distance
`d=|S\T|=|T\S|`, then

```text
rank(Pi_S,Pi_T)=t+min(d,t).
```

Fix a slope `z` and choose independent uniform words `f,g`. A support
contributes `z` exactly when

```text
Pi_S(f+zg)=0 and Pi_S(g)!=0.
```

Writing `a=q^(-t)` and

```text
alpha_d=q^(-t-min(d,t)),
```

two distinct supports at distance `d` both contribute `z` with exact
probability

```text
P_d=alpha_d(1-2a+alpha_d).
```

In particular, this is `p_z^2` for `d>=t`, where
`p_z=a(1-a)`, and for `1<=d<t` it is

```text
q^(-t-d)(1-2q^(-t)+q^(-t-d)).
```

Hence every deterministic support family has the exact fixed-slope second
factorial moment printed in `proof.md`. This is the complete moment input
needed by `averaged_slope_conversion`.

## Scope

This theorem is an averaged random-line identity. It does not prove
worst-case exchange rigidity, an XR inverse theorem, or independence between
different slopes. Cross-slope independence is not needed by the occupancy
conversion.
