# D5 — WEAKEST-FORM RE-POSE (draft, round 21, floor-campaign style)

Draft only. No status flip proposed here; this is the re-pose the diagnosis
supports, with pre-registered falsifiers attached to each floor.

## Setting (fixed once)

`N'` a 2-power; `R = Z[zeta_{N'}] = Z[x]/(x^h + 1)`, `h = N'/2`;
`lambda = 1 - zeta` the unique prime over 2 (2 is totally ramified,
`(2) = (lambda)^h`).

`C(N')` := the set of `e_1` values of half-size (`|B| = N'/2`) subsets
`B ⊆ mu_{N'}`. Coordinatewise `C(N')` is exactly the set of
`v in {-1,0,1}^h` with an EVEN number of zero coordinates
(`|C(N')| = (3^h + 1)/2`); differences therefore lie in `{-2,...,2}^h`.

`POW2(d)` := `1` iff `|Norm_{R/Z}(d)|` is a power of 2. Equivalently
`(d) = (lambda)^v`, i.e. `d` is a unit times a power of `lambda`.

## FLOOR-GE — the 2-adic generator ceiling

    L_2adic(N') := max { |F| : F ⊆ C(N'),  POW2(f - f') = 1 for all f != f' in F }

**FLOOR-GE.** `L_2adic(N') = N' + 1` for every 2-power `N' >= 8`.

Evidence banked by this pilot:
- **Upper bound, exhaustive**: exact max-clique (greedy-coloured branch and
  bound) over the full POW2 Cayley graph gives `L_2adic(8) = 9` and
  `L_2adic(16) = 17`. `N' = 32` is beyond exhaustive enumeration
  (`5^16` difference box).
- **Lower bound, constructive at every `N'`**: `{0} u {x^r c : r}` with
  `Norm(c)` a 2-power is a POW2 clique of size `N' + 1`, verified at
  `N' = 8, 16, 32`. The canonical `c` is `1 + x` (`Norm = 2`).
- **Extension probe at `N' = 32`**: 240,000 sampled centers, 0 extend the
  canonical clique; 12,800 cross-orbit members, 1 clears even 2 of the 33
  constraints.

**Pre-registered falsifier.** Exhibit, at any 2-power `N' <= 64`, a set of
`N' + 2` elements of `C(N')` whose pairwise differences all have 2-power
norm. Protocol: seed with `{0} u orbit(1+x)` and attempt extension by
(i) exhaustive search at `N' <= 16`, (ii) sampled + lattice (BKZ) search for
`y` with `y` and every `y - x^r(1+x)` an associate of a power of `lambda` at
`N' = 32, 64`. One exhibit kills FLOOR-GE.

## COROLLARY GE-SUPPORT — what the cap is actually about

Every base in the banked certified set
`G = {zeta, 1 + zeta} u {zeta^k - 1 : 1 <= k < N'}` has 2-power norm
(verified exhaustively at `N' = 8, 16, 32`: norms `{2, 4, 16, 256, 65536}`).
Units have norm `±1`. Hence every element of `U * <G>` has 2-power norm, and

    any base set whose elements ALL have 2-power norm certifies at most
    L_2adic(N') centers -- INDEPENDENT of how many bases there are.

So `poly(N')` is **not** the binding constraint. The binding constraint is the
NORM SUPPORT of the base set. Template compression rearranges templates inside
the same 2-adic class and therefore cannot move the ceiling.

## ESCAPE-GE — the only way out, and why the named carve-out does not take it

**ESCAPE-GE.** A certified family of size `> N' + 1` must use at least one
base whose norm has an odd prime factor.

`profile_covering_obstruction` names one FREE class: "(integer) x (small
element) differences are self-certified". For `e_1` differences of half-size
subsets that carve-out is **empty beyond the 2-adic class**: a difference has
coefficients in `{-2,...,2}`, so an integer factor `m >= 3` would force every
coefficient into `{0, ±m}` with `|m| <= 2` — impossible. Hence `m in {1, 2}`,
and `2` is an associate of `lambda^h`. Verified over sampled difference pairs
at `N' = 8, 16, 32`: max integer factor `= 2` throughout.

**Pre-registered falsifier.** Exhibit half-size `B, B' ⊆ mu_{N'}` with
`e_1(B) - e_1(B')` divisible in `R` by an integer `m >= 3`. (This is refuted
by the coefficient argument above, so the falsifier's real target is the
*broader* flat-profile class: exhibit a certified base with an odd-prime norm
factor whose profile is flat.)

## GE-WEAK — the re-posed consumer obligation

The chain's demand is hard-thresholded per row
(`certified_valueset_lower/conditional.md:24`: `|{e1(B) mod p}| > B*`), with
`B* = floor(q/2^128)` and a free clique of `~2^33`, i.e.

    required centers = B*/2^33 = q/2^161 .

A certified family of size `2^m` decides exactly the rows with `q < 2^{m+161}`
("partial designs = proportional window fractions").

**GE-WEAK.** For each prize row it suffices to establish EITHER
- **(a)** a family of `>= q/2^161` pairwise `e_1`-distinct centers with
  poly-certified differences (the original construction), OR
- **(b)** `K_p` contains no ternary vector of support `<= 2l'` beyond the
  cyclotomic relations (`lattice_cone_certificate`).

FLOOR-GE prices (a): for any 2-adic base set it yields at most `129 = 2^7.01`
centers, decides only `q < 2^168.01`, and therefore decides **no prize row**
(the rows sit at `q ~ 2^250`). The 82-bit deficit is a CEILING for that class,
not a shortfall to be closed.

**Recommended re-pose.** Retire (a) as the node's route, keep it only as
FLOOR-GE (a falsifiable floor with the escape condition named), and make (b)
the node's obligation.

## What (b) costs — the pricing that goes with the re-pose

Per-row MITM `= C(N', w/2) * 2^{w/2}`: `w=12 -> 2^38.3`, `w=14 -> 2^43.5`,
`w=16 -> 2^48.4` (reproduces the banked C-4 numbers), but the full radius
`w = 2l' = 128` costs `2^188.2`. So MITM extends the certified radius and can
never close the cone; the cone/dual bound is the residue
(`integer_code_distance_cert`, TARGET). Two hard pricing facts:
1. **Memory, not time, binds**: a plain MITM table at `w=16` holds `2^48.4`
   entries, ~`2^18` over the 1.5 GB per-row ceiling. Streaming/sorted variants
   are required before any Modal claim.
2. **The row set is not finite**: "There is no hidden finite registry of
   official row primes" (`integer_code_distance_cert/statement.md:16-20`).
   Per-row certification is Modal-scale for a PINNED row and is not a closure
   strategy for the universal claim unless the whole route is exhibit-scoped.
