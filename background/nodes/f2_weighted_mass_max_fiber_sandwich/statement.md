# F2 weighted mass and heaviest-fiber sandwich

- **status:** PROVED
- **closure:** proof

Let `A:F_p^m -> V` be linear, let

```text
N(v)=#{S subset {1,...,m}: A 1_S=v},
M=max_v N(v),
Z(A)=sum_(eps in ker(A) intersect {-1,0,1}^m) 2^-wt(eps).
```

Then

```text
M^2/2^m <= Z(A) <= M.                               (MF-1)
```

If `A` has rank `d` and a max-fiber estimate for this syndrome map has the
normalized form

```text
M <= Lambda_Q * (2^m/p^d) + E_Q,                    (MF-2)
```

then, with no further loss,

```text
Z(A) <= Lambda_Q * (2^m/p^d) + E_Q.                 (MF-3)
```

Each `N(v)` is the output size of binary full-agreement list recovery in
one affine coset of `ker(A)`. Consequently, any uniform subexponential
max-fiber bound pays the weighted-mass terminal for both the plus-branch
GRS maps and the coupled minus-branch root-code maps.

This theorem is an exact interface. It does not prove `(MF-2)`, quotient
In particular, upstream `def:q-row-atom` bounds a first-match residual family
`P_Q(z)` at deployed adjacent rows, not `N(v)` as defined here. It can supply
`(MF-2)` only after a separate explicit map-and-owner transport theorem.

## Addendum (2026-08-07, wave-47 integration, coordinator)

The sentence at line 38 of the adopted statement is TRUNCATED
mid-clause (ends on "quotient") — it is a NONCLAIM FENCE; until
Codex supplies the completion, the fence is read in its widest
(most conservative) form: no claim about any quotient object is
made by this node.
