# Round-21 growing-petal attack correction

The N10 candidate box has the exact closed form

```text
Cand(k) = A1[C(k-1,1)+2C(k-1,2)+2C(k-1,3)]
        + A2[C(k-1,2)+2C(k-1,3)]
        + A3 C(k-1,3),
A1 = k,  A2 = C(k,2)-k/2,  A3 = C(k,3).
```

It reproduces `5,096`, `386,640`, and `27,152,032` exactly, has degree
exactly six, and has leading term `n^6/2304`. The field-corrected exponents
6.14-6.21 in the prior audit are the exact polynomial's pre-asymptotic local
slope (`6.50 -> 6.27 -> 6.14 -> ... -> 6.0000`) while the count approaches
`n^6/2304` from below. The previous phrase "above the disproved n^6 line"
was therefore a finite-size artifact. The count never exceeds `n^6/2304`.

The registered super-polynomial falsifier was structurally unfireable at
`ell=2`: the bucket is empty when `sigma > 2*ell+b-2`, and otherwise its box
has order `n^(4*ell+2b-4)`. The growth parameter is `ell`, not `n`.

## Retired and replacement runs

- Drop `L1-N10-128`. At `ell=2` it would add a fourth point on a curve whose
  closed form is already known and provably capped by `n^6`.
- The decisive request is `L1-N10-ELL`: fix `n=32` or `64`, sweep
  `ell=2..6` under both scalar schedules, and compare retained mass with
  `BOX(ell)/q`.
- The `ell=2,3,4`, `n=24` row is already complete locally in
  `d3_ell_sweep.py`; its counts are `475 -> 8,135 -> 20,942`.
- Do not interpret fixed-`ell` evidence as a uniform theorem or as
  floor-band emptiness. The open theorem is polynomial payment when
  `ell=Omega(n/log n)`.

The adversarial search and exact-box derivation are recorded under
`notes/pilots_20260807/l1_pma_diag/`. They identify exact-agreement promotion
as the mechanism suppressing degenerate-word spikes, but this remains
evidence rather than closure of the growing-petal target.
