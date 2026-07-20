# L1 polarized petal-entropy ledger

- **status:** PROVED
- **role:** preserve sparse/full petal polarity in the root-pinning aggregate
- **consumers:** `l1_mixed_residual_intersection_pin`,
  `l1_mixed_petal_amplification`, `petal_mixed_amplification`

## Statement

In one maximal-sunflower chart, let a non-planted listed word have exact
petal support sizes

```text
a_i=|S_i|,       1<=a_i<=ell,
h=sum_i a_i,
e=max(0,2d+1-h).
```

Define its polarized petal entropy by

```text
p=sum_i min(a_i,ell-a_i).                              (PE1)
```

For every fixed integer `E>=0`, the aggregate class

```text
p+e<=E                                                  (PE2)
```

has size at most

```text
2^M binom(M+E,E) n^(E+1).                              (PE3)
```

At the L1 lower cutoff `ell>=C_0 n/log_2 n`, one has
`M<=log_2(n)/C_0`, so `(PE3)` is polynomial in `n` with a fixed exponent.

This strictly strengthens the former fixed-`u+e` aggregate, where
`u=sum_i(ell-a_i)`: always `p<=u`, but a singleton petal contributes `1` to
`p` and `ell-1` to `u`. Thus, for example, one singleton support together
with any number of full petals is paid whenever the root excess `e` is
bounded.

## Scope

The theorem does not count the complementary `p+e->infinity` class, control
growing support entropy on a single petal, or provide a natural-scale owner.
It does not promote either L1 consumer.
