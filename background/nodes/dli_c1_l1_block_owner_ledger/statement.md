# DLI C1 L=1 four-coordinate block-owner ledger

- **status:** PROVED
- **closure:** proof
- **scope:** the L=1 C1 shape: `N = 256` coefficients
  `1, omega, ..., omega^255` in `F_q` with `omega` of exact order 512
- **consumer:** `dli_c1r3_gated_envelope_bound` (evidence)
- **provenance:** posed in the Pro inverse-flatness strategy document
  (`notes/pro_briefs_20260801/responses/blackhole/`), audited and replayed
  on our side 2026-08-01.

Let `mu` be the distribution of the Boolean subset sum
`S = sum_i xi_i omega^i` and

```text
Z = sum_(d in ternary kernel) 2^(-wt(d)),
```

so that (banked equivalences) the L=1 C1-ZERO target is
`Z - 2^256/q <= 4`.

Partition the 256 coordinates into 64 consecutive four-coordinate blocks.
Let `K_j` be the weighted signed-difference fibre after `j` blocks
(`sum_s K_j(s) = 2^(4j)`, `Z_j = K_j(0)`), and let `kappa_j` be the new
block's four-coordinate ternary difference measure (total mass
`(1 + 1/2 + 1/2)^4 = 16`; nonzero mass 15 whenever the block has no
internal signed relation of weight <= 4, which the banked Newton and
ambient weight-3/4 exclusions guarantee on every admissible row). Then

```text
K_(j+1) = K_j * kappa_j,
Z_(j+1) = Z_j + A_j,      A_j = sum_(s != 0) kappa_j(s) K_j(-s),  (BO-1)
```

and with the Haar baseline `B_j = 2^(4j)/q` and defect `X_j = Z_j - B_j`,

```text
X_(j+1) = X_j + [ A_j - 15 * 2^(4j)/q ].                          (BO-2)
```

Telescoping from `X_0 = 1 - 1/q` gives the EXACT identity

```text
Z - 2^256/q = 1 - 1/q + sum_(j=0)^63 [ A_j - 15 * 2^(4j)/q ].     (BO-3)
```

**Consequently, C1-ZERO at L=1 is exactly equivalent to**

```text
sum_(j=0)^63 [ A_j - 15 * 2^(4j)/q ]  <=  3 + 1/q.                (BO-4)
```

`A_j` is the actual weighted mass of previous differences landing on the
64 structured four-bit target sets; `15 * 2^(4j)/q` is what Haar-uniform
differences would contribute. The mystery is thereby localized: the 64
structured targets may attract at most ~3 units of excess weighted mass
beyond Haar, unless a resonance owns the attraction.

This theorem is an exact accounting identity. It does not bound any
`A_j`, does not prove C1-ZERO, SWIF-4, or any inverse-flatness statement,
does not treat `L > 1`, and does not prove either Prize result.

## Falsifier

A split prime `q` (order 512) on which the telescoping identity `(BO-3)`
fails against exact enumeration, or a block with `kappa_j(0) != 1` on a
row where the banked weight-<=4 exclusions hold.
