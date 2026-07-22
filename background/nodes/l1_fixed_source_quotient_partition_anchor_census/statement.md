# L1 fixed-source quotient-partition anchor census

- **status:** PROVED
- **role:** remove non-intrinsic quotient-polynomial multiplicity inside one fixed source
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Anchored quotient partitions

Fix one maximal sunflower source layout with pairwise disjoint source petals

```text
T_1,...,T_(M_src),       |T_i|=ell.                    (FQ1)
```

An anchored internal quotient partition is the additive-shift class of a
monic degree-`ell` polynomial `P` for which at least one source petal is a
complete level fiber:

```text
T_i={x in H:P(x)=a_i}.                                 (FQ2)
```

The class identifies `P` and `P+c`, since they induce the same partition of
the domain into level fibers.

Then the number of anchored quotient partitions is at most

```text
M_src.                                                 (FQ3)
```

Indeed, if `(FQ2)` holds, both `P-a_i` and the petal locator `L_(T_i)` are
monic degree-`ell` polynomials with the same `ell` distinct roots. Hence

```text
P-a_i=L_(T_i).                                         (FQ4)
```

Two quotient polynomials anchored by the same petal therefore differ by a
constant:

```text
P-P'=a_i-a_i'.                                        (FQ4a)
```

They define the same partition. Assigning a partition to the least
source petal it carries is injective, proving `(FQ3)`.

## Structural rechart keys

For one such partition, there are at most

```text
L<=n/ell                                                (FQ5)
```

complete degree-`ell` fibers in the domain. Even if an internal structural
key independently labels every complete fiber as core, petal, or unused, the
total number of anchored quotient keys in the fixed source is at most

```text
M_src 3^L <= M_src 3^(n/ell).                          (FQ6)
```

At the L1 cutoff

```text
ell>=c_0 n/log_2 n,       M_src<=n/ell,                (FQ7)
```

this is at most

```text
(log_2 n/c_0) n^(log_2(3)/c_0),                        (FQ8)
```

and is polynomial. Therefore any uniform polynomial payment for one
anchored quotient key aggregates polynomially across all non-intrinsic
anchored quotient keys inside the fixed first source.

Composing with `l1_quotient_chart_bipolar_entropy_closure`, every fixed
`(p_pet,p_core)` box of genuine quotient/coset common-pencil cells is
polynomial across all such anchored internal recharts.

The anchor hypothesis is not automatic. In particular, a contributor having
dense support on a source petal does not imply that an arbitrary internal
quotient map carries that whole petal as one level fiber. Such a map belongs
to the smaller-fiber/refinement residual below unless a separate argument
supplies `(FQ2)`.

## Scope

This theorem counts quotient partitions and their complete-fiber role keys.
It does not count contributor-dependent Forney coefficient strata within one
key, pay growing petal or core polarity, or cover arbitrary-locator cells.
It also does not cover a smaller-degree quotient map for which a source petal
is a union of several fibers rather than one complete fiber. Those are the
inputs left by this census. The downstream
`l1_fixed_source_anchored_triple_polarity_closure` pays the coefficient strata
at fixed layout/core-defect/petal polarity; growing polarity and the
unanchored/refinement branches remain live.
