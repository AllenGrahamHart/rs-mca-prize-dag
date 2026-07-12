# F3 h=3 Mobius-overlap cap compiler

Status: PROVED WEIGHTED CONDITIONAL COMPILER; WEIGHTED EXCESS OPEN;
POINTWISE CAP RETAINED AS A STRONGER BACKGROUND ROUTE.

## Claim contract

Let `H<=F_p^*` have official order `n`, put `A=(1-H)\{0}`, and define

```text
P(t)=#{(a,b) in A^2: ab=t},
R(t)=#{(c,d) in A^2: d/c=t}.
```

The open assertion is

```text
M=max {P(t): t!=1 and R(t)>0} <= 35.             (M35)
```

This is weaker than a global product-fiber cap: values outside `A/A` never
enter the three-to-one convolution. It is stronger than the weighted C36'
statement, but it isolates a one-parameter, two-variable subgroup
intersection with an exact falsifier.

## Exact convolution

For `a1*a2*a3=a4`, set `t=a1*a2=a4/a3`. Conversely, a product
representation and quotient representation of the same `t` reconstruct one
ordered three-to-one tuple. Therefore

```text
N_3to1(A)=sum_t P(t)R(t).                         (M1)
```

The identity quotient has only diagonal pairs, so

```text
R(1)=|A|=n-1,
sum_(t!=1) R(t)=|A|^2-|A|=(n-1)(n-2).            (M2)
```

Writing `a=1-x`, `b=1-y`, a product representation obeys

```text
(1-x)(1-y)=t,
y=(x+t-1)/(x-1),                                 (M3)
```

so `P(t)` is a Mobius-intersection fiber on `H x H`.

## Identity fiber

At `t=1`, equation `(M3)` is `x+y=xy`. Inverting both roots identifies
`P(1)` with

```text
I=#{(u,v) in H^2:u+v=1}.
```

The optimized one-shift Stepanov theorem already proved in
`F3_H3_TRACEZERO_OFFICIAL_PAYMENT.md` gives

```text
P(1)=I<4n^(2/3).                                  (M4)
```

No new premise is being hidden in the identity term.

## C36' compiler

Under `(M35)`, equations `(M1)`--`(M4)` give

```text
N_3to1(A)
 <4n^(2/3)(n-1)+35(n-1)(n-2).                    (M5)
```

For every official `n>=8192>20^3`,

```text
4n^(5/3) <= n^2/5,
16n^(4/3) <= n^2/25.
```

Moving the fractional-power terms in `(M5)` and the repaired C36' threshold
to the same side reduces the comparison to

```text
35(n-1)(n-2)+(6/25)n^2 < 36n^2-n/2,              (M6)
```

whose right-minus-left value, after multiplication by `50`, is
`38n^2+5225n-3500>0`. Thus `(M35)` proves C36' at all 29 official orders.

The critical path uses the weaker truncated excess

```text
X_35=sum_(t!=1) max(P(t)-35,0)R(t) <= n^2/2.      (M7)
```

Adding `n^2/2` to `(M5)` still proves C36': after the same radical bounds,
the remaining gap multiplied by `50` is `13n^2+5225n-3500>0`. Thus large
individual fibers are allowed when their quotient multiplicity is small.

## Literature boundary

The unrestricted form of `(M3)` is the Mobius subgroup-intersection problem.
Konyagin--Shparlinski--Vyugin formulate a general constant-fiber conjecture
and note that the optimal absolute constant may be `9`; their theorem does
not prove it in the official near-square-root regime. The shifted-energy
theorem of Macourt--Shkredov--Shparlinski gives only an implicit
`O(n^2 log n)` fourth-moment bound here. The 2026 shifted-ratio-set theorem of
Kim--Yip--Yoo rules out a complete ratio-set decomposition but does not give a
pointwise fiber cap. None of these results is consumed as a proof of `(M35)`.

Primary sources:

- Konyagin--Shparlinski--Vyugin, *Polynomial Equations in Subgroups and
  Applications*, arXiv:2005.05315, Conjecture 1.3 and Remark 1.4.
- Macourt--Shkredov--Shparlinski, *Multiplicative Energy of Shifted
  Subgroups and Bounds On Exponential Sums with Trinomials in Finite Fields*,
  arXiv:1701.06192, Corollary 4.1.
- Kim--Yip--Yoo, *Multiplicative Irreducibility of Shifted Multiplicative
  Subgroups*, arXiv:2602.20919, Theorem 1.11.

## Evidence and replay

The first twelve official primes at `n=8192` have exact overlap maxima
`14..20`, hence `X_35=0`; the latest prefix replay is
`ap-SSyWX6F4I6C3DMzaKwx3rk`. A focused replay of the maximum-20 row found
that its quotient multiplicity is only `1` (`ap-ttBP0c2JCopfqrGmGtvnI2`).
This is evidence only.

```bash
python3 critical/nodes/f3_h3_mobius_excess_half/verify.py
```

Expected digest:

```text
H3_MOBIUS_EXCESS_COMPILER_PASS official_orders=29 baseline=35 excess=n2/2 mutation=4n2/5
```
