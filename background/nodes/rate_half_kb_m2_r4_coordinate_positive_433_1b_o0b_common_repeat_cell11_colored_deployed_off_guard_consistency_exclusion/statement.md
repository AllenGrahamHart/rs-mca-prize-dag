# Repeated-BC cell-11 colored off-guard consistency exclusion

- **status:** PROVED
- **field:** `F_2130706433`
- **scope:** missing `BE` and `CF` on all eight guarded cell-11 source towers

Let `q` and `s^2` be the reconstructed product and squared endpoint sum.  A
missing `BE` packet necessarily satisfies

```text
e = q/b,       (b+e)^2 = s^2,
```

and a missing `CF` packet necessarily satisfies

```text
f = q/c,       (c+f)^2 = s^2.
```

The source-algebra norm of each consistency difference is a nonzero rational
function.  Its only deployed numerator roots are `x=0,1` for `BC-` and
`x=0,-1` for `BC+`; every one is a registered chart guard.  Hence neither
colored missing record occurs at a deployed off-guard source value.  This is
independent of the residual matching.

## Falsifier

A deployed non-guard root of either norm, a missing sign row, or a source
packet satisfying the colored product and squared-sum identities off guard.

