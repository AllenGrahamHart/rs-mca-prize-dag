# Proof

## 1. Canonical partition

The admissible source layouts form a finite set. Fixing a total order assigns
every member of `X_prim(U)` to exactly one first carried layout. The predicate
"that carried layout is full-petal and in the floor band" is therefore
Boolean. Its truth and falsehood classes are disjoint and exhaustive, proving
`(TP-PART)`.

This construction is source-level and occurs after global profile ownership.
Deleting already owned codewords cannot increase either class. In particular,
no quotient or near-quotient object receives a second charge here.

## 2. Top count

Take a codeword in `Top(U)` together with its first carried layout. By
`petal_g1_layer_maps`, every such layout-anchored full-petal floor-band
contributor is covered by the finite G1 atlas. Order that atlas as well and
assign the codeword to its first covering G1 chart. These chart classes are
now disjoint.

For a chart with `m_chi` petals, `petal_k4_primitive_bound` proves the stronger
complete-image bound

```text
#image(chi) <= m_chi+1.
```

Hence first-match summation gives

```text
#Top(U) <= sum_(chi in A_U) (m_chi+1).                       (1)
```

The exact G1 rigidity census evaluates this weighted sum. At rate `1/2`,
`t_ch=(n-k)/2=n/4` and its core cutoff is

```text
J=k+3-2t_ch=3.
```

There are two retained flavors, so

```text
sum_(chi in A_U) (m_chi+1)
 = 2(t_ch+1) sum_(j=0)^3 binom(k-1,j)
 = N_top.                                                    (2)
```

The G1 proof also proves `N_top<=n^4<n^6` on every in-scope dyadic row. At
rates `1/4`, `1/8`, and `1/16`, the same cutoff satisfies `J<0`, so the floor
band is empty for every contributor and `#Top(U)=N_top=0`.

Equations (1)-(2) prove the top cap in `(TP-CAP)`.

## 3. Common allowance

At rate `1/2`, `B_post=n^6-N_top` is nonnegative by the preceding bound and
`N_top+B_post=n^6` by definition. At the lower rates the same identity is
immediate from `N_top=0` and `B_post=n^6`.

If `(TP-OPEN)` is later proved on this same first-match partition, then

```text
#X_prim(U)
 = #Top(U)+#Post(U)
 <= N_top+B_post
 = n^6.
```

This proves the advertised consumer implication without asserting the open
Post bound.

## Layout guard

The proof starts from the first carried source layout. It never asks whether
the same codeword admits some other layout in the floor band. This preserves
the layout anchor in the G1 theorem and avoids the known re-basing
counterexample to the existential interpretation.
