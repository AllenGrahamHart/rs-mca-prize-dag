# Rank-eleven rank-eight owner-pair weight cap

- **status:** PROVED
- **scope:** one fixed rank-eight nine-subset in the typed affine-owner lane
- **units:** `(record, eleven-subset)` incidences

Put `n'=1048576+K'`. Fix a nine-subset `B` with evaluation rank eight and
let `U=ker(ev_B)`, so `dim U=2`. If `W_B` counts affine-owner component
eleven-subsets containing `B`, with extension multiplicity retained, then

```text
W_B <=981105*C(n'-9,2).                             (R8W1)
```

Every full-rank extension `T=B union {x,y}` determines at most one owner
pair in the affine `U^2` owner flat. Each fixed owner pair supports at most
`n'-m'+1=981105` selected records. Thus coordinate pairs, rather than
deduplicated records, pay the marked incidence unit.

## Nonclaim

The cap does not exploit the rank-three error form and does not by itself
pay rank eight for every shortening.

## Falsifier

One independent coordinate pair determining two owner pairs; one fixed
owner pair supporting more than `981105` selected records; one marked
incidence without a full-rank coordinate pair; or marked load above (R8W1).
