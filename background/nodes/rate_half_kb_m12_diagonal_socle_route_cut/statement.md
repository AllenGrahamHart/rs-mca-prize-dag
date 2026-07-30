# KoalaBear m12 diagonal-socle route cut

- **status:** PROVED
- **scope:** inner-degree-12 transverse branch of KoalaBear `Q=6,s=6,u=2`
- **dependency:** `rate_half_kb_m12_outer_subdegree_route_cut`
- **consumer:** `rate_half_band_closure`

Let `G` be the geometric monodromy of the degree-60 composition
`f=F composed h`, with five outer blocks of size twelve, let `N` be the
kernel of the action on the blocks, and let `S` be the nonabelian simple
socle of the terminal primitive degree-12 inner monodromy. Then

```text
D=[N,N] <= S^5
```

is a subdirect product. Scott's lemma and the primitive degree-five block
action force exactly two possibilities: `D=S^5`, or `D` is one full twisted
diagonal copy of `S` across all five blocks. The actual non-same-fiber
suborbit has size four, so the independent product is impossible. Thus `D`
is full diagonal.

The six terminal degree-12 groups are

```text
M11, M12, PSL(2,11), PGL(2,11), A12, S12,
```

with socles `M11`, `M12`, `PSL(2,11)`, and `A12`. In the degree-12 actions,
a socle point stabilizer has orbits `1,11`. The only inequivalent cross-
action is the pair of `M12` degree-12 actions exchanged by its outer
automorphism; there an `M11` point stabilizer is transitive, with orbit
length `12`.

Consequently, a size-four suborbit meeting an outer block contains at most
one point from that block, namely the unique diagonal-corresponding point.
Its block projection therefore has size four. Of the two previously live
types, only

```text
(r,delta)=(4,12)                                   (KBD-1)
```

survives; the `r=2` Dickson type is impossible. In the `M12` socle case all
five block actions must be in the same degree-12 action class.

This does not delete any of the five `r=4` branch profiles, impose the
canonical-pencil/source-star incidence, construct an owner, move the ledger,
close `m=12` or `u=2`, establish cap `68`, or close the KoalaBear row.

## Falsifier

A terminal degree-12 primitive group outside the six-row catalogue, a
nontrivial block kernel whose derived projection misses the simple socle, a
Scott strip partition not preserved by the block action, an `M12` cross-
action orbit shorter than twelve, or a size-four transverse suborbit with
two-block projection.
