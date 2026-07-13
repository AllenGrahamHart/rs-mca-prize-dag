# Proof

Write `q=65537=2^16+1`. Pocklington's theorem with the complete factor
`F=2^16=q-1` and witness `3` proves primality: direct modular arithmetic gives
`3^(q-1)=1 mod q` and `gcd(3^((q-1)/2)-1,q)=1`. Since
`3^((q-1)/2)=-1 mod q`, `3` is primitive.

Set `omega=3^128 mod q=15028`. Then `omega^512=1` and
`omega^256=-1`, so its order is exactly `512`. Direct reduction proves

```text
1 + omega^95 - omega^146 = 0 mod q.
```

No one- or two-term proper subsum vanishes. More generally, a reduced
weight-2 relation would give `omega^d` in `{1,-1}` for an integer
`0<|d|<256`, contradicting the exact order. Thus the relation is primitive
and has the minimum weight `3`.

In `Z[z]/(z^256+1)`, a nonzero signed shift stabilizing this three-point
coefficient vector would partition its support into orbits of a nontrivial
translation of the cyclic group of order `512`. Every such orbit has
power-of-two size greater than one, which cannot partition a set of odd size
three. Hence all `512=2N` signed shifts are distinct. At `ell=1` there is no
smaller positive level from which this primitive generator could lift, so at
least one first-owner copy is charged. Its mass is `512/8=64`.

Finally, `q=1 mod512`, `2^256>=q`, and `N=256>=16 ell`, so this is an
isolated C1' row. But `q-1=2^16` is not divisible by `2^41`, the top subgroup
order forced by the production schedule. The witness therefore refutes the
unscoped strengthening and not the official-row WCL-ZONE claim.
