# L1 FPC5 rate-half `M=4,t=3` split-slice payment

- **status:** TARGET
- **consumer:** `l1_full_petal_fpc5_payment`

At rate `1/2`, after the projective Johnson-positive cells are paid, the
three-touched-petal tail has

```text
N=4ell+b-2,       d=2ell-a,
b>=7,              1<=a<=floor((b-3)/4),
J=ell(4a-b+2)+a^2+2ab-4a<=0.
```

First-layout domination leaves four planted anchors and at most four touched
triples in one fixed maximal source layout. Each triple's three source labels
determine one normalized cross-ratio `lambda`; it is not a field-wide
summation parameter. For one fixed triple and defect, the cell is exactly

```text
{D monic : D|L_C, deg D=2ell-a,
            deg rem_(L_2L_3)(D Etilde)<=ell-a,
            gcd(D,rem_(L_2L_3)(D Etilde))=1}.       (LS6)
```

There are fewer than `4n` such `(triple,a)` cells. The target is therefore a
uniform polynomial/profile payment for one fixed guarded LS6 atom, strong
enough that its sum over these polynomially many cells is admissible. There
is no remaining source-layout or free-`lambda` composition problem. Bounding
the dimension of the ambient linear slice is not the conclusion.

For every nonempty atom, the proved master-flat descriptor injects its
candidates into an unpunctured full-domain split flat with

```text
j=2ell-a,       r=ell-2a+1,       j-2r=3a-2>=1,
gcd(P)=1,       binom(n,j)/Q^(j-r)<2^(-3ell-4),
```

where `Q` is the generated-field size of the descriptor.

Thus the live primitive issue is a sub-balance maximum-versus-average
split-flat bound. Pure multiplicative pullbacks are absent for odd `a`; the
even-`a` quotient and all dihedral strata still require owner-safe treatment.
Every nonempty atom also satisfies `deg Etilde>=a`. If the three touched
petal locators lie in one common pencil, affine source alignment makes
`Etilde` constant and misalignment forces a nonconstant common factor in
`D` and its remainder. Both cases are empty. The remaining branch is
therefore genuinely non-common-pencil.

Writing `e=deg Etilde`, the range `a<=e<=ell-a` is an exact prefix ladder:
it is the disjoint union of `Q_0^(e-a)` ordinary prefix cells of depth
`ell+e-1`, with effective average depth `ell+a-1` after cancellation. The
high-multiplier range `e>ell-a` has exact Pade quotient coordinates:

```text
D=quo_E((L_2L_3)Q),       V=-rem_E((L_2L_3)Q),
deg Q=e-a,                gcd(D,Q)=1.
```

If `F=E^(-1) mod L_2L_3`, every candidate also has
`D=rem_(L_2L_3)(FV)` and necessarily `deg F>=ell+a`. Thus the high branch
is a two-sided primitive rational-approximation cell, not an unstructured BC
flat. More generally every nonempty atom satisfies the source-only gate

```text
deg rem_(L_3)(L_1L_2^(-1))>=a;
```

failure is exactly a short syzygy between the three petal locators. Its split
maximum and quotient/dihedral owner transport remain open.

For any two distinct candidates, their primitive Pade quotients satisfy

```text
0!=D_1Q_2-D_2Q_1,       deg(D_1Q_2-D_2Q_1)<=ell-2a.
```

This determinant contains `gcd(D_1,D_2)` and separates candidates relative
to a fixed base. The induced root-intersection cap has Johnson denominator
exactly `J<=0`, so pairwise distance alone cannot close the target; the
remaining theorem must use split-root or owner structure.

The fixed-base determinant is now an exact coordinate, not merely an
injection. For one primitive base `(D_0,Q_0,V_0)`, every polynomial
`H` of degree at most `ell-2a` gives exactly one point of the complete monic
unguarded slice by

```text
R_H=rem_(D_0)(-H Q_0^(-1)),       D_H=D_0+R_H,
Q_H=(H+D_HQ_0)/D_0,              V_H=(D_HV_0-MH)/D_0.
```

All formal multi-determinant and Plucker identities therefore already hold
on the whole ambient slice and cannot supply a maximum bound. The guarded
atom is exactly the `H` subset for which `D_H` splits on the core and the
root-local primitive inequalities hold. This explicit split-root chart,
not abstract collective compatibility, is the remaining high-branch object.

The base overlap is now an exact canonical owner. For every non-base guarded
point, put

```text
G=gcd(D_0,H)=gcd(D_0,D_H),
D_0=GA,       D_H=GB,       H=GK.
```

Then `G,A,B` are pairwise coprime,
`K=AQ_H-BQ_0`, and primitivity is exactly
`gcd(K,B)=gcd(G,Q_H)=1`. At fixed `g=deg G`, candidate-only root sets have
pairwise intersection at most `h-g`, giving

```text
|F_G| <= floor(
  binom(2ell+a+b-2,h-g+1) / binom(2ell-a-g,h-g+1)).
```

In particular, if `g=h-c`, this is less than `3^(c+1)` per owner. The
fixed-owner top-overlap chambers are therefore paid. The unresolved content
is aggregation or chronology-valid transport across the potentially many
different owners `G`, together with the low-ladder prefix theorem.

## Round-23 diagnosis addendum (2026-08-07, coordinator-applied on replay: fpc5_diag)

**CLASSIFICATION: MYSTERY-HARD** (the master split-locator flatness
wall (MF), shared with the m4_t2 and large-source reds), with a
strictly harder ACCESS problem: the minimal live J <= 0 tail cell
is (ell,b,a) = (9,8,1) with binom(42,17) = 2.55e11 — provably
unreachable by any local census or chart enumeration, ever
(1,909,782 live cells for ell <= 400). The tightest of the three
consumer contracts: < 4n atoms means the PER-ATOM bound must beat
the global exponent by a full power of n.

**THE OWNER-QUALITY FINDING (measured at the off-tail cell
(4,1,1), q = 101, full 1,030,301-member chart enumerated exactly,
25 trials):** the atom matches its generic prediction to 2% (no
amplification); max core packing = 3 = EXACTLY the proved
Bonferroni cap from the pair-determinant overlap bound (the
instrument is tight); and the canonical-owner histogram puts the
MAJORITY of the atom (52.4%) at g = 0 — the single trivial owner
G = 1, where the fixed-owner packing charge 3^{h-g+1} is maximal.
The binding problem is OWNER-QUALITY AT G = 1, not owner-count:
the attack list's "coalesce the realized G strata" aims at
multiplicity, but one owner already holds the mass and the theorem
is worthless exactly there. (MEASURED at h = 2; larger h
untested.)

**Cheapest decisive probe:** the BASE-COVER NUMBER of the G = 1
stratum — how many bases D_0 cover every member at bounded
co-deficiency? O(1) => the fixed-owner theorem composes and the
atom is paid; growing => the route is dead. Computable from the
already-produced root-set data (a set-cover on 39-member atoms);
minutes. Also noted: the supplier's <= restated here as < (one
character); and the e/M/Q notation collisions across the
three-petal vs ladder nodes are a live hazard (e = 2d+1-3ell vs
deg Etilde). Source: notes/pilots_20260807/fpc5_diag/.

## Round-23b adjudication note (2026-08-07, coordinator-applied on replay: mf_wall_adversary)

The round-23 one-wall evidence is REPRICED under adversarial attack:
the statement-level (MF) shape-pun test FAILED its power control
(the PROVED rate-quarter sibling satisfies every (MF) clause with
better margins; the separating clause — over-determination
t*ell > N — is not part of (MF)), and the two quantitative handles
are WITHDRAWN as classification evidence (the cap-4 is
structure-specific — a random flat with identical parameters
reaches 5; the trivial-owner concentration is 92x its parametric
reference). Both remain valid node-level findings, and the cap-4
data is STRENGTHENED (exact, not sampled, at ell = 4, 5, 6 over
329 configs and three primes; the sharpened overlap cap ell-3
achieved tightly at every ell; the cap is soft — budget elasticity
+1..+4 core points — and stiffens with ell; the mechanism at
ell >= 5 is UNIDENTIFIED). The REPAIRED test (round-19 three
gates, METHOD = the-missing-theorem-is-the-same; passed all three
power controls incl. the PROVED-sibling hard control): the m4_t2
and m4_t3 reds SHARE ONE WALL at METHOD level — a
dimension-uniform max-to-mean bound for split locators in a
growing-dimensional flat (the anticode bound's exponent grows with
flat dimension). The same METHOD wall matches the PROVED
l1_rootfree_rational_q_projective_packing at its own open
d = Theta(n) regime and f_global_packing_step (identical formula,
identically named failure). The large-source red is UNDECIDED:
only 142/408 residual rows are even posable as flats; the other
266 await the t-petal overlap-cap lemma. Upstream
prob:capfr1-master-flatness has ZERO discriminating power as a
wall test (PROVED nodes are instances of it; (MF) is an instance,
not the same statement; a |B|^{-s} vs q^{-sigma} normalization
mismatch is unresolved). Source:
notes/pilots_20260807/mf_wall_adversary/ (coordinator-replayed).

**MYSTERY 7 MEMBERSHIP RATIFIED (2026-08-07, user):** this node is a
member of mystery 7, "the dimension-uniform split-locator
max-to-mean wall" (board of record: roadmap section 12, r5 update).

## Round-25 audit flag (2026-08-09, coordinator-applied: m7_complement_repose)

**The owner-quality finding's cell (4,1,1) is OUT OF THIS NODE'S
PARAMETER FAMILY, not merely "off-tail": all three admissibility
conditions fail there** (b=1 fails b>=7; the a-window
1<=a<=floor((b-3)/4) is empty at b=1; J=+19>0 —
coordinator-verified arithmetic). The Bonferroni-tightness claim
("max core packing = 3 = EXACTLY the proved cap") is therefore
made at a cell outside the family, and evaluating the node's own
fixed-owner bound there gives C(8,3)/C(7,3) -> 1 against a
measured 36-member atom — a further sign the cell is out of
domain. UNRESOLVED which of the two to repair: re-measure
owner-quality at an admissible cell (b>=7 forces ell large; exact
chart cost grows), or re-scope the finding as an off-family
structural analogue. FLAGGED, not resolved; the g=0
trivial-owner-majority phenomenon itself was independently
reproduced at the same cell in round 25 (91.6x the parametric
reference), so the finding's PHENOMENON is real even if its cell
is out of family. Source:
notes/pilots_20260809/m7_complement_repose/ (REPORT.md section 3).
