# Upstream determination datum (node-local, 2026-07-07)

Source: regime-map audit, `prize/notes/correspondence/REGIME_MAP.md`
(replay script `four_pairs_exact.py` there). Node-local per the
2026-07-07 rule: comparison-derived facts about a node live in the node.

## What this adds to F6 (BAND-DETERMINATION)

The floor's claim is determination-location fidelity: the true
unsafe/safe determination sits where the first-moment model predicts.
Our own evidence was the q = 97…1153 ladders (18/18 matches through the
σ = 1 crossing at q = 241…337, n ≤ 64).

Upstream (przchojecki/rs-mca, Paper D v13, prop:capg-moved-frontier +
cor:capg-adjacent-pairs) PROVES unsafe-side witnesses and predicts the
adjacent safe edge at four deployed rows at n = 2^21 — and their
crossing arithmetic is exactly a first-moment prediction:

    list: unsafe(m) ⟺ C(n,m) > p^(m−K)·⌊q·ε*⌋
    MCA : unsafe(m) ⟺ C(n,m) > p^(m−K−1)·⌊q·ε*⌋   (pencil dof, their remark)

We replayed all four locations and margins exactly (integer
arithmetic): KB MCA 1116047/1116048 @ 22.197, KB list 1116046/1116047
@ 22.011, M31 MCA 1116023/1116024 @ 3.259, M31 list 1116022/1116023
@ 3.073.

GRADING (honest): the unsafe side at a0 is THEIR THEOREM (witnesses
constructed); the safe side at a0+1 is their conjecture (Q/extremality).
So the datum confirms the first-moment model's location arithmetic and
its unsafe-side realization at n = 2^21; it does not by itself confirm
the safe side. It extends F6's determination-location evidence base by
five orders of magnitude in row size, in the same direction as every
banked ladder point.

Caveat for reuse: the M31 rows are extra-official (circle domain,
ε* = 2^−100, q = p'^4); the KoalaBear rows are official-shaped.
