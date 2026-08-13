# Global-core rank/support/distance MCA router

- **status:** PROVED
- **closure:** exact composition of complementary global-core payments
- **scope:** one non-global-affine whole-line global-core family

## Statement

After whole-line global-core cancellation, write the shortened row as

```text
(N,K,m)=(R+s,s,d+s).
```

Choose a minimum direction lift `q=r_1-b`, put

```text
e=|supp(q)|=R-j,
```

and let `r` be the affine rank of the transformed selected explanations
`c_gamma-gamma b`.  The family is paid if any one of the following holds:

1. the codeword-direction rank envelope is at most the official budget;
2. the exact common-zero support envelope at `(K,r,e)=(s,r,e)` is at most
   the official budget; or
3. `j` lies in the recursive direction-distance paid prefix at dimension
   `s`.

These are three bounds on the same slope set after the same global
cancellation and gauge.  No addition of their budgets is involved.

## Exact deployed gates

For KoalaBear, throughout `14<=s<=4992`, every family with `r<=13` is paid.
For the first residual ranks, uniformly over that entire dimension range,

```text
r=14: e<=31768,   r=15: e<=1576,
r=16: e<=94,      r=17: e<=5.
```

Ranks `r>=18` receive no positive low-support prefix from this envelope.
Every rank is separately paid when

```text
e>=R-J_rec(s),
```

where `J_rec(s)` is the exact recursive frontier of the proved
direction-mismatch theorem.  At each displayed rank's first legal dimension
`s=r`, `J_rec=4330`, so the exact surviving support intervals are

```text
r=14: 31769..1044245,   r=15: 1577..1044245,
r=16:    95..1044245,   r=17:    6..1044245,
r>=18:    1..1044245.
```

For Mersenne-31, throughout `6<=s<=4979`, every family with `r<=5` is paid,
and

```text
r=6: e<=11847,   r=7: e<=646,
r=8: e<=36,      r=9: e<=2.
```

Ranks `r>=10` receive no positive low-support prefix.  The high-support gate
is again `e>=R-J_rec(s)`.  At each rank's first legal dimension `s=r`, the
recursive frontiers are `4334,4333,4332,4331,4330`.  The exact surviving
intervals are

```text
r=6: 11848..1044241,   r=7: 647..1044242,
r=8:    37..1044243,   r=9:   3..1044244,
r=10:    1..1044245.
```

The complete recursive frontier is deterministic from the pinned recurrence;
selected checkpoints are recorded in `source_contract.json`.

## Consequence

The former undifferentiated `GLOBAL_CORE_SHORTENED_S_GE_14` and
`LOW_DIRECTION_DISTANCE_GLOBAL_CORE` descriptions can be refined, on the
displayed deployed ranges, to an explicit middle-support/high-rank cell.
At KoalaBear `s=14`, for example, `r<=s` leaves only transformed rank `14`,
with support in exactly `31769..1044245`.

## Nonclaims

This does not pay any displayed middle interval, control dimensions beyond
the printed ranges, establish the active K3 first-match atlas, allocate a
K3 budget, or close a deployed row or prize.

## Falsifier

A selected family satisfying one printed gate but exceeding its official
budget, an incorrect rank/support wall or recursive checkpoint, or an
attempt to add bounds belonging to different selected families.
