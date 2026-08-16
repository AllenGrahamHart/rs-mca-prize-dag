# Attack

## Direct falsification

At small fields, enumerate five-dimensional polynomial subspaces after
factoring a fixed common locator. Record only squarefree sections whose roots
lie in the evaluation domain, reconstruct the corresponding rank-three and
rank-four flats, and deduplicate minimal circuits before applying weights.
Scale the observed saturation mass against the exact bound, not against the
number of coefficient vectors.

## Proof routes

1. **Rich-flat transversality.** Adapt upstream PR #1173's ordered-basis
   router to hyperplane sections of the residual evaluation columns. Route a
   nontransverse section recursively to a rich proper flat.
2. **Split-pencil census.** Classify degree-34 common cores of residual
   two-spaces, then count the degree-35 sections extending them.
3. **Exchange compression.** Compare saturated root sets by one-root
   exchanges; repeated fibers should either share a rich lower flat or pay a
   collision loss.
4. **Weighted coupling.** Use one census for both supports instead of proving
   separate uniform completion drops, which exact arithmetic shows are
   stronger than necessary.

The first small-scale task is to search for a representable flag exceeding
the normalized `(K72-SC)` ratio. Any such witness changes the proof route; it
does not refute the two proved supplier nodes.
