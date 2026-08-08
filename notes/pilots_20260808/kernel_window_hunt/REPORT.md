# REPORT part 1 — kernel_window_hunt (persisted verbatim by the coordinator, task a94d3f0541fbd3461, 2026-08-08)

## AMENDMENT to my report — novelty subtraction corrected

The prior-art sweep returned after I reported, and it **overturns two of my novelty claims**. I verified its central finding myself before accepting it. Corrections first, then what stands.

### Retractions (my earlier claims were wrong)

**1. "No banked large-prime witness at N′=128 or 256" — WRONG for N′=256.** The repo has held **eight exhibited (w, p) pairs at 226–255 bits since July 2026**. I independently reproduced the cleanest one with my own machinery: from `experiments/prize_resolution/e1_profile_36_mu1_m514_live_norms_result.json`, w with support 9 (‖w‖₁ = 12), Norm(w) = 264 bits = **514 · p** exactly, p a 255-bit probable prime, **p ≡ 1 mod 256**, and I confirmed **kernel membership at s = 93**. So my D3 "positive control" validates the pipeline end to end but **banks nothing new as an exhibit** — it re-derives known objects by a different route. Those exhibits are also *lower* support than mine, so they sit inside every declared support bound (2ℓ′ = 66, 130, 256).

**2. "No prior use of the forward direction (sample w, factor Norm(w))" — WRONG at h=128.** The whole `e1_n256_*` campaign is exactly that direction at prize scale, stated explicitly: *"test the odd part for primality … A prime odd part in `(2^250,2^256)` is an immediate candidate collision row"* (`notes/compute_requests/sections/07-e1-exact-censuses.md:291`), over 320M+ exact resultants. The direction is **free only at h=64 and only for generic-box sampling**; the prior campaign enumerated restricted low-square-mass profiles, never the generic box.

**3. NORMLAW-128 is more routine than I presented it.** `background/nodes/e1_n256_local_norm_cofactor_collapse` is **PROVED**: R/2^μ ≡ 1 mod 256 at h=128, by local reciprocity (Norm(O_K^*) = 1 + 256·Z₂, π = 1−ζ). My measured Norm(w) ≡ 1 mod 128 at h=64 is the direct conductor-128 analogue — free in the repo, but a referee will rightly call it routine, and it is presumably provable by the identical argument (a proof lead, not a claim I am making). **Only the v₂(Norm − 1) refinement is genuinely new** — nothing in the repo constrains v₂(Norm − 1) at all, and that is the load-bearing part, since it is what protects the deployed rows.

### A catch worth surfacing: the falsifier was already in the building

The repo **had the N′=256 falsifying objects and mis-filed them**. `background/nodes/e1_n256_local_norm_cofactor_collapse/audit.md:44-47` dismisses the 248-bit prime as *"below `2^250` and therefore harmless"*, reading it only as a falsifier of a local shortcut — never as a folded-kernel witness. The campaign filtered candidates by **prize-interval membership** (p ≥ B_P·2¹²⁸ ≈ 2²⁵⁵·⁹), a strictly harder bar than admissibility. So the family-uniform conclusion at N′=256 was available on banked evidence months ago and was missed by a filter mismatch, not by absence of data. `e1_folded_certificate_manifest_payload`'s N′=256 entry was already dead.

### What stands, unchanged

- **The headline is intact and is the novel object**: the first exhibited non-cyclotomic ternary kernel witness at **N′=128** — p = 188382597256048064054491654557433363720577825648201882790490986150665597569 (247 bits, **BLS-proven prime**, Norm(w) = p exactly, ‖w‖₁ = 127 ≤ 2ℓ′), plus 20,636 W_TOP hits, 2747 stored with all-distinct primes. N′=128 at large prime is confirmed **free** of prior art; the only near-miss, `ge_lattice_cert/witness_repro.py` PLANT-64, plants against a random co-cyclic functional rather than powers of a 128th root, so p ∤ Norm(w) there.
- **"Family-uniform emptiness is FALSE" as a stated conclusion is free** — even at N′=256, where the objects existed, nobody drew it.
- The h=64 bad-prime count-per-window, the calibration (C1–C4), the coverage (2²²·⁰ of the box), the measured distributions, the 2h² = 8192 orbit verification, and the deployed-row protection argument (v₂ = 7 generic vs 92–200 on every pinned row) are all unaffected.

### Corrected bottom line for the coordinator

The consumer-narrowing decision is **more urgent, not less**: the uniform form is dead at N′=128 (new, proven-prime exhibit) *and* was already dead at N′=256 on evidence banked in July. Closure must go exhibit-scoped with consumers narrowed, or be re-posed as o(1)-sparsity (untouched, even supported, by my measurements), or narrowed to large-v₂ rows — which the v₂ finding makes a real and possibly defensible restriction. My earlier subtraction paragraph was based on my own limited grep and should be replaced by this one; the dedicated sweep held the quarantine (ledger read only below line 3173, the three round-24 pilot dirs excluded from every grep and never opened).

# REPORT part 2 — kernel_window_hunt (persisted verbatim by the coordinator, task a94d3f0541fbd3461, 2026-08-08)

## AMENDMENT to my report — novelty subtraction corrected

The prior-art sweep returned after I reported, and it **overturns two of my novelty claims**. I verified its central finding myself before accepting it. Corrections first, then what stands.

### Retractions (my earlier claims were wrong)

**1. "No banked large-prime witness at N′=128 or 256" — WRONG for N′=256.** The repo has held **eight exhibited (w, p) pairs at 226–255 bits since July 2026**. I independently reproduced the cleanest one with my own machinery: from `experiments/prize_resolution/e1_profile_36_mu1_m514_live_norms_result.json`, w with support 9 (‖w‖₁ = 12), Norm(w) = 264 bits = **514 · p** exactly, p a 255-bit probable prime, **p ≡ 1 mod 256**, and I confirmed **kernel membership at s = 93**. So my D3 "positive control" validates the pipeline end to end but **banks nothing new as an exhibit** — it re-derives known objects by a different route. Those exhibits are also *lower* support than mine, so they sit inside every declared support bound (2ℓ′ = 66, 130, 256).

**2. "No prior use of the forward direction (sample w, factor Norm(w))" — WRONG at h=128.** The whole `e1_n256_*` campaign is exactly that direction at prize scale, stated explicitly: *"test the odd part for primality … A prime odd part in `(2^250,2^256)` is an immediate candidate collision row"* (`notes/compute_requests/sections/07-e1-exact-censuses.md:291`), over 320M+ exact resultants. The direction is **free only at h=64 and only for generic-box sampling**; the prior campaign enumerated restricted low-square-mass profiles, never the generic box.

**3. NORMLAW-128 is more routine than I presented it.** `background/nodes/e1_n256_local_norm_cofactor_collapse` is **PROVED**: R/2^μ ≡ 1 mod 256 at h=128, by local reciprocity (Norm(O_K^*) = 1 + 256·Z₂, π = 1−ζ). My measured Norm(w) ≡ 1 mod 128 at h=64 is the direct conductor-128 analogue — free in the repo, but a referee will rightly call it routine, and it is presumably provable by the identical argument (a proof lead, not a claim I am making). **Only the v₂(Norm − 1) refinement is genuinely new** — nothing in the repo constrains v₂(Norm − 1) at all, and that is the load-bearing part, since it is what protects the deployed rows.

### A catch worth surfacing: the falsifier was already in the building

The repo **had the N′=256 falsifying objects and mis-filed them**. `background/nodes/e1_n256_local_norm_cofactor_collapse/audit.md:44-47` dismisses the 248-bit prime as *"below `2^250` and therefore harmless"*, reading it only as a falsifier of a local shortcut — never as a folded-kernel witness. The campaign filtered candidates by **prize-interval membership** (p ≥ B_P·2¹²⁸ ≈ 2²⁵⁵·⁹), a strictly harder bar than admissibility. So the family-uniform conclusion at N′=256 was available on banked evidence months ago and was missed by a filter mismatch, not by absence of data. `e1_folded_certificate_manifest_payload`'s N′=256 entry was already dead.

### What stands, unchanged

- **The headline is intact and is the novel object**: the first exhibited non-cyclotomic ternary kernel witness at **N′=128** — p = 188382597256048064054491654557433363720577825648201882790490986150665597569 (247 bits, **BLS-proven prime**, Norm(w) = p exactly, ‖w‖₁ = 127 ≤ 2ℓ′), plus 20,636 W_TOP hits, 2747 stored with all-distinct primes. N′=128 at large prime is confirmed **free** of prior art; the only near-miss, `ge_lattice_cert/witness_repro.py` PLANT-64, plants against a random co-cyclic functional rather than powers of a 128th root, so p ∤ Norm(w) there.
- **"Family-uniform emptiness is FALSE" as a stated conclusion is free** — even at N′=256, where the objects existed, nobody drew it.
- The h=64 bad-prime count-per-window, the calibration (C1–C4), the coverage (2²²·⁰ of the box), the measured distributions, the 2h² = 8192 orbit verification, and the deployed-row protection argument (v₂ = 7 generic vs 92–200 on every pinned row) are all unaffected.

### Corrected bottom line for the coordinator

The consumer-narrowing decision is **more urgent, not less**: the uniform form is dead at N′=128 (new, proven-prime exhibit) *and* was already dead at N′=256 on evidence banked in July. Closure must go exhibit-scoped with consumers narrowed, or be re-posed as o(1)-sparsity (untouched, even supported, by my measurements), or narrowed to large-v₂ rows — which the v₂ finding makes a real and possibly defensible restriction. My earlier subtraction paragraph was based on my own limited grep and should be replaced by this one; the dedicated sweep held the quarantine (ledger read only below line 3173, the three round-24 pilot dirs excluded from every grep and never opened).

# REPORT part 3 — kernel_window_hunt (persisted verbatim by the coordinator, task a94d3f0541fbd3461, 2026-08-08)

'); j = s.find('

