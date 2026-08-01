# DLI C1 L=1 four-coordinate block-owner ledger

- **status:** PROVED
- **scope:** the official `L=1` C1 shape, `N=256`, with coefficients
  `1,omega,...,omega^255` and `omega` of exact order `512`
- **dependencies:** `dli_wcl_newton_short_window_exclusion`,
  `dli_wcl_weight3_ambient_exclusion`,
  `dli_wcl_weight4_ambient_exclusion`
- **consumer:** `dli_c1r3_gated_envelope_bound` (evidence)

Let `mu` be the Boolean subset-sum distribution of
`S=sum_i xi_i omega^i`, and put

```text
Z = sum_(d in ternary kernel) 2^(-wt(d)).
```

The banked collision identity makes the `L=1` C1-ZERO target
`Z-2^256/q<=4`.

Partition the 256 coordinates into 64 consecutive four-coordinate blocks.
Let `K_j` be the weighted signed-difference fibre after `j` blocks, so
`sum_s K_j(s)=2^(4j)` and `Z_j=K_j(0)`.  Let `kappa_j` be the new block's
four-coordinate ternary difference measure.  Its total mass is `16`.
The three dependencies exclude every nonzero internal relation of weight at
most four on every official row, so `kappa_j(0)=1` and its nonzero mass is
`15`.  Define

```text
A_j = sum_(s!=0) kappa_j(s) K_j(-s).              (BO-1)
```

Convolution gives

```text
K_(j+1)=K_j*kappa_j,       Z_(j+1)=Z_j+A_j.       (BO-2)
```

With Haar baseline `B_j=2^(4j)/q` and defect `X_j=Z_j-B_j`, this is

```text
X_(j+1)=X_j+[A_j-15*2^(4j)/q].                    (BO-3)
```

Since `X_0=1-1/q`, telescoping on the official admissible stratum gives the
exact identity

```text
Z-2^256/q
 = 1-1/q + sum_(j=0)^63 [A_j-15*2^(4j)/q].        (BO-4)
```

Consequently C1-ZERO at `L=1` is exactly equivalent to

```text
sum_(j=0)^63 [A_j-15*2^(4j)/q] <= 3+1/q.          (BO-5)
```

Thus the 64 structured four-bit target sets may attract at most about three
units of weighted relation mass beyond Haar.  This is an exact accounting
identity, not a bound on any `A_j`.  It does not prove C1-ZERO, SWIF-4,
CERP-512, any `L>1` statement, or either Prize result.

## Falsifier

An official row on which `(BO-4)` fails, or a block with
`kappa_j(0)!=1` despite the three wired short-relation exclusions.
