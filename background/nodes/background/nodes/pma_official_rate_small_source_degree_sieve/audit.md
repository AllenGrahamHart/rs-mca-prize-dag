# Audit - PMA official-rate small-source degree sieve

## Hypothesis ledger

| hypothesis | use | boundary |
|---|---|---|
| exact official rate `n=rk` | converts source size to `(r-1)k+1` | no claim for rounded rates |
| core size exactly `k-1` | gives both the `+1` in (SRC) and `d<=k-1` | replacing either by `k` shifts the sharp constants |
| maximal-source decomposition | gives `Mell+b=n-k+1` with `b<ell` | a nonmaximal selected subfamily need not satisfy the sieve |
| exact core defect | makes `D` a subset of the core | supersets or non-exact encodings are out of scope |
| full petals | identifies the strict `d>ell` residual and permits the mu-basis import | partial petals remain open |
| three touched petals for (BG) | invokes the one-projective-point lower branch | `t=2` is not paid by this clause |

## Sharpness and route boundary

The general inequality is deliberately `M<=r-2`. At `M=r-1`, examples with
`ell<=k` occur, so the conclusion `ell>k` is false. The rate-quarter constant
`ell+8` retains both the `+1` in `n-k+1` and the exact defect cap `k-1`.
Equality occurs. On the admissible integer lattice, the two cosmetic thresholds
`ell+7` and `ell+6` happen to be equivalent because `2b-ell` skips those
values; `ell+5` is the first genuinely false weakening.

The theorem removes impossible or one-projective-point cells only. It does
not prove that the surviving large-background upper branch is populated, nor
does it count that branch.

## Adversarial controls

The verifier exhausts integer source decompositions over all four official
rates and checks:

1. every `M<=r-2` row has `ell>=k+1`;
2. the rate-quarter upper-branch existence test is equivalent to
   `2b>=ell+8` including equality;
3. extending the source-scale claim to `M=r-1` fails;
4. replacing `d<=k-1` by `d<=k`, changing the core size, using a strict
   half-strip boundary, or weakening the background gate to `ell+5` changes a
   witnessed row.
