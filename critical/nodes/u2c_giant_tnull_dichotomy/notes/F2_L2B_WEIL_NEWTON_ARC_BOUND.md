# F2 campaign L2b': the WEIL–NEWTON ARC BOUND
# (uniform minor-arc estimate — supersedes the pre-registered
#  per-orbit arc-max plan with something stronger: uniform in lambda)

Status: PROVED (two lemmas + corollary, proofs inline; the Weil input
is the standard twisted-polynomial bound, cited) + machine-verified
(f2_l2b_weil_newton_modal.py, digest F2_L2B_WEIL_NEWTON_PASS).

## Pre-registration

Question: bound |E_b(lambda)| for every nontrivial arc lambda != 0 in
closed form, strong enough to make Fourier inversion non-lossy at
official row shapes for an explicit range of block sizes b.

Success: a proof whose only external input is the classical Weil bound
for multiplicatively-twisted additive character sums; exact machine
verification at the L1 rows (no violation at ANY arc); an exact-integer
reach table (which b are covered at official shapes).
Failure: any arc violating the bound (would refute the derivation);
silently claiming the mid-band b it does not cover.

## Lemma A (subgroup Weil bound, t = 2)

For lambda = (l1, l2) != (0,0) and f(x) = l1 x + l2 x^2:

    | sum_{x in mu_n} psi(f(x)) |  <=  2 sqrt(q).

Proof. 1_{mu_n}(x) = (1/m) sum_{chi in C_m} chi(x) (annihilator
decomposition, as in L2a), so the sum is (1/m) sum_{chi in C_m}
sum_{x in F_q^x} chi(x) psi(f(x)). Each inner sum is a Weil sum for
the nonconstant polynomial f of degree <= 2 < q twisted by chi:
|sum_{x != 0} chi(x) psi(f(x))| <= 2 sqrt(q) (Weil; for chi = eps it
is a quadratic Gauss sum minus the x = 0 term, <= sqrt(q) + 1 <=
2 sqrt(q); l2 = 0 cases are Gauss sums, <= sqrt(q) + 1). Averaging the
m bounds gives the claim. QED

## Key observation (dilation identity)

The r-th power sum of the phase system Omega(lambda) =
(psi(f_lambda(x)))_{x in mu_n} is

    p_r = sum_x psi(f_lambda(x))^r = sum_x psi(f_{r lambda}(x)),

i.e. p_r(lambda) = e_1(r * lambda): power sums are FIRST moments of
dilated arcs. For 1 <= r <= b < q and lambda != 0, r*lambda != 0, so
Lemma A gives |p_r| <= 2 sqrt(q) for every r in play.

## Lemma B (Newton majorization)

If a system of N unimodular phases has |p_r| <= M for r = 1..b, then

    |e_b|  <=  [z^b] (1-z)^{-M}  =  M(M+1)...(M+b-1) / b! .

Proof. sum_b e_b z^b = exp( sum_r (-1)^{r+1} p_r z^r / r ). The
exponential of a formal series is a positive-coefficient combination
of products of its coefficients, so termwise |p_r|/r <= M/r majorizes:
|e_b| <= [z^b] exp( sum_r M z^r / r ) = [z^b] (1-z)^{-M}. QED

## Corollary (the arc bound and the small-band fiber bound)

For EVERY lambda != 0 (generic, quotient, and linear arcs alike):

    |E_b(lambda)|  <=  W(q,b) := prod_{r=0}^{b-1} (2 sqrt(q) + r) / b! .

Hence by Fourier inversion, at every row and every block size b:

    N(0)  <=  C(n,b)/q^2  +  W(q,b),

and by the PROVED complementation lemma the same bound covers n - b.
At sub-balance cells C(n,b)/q^2 <= 1, so the t-null census at block
size b is <= 1 + W(q,b) — POLYNOMIAL-SIZED whenever W(q,b) is.

## Honest reach (what this does NOT do)

W(q,b) ~ (2 sqrt q)^b / b! beats C(n,b) ~ (n/b)^b-scale precisely when
b log(2 sqrt q / b-ish) is small against b log(n/b): strong for
b << sqrt(q), useless at the window peak b ~ n/2. With
complementation, the COVERED band is b <= b*(q,n) and b >= n - b*,
where b* = max{b : W(q,b) <= budget} — printed exactly per row by the
verifier. THE MID-BAND REMAINS OPEN and is where L3 must work
(Parseval/SP route + the banked energy dichotomy). This rung converts
F2's branch (b) from "all block sizes" to "the mid band", with exact
boundaries.

## Replay

    ~/.venvs/modal/bin/modal run critical/nodes/u2c_giant_tnull_dichotomy/notes/f2_l2b_weil_newton_modal.py

Digest: F2_L2B_WEIL_NEWTON_PASS. Gates: (a) |e_1(r lambda)| <=
2 sqrt(q) for ALL lambda != 0, r <= b, at every test row (exhaustive);
(b) |E_b(lambda)| <= W(q,b) at every arc of the L1 cells (exhaustive);
(c) N(0) <= C(n,b)/q^2 + W(q,b) at every cell; (d) exact-integer reach
table b*(q,n) at official-shaped rows.
