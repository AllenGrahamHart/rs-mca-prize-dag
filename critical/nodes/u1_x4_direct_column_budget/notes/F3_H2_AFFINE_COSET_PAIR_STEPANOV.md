# F3 h=2 affine-coset pair Stepanov corollary

Status: PROVED COROLLARY OF THE OPTIMIZED H2 RICH-COSET THEOREM.

This packet factors out the h=2 corollary used by the h=3 repeat-boundary q0
and fiber-cap packets.

## Statement

Let `H <= F_p^*` have order `n`.  Let

```text
L_1(X)=a_1 X+b_1,  L_2(X)=a_2 X+b_2
```

be affine forms with nonzero slopes, and suppose that after using `Y=L_1(X)`
one has

```text
L_2(X)=alpha Y + beta
```

with

```text
alpha != 0,  beta != 0.
```

Under the single-shift h=2 Stepanov hypothesis

```text
n^4 < p^3,
```

one has

```text
#{X : L_1(X) in H, L_2(X) in H} <= 66 n^(2/3).
```

## Proof

The change of variable `Y=L_1(X)` is bijective, so it is enough to bound

```text
#{Y in H : alpha Y + beta in H}.
```

Put `u=-beta/alpha`, so `u != 0`.  After scaling `Y=uZ`, the counted points
satisfy

```text
Z^n = u^(-n),
(Z-1)^n = (alpha u)^(-n).
```

These are the same two shifted h-power equations used in
`F3_H2_RICH_COSET_OPTIMIZED.md`, except that the right-hand sides are nonzero
constants rather than `1`.

The optimized h=2 proof is unchanged:

- the auxiliary polynomial is still `Phi(Z,Z^n,(Z-1)^n)`;
- the logarithmic derivative and linear-system counts are unchanged;
- the sparse nonvanishing lemma is unchanged, because it concerns the
  substituted polynomial, not the constants imposed at the incidence points;
- the optimized parameter choice gives the same constant `66`.

Therefore the affine coset-pair count is at most `66 n^(2/3)`.

The excluded case `beta=0` is a proportional-coset case and is not the shifted
intersection used by the repeat-boundary line pencil.

## Role in F3

This corollary supplies:

- the q0 payment `B_q0 <= 132 n^(2/3)`;
- the fixed-fiber cap `T_r <= 66 n^(2/3)` for every nondegenerate
  repeat-boundary line parameter.

## Replay

Standalone sample ledger:

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_affine_coset_pair_stepanov.py
```

Expected digest:

```text
H2_AFFINE_COSET_PAIR_STEPANOV_PASS
```
