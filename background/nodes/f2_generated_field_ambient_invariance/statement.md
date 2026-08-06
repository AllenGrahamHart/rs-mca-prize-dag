# F2 generated-field ambient invariance

- **status:** PROVED
- **closure:** proof

Let `F=F_(p^e)`, let `B=F_p(mu_n)=F_(p^k)` with `k|e`, and let the
evaluation domain be `D=g mu_n` for some `g in F^*`. Scaling by `g^-1`
gives a canonical bijection between subsets of `D` and subsets of `mu_n`.
For every subset `S=gT` and every `j>=1`,

```text
sum_(x in S) x^j = g^j sum_(y in T) y^j,
e_j(S)           = g^j e_j(T).                         (AI-1)
```

Consequently this bijection preserves exactly:

1. `t`-null blocks in either the power-sum or elementary-symmetric
   formulation;
2. equality of the first `t` moments between two blocks;
3. size, complement, disjointness, and unions of cosets of every subgroup
   of `mu_n`; and
4. moment-trade and mixed-pullback block families, by substituting `X=gY`
   in their fiber polynomials.

For any window `W=gW_0` and exponent set `Lambda`, let

```text
A_D(a)=(sum_(x in W) a_x x^ell)_(ell in Lambda).
```

After identifying coordinates by `gx <-> x`,

```text
A_D = diag(g^ell)_(ell in Lambda) A_(W_0).             (AI-2)
```

The diagonal map is injective. Hence the `F_p` kernel, rank, ternary
weight enumerator, weighted mass `Z`, subset-syndrome fibers, their maximum,
and their collision sum are all unchanged by the ambient extension and the
domain coset.

For the 12 official degree/order types, the seven non-generating types
therefore descend exactly as follows:

```text
plus  (k=1,e=2,3,4,5,6) -> plus  (k=e=1),
plus  (k=2,e=4)         -> plus  (k=e=2),
minus (k=2,e=4)         -> minus (k=e=2).
```

Thus the final F2 extras-plus-trades count and the associated kernel-mass
problem on every official row reduce to the five signed generating types.
This does not restore the refuted ambient-normalized `(O1)` statement and
does not prove any mass upper bound or the final `n^3` budget.
