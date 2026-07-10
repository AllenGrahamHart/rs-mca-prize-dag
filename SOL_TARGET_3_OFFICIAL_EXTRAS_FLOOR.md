# TARGET 3 — THE GUARDED OFFICIAL EXTRAS FLOOR. Prove or falsify.

This is the load-bearing conjecture of the finite prize (DAG node
u2c_giant_tnull_dichotomy's floor), posed with every guard explicit.
It survived 1,440 norm-engineered adversarial trials, exhaustive
censuses, and nine falsification rounds in-repo; the constructions
that killed weaker faces (char-p index redundancy; complement
double-counts; mis-centered struct) are all excluded below BY
HYPOTHESIS — a falsifier must beat the guarded form.

## Setup

F a finite field of characteristic p, D = mu_N <= F^x with N a power
of two, t >= 1. Let B0 = F_p(D) (the generated field). Call an index
i P-FREE if p does not divide i, and let t* = #{p-free i <= t} (the
EFFECTIVE conditions; char-divisible indices are redundant:
p_{pi} = (p_i)^p). SUB-BALANCE HYPOTHESIS (required):
|B0|^{t*} >= 2^N. For a subset B of D let p_i(B) = sum_{x in B} x^i.
Call B t-NULL if p_i(B) = 0 for all p-free i <= t. STRUCT = the
unions of mu_M-cosets with M > t (all t-null; exactly countable;
level-dependent — at 2-power N the char-0 census is unions of
mu_{M_t}-cosets, M_t the least 2-power exceeding t). EXTRAS =
t-null non-struct subsets. Complements: D minus a t-null set is
t-null; counts below are TWO-SIDED (the full band, or equivalently
2 C_< + C_= over sizes b in [t+16, N/2]).

## The conjecture

At every row satisfying the hypotheses with official shape
(N ~ 2^41, p ~ 2^31, |B0| = p^k, t* ~ 7e10 — and any scaled family
of such rows), the TOTAL two-sided extras count over the band
t + 16 <= b <= N - t - 16 satisfies

    #EXTRAS <= N^3.

## PROVE OR FALSIFY.

Pre-registered falsifier form: a family of guarded rows (sub-balance
in the p-free effective sense, generated-field normalized) at 3+
growing scales with #EXTRAS > N^3, by exact count. Known ground
truth (exact, in-repo verifiers): zero extras at every measured
sub-balance point (five exhaustive N=32 primes: 601M subsets each,
700 struct blocks, 0 extras; MITM sweeps through the transition;
the deep-regime exactness theorem proves extras = 0 for almost all
q >> 2^N at fixed j). The proved bands: sizes <= t and >= N - t are
EMPTY of t-null sets; the edge band (t, t+15] has zero extras
(six-link proved chain); near-tails contribute < 2^122 two-sided.
What is NOT assumed: no per-level factorization, no uniformity in
anything unstated, no worst-case-over-words quantifier (the count
is a census). Do not attack: char-divisible index redundancy
(excluded by t*), unbalanced rows (excluded by hypothesis),
mis-centered struct (level-dependent by definition above),
complement double-counts (the count is defined two-sided).
