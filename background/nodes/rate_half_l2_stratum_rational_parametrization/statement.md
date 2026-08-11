# The (PAR) rational parametrization of the e = m = 2 (L2) stratum

- **status:** PROVED (the parametrization, the determinantal form and the
  two syzygies). The (RES) membership criterion is PROVED in one direction
  and MEASURED in the other — see the status ledger.
- **closure:** birational parametrization + a determinantal identity
- **consumer:** `rate_half_band_crossing_location`
- **wired:** 2026-08-11 mint session (task #41), from the round-37 draft
  `notes/pilots_20260811/r37_mint_drafts/l2_par_parametrization/`,
  coordinator line-audited; the T = 3 scope bullet updated (round 38
  achieved it).

## Setting

`m = 2`: `rho = 4m-1 = 7`, `N = 32`, `R = 16`, `r = 7`, `A = R+1-2rho = 3`,
`e = m = 2`. The syndrome pencil is

```text
M(Z) = M_r(y_0) + Z M_r(y_1),   M_r(y)[a][b] = y[a+b],   9 x 8,  y_i in F^16,
```

and the (L2) condition is `M(Z) Q_Z = 0` for `Q_Z = Q_0 + Z Q_1 + Z^2 Q_2`,
`deg Q_j <= 7` — four 9-row blocks, `36` equations on `32` unknowns.

## (PAR) — the parametrization of record

Let `B = (f, g, h, k)` with `deg f, g, h, k <= 4` and let `L` be linear with
root `ell`. Put

```text
A := f^2 - kg,     B~ := fg + hk,     C := g^2 + hf.                  (PAR0)
```

Then

```text
L*Q_0 = A,        L*Q_1 = B~,        L*Q_2 = C                        (PAR)
```

is a birational parametrization of the whole `e = m = 2` (L2) stratum,
subject to **exactly TWO conditions at `ell`**, namely `A(ell) = C(ell) = 0`.
Hit rate `1` (against `1/q` for the round-35 inversion and `q^-5` blind).

## (DET) — the determinantal form

```text
det( [[f, k], [g, f]]  +  z*[[g, f], [-h, g]] )
      = (f^2-kg) + z(fg+hk) + z^2(g^2+hf)
      = L * Q_z.                                                      (DET)
```

## (SYZ) — the two syzygies, and the exact scope of the third condition

```text
f*C  =  g*B~ + h*A,          f*B~ =  g*A  + k*C.                      (SYZ)
```

Consequently `A(ell) = C(ell) = 0` implies `B~(ell) = 0` — i.e. the middle
condition is FREE, which is why only two conditions are imposed — **except
exactly when `f(ell) = g(ell) = 0`**, in which case `A(ell) = C(ell) = 0`
hold automatically and `B~(ell) = h(ell)k(ell)` is unconstrained. The
exception is nonempty and is exhibited by the verifier.

## (RES) — the membership criterion

```text
det M(B) = 0   <=>   gcd(f^2-kg, fg+hk, g^2+hf) != 1.                 (RES)
```

**STATUS SPLIT (this package's forced correction).** The `=>` direction is a
one-line consequence of (PAR): `L` divides all three forms, so the gcd is
nonconstant. The `<=` direction is supported in the source bank by a
`1200/1200` measurement over two fields, **not** by a coordinator hand-check
(the hand-check list covers the elimination, the converse substitutions, the
determinantal identity, the third `ell`-condition, the dimension, and the
`+4-O` arithmetic — it does not cover the (RES) biconditional). This package
therefore records (RES) as **PROVED forward / MEASURED backward** and does
not carry the "iff" at PROVED.

## Dimension

```text
20 coordinates (f,g,h,k)  +  1 (ell)  -  2 (the conditions at ell)
  = 19 affine  -  1 (scaling)  =  18 projective,
```

with finite fibres in both directions (nullity of `M(B)` given the curve, and
of `Phi` given `B`, both measured `1` on `40/40` per field) — so the image
has dimension exactly `18`, independently re-deriving the round-35 value.

## Certified witness (replayed from scratch by verify.py)

`q = 97`, doubly prescribed, `T = 2` over `mu_32`:

```text
S_0 = {30,33,51,63,69,77,85}   (roots of Q_0, slope z = 0)
S_2 = {8,12,18,27,45,52,78}    (roots of Q_2, slope z = infinity)
|S_0 ^ S_2| = 0
f = [42,3,81,6,89]   g = [71,19,15,60,1]
h = [5,40,44,0,6]    k = [24,46,52,68,63]   L = [53,1]
degs (7,7,7),  s = 0,  nullity(36x32) = 1,  generic rank 7,
single finite rank drop at z = 89 to rank 6, full rank at infinity,
no kernel vector of parameter degree <= 1  =>  e = m = 2 EXACTLY,
T over mu_32 (counting z = infinity) = 2.
```

## Scope

- **m = 2 SPECIFIC.** The elimination uses `deg(f^2-kg) <= deg Q_0 + 1`;
  there is no `m >= 3` statement here.
- Two fields for all structure.
- The witness satisfies the pencil-intrinsic half of (SAT1);
  (SAT2)/(SAT4)/(SAT5) are inapplicable at `T = 2` (`sum d_x = 14`, no
  doubled point, against the 31 doubles (SAT3) needs).
- The draft recorded "T = 3 over mu_32 was NOT reached; the failure is
  algorithmic". [WIRING UPDATE 2026-08-11: CLOSED — round 37 proved there
  is NO third exact solve (the two-slot ladder is complete; the third
  prescription is type-(4,4) Cauchy with deficit 3), and round 38 then
  ACHIEVED `T = 3` over `mu_32` by SCALE ELIMINATION through this very
  parametrization (two 2x5 Hankel moment kernels + one rank condition;
  ten witnesses at the predicted rate, two coordinator-certified
  `e = m = 2` at `q = 97` and `q = 193`). The construction instrument is
  exactly (PAR); `T = 4` is the rank-<=2 inverse, open. See A1's round-37
  third-solve and round-38 Cauchy-lattice addenda.]
- The `s != 0` degeneracy yield (42/46 rejected) still has no predictive
  criterion at drafting; the round-38 side-door bank added the mu_32 \ S_0
  restriction giving 100% s=0 yield at 1/7.00 the cost (see A1).

## Cross-pointers

- Supersedes the (D-F) inversion of
  `rate_half_l2_stratum_nonempty_at_m_two` as the construction instrument
  (hit rate 1 vs 1/q); the witness theorem itself is unaffected.
- The (SAT3)-on-(L2) gate is attacked through this parametrization; the
  first-moment gate formula lives in
  `rate_half_sat3_realizability_ledger_record`.

## Source

- `critical/nodes/rate_half_band_crossing_location/statement.md:4347-4418`
  (Round-36 (SAT3)-on-(L2) addendum, 2026-08-11, coordinator-audited; round
  36 bank 2, pilot `r36_sat3_on_l2`).
- (PAR)/(RES): ibid. :4357-4366. Coordinator hand-checks: ibid. :4349-4355.
- The pencil model `M(Z) = M_r(y_0) + Z M_r(y_1)`:
  `notes/pilots_20260811/r35_l2_gate/d1_structure.py:6-9`.
- Certified `T = 2` witness:
  `notes/pilots_20260811/r36_sat3_on_l2/d2_results.txt:18-33`.
- Dimension fibre measurements:
  `notes/pilots_20260811/r36_sat3_on_l2/d1_results.txt:15-19`.

## Replay

```text
tools/ramguard tiny -- python3 \
  background/nodes/rate_half_l2_stratum_rational_parametrization/verify.py
tools/ramguard tiny -- python3 \
  background/nodes/rate_half_l2_stratum_rational_parametrization/verify_audit.py
```
