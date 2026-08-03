# Proof

Notation as in `statement.md`. Claim 1 is transplanted verbatim in
substance from the pilot's derivation of record
(`notes/pilots_20260802/f2_deployed_windows/deployed.py:37-56`). Claims
2-5 are **reconstructed here**: the pilot states the value
`D = ((p-1)/2)^2` and CHECKS it at `p = 11..41` for two frequencies
(`verify.py:300-321`), but no derivation of the value, and no scope
condition on `c`, appears anywhere in the record. See
`../../AUDIT_CHECKLIST.md` items F0.b and F2.b-F2.d.

Throughout, `M := (p-1)/2`, and for `x in Z/p` let `cen(x)` be the
representative of `x` in `[-M, M]` and

```text
kappa(x) := (-1)^{cen(x)}   in {+1, -1}.
```

Two facts used repeatedly:

- **(N1)** `sigma(s) = s + p[2s>p] (mod 2p)` is exactly `cen(s)` read in
  `Z/2p`: for `s < p/2` it equals `s`, and for `s > p/2` it equals
  `s + p == s - p (mod 2p)` with `s - p in (-p/2, 0)`. (`p` is odd, so
  `2s = p` never occurs.) In particular `sigma` is an ODD function of
  `s (mod p)`, and `(-1)^{sigma(s)} = kappa(s)`.
- **(N2)** parity is well defined on `Z/2p` (as `2p` is even), and
  `(-1)^{Delta_i} = (-1)^{sigma_i^+ - sigma_i^-} = (-1)^{sigma_i^+}
  (-1)^{sigma_i^-} = kappa(s_i^+) kappa(s_i^-)`.

## Claim 1 (Theorem 1: the certificate)

Let `k` be ODD. Since `omega = zeta_{2p}` has `omega^p = -1`,

```text
omega^{k(x+p)} = omega^{kx} (omega^p)^k = -omega^{kx}.
```

Fix `d in Z/p`. The `Delta_i` congruent to `d` mod `p` take only the two
values `x_d` and `x_d + p` in `Z/2p` (the even and the odd
representative of the class, in some order — `x_d` is defined to be the
even one). By the display, the coordinates sitting at the ODD
representative contribute `-omega^{k x_d}` and those at the even
representative contribute `+omega^{k x_d}`; so the whole class
contributes `c_d omega^{k x_d}`, with `c_d` the signed count of the
statement. Summing over classes,

```text
R_k = (1/m) sum_i omega^{k Delta_i} = (1/m) sum_{d in Z/p} c_d omega^{k x_d}.
```

That is `(ID)`, and it holds **simultaneously for every odd `k`** — the
class collapse is `k`-free. The triangle inequality with
`|omega^{k x_d}| = 1` gives

```text
|R_k| <= (1/m) sum_d |c_d| = D/m
```

for every odd `k`, hence `(DEF)`, and `(FLAT)` by definition of `flat`.
`c_d` and `D` are integers computed from the `Delta` multiset. QED (1)

## Claim 2 (the class structure at the full group)

Let `n_ord = p^2 - 1`, so `mu_{n_ord} = F_{p^2}^*` and, with the
representative convention (`w`-component in `[1, M]`), the pair reps are
exactly

```text
{ y = (a_y, b_y) : a_y in F_p, b_y in [1, M] },     m = p * M = p(p-1)/2.
```

(Each genuine pair `{y, y^p}` has `y^p = (a_y, -b_y)`, so exactly one of
the two has `w`-component in `[1, M]`; and no `y` with `b_y = 0` is
genuine.) This is the pilot's `m = p(p-1)/2`.

For `c = (a_c, b_c)` the model gives
`s^+ = 2(a_c a_y + N_0 b_c b_y)` and `s^- = 2(a_c a_y - N_0 b_c b_y)` in
`F_p`. Write

```text
u := 2 a_c a_y,        v := 2 N_0 b_c b_y,      so  s^+ = u+v,  s^- = u-v.
```

Then `Delta_i == s^+ - s^- == 2v (mod p)`.

**Assume `a_c != 0` and `b_c != 0`.**

- `b_y -> 2v = 4 N_0 b_c b_y` is injective on `[1, M]`, so the `M`
  classes `d = 2v` are distinct and non-zero, and the class of `d`
  consists of exactly the `p` coordinates with that `b_y` and `a_y`
  ranging over `F_p`.
- `a_y -> u = 2 a_c a_y` is a bijection of `F_p`, hence so is
  `a_y -> a := s^- = u - v`; and then `s^+ = a + 2v = a + d`.

Using (N2),

```text
c_d = sum_{a in F_p} kappa(a) kappa(a + d) =: A(d).
```

QED (2)

## Claim 3 (the autocorrelation `A(t) = (-1)^t (p - 2t)`, `0 <= t <= M`)

Parametrise `a in Z/p` by `j := cen(a) in [-M, M]` (a bijection), so
`kappa(a) = (-1)^j`. Fix `0 <= t <= M`. Then `j + t in [-M, 2M]` and
`2M = p-1`, so only an upper overflow can occur:

- if `j + t <= M`: `cen(a+t) = j+t`, so
  `kappa(a)kappa(a+t) = (-1)^j (-1)^{j+t} = (-1)^t`;
- if `j + t > M`: `cen(a+t) = j + t - p`, so
  `kappa(a+t) = (-1)^{j+t-p} = -(-1)^{j+t}` (`p` odd), and the product is
  `-(-1)^t`.

The second case is `j in [M-t+1, M]`: exactly `t` values of `j`. The
first case has the remaining `(2M+1) - t = p - t` values. Hence

```text
A(t) = (-1)^t (p - t) + (-(-1)^t) t = (-1)^t (p - 2t).
```

Finally `A` is even: `A(-t) = sum_a kappa(a)kappa(a-t)
= sum_{a'} kappa(a'+t)kappa(a') = A(t)`. QED (3)

*(Sanity: `A(0) = p`, and `sum_{t in Z/p} A(t) = (sum_a kappa(a))^2
= ((-1)^M)^2 = 1`, matching `p + sum_{t != 0} A(t) = 1`.)*

## Claim 4 (Theorem 2: `D = ((p-1)/2)^2` at the full group)

Keep `a_c b_c != 0`. By Claim 2 the support of `(c_d)` is

```text
S_c = { 4 N_0 b_c b : b = 1..M }  =  lambda * {1, ..., M},
      lambda := 4 N_0 b_c  in F_p^*.
```

`{1, ..., M}` is a **half-system** of `F_p^*`: it contains exactly one of
`{x, -x}` for each of the `M` pairs, since `-b == p-b in [M+1, p-1]`.
Multiplying by a non-zero constant preserves this (`lambda H` contains
`lambda b`, and would contain `-lambda b = lambda(-b)` only if `-b in H`,
which is false). So `S_c` is a half-system too, and by Claim 3 (with `A`
even) the multiset

```text
{ |c_d| : d in S_c } = { |A(d)| : d in S_c } = { p - 2t : t = 1..M }
```

with each value occurring exactly once. Therefore

```text
D = sum_{t=1}^{M} (p - 2t) = M p - 2 * M(M+1)/2 = M(p - M - 1) = M * M,
```

using `p - M - 1 = p - (p-1)/2 - 1 = (p-1)/2 = M`. So
`D = M^2 = ((p-1)/2)^2`. QED (4)

**The flatness corollary.** `m = pM`, so `D/m = M^2/(pM) = M/p = (p-1)/(2p)`
and

```text
flat >= 1 - (p-1)/(2p) = (p+1)/(2p) > 1/2.
```

QED

## Claim 5 (Theorem 3: the two exceptional lines)

- **`b_c = 0`.** Then `v = 0`, so `s^+ = s^- = u` and `Delta_i = 0` for
  every `i`. Every `Delta_i` is even and lies in class `d = 0`, so
  `c_0 = m`, all other `c_d = 0`, and `D = m`. `(FLAT)` reads
  `flat >= 0`. (Indeed `R_k = 1` for every `k` here: total degeneracy.)
- **`a_c = 0`.** Then `u = 0`, so `s^- = -s^+`. By (N1) `sigma` is odd,
  so `sigma^- = -sigma^+` and `Delta_i = 2 sigma_i^+` is EVEN for every
  `i` — the same mechanism as `f2_antipodal_descent_lemma` Corollary B,
  arrived at here from the frequency side rather than the subgroup side.
  Hence every `c_d = #{i : Delta_i == d} >= 0` and
  `D = sum_d c_d = m`; `(FLAT)` reads `flat >= 0`.

Both lines are `F_p`-lines through the origin in `F_{p^2}` minus `0`, of
size `p-1` each, and Claim 4 covers everything else. QED (5)

## Claim 6 (Corollary 4, and the flip statement)

**Degenerate branch.** If every `Delta_i` is even then, by definition,
`c_d = #{i : Delta_i == d (mod p)} >= 0` for every `d`, so
`D = sum_d c_d = m` and `(FLAT)` gives `flat >= 0` — no information.
This is the case at every deployed rung window
(`f2_antipodal_descent_lemma` Corollary B), where the true value is
`flat = 0` (that node's Corollary C): the certificate is **tight but
vacuous** there. QED

**Global flip.** Reversing every orientation sends
`Delta_i -> -Delta_i`. In `Z/2p`, `-Delta == 2p - Delta` has the same
parity as `Delta`, and its class mod `p` is `-d`. So `c_d -> c_{-d}`,
a permutation of the multiset `{|c_d|}`, and `D` is unchanged. QED

**Partial flips are NOT covered**: flipping a proper subset moves
individual coordinates between classes `d` and `-d` while keeping their
parity, which changes the cancellation pattern inside each class. The
verifier exhibits partial flips at which `D` changes, so `D` must always
be quoted with its labelling. (This is the exact form of the pilot's
convention caveat, `REPORT.md:71`.)

## Honest scope

- Claim 1 is the pilot's; Claims 2-6 are **reconstructed** — the record
  contains the VALUE `D = ((p-1)/2)^2` and a 12-instance check, not a
  derivation, and states no condition on `c`. The reconstruction both
  proves the value and shows the pilot's unrestricted phrasing ("the
  FULL-group window has `D = ((p-1)/2)^2` exactly", `REPORT.md:37`) is
  **too broad by exactly `2(p-1)` frequencies**. Flagged, not silently
  adopted.
- Nothing here is a discharge of anything in the F2 lane. The full-group
  window is not deployed; the deployed windows are in the degenerate
  branch. The node's value is the exact, mode-uniform, integer template.
- The multiplicity law (`sorted non-zero Delta-counts = [1..p-1]`) is
  part of the pilot's A8 assertion; it is machine-verified here and
  labelled MEASURED. It is NOT used in any proof above.
