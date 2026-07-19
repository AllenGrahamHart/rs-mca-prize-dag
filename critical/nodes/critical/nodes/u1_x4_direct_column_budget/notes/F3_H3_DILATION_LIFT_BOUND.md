# F3 h=3 dilation lift bound

Status: PROVED NORMALIZATION COMPILER LEMMA, NOT `H3-ACT`.

This packet banks the normalization step used by the h=3 activation compiler.
The object `A_3(n,p)` is counted modulo common multiplication by `H=mu_n`.
The contribution bound uses `n*A_3(n,p)`.  That factor is an upper bound, not a
free-action assertion: some unordered pair shapes may have a side-swap
stabilizer, but no orbit can lift to more than `n` raw dilates.

## Pre-registration

Question:

```text
If A_3(n,p) counts non-toral activated h=3 shape pairs modulo common
multiplication by H, why is multiplying by n a valid raw-shape upper bound?
```

Success criterion:

- prove the group-action lifting inequality;
- explicitly allow side-swap stabilizers;
- replay the inequality on finite subgroup rows;
- keep this below the activation sparsity theorem.

Failure criterion:

- claim the dilation action is always free;
- ignore that `{P,Q}` is an unordered pair of sides;
- use the lemma as a proof of the normalized bound `A_3(n,p) <= Cn`.

## Lemma

Let `X` be any set of unordered h=3 shape pairs

```text
{P,Q},        P,Q <= H,  |P|=|Q|=3,  P cap Q = empty,
```

stable under common multiplication by `H`.  Let `X/H` be the quotient by this
action, where side swap is already built into the unordered pair notation.
Then

```text
|X| <= |H| * |X/H| = n |X/H|.
```

In particular, if `A_3(n,p)` is the number of dilation-normalized activated
non-toral h=3 shape-pair orbits, the number of unnormalized activated shape
pairs is at most

```text
n A_3(n,p).
```

## Proof

This is orbit-stabilizer.  Every orbit of the `H` action has size

```text
|H| / |Stab({P,Q})| <= |H|.
```

Summing this inequality over all quotient orbits gives the result.

The side-swap issue is harmless because `{P,Q}` is an unordered pair.  If some
`gamma in H` satisfies `gamma P=Q` and `gamma Q=P`, then `gamma` belongs to the
stabilizer of the unordered pair and the orbit is smaller, not larger.  Thus
the factor `n` remains a safe upper bound without needing a freeness theorem.

## Role in h=3

Together with the local fiber-count bridge, this justifies the normalization
part of the existing compiler:

```text
T_3 <= toral + poisson_boundary + n A_3(n,p).
```

It does not prove `A_3(n,p) <= Cn`; that remains the h=3 rank/bridge or
certificate problem.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_dilation_lift_bound.py
```

Expected digest:

```text
H3_DILATION_LIFT_BOUND_PASS
```
