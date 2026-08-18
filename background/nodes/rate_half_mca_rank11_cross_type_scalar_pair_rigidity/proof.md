# Proof

Use the notation of atom collision rigidity. The two certificates give

```text
P_0=Q'c_0-Qc'_0,       P_1=Q'c_1-Qc'_1,
H={x in G:P_0(x)=P_1(x)=0}.
```

Assume for contradiction that `s=(c_0,c_1)` and
`s'=(c'_0,c'_1)` are linearly independent. At a point of `H`,

```text
Q'(x)s=Q(x)s'.                                         (1)
```

Independence in the two-dimensional scalar space forces

```text
Q(x)=Q'(x)=0.                                          (2)
```

Each certificate is pole-simple: a domain root of its denominator belongs
to at most one selected exact support. The 28 supports are selected in both
certificates, so every point of `H` has incidence at most one in the shared
deck.

Put `z=|G\H|`. Outside `G`, the affine collision equation has at most one
slope solution, so support incidence is at most one. On `G\H` use the
trivial upper bound 28. On `H`, equation `(2)` and pole-simplicity give the
upper bound one. Counting the `28m'` support incidences therefore gives

```text
28m' <= (n'-|G|) + 28|G\H| + |H|
      = n' + 27z.
```

Consequently

```text
z >= ceil((28m'-n')/27).
```

With `(n',m')=(2097152-c,1116048-c)`, integer shortening commutes with the
ceiling and yields

```text
z >= ceil((28*1116048-2097152)/27)-c
  = 1079711-c.                                         (3)
```

Atom collision rigidity also says every point of `G\H` belongs to at least
27 of the 28 supports. The deck contains 14 supports from each pair type, so
such a point belongs to at least 13 supports from each type. Two supports of
one saturated type intersect exactly in its pair core. Hence every point of
`G\H` lies in both pair cores.

The types are distinct. Their two component differences are
degree-below-`K'` Reed--Solomon polynomials, so a common pair-core intersection
of size at least `K'` would make both differences zero. Therefore

```text
z <= K'-1=1048575-c.                                  (4)
```

Bounds `(3)` and `(4)` contradict one another by 31,136. The scalar pairs
must be proportional.

Finally, in the degree-two split-pencil normal form, `c_0` and `c_1` are the
leading coefficients of `u` and `v`, because every `L_(E_gamma)` is monic.
The projective limit of `f=-u/v` at infinity is therefore `[-c_0:c_1]`.
Proportional scalar pairs have the same value. QED.
