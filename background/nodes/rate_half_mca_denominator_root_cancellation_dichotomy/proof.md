# Proof

The harvested cancellation theorem gives `P subset S_i`, the reduced support
size `|S_i'|=m-t`, and `t<=deg Q<=m-k`. Therefore

```text
|S_i'| = m-t >= k.                                  (1)
```

Partition the nonzero-scalar indices according to whether a simultaneous
degree-`<k` explaining pair exists on `S_i'`. This is exhaustive and
disjoint. The `N` indices satisfy reduced support-wise MCA nontriviality by
definition, and the harvested divided identity preserves the original line,
slope, and exact support locator.

Fix `i in T` and choose one explaining pair `(p0_i,p1_i)`. On `S_i'`, both
`h_i` and `p0_i+gamma_i p1_i` equal `r0+gamma_i r1`. Their difference has
degree less than `k` and at least `k` roots by (1), hence

```text
h_i = p0_i + gamma_i p1_i
```

as polynomials. On every point of `P subset S_i`, the original support
agreement then gives

```text
(r0-p0_i) + gamma_i (r1-p1_i) = 0.                 (2)
```

If `v_i=(r1-p1_i)|_P` were zero, (2) would also make
`u_i=(r0-p0_i)|_P` zero. The pair would then simultaneously explain the
received pair on `S_i' union P=S_i`, contrary to the original support-wise
MCA nontriviality. Thus `v_i` is nonzero, and (2) recovers `gamma_i` at any
coordinate where `v_i` is nonzero.

Finally suppose distinct slopes `gamma_i` and `gamma_j` used the same ordered
polynomial pair `(p0,p1)`. Their pole defects would be the same vectors
`u,v`, and (2) for both slopes would give

```text
(gamma_i-gamma_j)v=0.
```

Distinctness forces `v=0`, contradicting the preceding paragraph. Hence the
pair assignment is injective. QED.
