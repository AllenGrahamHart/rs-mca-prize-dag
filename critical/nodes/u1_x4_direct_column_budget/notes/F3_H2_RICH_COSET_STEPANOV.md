# F3 h=2 rich-coset Stepanov theorem (Terminal B)

Status: PROVED, with explicit conservative constants.

This note removes the last black-box part of the Terminal B reconstruction at
the level needed for an explicit additive-energy theorem.  It proves the
rich-coset estimate used by `F3_H2_HBK_CONDITIONAL_COMPILER.md`; combined with
that compiler, it gives a self-contained bound

```text
E(H) <= 83851 |H|^(5/2)
```

for multiplicative subgroups `H <= F_p^*` with `|H| <= p^(2/3)`.

The constant is deliberately not optimized.  The target `C <= 100` remains a
nice sharpening problem, but Terminal B's in-house theorem no longer depends on
an imported Vinogradov-constant form of Heath-Brown--Konyagin.

## Source Map

Primary source map:

```text
Heath-Brown--Konyagin, "New bounds for Gauss sums derived from k-th powers,
and for Heilbronn's exponential sum", Quart. J. Math. 51 (2000), 221--235.
Oxford ORA record:
https://ora.ox.ac.uk/objects/uuid:f2d980d4-ef1d-4b72-89a9-3d9d8527a024
```

The construction below is the paper's Lemma-5 Stepanov argument rewritten in
the notation of this node, with all constants made explicit and with a
conservative parameter choice.

## Statement

Let `H = mu_h <= F_p^*`, `h = |H|`, and for a nonzero shift `u` define

```text
C(u) = {x in H : x - u in H}.
```

Let `U` be a set of `T >= 1` nonzero shifts, no two in the same multiplicative
coset of `H`, and put

```text
R(U) = sum_{u in U} |C(u)|.
```

If

```text
h^4 T < p^3,
```

then

```text
R(U) <= 129 * (hT)^(2/3).
```

In the energy application, `T` is always at most the number of nonzero cosets.
If `h <= p^(2/3)`, then `h^4 T <= h^3(p-1) < p^3`, so the hypothesis is
automatic.

## Proof

### 1. Normalize the shifted fibers

For each `u in U`, set

```text
D(u) = u^(-1) C(u).
```

Then the sets `D(u)` are disjoint because the shifts are chosen from distinct
`H`-cosets, and

```text
E = union_{u in U} D(u)
```

has size

```text
|E| = R(U).
```

For `x in D(u)` one has

```text
x^h = (x-1)^h = u^(-h).
```

### 2. Auxiliary polynomial

Choose integers `A,B,D >= 1` and seek a nonzero polynomial

```text
Phi(X,Y,Z) = sum lambda_{a,b,c} X^a Y^b Z^c
```

with

```text
0 <= a < A,   0 <= b < B,   0 <= c < B.
```

Put

```text
Psi(X) = Phi(X, X^h, (X-1)^h).
```

We impose linear conditions forcing `Psi` to vanish to order at least `D` at
each point of `E`.  Multiplying the `j`-th derivative by `[X(X-1)]^j` removes
denominators.  At points of `D(u)`, the derivative condition becomes the
vanishing of a polynomial `P_{j,u}(X)` of degree `< A+j <= A+D`.

Thus the number of linear conditions is at most

```text
D (A+D) T.
```

There are `A B^2` coefficients.  Hence if

```text
D (A+D) T < A B^2,                     (LS)
```

there is a nonzero `Phi` satisfying all imposed derivative conditions.

### 3. Nonvanishing

We need `Psi` not to vanish identically.  The only nonvanishing input is the
following elementary sparse-polynomial lemma.

**Sparse lemma.**  If `P(X) in F_p[X]` is a nonzero sum of `N` distinct
monomials and `deg P < p`, then `(X-1)^N` does not divide `P`.

Proof: induct on `N`.  For `N=1` this is immediate.  For `N>1`, choose one
exponent `ell0` appearing in `P`.  If `(X-1)^N | P`, then

```text
X P'(X) - ell0 P(X)
```

is divisible by `(X-1)^(N-1)` and has at most `N-1` monomials, contradicting
the induction hypothesis after choosing `ell0` so that one term is killed.

Write

```text
Phi(X,Y,Z) = sum_c Phi_c(X,Y) Z^c
```

and let `c0` be the smallest index with `Phi_c0 != 0`.  If `Psi` were zero,
then `Phi_c0(X,X^h)` would be divisible by `(X-1)^h`.

If

```text
A B <= h,       A + hB < p,             (NV)
```

then `Phi_c0(X,X^h)` is a nonzero sparse polynomial with at most `AB <= h`
distinct monomials and degree `< p`, contradicting the sparse lemma.  Therefore
`Psi` is nonzero under `(NV)`.

### 4. Degree contradiction

When `(LS)` and `(NV)` hold, `Psi` is nonzero and has at least `D|E|` roots
counted with multiplicity.  Also

```text
deg Psi < A + 2hB.
```

Therefore

```text
|E| < (A + 2hB) / D.                   (DEG)
```

### 5. Explicit parameter choice

Set the real scale parameters

```text
X = h^(2/3) T^(-1/3),    Y = h^(1/3) T^(1/3).
```

Then `XY=h` and `(hT)^(2/3)=h^2/X^2`.

If `X <= 1024`, the trivial bound `|E| <= h` gives

```text
|E| / (hT)^(2/3) = X^2/h <= sqrt(X) <= 32,
```

because `T >= 1` implies `h >= X^(3/2)`.

Assume now that `X > 1024`.  Then `h >= X^(3/2)` and `Y >= sqrt(X) > 32`.
Choose

```text
A = floor(X/4),       B = floor(Y/2),       D = floor(X/64).
```

The floor losses are harmless:

```text
A >= X/8,       B >= Y/4,       D >= X/128.
```

The linear-system inequality holds since

```text
A B^2 >= X Y^2 / 128 = X^2 T / 128
```

while

```text
D(A+D)T <= (X/64)(X/4 + X/64)T = 17 X^2 T / 4096
          < X^2 T / 128.
```

The nonvanishing inequalities hold because

```text
AB <= (X/4)(Y/2) = h/8 <= h
```

and the hypothesis `h^4 T < p^3` says `hY < p`, while also `X < p`; hence

```text
A + hB < X/4 + hY/2 < p.
```

Finally, from `(DEG)`,

```text
|E| < (A + 2hB)/D
     <= (X/4 + hY)/(X/128)
     = 32 + 128 hY/X
     = 32 + 128 (hT)^(2/3).
```

Since `X > 1024` and `T >= 1`, `(hT)^(2/3) = h^2/X^2 >= X > 1024`; hence

```text
|E| <= 129 (hT)^(2/3).
```

This proves the rich-coset estimate with explicit `K = 129`.

## Energy Consequence

The conditional compiler in `F3_H2_HBK_CONDITIONAL_COMPILER.md` proves

```text
R(U) <= K(h|U|)^(2/3) for all coset sets U
    => E(H) <= (1 + 5(K^2+K)) h^(5/2).
```

With `K=129`, this gives

```text
E(H) <= 83851 h^(5/2).
```

Consequently

```text
T_2 <= E(H)/8 <= (83851/8) h^(5/2).
```

This implies `T_2 < h^3` for

```text
h > (83851/8)^2 = 7030990201/64 < 109859222.
```

The replayed ladder rows are far below the theorem's constant but pass exactly;
using this self-contained constant alone, the remaining universal h=2 floor
certificate is a finite midrange check below `109859222`.  The additive-energy
theorem itself is fully proved here for all `h <= p^(2/3)`.

## Replay

```bash
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_rich_coset_stepanov.py
```

Expected digest:

```text
H2_RICH_COSET_STEPANOV_PASS
```
