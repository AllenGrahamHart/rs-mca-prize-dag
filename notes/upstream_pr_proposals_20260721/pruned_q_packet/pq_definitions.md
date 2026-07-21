# pq_definitions: verbatim upstream definitions for the pruned-Q toy packet

Pins: upstream rs-mca @ origin/main = 18cfc199 (local checkout adds only our PR #1010
commit; none of the files quoted below are touched by it). All line numbers below are
against that checkout. Date: 2026-07-21.

## 1. The target problem, verbatim

`experimental/grande_finale.tex` L3574-3580:

> \begin{problem}[Row-sharp multilevel Q target]\label{prob:row-sharp-q}
> For each active row, after every earlier first-match cell has been removed, prove
> \[
>  \max_z|\mathcal P_Q(z)|\le R_Q^{\rm row}\binom n{a_+}|\B|^{-(a_+-K)}
> \]
> with the literal row constant $R_Q^{\rm row}$ fitting the remaining integer budget.
> A moment proof must use the actual residual mass and satisfy
> \eqref{eq:finite-moment-criterion} with the allocated bit margin.
> \end{problem}

The quantity bounded: the max over prefix targets z of the size of the *residual*
(post-pruning) prefix fiber family P_Q(z) ⊆ Fib_w(z). The bound form: constant
R_Q^row times the average full-slice fiber C(n,a_+)|B|^{-w}, w = a_+ - K.

The atom form, `experimental/grande_finale.tex` L3414-3430 (`def:q-row-atom`):

> Fix a deployed adjacent row, let \(a_+\) be its adjacent agreement, let \(K\) be
> the list dimension used on that route, and put \(w=a_+-K\).  For a first-match
> residual prefix-boundary family \(\mathcal P_Q(z)\subseteq\Fib_w(z)\), define
> \[ R_Q^{\max} = |\B|^w\max_z\frac{|\mathcal P_Q(z)|}{\binom n{a_+}}. \]
> The row-sharp Q atom bound with bit margin \(\Delta_Q\) is \(R_Q^{\max}\le 2^{\Delta_Q}\).
> ... Any non-Q cell paid in the same first-match ledger only decreases the
> available \(\Delta_Q\).

Row parameters it ranges over: the four active adjacent rows (`prop:q-exact-target`,
L3432-3452), n = 2^21, K = k+1 = 1048577 (MCA route) / K = k = 1048576 (list route),
w ∈ {67471, 67447}; full-budget ceilings B*/⌈C(n,a_+)|B|^{-w}⌉ =
4807520.9295 / 4226236.5253 / 9.5722 / 8.4152. Binding case (L3451):

> Thus the binding Q problem is the Mersenne-31 list row: after all first-match
> payments, the remaining primitive prefix-boundary atom must be at most about
> \(8.42\) times its average size, and less if any other cell consumes budget.

and L3546 (`sec:finite-q-barrier`):

> The Mersenne-31 list row is the binding case: before any other cell is paid, its
> maximum-prefix-fiber overhead may be at most $8.4152$ times the full-slice
> average.  A first-match payment elsewhere only decreases that allowance.

Residual mass in a moment proof (`prop:q-moment-order-floor`, L3464-3477):

> Let \[ \tau=\frac{\sum_z|\mathcal P_Q(z)|}{\binom nm}\in(0,1] \] be the mass of
> the pruned residual relative to the full support slice.  A proof based only on
> the moment criterion of \cref{thm:moment-q} must satisfy the necessary condition
> \[ r\bigl(\Delta_Q-\log_2\tau\bigr) \ge w\log_2|\B| . \]

and L3489:

> After first-match pruning, the displayed row floors remain applicable only when
> \(\tau=1\); otherwise the residual mass must be carried explicitly, or one must
> use an off-diagonal or falling-factorial moment or isolate sparse-heavy fibers
> as a separate cell.

## 2. First-match semantics and the cell ledger

### 2a. The semantics (what "removed" means)

`experimental/grande_finale.tex` L1842-1849:

> The three words in \emph{primitive first-match residual} have separate content.
> ``First match'' means that a slope is removed as soon as one of its witnesses
> occurs in an earlier ordered cell; ``residual'' means that only witnesses
> surviving those removals remain; and ``primitive'' means that the row-specific
> quotient, planted, field-descent, rank, and ray-saturation certificates named by
> the atlas have all been applied.

L1895: "Deleting earlier cells can only decrease every fiber."
L1773: "A first-match residual only deletes supports from a full-slice fiber."

### 2b. The deployed-row cell list (and order)

`experimental/grande_finale.tex` L3561 (`sec:exact-completion-ledger`):

> $U_{\rm paid}$ is the exact first-match sum of tangent, common-support, quotient,
> planted, field-drop, extension, rank, and already certified cells; $U_Q$ is the
> row-sharp pruned prefix maximum; ...

`experimental/grande_finale.tex` L3184 (`cor:bc-one-pencil` hypothesis names the
branch order for BC charts): "after the first-match tangent, common-support,
quotient, extension, degree-drop, and common-GCD branches have been removed".

Ordering at atlas level is a FIXED BUT ARBITRARY choice, L1283-1284
(`thm:canonical-partial-occupancy-atlas`): "order these cells arbitrarily.  Then
they form a witness-exhaustive first-match atlas".

Sidon-cell positioning, L2218-2221:

> The first-match order is: algebraic major arcs first, then a separately
> certified Sidon/Fourier cell, and only then the high-energy primitive inverse
> step.  Naming a large low-energy fiber a cell does not pay it.

### 2c. THE AMBIGUITY, honestly stated (scope decision)

His text defines the deployed-row cell names (tangent, common-support, quotient,
planted, field-drop, extension, rank, ...), but gives NO toy-scale instantiation
of most of them: for the bare subset toy on a subgroup D ⊆ F_p^* (his census
object, §3 below), "tangent / common-support / planted / field-drop / extension /
rank" refer to locator-polynomial and field-descent structure that his text never
maps onto (p, N, m, w) census rows. The ONLY first-match membership tests he has
himself instantiated at toy scale are the two "quotient-pullback classifiers" in
his own script `experimental/scripts/qsp_modeatnull_structure.py` L20-23:

>     coset-union members (unions of mu_2-antipodal pairs): 0
>     dilation-stable members (gS = S for some g != 1):     0
>
> so the fiber is not charged by the obvious quotient-pullback classifiers.

with code (same file, L55-61):

>     def is_pair_union(S):
>         Ss = set(S)
>         return all((P - x) % P in Ss for x in S)
>
>     def dilation_stable(S):
>         Ss = set(S)
>         return any(all((g_ * x) % P in Ss for x in S) for g_ in D if g_ != 1)

and the matching prose in `experimental/notes/rowsharp_q_external_calibration.md`
L69-70 ("0 members are coset unions (unions of antipodal mu_2-pairs), 0 members
are dilation-stable") and L49 ("the (−1)-dilation pullback class").

SCOPE CONSEQUENCE (per the honest-scope rule): the packet prunes EXACTLY these
two cells, in his script's order (coset-union first, then dilation-stable), labels
the ledger "his own in-tree toy quotient-pullback classifiers, applied by us in
first-match order", and FLAGS that the remaining deployed-row cells have no
in-tree toy instantiation (they are reported as not-instantiated, not silently
assumed empty). Two structural facts make this scope robust:

- coset-union ⊆ dilation-stable whenever -1 ∈ D (g = -1 realizes S = -S); all
  rows below have N even, so the CUMULATIVE residual after both cells equals
  {S : gS ≠ S for every g ∈ D \ {1}} — the trivial-multiplicative-stabilizer
  ("primitive" in the natural toy sense) subsets;
- the residual after removing a UNION of cells is independent of the first-match
  order (order only re-attributes the removed mass between cells), matching
  L1283-1284's "order these cells arbitrarily".

## 3. His toy-row census conventions

`experimental/scripts/qsp_fiber_census.py`:

- Row tuples (L33-39): fiber jobs (p, N, m, w) ∈ {(17,16,8,1..3), (41,20,10,1..3),
  (257,64,34,1..2), (101,50,25,2..3), (577,96,48,2), (1153,128,64,2)}.
- Object (docstring L4-8): "Full fiber histogram of the depth-w power-sum prefix
  map on m-subsets of the order-N subgroup D of F_p^* (Newton-equivalent to the
  elementary-symmetric prefix map for w < p: identical fibers). Reports max fiber,
  null fiber, mean, and the exact second moment sum_z N_w(z)^2 (= C(n,m) + total
  shift-pair mass, thm:capg-second-moment)."
- D construction (L46-51): D = the order-N subgroup generated by g^((p-1)/N), g a
  primitive root.
- Checksum standard (L86): assert sum_z N_w(z) == C(N,m).
- Output standard (L138-142): lines of the form
  `fiber (p,N,m,w) EXACT: max/mean-1 = ..., null/mean-1 = ..., max = ..., null = ...`
  with mean = C(N,m)/p^w.
- Second-moment identity: `experimental/grande_finale.tex` L3117
  (eq:imported-second-moment): sum_z N_w(z)^2 = C(n,a_+) + sum_e P_e.

Exact committed anchors, `experimental/data/rowsharp_q_external_calibration.json`
(exact_int64 rows):

| (p,N,m,w)      | max              | null             | sum N^2 |
|----------------|------------------|------------------|---------|
| (17,16,8,1)    | 758              | 758              | 9743348 |
| (17,16,8,2)    | 54               | 54               | 574020  |
| (17,16,8,3)    | 7                | 6                | 38356   |
| (41,20,10,1)   | 4516             | 4516             | 832556056 |
| (41,20,10,2)   | 133              | 66               | 20390226  |
| (41,20,10,3)   | 11               | 6                | 744166    |
| (101,50,25,2)  | 12392018052      | 12392018052      | 1566477935492737080014204 |
| (257,64,34,1)  | 6304622609083424 | 6304622609083424 | 10215304424390627411534790353735040 |

Mode-at-null datum (`qsp_modeatnull_structure.py` asserts, L75-76): at
(41,20,10,2): null = 66, max = 133 at z = (11,0); dilation orbit uniform [133];
argmax-fiber classifier counts 0 (coset-union) and 0 (dilation-stable).

Printed-paper anchor, `tex/cs25_cap_v13_2.tex` L6325 `rem:capff1-collision-gap`
(table paragraph L6334): "max-to-mean ratios $1.0012,\ 1.21,\ 2.67$ at depths
$1$--$3$ for $(p,N,m)=(17,16,8)$; $1.0022,\ 1.21,\ 4.10$ for $(41,20,10)$; ...
maximum $11$ against mean $2.7$ over $41^3$ cells, matching the Poisson tail".
Four-decimal versions in `experimental/notes/rowsharp_q_external_calibration.md`
L26-30: "1.0012 / 1.2126 / 2.6722 at (17,16,8), depths 1–3; 1.0022 / 1.2101 /
4.1034 at (41,20,10); Poisson row max 11 vs mean 2.68; 1 + 2.5e-12 and
1 + 6.9e-9 at (257,64,34), depths 1–2".

## 4. The assignment being answered, verbatim

`agents.md` L518-519 (Good first PRs, item 1):

> 1. Write a small exact Q toy packet that tests `prob:row-sharp-q` on a row where
>    the full fiber distribution can be enumerated.

`agents.md` L467-469: "Small toy cases are useful only when they test a named
route.  A toy-case note should say which label it attacks or supports, for
example `prob:row-sharp-q`, ..."

## 5. What is absent in-tree (the gap this packet fills)

- `rowsharp_q_external_calibration.md` + `qsp_fiber_census.py` report RAW fiber
  distributions only; no in-tree artifact computes the fiber distribution AFTER
  first-match pruning at any enumerable row (grep sweep over experimental/:
  `verify_general_pruned_signed_bound.py`, `verify_first_match_signed_gain.py`,
  `verify_charge_preserving_split_decomposition.py` treat signed Fourier masks on
  abelian charts — a different object; no pruned fiber census exists).
- `qsp_modeatnull_structure.py` classifies members of ONE fiber (the argmax at
  (41,20,10,2)); it does not produce the pruned distribution.

## 6. Cite-and-distinguish targets

- `experimental/notes/rowsharp_q_external_calibration.md` — HIS raw-census
  falsifier fleet (both hunts negative). This packet extends it by the pruned
  distribution; digit-exact raw reproduction is the cross-implementation anchor.
- `experimental/notes/thresholds/atom_toy_r_gt_w.md` — a DIFFERENT atom:
  `prob:entropy-inverse-q` (Q1, L827 of grande_finale.tex), the R>w moment-curve
  wall-break; asymptotic-lane, extension-field instrumentation. Distinguish: this
  packet is the finite `prob:row-sharp-q`/`def:q-row-atom` object at R=w toy rows.
- `experimental/notes/audits/audit_quotient_cell_prefix_fiber_and_split_pencil_census.md`
  (ours, integrated) — a super-polynomial QUOTIENT-CELL fiber on rate-1/2 rows;
  shows the quotient payment is load-bearing at deployed-shaped rows. Distinguish:
  here the quotient-type cells are REMOVED at enumerable rows and the residual
  distribution itself is printed.
