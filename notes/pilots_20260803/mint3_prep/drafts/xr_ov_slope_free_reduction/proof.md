# Proof

Notation as in `statement.md`.

**PROVENANCE — READ FIRST.** The OV pilot's `REPORT.md` **write was
harness-blocked and the file does not exist in the repository**. The
full proofs survive only in an out-of-tree subagent transcript, which is
not citable from a permanent node. Every proof below is therefore
**RECONSTRUCTED** from the in-repo sources — chiefly the coordinator's
hand-check descriptions at
`notes/pilots_20260803/ov_conjecture/FABLE_AUDIT.md:7-15`, which state
the mechanisms precisely but are not themselves proofs. Steps are marked
**[H]** where the coordinator hand-verified the mechanism and **[R]**
where the reconstruction is mine alone. **Nothing here should be treated
as transplanted.** See `statement.md` FLAG 1 for the recommended fix.

---

## 0. The MDS fact

`U` carries `RS_k|_U` of dimension `k`; `W = F^U/RS_k|_U` has dimension
`m = n_U - k`. For `B <= U`, `{e_x : x in B}` is **dependent** iff some
non-zero `deg < k` polynomial is supported off `B`, i.e. vanishes on
`U \ B`; a non-zero `deg < k` polynomial has at most `k-1` roots, so this
happens iff `|U \ B| <= k-1`, i.e. `|B| >= m+1`. Hence

```text
{e_x : x in B} independent  <=>  |B| <= m.
```

## 1. THEOREM 1 (the dictionary) [H]

Each row is a substitution.

- **Pairs.** `|A_a u A_b| = n_U - |S_a ^ S_b| = n_U - (k+d) = m - d`.
  The pairwise gate is `d >= 1`, so `|A_a u A_b| <= m-1 <= m`, and by the
  MDS fact the pair-union classes are **independent**. Conversely a
  dependent pair-union would need `|A_a u A_b| >= m+1`, i.e.
  `|S_a ^ S_b| <= k-1`, violating the pairwise gate.
- **Triples.** `|A_a u A_b u A_c| = n_U - |S_a^S_b^S_c| >= n_U - (k-1)
  = m+1` exactly when gate (T) holds. By the MDS fact triple-unions are
  **dependent**.
- **Zero escape.** `x in A_a u A_b` for **every** pair `a<b` iff `x` lies
  outside at most one block, i.e. `m_x >= V-1`. Zero escape says
  `m_x <= V-3 < V-1`, so no such `x` exists and
  `^_{a<b}(A_a u A_b) = empty`.

**QED (1)**

**The wall explanation.** A "one-shot" argument of the sibling pilots'
shape concludes by exhibiting either a **dependent pair-union** (to get a
`deg < k` polynomial vanishing where it should not) or an **independent
triple-union** (to force a rank). The three rows above say the gates
**forbid both, always**. Hence no argument of that shape can close OV,
for any sharpening. This is a statement about the *method*, and it is
what makes the reduction of THEOREM 2 necessary rather than merely
convenient.

## 2. THEOREM 2 (the slope-free reduction) [H]

Let `0 != (lam, mu) in Ann`, and put `u_a := lam + z_a mu in W_a`.

**Non-degenerate branch (`lam, mu` independent).** Set
`P := span(lam, mu)`, of dimension 2. For `a != b`, `u_a` and `u_b` are
independent: a dependence would give
`(lam + z_a mu) ~ (lam + z_b mu)`, forcing `z_a = z_b`, contradicting
distinct slopes. Two independent vectors of the 2-dimensional space `P`
span it, and both lie in `W_a + W_b`; hence

```text
P = span(u_a, u_b) <= W_a + W_b     for EVERY pair a < b,
```

so `P <= ^_{a<b}(W_a + W_b) = Jperp` and `dim Jperp >= 2`.

**Degenerate branch (`lam = c mu`, or `mu = 0`).** Then a single non-zero
vector — call it `y` — lies in `W_a` for every `a` outside at most one
index; let `A` be that index set, `|A| >= V-1`. Fix `a in A`. For
`b in A \ {a}`, THEOREM 1 gives `|A_a u A_b| <= m-1`, so the classes on
`A_a u A_b` are independent and therefore

```text
W_a ^ W_b = span{e_x : x in A_a ^ A_b}.
```

All the sets `A_a ^ A_b` lie inside `A_a`, and `|A_a| = t <= m`, so the
`e_x` for `x in A_a` are independent and the intersections **compose**:

```text
^_{b in A\{a}} span(A_a ^ A_b) = span( ^_{b in A} A_b ).
```

A point of `^_{b in A} A_b` lies in `>= V-1` blocks, i.e. has
`m_x >= V-1 > V-3`, contradicting **zero escape**. So the set is empty
and `y = 0` — the degenerate branch supplies no annihilator.

Combining: `Ann != 0` forces `dim Jperp >= 2`. Contrapositive:
`Jperp = 0` (indeed `dim Jperp <= 1`) forces `Ann = 0`, **for every slope
tuple**, since `Jperp` does not mention the slopes. **QED (2)**

**Why "for every slope tuple" is the whole point.** `Ann` is defined per
slope tuple; `Jperp := ^_{a<b}(W_a + W_b)` is a function of `U` and the
blocks alone. The reduction therefore **removes the entire slope
quantifier**. This is what re-labels the sibling's 3.3e12 slope-tuple
sweep as wrong-space evidence.

## 3. THEOREMS 3 and 4 [R] — derivation-in-statement

*Not hand-verified by the coordinator; no separate proof paragraph exists
even in the out-of-tree source. Recorded at the level the source gives.*

**THEOREM 3.** Dualising, a class of `Jperp` is represented by a function
`v : U -> F` whose restriction to each `I_ab = S_a ^ S_b` agrees with some
`deg < k` polynomial `f_ab` — this is exactly the condition of lying in
`W_a + W_b` for that pair, read through the perp identity
`(W_a + W_b)^perp = L_ab * F[X]_{<d}` (`PREREG.md:30-34`). `f_ab` is
unique because `|I_ab| = k+d >= k+1` exceeds the degree bound. By THEOREM
1's zero-escape row, `union_{a<b} I_ab = U`; so if all `f_ab` coincide
they glue to a single `deg < k` polynomial agreeing with `v` on all of
`U`, i.e. `v in RS_k|_U`, i.e. the class is 0. Hence **all `f_ab` equal
`=> Jperp = 0`.**

**THEOREM 4.** Identify `v` with its interpolant in `F[X]_{<n_U}`;
`r := deg v - k` is constant on the class (adding `RS_k|_U` cannot change
the leading behaviour above degree `k`). `v` is k-flat on `I_ab` iff
`M_ab := prod_{x in I_ab}(X - x)` — monic of degree `k+d` — divides
`v - f_ab`. Since `deg f_ab < k`, this forces `deg v >= k+d`, i.e.
**`r >= d`**. Equality `r = d` holds iff `v - f_ab = c_ab M_ab` with
`c_ab` a constant, and comparing leading coefficients across pairs
forces the `c_ab` to be a common `c`; expanding `M_ab` then says the
elementary symmetric functions `e_1(I_ab), ..., e_d(I_ab)` are **constant
across pairs**. In particular for `e_1`, with
`sigma_a := sum_{x in A_a} x` and `sigma_ab := sum_{x in A_a ^ A_b} x`,
inclusion-exclusion on `I_ab` gives

```text
sigma_a + sigma_b - sigma_ab = C   (a constant, independent of the pair).
```

**QED (3),(4) — at derivation-in-statement level, machine-corroborated by
check A7 only.**

## 4. THEOREM 5 (shared-point forcing) [H]

Hypotheses: gate-clean, zero-escape, `L = 1` (every two complements meet
in exactly one point), **uniform multiplicity** `m_x = mu` on
`Y = union_a A_a`, and `char F` does not divide `V-1-mu`.

Assume the `r = d` branch is non-empty, so by THEOREM 4
`sigma_a + sigma_b - sigma_ab = C` for all pairs. **Sum over `b != a`.**
On the left, `sigma_a` appears `V-1` times. For the third term, summing
`sigma_ab` over `b != a` counts each point `x in A_a` once for each other
block containing it, i.e. `m_x - 1` times... more usefully, sum the
*second* term: `sum_{b != a} sigma_b` counts each point `x` of `Y` with
weight `m_x` minus its contribution from `a` itself. Writing
`S := sum_{x in Y} x * m_x`, the identity becomes

```text
(V-1) sigma_a + ( S - sum_{x in A_a} x m_x )  =  (V-1) C .
```

**Uniform multiplicity** gives `sum_{x in A_a} x m_x = mu * sigma_a`, so

```text
(V - 1 - mu) sigma_a = (V-1) C - S ,
```

**the same constant for every `a`**. Zero escape forces `mu <= V-3`, so
`V-1-mu >= 2`, and by hypothesis it is non-zero in `F`. Therefore **all
`sigma_a` are equal**, say `= sigma`. Then for every pair

```text
sigma_ab = sigma_a + sigma_b - C = 2 sigma - C ,
```

the **same** value. With `L = 1`, `A_a ^ A_b` is a single point `y_ab`,
and `sigma_ab` **is** that point. So all `y_ab` are the same point `y`.
But then `y in A_a` for every `a`, giving `m_y = V > V-3` — contradicting
zero escape. Hence the `r = d` branch is empty. **QED (5)**

**PG(2,3) is covered exactly:** `V=13`, `t=h=4`, `k=5`, `d=1`, `L=1`,
every point on `mu=4` lines, `V-1-mu = 8 != 0` in the fields used. The
hypotheses hold verbatim.

## 5. Honest scope

- **The `r > d` branch is OPEN and this proof cannot reach it.** THEOREM
  5 consumes exactly one equation — the `e_1` identity from THEOREM 4's
  `r = d` characterisation. At `r > d` no linear-in-the-points equation
  is available, and the obstruction becomes a dependency among the higher
  elementary symmetric functions `e_2, ..., e_{m-1}` of the pair-unions,
  for which no forcing is known.
- **THEOREM 5's hypotheses were not removed and it is not sharp.**
  MINWIT violates uniform multiplicity and is nonetheless dead — so the
  true statement is strictly stronger than what is proved, and the sharp
  form was not attempted.
- **THEOREMS 3/4 are the weakest links in this node.** No hand-check, no
  standalone proof, and the reconstruction above (particularly the step
  forcing the `c_ab` to a common constant) is mine. Line-audit target.
- **Nothing here bounds anything at prize scale.** All computations are
  toy (`q <= 41` for the linear algebra over `W`, `n_U <= 15`).
- **OV remains OPEN.** This node reduces it and settles a branch; it does
  not close it, and the two named consumers stay blocked.
