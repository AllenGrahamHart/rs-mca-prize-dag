# F3 h=2 in-house Stepanov reconstruction (Codex, 2026-07-08)

Status: PARTIAL.  The h=2 stratum remains closed by the existing
Heath-Brown--Konyagin/Konyagin import.  This note banks the in-house
combinatorial reduction, exact replay data, the auxiliary-polynomial ansatz,
and the precise missing steps needed to remove the import.

## Pre-registration

Stage: Terminal B.

Target theorem:

> For a multiplicative subgroup `H <= F_p^*` of size `n <= p^(2/3)`,
> prove in-house, with explicit constants, that its additive energy satisfies
> `E(H) <= C n^(5/2)`.

Success criterion:

- a self-contained proof of the energy theorem with an explicit numeric `C`;
- exact verification that the h=2 F3 stratum obeys `T_2 <= E(H)/8`, and that
  the chosen constant closes `T_2 < n^3` in the banked rows and asymptotically.

Failure/partial criterion:

- if the full energy proof stalls, bank the exact combinatorial identities, the
  auxiliary-polynomial parameter construction, and the named missing step(s).

Falsification runs:

- exact h=2 censuses through `n=512` at `q ~ n^2` and `q ~ n^3`; a row with
  measured `E(H) / n^(5/2)` exceeding a proposed constant falsifies that
  constant;
- parameter audit for the Stepanov single-shift ansatz; a row where the
  inequality system cannot produce more degrees of freedom than vanishing
  constraints falsifies the chosen ansatz.

Replay:

```text
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h2_energy_replay.py
```

Expected digest:

```text
H2_ENERGY_REPLAY_PASS
```

## What is proved here

### 1. Exact relation between F3 h=2 trades and additive energy

Let

```text
E(H) = #{(a,b,c,d) in H^4 : a+b=c+d}
```

and let `T_2` be the F3 h=2 unordered disjoint-pair count:

```text
T_2 = #{ {{a,b},{c,d}} : {a,b} cap {c,d}=empty, a+b=c+d }.
```

Let `M_2` be the midpoint count

```text
M_2 = #{(a,{b,c}) : a,b,c in H, b != c, 2a=b+c}.
```

For odd characteristic, the exact ordered-energy decomposition is

```text
E(H) = 8 T_2 + 4 M_2 + 2 n^2 - n.
```

Reason: a nontrivial unordered trade contributes `2*2*2=8` ordered
quadruples, a diagonal-to-nondiagonal midpoint collision `2a=b+c`
contributes `4`, and equal-multiset trivial quadruples contribute
`2n(n-1)+n = 2n^2-n`.  Any distinct pair with midpoint `a` is disjoint
from `a` in odd characteristic.  Therefore `T_2 <= E(H)/8`.

Catch banked: the first replay used the false identity
`E(H)=8T_2+2n^2-n`; the direct ordered-energy bucket check failed already at
`(n,q)=(16,257)`, where midpoint collisions account for the missing energy.

### 2. Exact replay data

The replay script computes the subgroup, all unordered h=2 signatures, `T_2`,
the midpoint count `M_2`, and the ordered energy via the corrected identity
above.  It verifies:

- the direct bucket count agrees with the energy identity;
- all banked rows through `n=512` satisfy `T_2 < n^3`;
- the empirical constants `E(H)/n^(5/2)` are small;
- a hypothetical explicit constant `C=100` would close the h=2 stratum for
  every `n >= 157` by `(C/8)n^(5/2) < n^3`, while the finitely many smaller
  measured rows are checked directly.

This is a replay of the data and arithmetic closure condition, not a proof of
`C=100`.

Replay output summary (exact rows `n=16,32,64,128,256,512`, each at the first
prime `q=1 mod n` above `n^2` and `n^3`):

```text
max measured E(H)/n^2.5 = 0.8906
H2_ENERGY_REPLAY_PASS
```

The only nonzero midpoint terms in this grid are:

```text
(n,q,M_2) = (16,257,16), (256,65537,1024).
```

### 3. Explicit external constant located

This does **not** complete Terminal B's in-house proof requirement, but it
sharpens the existing external import to a concrete constant.

Cochrane--Hart--Pinner--Spencer, *Waring's number for large subgroups of
`Z_p^*`*, record that Heath-Brown--Konyagin proved the Stepanov energy estimate
and that Cochrane--Pinner made the constant explicit:

```text
E(A) <= (16/3) |A|^(5/2)        for |A| < p^(2/3).
```

Source trail:

```text
https://www.math.ksu.edu/~cvs/cochrane_hart_pinner_spencer-waring_subgroup.pdf
lines 641--654 in the web extraction; references [4] and [9].
```

If that explicit external theorem is accepted as an import, then the corrected
h=2 reduction gives

```text
T_2 <= E(H)/8 <= (2/3)n^(5/2) < n^3
```

for every `n >= 1`.  The replay script prints this arithmetic gate.  Again,
this is an explicit external close, not the requested self-contained Stepanov
reconstruction.

## Stepanov reconstruction skeleton

Normalize a nonzero shift to `1`.  For

```text
I(1) = |H cap (H+1)|,
```

the classical Stepanov route constructs an auxiliary polynomial

```text
Psi(X) = Phi(X, X^n, (X+1)^n),
```

where

```text
Phi(U,V,W) = sum lambda_{a,b,c} U^a V^b W^c,
0 <= a < A, 0 <= b < B, 0 <= c < C.
```

At every `x in H cap (H+1)`, both `x^n=1` and `(x+1)^n=1`.  The
coefficients `lambda_{a,b,c}` are chosen so that `Psi` has multiplicity at
least `D` at every point of the intersection.  The usual Stepanov shape needs:

```text
ABC > D * I(1)                  (enough coefficients for vanishing)
Psi != 0                        (nonvanishing / independence)
deg Psi < D * I(1)              (degree contradiction if I(1) too large)
```

after optimizing `A,B,C,D`, yielding a single-shift estimate of shape

```text
I(mu) <= C0 n^(2/3).
```

The replay script audits one explicit parameter family for the contradiction
inequalities under the assumption `I(mu) > 4 n^(2/3)`: choose
`A=8ceil(n^(2/3))`, `B=C=ceil(n^(1/3))`, and the least `D` for which
`D*M0 > deg Psi` at `M0=floor(4n^(2/3))+1`.  In all replayed rows through
`n=512`, the audit has both coefficient slack (`ABC > D*M0`) and positive
degree margin.  This is only parameter arithmetic; the nonvanishing and
coefficient-rank argument is not yet proved in-house.

## Missing steps

### Missing B1: nonvanishing / rank lemma

Prove that the auxiliary polynomial `Psi(X)=Phi(X,X^n,(X+1)^n)` produced by the
linear system is nonzero and has the declared degree.  Equivalently, prove the
linear independence modulo the two subgroup equations needed by the
Heath-Brown--Konyagin Stepanov construction, with explicit ranges for
`A,B,C,D`.

### Missing B2: energy-level upgrade

The single-shift bound `|H cap (H+mu)| <= C0 n^(2/3)` alone gives only
`E(H) <= C0 n^(8/3)`.  The actual terminal theorem needs
`E(H) <= C n^(5/2)`, so one also needs the Konyagin/HBK dyadic level-set or
higher-convolution upgrade that bounds the distribution of large intersections,
not just their maximum.

This is the main import still not reconstructed here.

Follow-up reduction banked after the Terminal C aggregate:
`F3_H2_LEVEL_SET_REDUCTION.md` proves the exact coset-level identity

```text
E(H) = n^2 + n * sum_C r_C^2,
```

where `r_C` is the common value of `|H cap (H+s)|` on a multiplicative coset
`C=sH`.  Thus B2 is precisely the explicit L2/level-set estimate

```text
sum_C r_C^2 <= C' n^(3/2).
```

The replay `f3_h2_levelset_replay.py` verifies this identity through `n=512`;
the measured maximum is `sum_C r_C^2 / n^1.5 = 0.6406`.
