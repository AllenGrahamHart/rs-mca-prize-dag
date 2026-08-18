# Cycle 451: DLI first-junction split-Pell normal form

## Starting pins

```text
our branch: codex/full-prize-resolution-v12-20260807
our SHA: b4f4dfc40
canonical prize SHA: 0dd5b3244
upstream main SHA: 93fba1be3
newest open upstream PR: #1173 (2788d5ec3)
critical mandatory-open count: 28 declarations / 27 orbit targets
```

Canonical and upstream remained unchanged.

## Action

Replace the truncated primitive-prefix description by an exact algebraic
classification surface that retains the binary alphabet and owner deletion.

## Result: PROVED split-Pell bijection

For `n=2h`, `t=2L`, interpolate on the order-`h` subgroup

```text
A(y_i)=a_i+b_i-1,       W(y_i)=x_i(a_i-b_i).
```

The first `t` moments vanish exactly when

```text
deg A<=h-L-1,       W(0)=0,       deg W<=h-L.
```

The four binary pair states are exactly equivalent to

```text
Y^h-1 | A(A^2-1),       Y^h-1 | W^2+YA^2-Y.
```

The converse reconstructs a unique binary word, and antipodal primitivity is
exactly `W!=0`. Thus `Z_0-C_1` is the nonzero-`W` split-Pell pair count. At
the official aspect `L<h/2`, the Pell quotient has degree at most `h-2L`.

Two independent exhaustive implementations on `(n,t,q)=(16,2,17)` recover
`224` total null words, `16` owner words, and `208` primitive pairs.

## Burn-down

```text
node/workboard item: reduced DLI C2'' / C2-INT
result: primitive first-junction prefix reduced to split-Pell census
DAG delta: +1 PROVED background node, +1 evidence edge
upstream delta: future Q/SPI algebraic bridge recorded; no live-PR export
delta-star movement: none
new assumptions: none
live compute requests: none
Modal spend: zero
next action: seek a counting/classification theorem for nonzero-W split-Pell
             pairs that composes with the exact tower marginals
```

## Replay

```text
tools/ramguard tiny -- python3 background/nodes/dli_first_junction_split_pell_normal_form/verify.py
tools/ramguard tiny -- python3 background/nodes/dli_first_junction_split_pell_normal_form/verify_audit.py
```
