# Proof

Notation as in `statement.md`. The lemma and its proof are transplanted
from the pilot's statement of record
(`notes/pilots_20260802/f2_deployed_windows/tower.py:22-43`); clause (i)
and clause (ii) are written out in full here (the source states (i) as
"[LTE]" and (ii) without argument), and clause (iii) is the source's own
three-line argument. The coordinator's independent hand-derivation is
`notes/pilots_20260802/f2_deployed_windows/FABLE_AUDIT.md:27-33`.

## Claim 1 (i): `v_2(q_j - 1) = e + j`

For `j = 0`, `q_0 = p` and the claim is the definition of `e`.

For `j >= 1` factor the difference of squares repeatedly:

```text
p^{2^j} - 1 = (p-1)(p+1) (p^2+1)(p^4+1) ... (p^{2^{j-1}}+1).
```

- `v_2(p-1) = e` by definition.
- `e >= 2` gives `p == 1 (mod 4)`, so `p+1 == 2 (mod 4)` and
  `v_2(p+1) = 1`.
- For `i >= 1`, `p^{2^i}` is an odd square, hence `== 1 (mod 8)`, so
  `p^{2^i} + 1 == 2 (mod 8)` and `v_2(p^{2^i}+1) = 1`. There are `j-1`
  such factors (`i = 1..j-1`).

Adding valuations: `v_2(q_j - 1) = e + 1 + (j-1) = e + j`. QED (i)

*(This is Lifting-The-Exponent in its 2-adic form; the hypothesis
`e >= 2` is exactly what makes `v_2(p+1) = 1` and hence makes the
increment per rung equal to 1.)*

## Claim 2 (ii): the tower of root groups

`mu_{n_j} <= F_{q_j}^*` iff `n_j | q_j - 1`. By (i),
`v_2(q_j-1) = e+j` and `n_j = 2^{e+j}`, so `2^{e+j} | q_j - 1`. QED
(first half)

For `j >= 1`, an element `y in mu_{n_j}` lies in `F_{q_{j-1}}` iff its
order divides `q_{j-1} - 1`; since its order also divides `n_j`, this
says `ord(y) | gcd(n_j, q_{j-1}-1)`. Both are powers of 2 times a unit:
`v_2(n_j) = e+j` and `v_2(q_{j-1}-1) = e+j-1` by (i), while `n_j` has no
odd part, so

```text
gcd(n_j, q_{j-1}-1) = 2^{min(e+j, e+j-1)} = 2^{e+j-1} = n_{j-1}.
```

Hence `mu_{n_j} ^ F_{q_{j-1}} = mu_{n_{j-1}}`. QED (ii)

## Claim 3 (iii): the antipodal identity `y^{q_{j-1}} = -y`

Let `y` have order exactly `n_j = 2^{e+j}`, `j >= 1`. Write
`q_{j-1} - 1 = 2^{e+j-1} u` with `u` odd — legitimate by (i), which gives
`v_2(q_{j-1}-1) = e+j-1` exactly.

Since `y` has order `2^{e+j}`, the element `y^{2^{e+j-1}}` has order
exactly 2, and the only element of order 2 in a field is `-1`:

```text
y^{2^{e+j-1}} = -1.
```

Therefore

```text
y^{q_{j-1}-1} = (y^{2^{e+j-1}})^{u} = (-1)^u = -1,
```

because `u` is odd. Multiplying by `y`: `y^{q_{j-1}} = -y`. QED (iii)

## Claim 4 (Corollary A): the Frobenius pair is `{y, -y}`

The rung-`j` descent is the extension `F_{q_j} / F_{q_{j-1}}`, whose
Frobenius is `x -> x^{q_{j-1}}`. By (iii) it sends a genuine `y` (one of
order exactly `n_j`, i.e. one NOT in `F_{q_{j-1}}` by (ii)) to `-y`. Both
`y` and `-y` have order exactly `n_j` (as `e+j >= 2` makes `-1 = y^{2^{e+j-1}}`
a power of `y`), so the pair is `{y, -y}` and the pairing is an involution.
QED (A)

## Claim 5 (Corollary B): every `Delta_i` is even

Fix a rung-`j` window and a frequency `c`. By Corollary A the two members
of coordinate `i` are `y_i` and `-y_i`, so with `Tr` the `F_{q_j}/F_p`
trace (`F_{p^2}/F_p` in the banked model),

```text
s_i^- = Tr(c(-y_i)) = -Tr(c y_i) = -s_i^+   in F_p.
```

Now push this through the carry normalisation
`sigma(s) = s + p[2s > p] (mod 2p)`. Two observations:

- `sigma(s)` is exactly the representative of `s (mod p)` lying in the
  centred interval `(-p/2, p/2)`, read in `Z/2p`: for `s < p/2` it is `s`,
  and for `s > p/2` it is `s + p == s - p (mod 2p)` with
  `s - p in (-p/2, 0)`. (`p` odd, so `2s = p` never occurs.)
- The centred representative is an ODD function of `s (mod p)`:
  `cen(-s) = -cen(s)`.

Hence `sigma_i^- = sigma(-s_i^+) = -sigma(s_i^+) = -sigma_i^+` in `Z/2p`,
and

```text
Delta_i = sigma_i^+ - sigma_i^- = 2 sigma_i^+   (in Z/2p),
```

which is even (`2p` is even, so parity is well defined on `Z/2p`). The
degenerate coordinate `s_i^+ = 0` gives `s_i^- = 0`, `sigma_i^pm = 0`,
`Delta_i = 0` — even as well. This holds for **every** `i`, every `c`,
every rung. QED (B)

## Claim 6 (Corollary C): `R_p = 1` and `flat = 0`

`omega = zeta_{2p}` satisfies `omega^p = -1`. Since `p` is odd, `k = p`
is one of the odd modes. By (B) every `Delta_i` is even, so

```text
R_p = (1/m) sum_i omega^{p Delta_i} = (1/m) sum_i (-1)^{Delta_i}
    = (1/m) sum_i 1 = 1.
```

`|R_k| <= 1` for every `k` (a mean of unit-modulus terms), so
`max_{k odd}|R_k| = 1` and `flat = 1 - 1 = 0`, exactly — not
approximately. QED (C)

## Claim 7 (Corollary D): sub-window inheritance

"`Delta_i` is even" is a statement about the single coordinate `i`. A
sub-window is a subset `I` of the coordinates; every `i in I` still
satisfies it, so Claim 6 applies verbatim with `m` replaced by `|I|`,
giving `R_p = 1` and `flat = 0` on the sub-window. There is therefore no
subset of a deployed rung window on which the mode `k = p` is alive:
**selection inside coordinate space cannot repair the degeneracy.** QED (D)

## Honest scope

- Claims 1-7 are exact and scale-free; the official-scale content is
  entirely in Claim 1 at `p = 2^31-2^24+1`, `e = 24`, `j = 1..16`, which
  the verifier checks on the actual integers.
- What Claim 5 uses about the model is only (a) `Tr` is `F_p`-linear so
  `Tr(-x) = -Tr(x)`, and (b) the carry normalisation `sigma` is the
  centred representative, hence odd. Both are properties of the banked
  model as implemented (`f2model.residues`, `f2model.half_flag`,
  `slicecore.sigma_of`), re-implemented from scratch in `verify.py`.
- The pilot reports the same conclusion from the census side (the
  degeneracy law, 194 rows). That census is **not** used as an input
  here and is **not** claimed: this node proves the implication in the
  direction the lane consumes and leaves the converse measured.
- The pilot's own honest caveat is inherited: the per-rung window was
  reconstructed from campaign-log entry #76 and is "nowhere explicitly
  defined"; a different reading changes `m_j` by a factor 2 but
  **cannot** change the antipodal law, because the law is about the
  subgroup, not about how many of its pairs a rung processes
  (`REPORT.md:69`).
