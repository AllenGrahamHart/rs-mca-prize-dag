# DLI-CLOSE-5 fulfilment

[Pro's round-7 reply, received 2026-07-06 via user relay. Saved verbatim.
Verifier saved alongside as `pro_reply_round7_verifier.py` (PASS); independent
replay `verify_round7_reply.py` — 18/18 PASS. Verdict, band-census context,
exact-E pricing and absorption in `DLI_CLOSE_PINNED.md` § ROUND-7 RETURN.]

Outcome: **B1 refutation/certificate**, plus a conservative conditional/exceptional-set route for the remaining aggregate close.

This does **not** refute the adopted aggregate budget: it certifies four low-weight base generators, but it does not certify a complete all-weight shadow ledger with `M > M*=13.2907840779...`.  It does refute any literal sub-volume theorem of the form "a sub-volume prime has at most one multiplier-independent generator", and it supplies the exact replayable certificate requested by B1.

---

## 1. The certified sub-volume row

Take

\[
q=110849,\qquad n'=64,
\qquad N=32,
\qquad L=1.
\]

Then

\[
q-1=110848=2^8\cdot 433,
\qquad q\equiv 1\pmod {64}.
\]

The verifier proves primality by Pocklington with witness `a=3`:

\[
3^{q-1}\equiv1\pmod q,
\qquad
\gcd(3^{(q-1)/2}-1,q)=1,
\qquad
\gcd(3^{(q-1)/433}-1,q)=1.
\]

It also checks that `2` is not a primitive root and `3` is the smallest primitive root.  Therefore the pinned embedding is

\[
\omega=3^{(q-1)/64}\equiv 98761\pmod q.
\]

The order checks are

\[
\omega^{64}\equiv1\pmod q,
\qquad
\omega^{32}\equiv -1\pmod q.
\]

The R* volume guard is also satisfied:

\[
2^N=2^{32}=4294967296>110849=q^L.
\]

---

## 2. The four primitive generator relations

In \(\mathbb F_{110849}\), with \(z\mapsto \omega=98761\), the following four reduced ternary polynomials vanish:

\[
\begin{aligned}
P_1 &= 1+z^4+z^{21}-z^{27}+z^{29},\\
P_2 &= 1+z^3-z^{21}+z^{23}-z^{28},\\
P_3 &= 1+z^3-z^6-z^{25}+z^{29},\\
P_4 &= 1+z^3+z^8-z^{19}+z^{25}.
\end{aligned}
\]

Every exponent lies in the full half-section \(0\le e<32\), and every relation has weight `5`.  Since `L=1`, each is already a valid odd-moment kernel relation.

The verifier checks:

* \(P_i(\omega)\equiv0\pmod q\) for all four listed \(P_i\);
* no proper nonempty signed sub-sum of any \(P_i\) vanishes at the pinned embedding, so all four are primitive;
* exhaustive enumeration of all primitive reduced ternary vanishers of weights `3`, `4`, and `5` at this pinned embedding gives **exactly these four signed-shift classes**.

---

## 3. Sub-volume check

For `n'=64`, the signed-shift group has size `64`.  Because `n'` is a power of two, every nonzero signed shift has only the zero reduced ternary vector fixed on weights `<32`; hence the action is free on weights `3..5`.

Therefore the exact number of signed-shift orbits in the entire weight-`3..5` window is

\[
\frac{1}{64}\sum_{w=3}^{5}2^w\binom{32}{w}
=110298.
\]

Since

\[
110298<110849=q,
\]

this is a genuinely **sub-volume** window, not a forced/super-volume floor case.

---

## 4. Independence checks

The verifier checks all of the non-counting escapes printed in the brief.

### 4.1 Signed shifts

The four canonical signed-shift representatives are distinct.

### 4.2 Complete reduced-ternary multiplier check

For every ordered pair \((P_i,P_j)\), \(i\ne j\), and every signed shift \(z^sP_j\), the verifier asks whether there exists a reduced ternary multiplier

\[
m\in\{-1,0,1\}^{32}
\]

such that

\[
P_i\cdot m=z^sP_j\quad\text{in }\mathbb Z[z]/(z^{32}+1).
\]

This is checked completely as follows.  For each source \(P_i\), form the `32 x 32` integer matrix for left multiplication by \(P_i\) in \(\mathbb Z[z]/(z^{32}+1)\).  Reduce it modulo

\[
p_0=1000003.
\]

The matrix is invertible modulo \(p_0\).  If an integer reduced-ternary multiplier existed, then the unique modular solution would have every coordinate in \(\{0,1,-1\}\).  The verifier solves all `4*3*64` systems modulo \(p_0\) and in every case finds at least one coordinate outside \(\{0,1,-1\}\).  Therefore no reduced ternary multiplier exists between any two of the four orbits.

### 4.3 Level lifts

A lift from level `32` to level `64` has, after signed shift, support all of one parity.  Every listed generator has mixed parity support after every signed shift, so none is a level lift.

### 4.4 Same-norm Galois/dilation class

For each odd dilation \(z\mapsto z^a\), \(a\in(\mathbb Z/64\mathbb Z)^\times\), the verifier normalizes the dilate under signed shifts.  No listed generator lands in the dilation class of any other listed generator.

Thus the four listed relations are multiplier-independent under the stated closure conventions.

---

## 5. What this refutes, and what it does not refute

This is an exact B1 certificate:

\[
\boxed{\text{one Pocklington-certified admissible sub-volume prime with four multiplier-independent generators.}}
\]

It refutes any literal uniform second-minimum conclusion of the form

\[
M\le 1+o(1)
\quad\text{or}\quad
\text{"sub-volume primes cannot have two independent short generators".}
\]

It does **not** refute the accepted aggregate threshold.  The certified low-weight base-generator contribution is only

\[
G_{3..5}=4.
\]

There are no multiplier shadows among the four listed orbits inside the certified weight-`3..5` window, but I have **not** certified the complete all-weight shadow ledger for this row.  The certified contribution alone is below

\[
M^*=13.2907840779\ldots.
\]

So this is **B1**, not B2 and not B3.

---

## 6. Conservative A1(b) route left standing: a norm-sieve exceptional set

The B1 row says that the honest A1 theorem should not be a "never two generators" theorem.  The natural surviving form is the exceptional-set form flagged by the brief.

Here is the precise sieve leaf.

Fix a level with order \(n'=2N\), a finite normalized generator family \(\mathcal F\) of reduced ternary polynomials of weights at most \(w_{\max}\), and a prime band \([Q,2Q)\).  For \(P\in\mathcal F\), let

\[
\mathcal N(P)=\operatorname{Norm}_{\mathbb Q(\zeta_{n'})/\mathbb Q}(P(\zeta_{n'})).
\]

Since \(n'\) is a power of two, reduced exponents \(0\le e<N\) form an integral basis and a nonzero reduced ternary \(P\) is not zero in characteristic zero.  Also every complex conjugate satisfies \(|P(\zeta)|\le w_{\max}\), hence

\[
|\mathcal N(P)|\le w_{\max}^{N}.
\]

If an admissible prime \(q\ge Q\) sees \(P\) vanish at any primitive embedding, then

\[
q\mid \mathcal N(P).
\]

Therefore each fixed \(P\) can hit at most

\[
D(Q,N,w_{\max})=
\left\lfloor \frac{N\log w_{\max}}{\log Q}\right\rfloor
\]

primes in the band.  Consequently, for every integer \(k\ge1\),

\[
\#\{q\in[Q,2Q):\ q\equiv1\pmod {n'},\ G(q)\ge k\}
\le
\frac{|\mathcal F|}{k}
\left\lfloor\frac{N\log w_{\max}}{\log Q}\right\rfloor,
\]

where \(G(q)\) is the raw number of generator-family hits at \(q\).  This is deliberately conservative: it counts all primitive embeddings, not just the pinned smallest-primitive-root embedding, and it does not assume independence.

If a separate deterministic shadow cap \(s_g\le\sigma\) is certified for this family, then

\[
M(q)>M^*
\quad\Longrightarrow\quad
G(q)\ge \left\lceil\frac{M^*}{\sigma}\right\rceil,
\]

so the same display gives an explicit exceptional-set bound for the event \(M(q)>M^*\).

At the production scale described in the brief, the relevant windows are claimed to be about \(2^{216}\)-fold sub-volume.  Plugging that volume ratio into the norm-sieve display leaves an exceptional density of order

\[
2^{-216}\cdot\frac{N\log w_{\max}}{\log Q}\cdot \frac{1}{k},
\]

before the pinned-embedding saving.  This is exactly the kind of A1(b) statement the brief says would be acceptable, but it still needs the production family \(\mathcal F\), shadow cap \(\sigma\), and endpoint rule for avoiding or explicitly certifying exceptional primes.

---

## 7. Remaining status after this fulfilment

* **B1:** fulfilled by the row above.
* **B2:** not fulfilled; the certified low-weight base count is `4`, and no full shadow-weighted `M>13.29` ledger is certified.
* **B3:** not fulfilled; no aggregate budget break is produced.
* **A1:** the right uniform theorem is not `M<=1`; an average/exceptional norm-sieve form survives and is stated above with exact constants.
* **A2/R-bound:** still a separate analytic leaf.  Nothing in this B1 row creates a high residual `R`; it only shows that independent sub-volume generator multiplicity can be greater than one.

So the window did not close outright in this round, but the next target is sharper: prove the norm-sieve exceptional-set leaf with the production family and shadow cap, and pair it with the residual `R` bound.
