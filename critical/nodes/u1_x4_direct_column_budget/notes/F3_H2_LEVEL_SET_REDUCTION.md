# F3 h=2 level-set reduction (Terminal B re-entry)

Status: PROVED REDUCTION + MACHINE-VERIFIED ROW REPLAY.  This does not prove
the in-house HBK/Konyagin energy theorem, but it isolates the missing B2
energy-level upgrade as a concrete coset-level L2 estimate.

## Pre-registration

Stage: Terminal B, missing B2.

The previous Terminal B note reduced h=2 trades to additive energy and named
the missing upgrade from a single-shift Stepanov intersection bound to the full
energy bound.

This pass banks the exact level-set form of that missing upgrade.

Success criterion:

- prove an exact identity expressing `E(H)` through multiplicative-coset
  intersection counts;
- state the exact L2 estimate that would imply `E(H) <= C n^(5/2)`;
- replay the identity on the banked rows through `n=512`.

Failure criterion:

- if the coset constancy or energy identity fails on any row, do not use this
  formulation.

## Exact Reduction

Let `H <= F_p^*` be a multiplicative subgroup of size `n`.  For `s != 0`, set

```text
r(s) = #{(x,y) in H^2 : x - y = s}
     = |H cap (H+s)|.
```

If `h in H`, then multiplication by `h` bijects solutions for `s` with
solutions for `hs`, so `r(s)` is constant on each multiplicative coset
`sH`.  Write this common value as `r_C`.

The additive energy is the difference-energy identity

```text
E(H) = #{(a,b,c,d) in H^4 : a+b=c+d}
     = sum_s r(s)^2
     = n^2 + n * sum_C r_C^2,
```

where the `n^2` term is the zero shift and `C` ranges over nonzero
multiplicative cosets of `H` in `F_p^*`.

Therefore the desired explicit energy theorem is equivalent to

```text
sum_C r_C^2 <= C' n^(3/2)
```

with an explicit `C'`; then

```text
E(H) <= n^2 + C' n^(5/2).
```

In level-set form, for dyadic levels

```text
L_j = #{C : 2^j <= r_C < 2^(j+1)},
```

it is enough to prove

```text
sum_j L_j * 2^(2j) <= C'' n^(3/2)
```

with explicit constants.  This is the precise B2 upgrade missing from the
single-shift Stepanov bound.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_levelset_replay.py
```

Expected digest:

```text
H2_LEVEL_SET_REPLAY_PASS
```

## Result

The replay verifies the coset constancy and energy identity on
`n = 16,32,64,128,256,512`, each at the first prime `q = 1 mod n` above
`n^2` and `n^3`.

The exact row maximum is:

```text
max coset_l2 / n^1.5 = 0.6406
```

This is consistent with the external `n^(5/2)` theorem and much stronger than
the trivial consequence of a max-intersection bound.  It remains evidence, not
the in-house proof: the missing theorem is now the explicit level-set/L2 bound
for the coset counts `r_C`.
