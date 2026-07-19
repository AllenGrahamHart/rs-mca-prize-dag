# F2: the EFFECTIVE ENERGY DICHOTOMY (kernel-summit base camp)
# — printed-constant BSG/quasicube composition, aimed at the mildest
#   kernel instance (F2's sub-balance entropic suppression, ~2% margin)

Status: the COMPOSITION LEMMA is PROVED (self-contained, below). Its
two inputs are NAMED EXTERNAL THEOREMS (published additive
combinatorics), imported with symbolic constants and NOT assumed sharp
— the instantiation table prints the conclusion as a function of the
constants. Numeric layer machine-verified
(f2_effective_energy_dichotomy_modal.py: quasicube exhaustive d <= 4,
sampled families d <= 16, exact composition grid, exact F2 table).

Provenance: the mechanism is the unconditional half of the
Sidon/energy dichotomy in upstream's asymptotic proof
(experimental/asymptotic_rs_mca.tex, prop:no-high-energy). This packet
effectivizes it: no o(N), printed constants, consumable at finite rows.

## Pre-registration

Question: can the "no large high-energy Boolean fiber" mechanism be
stated with printed constants strong enough to bite at F2's official
rows (budget n^3 = 2^123 at prize-max)?

Success: a self-contained composition with the external inputs named
and symbolic; an exact instantiation table; an honest statement of
which branch of F2's obligation it closes.

Failure: assuming unpublished constants; letting the asymptotic o(N)
leak back in; claiming the accident count itself.

## External inputs (NAMED, not assumed)

QUASICUBE (Green–Matolcsi–Ruzsa–Shakan–Zhelezov, arXiv:2003.04077,
via Matolcsi–Ruzsa–Shakan–Zhelezov, arXiv:2003.04075): for finite
nonempty P, Q in Z^d and U inside {0,1}^d:
|P + Q + U| >= |P|^{1/2} |Q|^{1/2} |U|.
COROLLARY (P = -A, Q = {0}, U = A): every finite A inside {0,1}^d has
|A - A| >= |A|^{3/2}. Machine-checked exhaustively at d <= 4 (all
subsets; the inequality is tight at singletons) and on structured
families to d = 16.

BSG(c1, e1, c2, e2): if E(A) >= |A|^3 / K then some A' inside A has
|A'| >= |A| / (c1 K^{e1}) and |A' - A'| <= c2 K^{e2} |A'|.
Published exponent classes: (e1, e2) = (1, 4) (Schoen 2015-type) and
classical proofs with (e1, e2) up to (2, 5). Constants kept symbolic.

## COMPOSITION LEMMA (proved)

Let A be a finite subset of {0,1}^d with E(A) >= |A|^3 / K, and assume
BSG(c1,e1,c2,e2) and the quasicube corollary. Then

    |A| <= c1 c2^2 K^{e1 + 2 e2}.

Proof. BSG gives A' with |A'| >= |A|/(c1 K^{e1}) and |A'-A'| <=
c2 K^{e2} |A'|. A' inherits Booleanness, so the quasicube corollary
gives |A'|^{3/2} <= |A'-A'| <= c2 K^{e2} |A'|, whence |A'|^{1/2} <=
c2 K^{e2}, i.e. |A'| <= c2^2 K^{2 e2}. Then |A| <= c1 K^{e1} |A'| <=
c1 c2^2 K^{e1 + 2 e2}.

CONTRAPOSITIVE (the consumable form): if |A| > c1 c2^2 K^{e1+2e2}
then E(A) < |A|^3 / K. Equivalently, every A of size |A| forces

    E(A) < |A|^3 / K   for every K < K* = (|A| / (c1 c2^2))^{1/(e1+2e2)}.

Dimension-free: d never appears. No o(*) anywhere.

## F2 instantiation (exact, prize-max row n = 2^41, budget n^3 = 2^123)

Any family A of t-null blocks (indicators in {0,1}^n) EXCEEDING the
consumer budget |A| > 2^123 is forced to be energy-deficient:

    idealized-Schoen   (c1=c2=1,    e1=1, e2=4):  E(A) < |A|^3 / 2^13.67
    conservative-Schoen(c1=c2=2^10, e1=1, e2=4):  E(A) < |A|^3 / 2^10.33
    classical-safe     (c1=c2=2^10, e1=2, e2=5):  E(A) < |A|^3 / 2^7.75

Even under the weakest instantiation, a super-budget accident family
cannot carry additive energy within 2^7.75 of maximal. Contrast datum:
a full Boolean subcube of size 2^123 has E = |B|^{log2 6} =
|B|^3 / |B|^{0.415} = |B|^3 / 2^51 — comfortably inside the allowed
zone, so the lemma is consistent with the existence of structured sets;
what it forbids is the EXTREME-energy end (few-piece structures: a set
that is a union of c translates of a single set carries E >=
|A|^3 / c^2-type energy, so super-budget families with c <= 2^3.8
pieces are excluded outright under the weakest row of the table).

## What this closes / what remains for F2

F2's remaining obligation (statement: "entropic suppression — zero
accidents in the sub-balance regime; anti-concentration, same shape as
the dli RES count") now SPLITS in two named branches:

  (a) HIGH-ENERGY branch: CLOSED by this instrument with printed
      constants — any super-budget accident family is quantitatively
      far (>= 2^7.75, weakest row) from maximal additive energy; in
      particular the few-structured-pieces shape is dead.
  (b) LOW-ENERGY residual: rule out large additively-dissociated
      t-null families in sub-balance. This is the Fourier-flatness /
      major-arc-routing shape (upstream's C9 payment), and it is where
      the ~2% sub-balance margin must do its work. OPEN, now sharply
      posed.

Portability note: the same instrument applies verbatim to F5's
far-from-pencil heart (fibers of the pencil live-count map are Boolean
support families — see F5 P9, same day) and to F1's B-WEAK joint
budget. Branch (a) closes uniformly; each floor keeps its own (b).

## Replay

    ~/.venvs/modal/bin/modal run critical/nodes/u2c_giant_tnull_dichotomy/notes/f2_effective_energy_dichotomy_modal.py

Digest: F2_EFFECTIVE_ENERGY_DICHOTOMY_PASS.
