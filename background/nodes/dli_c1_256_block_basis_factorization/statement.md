# DLI C1 256-block basis factorisation

- **status:** PROVED
- **closure:** proof
- **scope:** every official-shape C1 level: `N = 256L`, field `F_q` with an
  element `omega` of exact multiplicative order `2N = 512L`
- **consumer:** `dli_c1r3_gated_envelope_bound` (evidence)
- **provenance:** posed in the Brief-1 Pro dossier
  (`notes/pro_briefs_20260801/responses/BRIEF1_PRO_DOSSIER.md`), audited in
  `notes/pro_briefs_20260801/responses/BRIEF1_DOSSIER_AUDIT.md`; proof and
  verifier replayed on our side 2026-08-01.

Let `A in F_q^(L x N)` be the odd-moment matrix `A_(j,y) = omega^((2j+1)y)`,
`j = 0..L-1`, `y = 0..N-1`. Write every column index uniquely as

```text
y = a + 256 b,      0 <= a < 256,   0 <= b < L,
```

and put `theta = omega^256`.

**(i) Block factorisation.** `theta` has exact order `2L`, and the `a`-th
`L`-column block of `A` is

```text
A_a = D_a F,
D_a = diag(omega^a, omega^(3a), ..., omega^((2L-1)a)),
F_(j,b) = (theta^(2j+1))^b.                              (KBB-1)
```

`F` is the Vandermonde matrix on the `L` distinct odd powers
`theta, theta^3, ..., theta^(2L-1)` (the roots of `X^L + 1`), hence
invertible; each `D_a` is an invertible diagonal. **All 256 blocks are
bases of `F_q^L`.**

**(ii) Convolution form.** Splitting the Boolean input into 256 independent
`L`-bit blocks `B = (B_0, ..., B_255)`, each image `Y_a = A_a B_a` is
uniform on a parallelepiped `S_a = A_a {0,1}^L` of full size `2^L`, and the
subset-sum distribution is the 256-fold convolution of these uniform cube
measures.

**(iii) Exact iid block marginals.** For `lambda` uniform on `F_q^L`, each
block Fourier vector `C_a = A_a^T lambda` is exactly uniform on `F_q^L`;
its `L` entries are independent uniform residues. Each block cosine factor
`T_a(lambda) = prod_b cos^2(pi (C_a)_b / q)` therefore has exactly the iid
`L`-coordinate distribution.

**(iv) Companion orbit.** `D_a = D_1^a`, and with

```text
M = F^T D_1 F^(-T),
C_a = M^a C_0,      a = 0, ..., 255.                     (KBB-2)
```

All cross-block dependence of the C1 spectrum is carried by this single
deterministic 256-step linear orbit; the block marginals themselves carry
none.

This theorem does not prove joint independence of the blocks, any mixing
or expansion property of `M`, any bound on `E - 1`, C1-ZERO/SWIF-4, any
role of the `v_2(q-1) >= 41` gate, coverage of non-official aspects
`N != 256L`, or either Prize result.

## Falsifier

An official-shape row and block index `a` with `det A_a = 0`; a `theta` of
order other than `2L`; a `lambda`-block marginal deviating from exact
uniformity; or failure of the orbit identity `(KBB-2)`.
