# Rank-eleven rank-nine split-pencil cell ledger

- **status:** PROVED
- **scope:** records routed by the component-star theorem to one fixed
  rank-nine ten-coordinate cell `B`

Let `u` span `ker(ev_B:V'->F^B)`. All affine codeword-pair owners which
agree with the received pair on `B` form one affine plane `Pi_B` with
translation directions `(u,0)` and `(0,u)`. Every record of slope `gamma`
assigned to this cell defines one line in that plane, with direction

```text
(-gamma*u,u).
```

Distinct record slopes give distinct line directions. Hence their owner
blocks form a pairwise-balanced design: if `t_p` is the number of record
lines through owner point `p`, then for `g` records

```text
sum_p C(t_p,2)=C(g,2).                               (1)
```

Let `J_B` be the coordinates in `Z(u)` where the whole owner plane agrees
with the received pair. Every owner core decomposes exactly as

```text
C_p=J_B disjoint_union P_p,
```

and the petals `P_p` are pairwise disjoint across owner points. Each record
has at least 45153 full-rank component extension coordinates, all lying in
petals of points on its line. Therefore

```text
45153*g <= sum_p t_p |P_p|.                          (2)
```

Fixed-owner exception disjointness gives `t_p<=981105`, while
`sum_p|P_p|<=n'-|J_B|<=2097152-10`. Consequently

```text
g<=ceil(981105*(2097152-10)/45153)=45567659.         (3)
```

Thus one fixed rank-nine split-pencil cell cannot carry a macroscopic
fraction of the unsafe residual. This does not bound the number of distinct
cells or select a chronology owner across cells.

## Falsifier

An owner agreeing on `B` outside the affine plane; equal directions for two
distinct slopes; two record lines with no unique intersection owner; a
coordinate outside `Z(u)` lying in two owner cores; failure of (1) or (2);
one owner owning more than 981105 slopes; or a fixed cell with more than
45567659 assigned records.
