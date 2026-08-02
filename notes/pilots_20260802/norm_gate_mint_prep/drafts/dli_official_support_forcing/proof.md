# Proof

All arithmetic below is exact integer arithmetic; no logarithms, no floats.
The two inputs are banked in sibling nodes and are not re-derived:

- **(IN-1)** `dli_norm_gate_forward_and_ofold`, Claim 3 (LN2): a nonzero
  element of `Z[zeta_{h_j}]` supported in the basis range `[0, phi(h_j))`
  that is annihilated by the `L_j` block characters has
  `q^{L_j} | Norm != 0`.
- **(IN-2)** `dli_norm_gate_energy_ceiling`, Claim 1 (LN4): a nonzero
  integer-coefficient element of a ring `Z[x]/(x^N+1)` has
  `1 <= Norm <= E^{N/2}`, `E = sum_i a_i^2`.

## Step 0: the schedule pins are what they are said to be

The banked official row (`official_scale.json`) fixes `n = 2^41`,
`t = 2^33`, and the block schedule
`ell = (2^32, 2^31, ..., 2, 1, 1)` of length 34. These are not assumed but
DERIVED: block `j` owns the constraints `r <= t` with `v_2(r) = j`, and

```text
#{ r <= 2^m : v_2(r) = j } = 2^{m-1-j}  (j < m),   = 1  (j = m).
```

(For `j < m` the relevant `r` are `2^j u` with `u` odd and `u <= 2^{m-j}`,
of which there are `2^{m-j-1}`; for `j = m` only `r = 2^m`.) With `m = 33`
this is exactly the pinned `ell`, and `sum_j L_j = (2^33 - 1) + 1 = 2^33 = t`.
The 33 junctions `j = 0..32` have root order `h_j = n/2^j = 2^{41-j}` and
field degree

```text
N_j = phi(h_j) = h_j/2 = h_{j+1} = 2^{40-j},
N_j / L_j = 2^{40-j} / 2^{32-j} = 2^8 = 256   for every j.            (OS-1)
```

The skew index range at junction `j` is `0 <= i < h_{j+1} = N_j = phi(h_j)`,
i.e. **exactly the basis range** — so `(IN-1)` applies with no side condition
(this is the load-bearing "no opposite pairs" clause, satisfied by
construction).

## Claim 1 (the uniform junction criterion)

Let `delta = sum_{i < N_j} d_i zeta_{h_j}^i != 0` be a junction-`j` skew
solution of energy `E = sum_i d_i^2`. By `(IN-1)`, `Norm(delta) != 0` and
`q^{L_j} | Norm(delta)`; since `Norm(delta) >= 1` by `(IN-2)`, divisibility
gives `q^{L_j} <= Norm(delta)`. By `(IN-2)` with `N = N_j`,
`Norm(delta) <= E^{N_j/2}`. Chaining,

```text
q^{L_j} <= E^{N_j/2}.
```

By `(OS-1)`, `N_j/2 = 128 L_j`, so `E^{N_j/2} = (E^{128})^{L_j}` and the
inequality reads `q^{L_j} <= (E^{128})^{L_j}`. Both `q` and `E^{128}` are
positive integers and `t -> t^{L_j}` is strictly increasing on positive
integers, so this is equivalent to

```text
q <= E^{128}.                                                        (OS-2)
```

The junction index has disappeared. Since `E -> E^{128}` is strictly
increasing, `(OS-2)` is equivalent to `E >= E_min(q)`. QED (1).

*Why the `j` drops out.* `L_j` halves at each junction and `N_j` halves at
each junction, so the ratio `N_j/L_j` is a schedule invariant. Everything
about the strength of the gate is that one number, `256`.

## Claim 2 (the `E_min` ledger)

`E_min(q) = min{E : E^{128} >= q}` is well defined and non-decreasing in
`q`. By definition `E_min(q) = k` iff `(k-1)^{128} < q <= k^{128}`. Since

```text
1^{128} = 1,   2^{128},   3^{128} = 11790184577738583171520872861412518
                                    665678211592275841109096961,
4^{128} = (2^2)^{128} = 2^{256}   (exact identity),
```

we get exactly the three-line table of the statement, and `E_min <= 4` on the
whole official range `q < 2^256 = 4^128`. Numerically `3^128` has bit length
`203`, so `2^{202} < 3^{128} < 2^{203}`, and

```text
2^{53} * 3^{128} < 2^{256} < 2^{54} * 3^{128},
```

i.e. the production window `q ~ 2^{255.9}` clears the `E_min = 4` threshold
by more than 53 bits. QED (2).

*The cap coincidence is arithmetic, not numerology.* `4^{128} = 2^{256}` is
an identity; it says the official modulus cap lands precisely on the `E = 4`
rung of the gate. That is exactly why the banked ambient exclusions at weight
`<= 3` were cheap while weight 4 required a `1,398,341,120`-polynomial
enumeration — recorded in the provenance pilot §5.

## Claim 3 (official support forcing)

Let `q > 3^{128}` be official-admissible and let `j = 0`. The junction-0 skew
domain is `{+-1}^{S_0}` (every unsaturated level-1 cell has `c_i = 1`, so
`d_i in {-1,+1}`), whence `E = sum_{i in S_0} d_i^2 = |S_0|` for EVERY
element of the domain, and the domain contains no zero vector.

If `1 <= |S_0| <= 3` then any element `delta` of the domain is a nonzero
junction-0 element of energy `E = |S_0| <= 3`, so by Claim 1 a solution would
force `q <= E^{128} <= 3^{128}`, contradicting `q > 3^{128}`. Hence no
element of the domain solves the block, and — since a `t`-null state must
solve every junction block — no `t`-null state has `|S_0| in {1,2,3}`:

```text
|S_0| = 0   or   |S_0| >= 4.                                         (OS-3)
```

*General junction form.* At junction `j` the domain is
`prod_{i in S_j} {-c_i, -c_i+2, ..., c_i}`, so every element has
`E <= sum_{i in S_j} c_i^2`. If `sum_{i in S_j} c_i^2 <= 3` then every
element has `E <= 3` and, by Claim 1 again, no nonzero element solves the
block. When all `c_i = 1` this says: at most 3 unsaturated cells `=>` the
state is killed. QED (3).

## Claim 4 (the exclusion is total at junction 0)

With the banked definition
`rho_j(state) = (#admissible skews solving block j) * q^{L_j} / |domain|`
(`notes/pilots_20260802/c2pp_nullity_structure/junctions.py`), an excluded
junction-0 state has solution count `0` — there is no zero skew to rescue it,
because `{+-1}^{S_0}` omits the origin — hence `rho_0 = 0` exactly.
Substituting into the banked exact decomposition
`rho_j = q^{delta_j} + Rem_j` (certified in `Z[zeta_q]`, 24/24 at
`(16,2,17)`, `(16,3,17)`, `(16,2,97)`) gives `Rem_0 = -q^{delta_0}` exactly.
QED (4).

*Scope.* The step "solution count `0`" uses that the domain omits `0`. At a
junction where some `c_i` is even the domain contains `d = 0`, which solves
every block trivially, so `rho_j >= q^{L_j}/|domain| > 0` and only the
NONZERO solutions are excluded. Claim 4 is therefore stated at junction 0
(and holds verbatim at any junction all of whose `c_i` are odd).

## Honest pricing of the single-constraint gate

Using only ONE of the `L_j` constraints at junction 0 gives the ceiling
`q <= E^{N_0/2}` with `N_0/2 = 2^{39}`. Since `q < 2^{256}` and
`2^{256} <= 2^{2^{39}} <= E^{2^{39}}` for every `E >= 2`, a single constraint
excludes only `E = 1`. **All of the strength of Claim 3 comes from `(IN-1)`
supplying the full block exponent `L_j`, together with the fixed `256:1`
ratio.** This is worth stating because it says exactly where the theorem
would break: any weakening of the `o`-fold upgrade (e.g. a seam that makes
the `L_j` characters non-distinct) collapses the gate from `E >= 4` to
`E >= 2`.

## Empirical corroboration (provenance, not part of the proof)

At real tower junctions `j = 0, 1, 2` with `(n,t,q)` in
`{(32,8,97), (32,8,193), (32,8,257), (64,8,193), (32,16,97)}` the provenance
pilot enumerated bounded non-ternary skews over sampled states
(`results/tower.json`, `all_hold = true`): 0 violations of LN2, LN4 and LN5,
and **2,453 states predicted empty by the router contained 0 solutions**
between them. (The pilot's prose reports "2,053"; the persisted per-row
counts in `tower.json` sum to `2453`. The persisted artifact is
authoritative.)
