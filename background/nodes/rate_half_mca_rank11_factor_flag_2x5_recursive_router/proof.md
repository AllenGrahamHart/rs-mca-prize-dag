# Proof

Work in the anchor-good universe `G_0`, whose size is at most
`m=1116048`. Every promoted container has a selected common-zero set `J_i`
of size at least

```text
H=38385.
```

If `P` has a common zero in `G_0`, every product in `PB=C'` vanishes there,
which is output 1. Hence assume the pencil is base-free on `G_0`.

For a projective pencil member `g`, let `a(g)` be its number of zeros in
`G_0`. Distinct projective members have disjoint zero sets: at a coordinate
where evaluation on `P` is nonzero, its kernel is one projective pencil
member. For a residual subspace `B_i`, let `b(B_i)` be the number of common
zeros of all its polynomials in `G_0`. Since

```text
Z(g_iB_i)=Z(g_i) union Z(B_i),
```

the rich-container zero set gives

```text
H <= a(g_i)+b(B_i).                                    (1)
```

Set `T=408`. Orient a container to its factor when `a(g_i)>=T`; otherwise
(1) gives

```text
b(B_i)>=H-T+1=37978.                                  (2)
```

The disjoint pencil root sets allow at most

```text
floor(m/T)=2735
```

factor-heavy projective members. For one fixed `g`, all assigned pair
differences lie in `gB`, of dimension at most five. The ordinary affine-span
and sub-square interleaving cap at the inherited agreement is

```text
R_5=1010335321405.
```

Thus factor-heavy classes cost at most `2735 R_5`.

Now consider residual-oriented containers. Suppose every `B_i` is
`18165`-transverse: every proper subspace of `B_i^perp` contains at most
`18165` labelled restricted evaluation columns from its common-zero set.
For `dim B_i=2`, the annihilator in the five-space `B` has dimension three.
Greedy ordered bases and (2) give at most

```text
N_2=floor(m^(underline 3)/(37978-18165)^3)=178729
```

distinct residual planes. For `dim B_i=3`, the annihilator has dimension two
and similarly

```text
N_3=floor(m^(underline 2)/(37978-18165)^2)=3172.
```

For a fixed residual `B_i`, all assigned pair differences, as `g` varies,
lie in `PB_i`. Its dimension is at most four when `dim B_i=2` and at most six
when `dim B_i=3`. The exact pair/slope caps are

```text
R_4=63397365764,   R_6=16100859197492.
```

The factor orientation and residual orientation partition all promoted
containers, and the anchored row-space partition assigns every residual
slope once. Hence their complete cost is at most

```text
2735 R_5 + 178729 R_4 + 3172 R_6
=65166140264121255.                                  (3)
```

Adding (3) to the full-span transverse envelope `209812758437679617` gives
`274978898701800872`, below `B*` by `1829409594215`. This contradicts
unsafety. Therefore an unsafe base-free factor flag contains a residual
`B_i` that is not `18165`-transverse. A proper flat then contains at least
`18166` labelled common-zero columns. Taking its orthogonal inside `B`
strictly extends `B_i` and preserves all those zeros, proving output 2.

The exact verifier scans every legal `T` and the maximal payable residual
threshold at each. The global maximum is `18165`, at `T=408,411`; the former
has the larger slack. At `T=408,h=18166`, the total exceeds `B*` by
`15983178478905`.
