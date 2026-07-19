# Shifted-energy constant audit

Date: 2026-07-12.

Macourt--Shkredov--Shparlinski, Corollary 4.1, gives in the official regime
`n<sqrt(p) log p` the asymptotic-shape estimate

```text
E_x(H-1) - n^4/p << n^2 log n.
```

Since the oriented three-to-one count is at most this shifted multiplicative
energy, a sufficiently sharp explicit version could bypass the non-swap
moment and prove C36' directly. For all official orders it would suffice, for
example, to prove

```text
E_x(H-1) <= 35n^2.
```

Indeed `35n^2 < 36n^2-16n^(4/3)-n/2` for `n>=8192`.

The published corollary does not currently supply this finite theorem. Its
proof uses `<<` throughout, invokes Mitkin's rich-line estimate with an
implicit constant, and chooses a parameter with a merely "sufficiently
large" constant. At the largest official order, `log n=41 log 2`, so after
paying the main term `n^4/p<n^2`, the coefficient of `n^2 log n` would need
to be below roughly

```text
35/(41 log 2) < 1.24.
```

No such printed constant follows from the source. Therefore citing
Corollary 4.1 does not close C36'. A viable energy route must redo the
rich-line decomposition with exact constants, exploit the truncation/non-swap
conditions, or prove a direct constant-energy theorem for the shifted
power-of-two subgroup. The 7,090-row sweep, whose observed energy-adjacent
non-swap constant is below `3.825`, makes this a plausible route but not a
proved one.

Primary source: Macourt, Shkredov, and Shparlinski, *Multiplicative Energy of
Shifted Subgroups and Bounds on Exponential Sums with Trinomials in Finite
Fields*, arXiv:1701.06192, Lemma 2.6 and Corollary 4.1.
