# DRAFT — scope questions for Przemek (2026-08-06, round-19 state)

STATUS: DRAFT, not sent. Channel candidates: comment on PR #1143 /
new upstream issue. User ratification required before sending.

---

Subject: Four scope questions — one explicit row now decides two of
our statements

Dear Przemek,

Our falsification-first campaign on the two grand challenges has
reached a point where the remaining mathematics splits cleanly on
four questions about the intended reading of the challenge family.
Three are definitional, one is a confirmation. None asks you to
review proofs — every factual claim below has a self-contained
verifier script in our public repo
(github.com/AllenGrahamHart/rs-mca-prize-dag, master @ a37290e5),
each running in about a minute. The questions are about intent.

**Q1 — the one that decides two statements: does the challenge
family include rows where the smooth domain does not generate the
field?**

The rules text we work from ("for every choice of F, L, and k";
|F| < 2^256; smooth domain a coset of a power-of-2-order subgroup;
k <= 2^40) admits rows q = p^e with e up to 6 at the maximal
rate-1/2 row n = 2^41. Consider the explicit row

    p = 6,597,069,766,657 = 3*2^41 + 1  (prime),  q = p^6,
    log2 q = 255.51 < 256,  2^41 | q - 1,
    ord_{2^41}(p) = 1 < e = 6   (the smooth domain generates F_p,
                                 not F_q).

On this row, machine-verified at full scale:

(a) the first-moment identity underlying our correlated-agreement
counting (the K1 window lane) fails by a factor exponential in n —
and the failure is generic to every admissible row with
ord_{2^41}(p) < e, which exist at every e in {2,3,4,5,6}
(verifier: notes/pilots_20260806/f2_adm/verify.py);

(b) the window-vanishing count at agreement offset w = 2^34
strictly exceeds the periodic/structural count: we exhibit an
explicit NON-periodic set S of size 2^40 - 2^34 in mu_{2^41} with
all 2^34 - 1 window power-sum conditions vanishing, verified
directly at n = 2^41, not extrapolated
(verifier: notes/pilots_20260806/crossing_low_w/prize_exhibit.py,
stage `verify`).

If such rows are INSIDE the intended family, both statements need
re-posing around these counterexamples. If the intended reading
restricts to generating rows (equivalently here, e = 1 / prime
fields at the top rate), the counterexamples vanish and our
positive results at prime rows stand as scoped. Either answer
unblocks us immediately.

**Q2 — a one-sentence definitional pin.** In the Newton-window
lane: is the deployed condition parameter t the LARGEST Newton
index in the window (so the odd-condition count is ceil(t/2)), or
the NUMBER of conditions (|Lambda| = t)? Five of our source
surfaces read it the first way, one the second; the factor 2
between them flips a proved necessary condition at the top rung, so
we currently carry both values everywhere.

**Q3 — the ensemble calibration.** For the K1 first-moment target
2^{n/2 + o(n)}: which block ensemble calibrates the condition
count — ALL 2^n subsets, or the fixed-size slice C(n, n-k-t) with
the 2^{-128} list gate? At generating rows the necessary condition
holds with exactly zero margin, so this choice — the two
calibrations differ by only 0.0044% in t — decides the statement's
truth outright: it survives under the full-subset reading and fails
by 2^{Theta(n)} under the slice reading. Per your rules-freeze
ambiguity clause we plan against the stricter reading, but this one
genuinely needs intent rather than convention.

**Q4 — confirmation at leisure.** The composition rule for the K1
average: we read the target as an average over K1; the sum reading
costs an extra n/2 bits exactly. We have adopted the SUM reading as
working convention (again per the stricter-reading clause) and
carry both pricings everywhere. Confirm or correct whenever
convenient.

One reconciliation heads-up, no action needed: the corridor-edge
constant t* = 8,592,912,739 in our radius-arithmetic lane
coincides exactly (as sigma* + 1) with the agreement excess your
mca-floor result proves unsafe on 1 <= sigma <= 2^34 - 1; the two
records now cross-reference each other in our tree.

Everything above is banked with full provenance in the public
repo's campaign ledger; happy to expand any item on request.

Best,
Allen (with the agent fleet)
