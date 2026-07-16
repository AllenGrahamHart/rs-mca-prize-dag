# PMA quotient-closure scope and route cut

- **status:** PROVED
- **consumer:** `petal_mixed_amplification`
- **evidence consumer:** `pma_wide_residual`
- **sources:** Przemek upstream `c35a6da3`,
  `experimental/notes/l1/l1_prefix_divisor_count.md` and
  `experimental/notes/l1/l1_quotient_defect_closure.md`

## Statement

Let `H=mu_n`, let `C=RS[H,k]`, fix a received word `U`, and let `P` be a
listed codeword at agreement at least `a=k+sigma`. Write

```text
A_P={x in H: P(x)=U(x)},
E_P=H\A_P.
```

The two precise quotient-closure mechanisms have the following scope.

### Folded source lists

Let `d>1` divide `n`. If both the received word and codeword factor through
the power map,

```text
U(x)=V(x^d),        P(x)=W(x^d),
```

then `A_P` is `K_d=mu_d`-invariant. Hence its exact stabilizer has order at
least `d`, and `P` is already exhausted by `pma_exact_periodic_owner`. In
particular, the proved arbitrary-word folding theorem creates no separate
exact-stabilizer-one folded class.

An algebraically folded codeword against a nonfolded received word has no such
conclusion and remains in the direct residual unless another source theorem
classifies it.

### Low-defect error supports

For each divisor `d>1`, define

```text
E_d^full = union{x K_d: x K_d subset E_P},
partial_d E_P = E_P \ E_d^full,
beta_d(E_P)=|partial_d E_P|.
```

For any printed thresholds `R_d`, the predicate

```text
LDEF_R(P) iff beta_d(E_P)<=R_d for some d>1
```

is source-level and chart-free. Ordering `(d,beta,partial_d E_P)` gives a
canonical first match. On an exact error-weight shell `|E_P|=j`, fixed scale
`d`, and fixed defect `beta`, boundary stripping gives

```text
#{P: |E_P|=j, beta_d(E_P)=beta}
 <= sum_(B subset H, |B|=beta)
      P_(d,j-beta)(T_B s),                         (LDEF)
```

where `s` is the fixed syndrome, `T_B s` is the boundary-filtered syndrome,
and `P_(d,j-beta)` counts primitive `K_d`-periodic multisequence supports.
The filtered reserve is exactly the original reserve `D-j`.

Formula `(LDEF)` is an overlap-safe structural reduction, not by itself a
realized-image payment.

### Official first-shell route cut

On the official dyadic `sigma=1` grid, put `j=n-k-1`, `N=n/2`, and
`h=k/2+1`. The word-free candidate-universe specialization of `(LDEF)` at
`d=2`, `beta=1` is

```text
Raw_(2,1)
 = n binom(N,(j-1)/2)
 = n binom(N,h)
 = n N/(N-h) Q_2(k+2),

Q_2(k+2)=binom(N-1,h).
```

For every official row `n>=2^13`, this is strictly larger than
`719 Q_2(k+2)`. Therefore defect stripping plus the raw periodic candidate
count cannot mint the finite paid `QCLOSE` line. Any such payment needs an
additional source-coupled theorem that removes the boundary-choice loss.

The campaign consequently takes

```text
QCLOSE = empty.
```

After `QOWN_per`, separately proved source-level owners may remove disjoint
subsets of the exact-stabilizer-one complement. The current finite route uses
`pma_sigma_one_dyadic_near_coset_owner`. The proved B11 router is then applied
to everything that remains. Its `GROW union RES` direct theorem must explicitly
include every surviving low-defect closure and every algebraically folded
codeword not covered by the folded-receiver theorem. Keeping `QCLOSE` empty is
an exhaustive route decision; it is not a bound on `GROW union RES`.

## Nonclaims

This theorem does not show that the actual low-defect class exceeds its
allowance, refute a source-coupled boundary owner, choose the finite B11
thresholds, or pay the final PMA residual.
