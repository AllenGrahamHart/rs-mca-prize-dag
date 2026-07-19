# DLI-CLOSE-4 fulfilment

[Pro's round-6 reply, received 2026-07-06 via user relay. Saved verbatim.
Checker saved alongside as `pro_reply_round6_checker.py`; independent
replay `verify_round6_reply.py` — 26/26 PASS. Verdict and absorption in
`DLI_CLOSE_PINNED.md` § ROUND-6 RETURN.]

Verdict: **C-style conditional close, with a literal correction to the printed round-6 reduction.**

I did **not** produce an honest DLI-AGG budget refutation of the kind requested in B: I did not engineer a Pocklington-certified `q < 2^256` dividing two or more multiplier-independent near-top low-weight norms whose combined aggregate cost exceeds 100 bits.

What I can close exactly is this:

1. the displayed orbit-decomposition upper bound in DLI-CLOSE-4 cannot be an upper bound for `E_j` itself;
2. after replacing it by an **excess-over-1 weighted generator ledger**, the aggregate arithmetic closes with explicit constants;
3. the remaining theorem is not a raw count of `K_j`, but a weighted, shadow-closed excess statement.

Sources used:

- `DLI_CLOSE_4.md`, round-6 aggregate target and orbit-count ask: <https://raw.githubusercontent.com/AllenGrahamHart/rs-mca/allen/prize-dag-delta/experimental/notes/roadmaps/pro_windows/DLI_CLOSE_4.md>
- `DLI_CLOSE_4_CENSUS.md`, closure/census evidence: <https://raw.githubusercontent.com/AllenGrahamHart/rs-mca/allen/prize-dag-delta/experimental/notes/roadmaps/pro_windows/DLI_CLOSE_4_CENSUS.md>

---

## 1. The printed orbit-decomposition bound is false as an upper bound for `E`

DLI-CLOSE-4 prints the target

\[
\sum_j \log_2 E_j \le 100,
\]

with

\[
E_j = E_U[\rho_j],
\]

and then states the orbit decomposition

\[
E_j \le
\frac{q^{L_j}}{2^{N_j}}
\left(1+K_j\,2N_j\,2^{-(L_j+1)}\right).
\tag{1}
\]

This cannot be correct for `E_j` itself, because the Fourier identity has the `lambda = 0` term equal to `1`, hence always

\[
E_j = \sum_{\lambda \in \mathbb F_q^{L_j}} T_j(\lambda) \ge 1.
\]

A concrete admissible row makes (1) fail by over 208 bits.

Take

\[
q=65537,\qquad n'=512,\qquad N=256,\qquad L=1.
\]

Then `q` is prime, `q < 2^256`, `q ≡ 1 mod 512`, and

\[
2^N=2^{256} \ge q.
\]

The pinned primitive root is `g = 3`, so

\[
\omega = g^{(q-1)/512}=3^{128}\equiv 15028 \pmod {65537}.
\]

It satisfies

\[
\omega^{512}=1,
\qquad
\omega^{256}=-1
\pmod q,
\]

and the primitive weight-3 relation

\[
1+\omega^{95}-\omega^{146}=0\pmod {65537}.
\]

So the minimal relation weight is at most `3 = L+2`; in particular the row has a nonzero minimal relation orbit.

Even if `K` is grossly overcounted by **every signed reduced weight-3 ternary element**, we have

\[
K \le 2^3 {256 \choose 3}=22,108,160.
\]

For this row,

\[
2N\,2^{-(L+1)}=512/4=128.
\]

Thus the right-hand side of (1) is at most

\[
\frac{65537}{2^{256}}\left(1+22,108,160\cdot128\right)
=
\frac{185459517751297}{2^{256}}
<2^{-208.60}<1.
\]

But `E >= 1`. Therefore (1) is not an upper bound for `E`.

The fix is to bound the **excess**

\[
B_j := E_j-1 = \sum_{\lambda\ne0}T_j(\lambda),
\]

not `E_j` itself.

---

## 2. Corrected conditional form

Let

\[
r_j := \frac{q^{L_j}}{2^{N_j}} \le 1.
\]

A primitive generator of weight at least `L_j+1` has at most `2N_j` signed shifts, so its base orbit ledger contributes at most

\[
2N_j\,2^{-(L_j+1)}.
\]

If the multiplier/lift shadow of a new independent generator has total weighted shadow factor `s_g` relative to that base orbit, then its contribution to the excess `B_j` is bounded by

\[
r_j\,s_g\,2N_j\,2^{-(L_j+1)}.
\]

Define the effective shadow-closed generator multiplicity at level `j` by

\[
M_j := \sum_{g\in G_j^{new}} s_g.
\]

The corrected conditional leaf is:

\[
\boxed{
B_j=E_j-1
\le
R_j
+
M_j\,r_j\,2N_j\,2^{-(L_j+1)}
}
\tag{H}
\]

where `R_j` is the residual non-generator Fourier/near-peak mass after the multiplier-shadow closure and level-lift de-duplication.

Under (H), DLI-AGG follows from the numerical condition

\[
\boxed{
\sum_j
\log_2\left(
1+R_j+M_j\,r_j\,2N_j\,2^{-(L_j+1)}
\right)
\le 100.
}
\tag{C}
\]

This is the exact aggregate statement to certify per row or prove uniformly.

---

## 3. Production-scale simplification: the 34-level arithmetic

For every row with `q < 2^256` and `2^N >= q^L`,

\[
r\,2N\,2^{-(L+1)}
= r\,N\,2^{-L}
\le 256L\,2^{-L}.
\tag{2}
\]

Proof of (2):

- If `N <= 256L`, then `r <= 1`, so

\[
rN2^{-L}\le N2^{-L}\le 256L2^{-L}.
\]

- If `N = 256L+m` with `m >= 1`, then `q < 2^256` gives

\[
r = q^L2^{-N}<2^{256L-N}=2^{-m},
\]

so

\[
rN2^{-L}< (256L+m)2^{-m}2^{-L}
\le 256L2^{-L}
\]

for `L >= 1`.

Thus the production 34-level schedule implicit in the brief's `51.2`-bit arithmetic, namely `L = 1, ..., 34`, is conditionally bounded by

\[
\sum_{L=1}^{34}
\log_2\left(1+R_L+M_L\,256L\,2^{-L}\right).
\tag{3}
\]

With no residual term and a uniform effective multiplicity `M_L <= M`, this becomes

\[
S(M)=\sum_{L=1}^{34}\log_2\left(1+M\,256L\,2^{-L}\right).
\]

Exact numerical values:

| uniform effective `M` | `S(M)` bits |
|---:|---:|
| 1 | 51.169972398501 |
| 5 | 79.702150945630 |
| 10 | 93.865052872155 |
| 13 | 99.516255311986 |
| 13.290784077959... | 100.000000000000 |
| 14 | 101.141256781990 |

So the aggregate closes under the clean sufficient condition

\[
\boxed{M_L\le 13.290784077959\ldots\quad\text{for all }1\le L\le34,
\quad R_L=0.}
\]

More generally, it closes under the exact weighted condition (3). For example, the census-scale post-closure worst value `M <= 5` leaves about

\[
100-79.702150945630 = 20.297849054370
\]

bits of aggregate slack for residual near-peak mass and shadow-factor looseness.

---

## 4. What is proved conditionally

The following theorem is immediate from (H) and the arithmetic above.

**Conditional DLI-AGG theorem.**  Consider a production tower with levels `L = 1, ..., 34`, `q < 2^256`, full half-sections, and balanced volume `2^N >= q^L` at every level. Suppose that after signed-shift quotienting, multiplier-shadow closure, and level-lift de-duplication, the excess Fourier mass satisfies

\[
E_L-1\le R_L+M_L\,r_L\,2N_L\,2^{-(L+1)}.
\]

If

\[
\sum_{L=1}^{34}
\log_2\left(1+R_L+M_L\,256L\,2^{-L}\right)
\le100,
\]

then

\[
\sum_{L=1}^{34}\log_2 E_L\le100.
\]

In particular, if `R_L = 0` and `M_L <= 13.290784077959...` for all levels, then DLI-AGG holds.

---

## 5. Remaining leaf

The remaining leaf is not the raw unweighted statement

\[
K_j=O(1)\quad\text{or}\quad K_j=\operatorname{poly}(\log q)
\]

by itself. The correct object is the **weighted effective excess ledger**

\[
M_j\,r_j\,2N_j\,2^{-(L_j+1)}
\]

plus a residual bound `R_j` for the non-shadow near-peak mass.

A replayable per-row certificate should therefore contain:

1. a Pocklington certificate for `q`;
2. the pinned primitive root and each level's `omega`;
3. the list of new independent generator representatives at their minimal levels;
4. shadow-factor bounds `s_g` after multiplier closure and lift de-duplication;
5. a residual near-peak certificate `R_j`;
6. the final rational check of condition (C).

This preserves the aggregate architecture and avoids the false printed upper bound for `E`.
