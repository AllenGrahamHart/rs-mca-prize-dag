# Frontier — the open question this node poses

**For the e1 lane owner (Codex). This node proves a reparametrization; it does
not answer the scope question below, and does not claim the question is a
defect.**

## The question

The variance-descent campaign is indexed `e1_n256_s16_*`, i.e. square mass
`S=16`, and works folded profile `(3,4,0)` — the split `(a,b) = (3,4)`. Its
scope is inherited from the sentence in
`e1_prime_field_l2_norm_collision_radius`:

> In the first surviving `N=256` band, only folded profiles `(4,2,0),(3,4,0)`
> remain.

That is a statement about **band `s=5`**. The censuses are statements about a
**coefficient profile**. Those are different quantifiers, and by the
reparametrization the norm test does not see `s` at all.

At `S=16` the live splits are `(3,4)`, `(2,8)`, `(1,12)`, `(0,16)`, with
minimal bands `s=5,6,7,8`. Only `(3,4)` is worked. A text search of
`critical/` and `background/` finds **no occurrence** of `(2,8,0)`,
`(1,12,0)` or `(0,16,0)` in any form.

**So: are `(2,8)`, `(1,12)`, `(0,16)` at `S=16` excluded somewhere, or are they
open?**

Three possibilities, and we cannot currently distinguish them:

1. **Already excluded** by an argument we have not connected — e.g. a support-
   size or agreement bound that caps `b`, or a constraint from `ell'` (the
   quotient agreement size) that we have not located. If so, that argument
   should be cited in the descent's scope sentence, because as written the
   scope sentence does not cover them.
2. **Reducible** to the `(3,4)` census by a symmetry or transport we have not
   spotted.
3. **Genuinely open**, in which case the descent at `S=16` is one of four
   splits, and `S=18` and upward sit behind that.

## Why it matters before more compute

If (3), the accounting changes materially. "Seventeen variance levels remain at
`S=16`" becomes "seventeen levels remain in one of four splits at the smallest
of many admissible square masses". That is a different decision about whether
to buy another level.

## What would settle it, cheaply

- an upper bound on `b` (equivalently on the singleton count, equivalently on
  the `l_1` height `2a+b <= 2 ell'`) for pair-feasible rows: with `S = 4a+b >=
  15` this immediately bounds the split list and, with `S <= 2(2a+b) <= 4 ell'`,
  bounds the square-mass range too;
- or a citation showing `(2,8)`, `(1,12)`, `(0,16)` already dead;
- or an explicit statement that they are open, added to the descent's scope.

**We looked for `ell'` and did not find it pinned for this lane.** That is the
single number that would close this out, in either direction.

## Caveat on this node's own reliability

The coordinate identities `S = 4a+b`, `s = a + b/2 + c` are reconstructed from
the definitions in the pinned lemma; they are not quoted from it. They
reproduce all four pinned profiles' band indices and the full band-`s=5`
survivor set exactly, which is strong evidence the reconstruction is the
intended one — but a lane owner who knows the intended convention should
confirm it before acting on the scope question.
