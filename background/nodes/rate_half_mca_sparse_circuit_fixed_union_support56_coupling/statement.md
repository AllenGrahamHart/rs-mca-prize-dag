# Fixed-union support-5/6 circuit coupling

- **status:** PROVED
- **correction dimension:** `10`

Let `V<=P_K` have dimension ten and empty common zero set.  Let `D` be a
fixed set of `u` domain points and let a fixed subspace `W<=V` of dimension
`g>=6` vanish on `D`.  Put

```text
R=K-u-g >= 0,                    N=m-u >= R+4.
```

Let `C_(d,i)` count support-`d` circuit supports containing exactly `i`
points of `D`.  For `0<=i<=3`,

```text
(6-i) C_(6,i) + (N-R-4+i) C_(5,i)
 <= C(u,i) R C(N,5-i).                              (S56)
```

Also

```text
C_(5,i) <= floor(C(u,i) R C(N,4-i)/(5-i)).          (S5)
```

For nonnegative integer weights `w5,w6`, define `L_i` as the right side of
`(S5)`, `A_i=C(u,i)R C(N,5-i)`, and

```text
lambda_i=(6-i)w5-(N-R-4+i)w6,
J_i=floor((w6 A_i + max(lambda_i,0)L_i)/(6-i)).
```

Then the complete weighted census satisfies

```text
w5 C_5+w6 C_6 <= sum_(i=0)^3 J_i
 + w5 (C(u,4)R+C(u,5))
 + w6 (floor(C(u,4)RN/2)+C(u,5)R+C(u,6)).          (WS56)
```

At `K=83,m=67555,u=29,g=6`, with selected-incidence weights
`w5=15 C(m-5,6)` and `w6=10 C(m-6,5)`, `(WS56)` is

```text
16499018112619081218909046137784886320200565035.
```

## Falsifier

A fixed union satisfying the hypotheses whose exact circuit strata violate
`(S56)`, or an arithmetic replay of the printed specialization that differs.
