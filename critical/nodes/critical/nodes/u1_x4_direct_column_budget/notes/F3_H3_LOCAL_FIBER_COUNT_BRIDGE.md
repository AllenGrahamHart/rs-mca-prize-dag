# F3 h=3 local fiber-count bridge

Status: PROVED LOCAL COUNTING BRIDGE, NOT `H3-ACT` AND NOT
`H3-BRIDGE-RANKCAP`.

This packet pins the local multiplicity between h=3 triples, ordered conic
points, and activated pair counts at a fixed `(e1,e2)` value.  It is a small
bridge-side lemma: it does not prove that the global activated shapes batch
into the rank-capacity budgets, but it removes a counting ambiguity that the
future bridge theorem must respect.

## Pre-registration

Question:

```text
For fixed elementary data (s1,s2), what is the exact relation between:
  unordered 3-subsets P <= H with e1(P)=s1, e2(P)=s2;
  ordered same-fiber triples (u,v,w) in H^3;
  unordered activated pairs of distinct triples with that same (s1,s2)?
```

Success criterion:

- prove the factor-six relation for distinct h=3 subsets;
- express local activated pair count as `binom(N,2)`;
- replay the identity on finite subgroup rows;
- avoid claiming any global dilation-normalized bound.

Failure criterion:

- count ordered triples as activated pairs;
- ignore the pairwise-distinct condition;
- treat the local identity as the geometric batching theorem.

## Statement

Let `H` be a finite subgroup of a field, and fix `(s1,s2)`.  Define

```text
N(s1,s2) =
  #{ unordered 3-subsets P <= H : e1(P)=s1, e2(P)=s2 }.
```

Define the ordered same-fiber count

```text
R(s1,s2) =
  #{ (u,v,w) in H^3 :
       u,v,w pairwise distinct,
       u+v+w=s1,
       uv+uw+vw=s2 }.
```

Then

```text
R(s1,s2) = 6 N(s1,s2).
```

Consequently the number of unordered pairs of distinct triples with the same
`(s1,s2)` is

```text
P(s1,s2) = binom(N(s1,s2), 2)
         = R(s1,s2) (R(s1,s2)-6) / 72.
```

In conic coordinates, with `a=-s1` and `b=s2`, the ordered triples are exactly
the pairwise-distinct points

```text
u,v in H,
G(u,v)=u^2+uv+v^2+a(u+v)+b=0,
w=-a-u-v in H.
```

## Proof

Every unordered 3-subset `{x,y,z}` with elementary data `(s1,s2)` has exactly
six orderings `(u,v,w)`.  Each ordering is pairwise distinct and satisfies the
two displayed elementary equations.  Conversely, any ordered triple counted by
`R(s1,s2)` is pairwise distinct, so forgetting the order gives one unordered
3-subset counted by `N(s1,s2)`.  These two maps are inverse up to the six
permutations of a 3-element set, proving `R=6N`.

The activated local pair count is then just the number of unordered pairs of
distinct triples in that same fiber ledger, namely `binom(N,2)`.

The conic form follows by putting `a=-s1`, `b=s2`, and
`w=s1-u-v=-a-u-v`; then

```text
uv+uw+vw
  = -u^2-uv-v^2-a(u+v),
```

so `uv+uw+vw=b` is equivalent to `G(u,v)=0`.

## Role in h=3

This gives the exact local multiplicity that any h=3 bridge theorem must pay.
It supports the chain:

```text
same-(e1,e2) triples -> conic H-points -> activated local pairs.
```

It does not prove that the total dilation-normalized activated pairs satisfy
`A_3(n,p) <= Cn`, and it does not bound the rank-effective capacity consumed by
the corresponding conic charts.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_local_fiber_count_bridge.py
```

Expected digest:

```text
H3_LOCAL_FIBER_COUNT_BRIDGE_PASS
```
