# GOAL (standing, overnight): Falsification-pruning of the critical DAG's red frontier

Author: roadmap owner. Date set: 2026-07-05. Runs turn after turn until stopped.

## Mission

Trim the critical DAG by **falsifying** its red frontier — not proving it — until every
remaining node **survives genuine adversarial falsification at its actual crux**. The
surviving nodes are the stable frontier where (expensive) proof effort will later belong.

## Setup / hygiene

- Clone a **fresh worktree from the latest `prize` main/master**. Work only there, on your
  own branch. **Never** touch main, the published artifact, or anyone else's branch.
- Modal creds in `~/.modal.toml`. **Every Modal run < 60 s wall**; checkpoint partial
  results before timeout; write results to JSON.
- Keep a running **ledger** (`experiments/falsification_pruning/ledger.md`) with, per
  attempt: the node, the exact obligation attacked, the script, the replay command, the
  Modal app name + wall time, and the verdict. Reproducibility is mandatory.
- Read `notes/EMPIRICAL_OBSERVATIONS.md` first and **build on** the existing findings
  (sov worst-case census + Lane-1 crux, PRK multi-character falsification, Gate N
  refutation, dli sup refutation). Do not re-derive what is already recorded.

## Principle

Each critical node is a conditional **"inputs A ⟹ claim B"**. Earning amber certifies the
*implication is valid* — but the node is **useless if A is false**. Two independent failure
modes; attack **both**:

1. **An input A is actually false** (the hypothesis is untrue) — the main target.
2. **The reduction A ⟹ B is invalid** (the derivation is wrong) — how Gate N fell.

**Do not try to prove nodes.** Try to **falsify** each node's claim.

## CRITICAL — attack the crux, not the mechanism

Prior falsification runs produced **false "resisted" verdicts** by testing the settled
sub-part (the mechanism, the arithmetic, the necessity of a clause) and stopping *before*
the real open obligation. Example: sov's attack tested "is there a small-value-set non-Bohr
cell?" (the decomposition — settled) and never touched "can the Bohr class be **priced**?"
(the real open obligation).

For **every** node: first write down its **actual open obligation** — the `REMAINING:` /
pricing / chargeability / descent / achievability question — and aim the attack **there**.
State explicitly which obligation each attack tested. **"Resisted" counts only if the crux
itself was adversarially hit.**

## Guardrails (learned the hard way)

- **Salvage before delete.** False-as-stated ≠ false. dli's sup and PRK's absolute bound
  were both re-posable. Delete a node **only** if no trivial modification saves it, and
  **record the reasoning**. Over-pruning a true-but-misstated node is the expensive mistake.
  Prefer re-pose to deletion; be conservative.
- **Verify every counterexample.** Re-derive it and test it against the **real object**.
  Known traps this campaign: a `z=1` primitive-root bug (spurious μ_k catches), an
  incomplete-frequency Bohr sweep, a whole-section **proxy** instead of the true object, and
  **degenerate samples** (first basis vectors) instead of generic ones.
- **"Not yet falsified" is not "true."** A resisting node is a *candidate* to prove later,
  not a proved node. Log it and move on; do not mark it green.

## The loop (per red leaf)

1. **Identify** the node's actual open crux (not the mechanism).
2. **Attack** the crux: adversarial numeric + algebraic falsification, verified, Modal < 60 s.
3. **Outcome:**
   - **RESISTS** after genuine effort → mark **STABLE FRONTIER**; record the tested range and
     the falsifier shape that was *not* found; move to the next leaf.
   - **FALSIFIED** → **salvage check**: does a trivial modification save it (absolute →
     parameter-dependent bound; add a scoping hypothesis; restrict the class)?
     - **salvageable** → re-pose the node's `statement.md`; attack the **re-posed** version (goto 2).
     - **unsalvageable** → **prune** the node from the critical DAG (remove node + its edges;
       archive its folder to `archive/`), and **move one level toward the prize**: attack the
       **consumer** node it fed (its claim may now be false, or true via other inputs). Repeat.
4. On any status / node / edge change: run `tools/dag_commit.sh` and record it in the ledger.

## Stop condition

Trim each leaf's chain until you reach a node whose claim **survives genuine adversarial
falsification at its crux**. That node is the frontier; log it and move to the next leaf.
The mission ends when all six leaf-chains rest on logged stable frontiers.

## Priority order (highest risk of a hidden false node first)

1. **sov_gridsum_residual** → attack the **Bohr / large_power_sum class PRICING**: does the
   class's *total mass* stay bounded by the ledger budget, or grow with the parameters? This
   is the same "charge a structured family" shape as the just-falsified PRK — highest risk.
2. **m720_conductor_compression** → take the **known non-toral survivors** and compute their
   **obstruction field degree**: small (survivor-conditioned descent holds) or large (descent
   fails)? Test the descent — not the (already-confirmed) height table.
3. **e22_mixed_petal_covariance** → does the **square-shift / moment-trade construction
   actually yield** pointwise covariance + off-tail exhaustivity, or only the *necessity* of
   those clauses? Attack achievability of the source, not clause-necessity.
4. **petal_primitive_residue_kernel_rank** (re-posed) → are the **multi-character kernel
   families chargeable** (structured ⇒ payable, PRK repairs) or unbounded/unpayable? If
   unpayable and unsalvageable, prune and descend to `petal_cofactor_chargeability`.
5. **dli_prime_weighted_large_block_support** (re-posed) → does the **U-weighted-average /
   RES-count** obligation resist? (Codex's own earlier flattening scans suggest yes.)
6. **rate_half_band_closure** → lowest priority (already resists both proof and falsification;
   needs a new mechanism, not a falsification attack).

## Coordination

The roadmap owner replays your honest results onto the canonical branch (one-writer rule)
and audits your ledger with the same "did it hit the crux?" scrutiny. Work autonomously;
surface each pruning/re-pose/frontier verdict clearly in the ledger so it can be replayed.
