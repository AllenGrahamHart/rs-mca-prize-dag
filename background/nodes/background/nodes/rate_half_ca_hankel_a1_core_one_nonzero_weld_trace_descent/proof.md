# Proof

The component deficit `C_*` is positive. Since `c` counts exactly the rows
with positive deficit, `1<=c<=C_*`, proving `(NWT2)`.

## 1. A root of `B_X`

Let `B_X(x)=0`. The products `P_X` and `B_X` partition the squarefree factors
of `G_X`, so `P_X(x)!=0`. Specializing the slope-side complement gives

```text
q_x A_x+P_cl B_x=0.                                  (1)
```

Factor as in `(NWT3)`. Since `Qhat_x` and `Phat_x` are coprime, `(1)` implies
that `Phat_x` divides `A_x` and `Qhat_x` divides `B_x`. Hence

```text
A_x=Phat_x H_x,       B_x=-Qhat_x H_x.               (2)
```

The domain-side complement specializes to

```text
R_x Qhat_x V_x+P_X(x)W_x=R_x Phat_x E_Z.             (3)
```

Because the scalar `P_X(x)` is nonzero, `R_x` divides `W_x`. Write
`W_x=R_xJ_x`; cancellation in `(3)` gives the middle identity in `(NWT4)`.
Substitution of `(2)` into the second weld identity yields

```text
P_X(x)H_xJ_x=-P_X(x)K_x,
```

and therefore `K_x=-H_xJ_x`.

The roots of `P_cl` are exactly the clean supported slopes. If `epsilon_x`
records the possible exceptional supported root, then

```text
v_x=a_x+epsilon_x.
```

The nonzero homogeneous specialization `q_x` has exact degree `e_*`, so
`deg Qhat_x=e_*-a_x=delta_x+epsilon_x`. Also

```text
deg A_x<T-D_*=deg P_cl,
```

which, after removing `Phat_x` of degree `deg P_cl-a_x`, gives
`deg H_x<a_x`. Finally the roots of `B_X` are exactly the nonsaturated rows,
so summing their positive deficits gives `C_*`. This proves `(NWT5)`.

## 2. The root of `E_Z`

Now assume `D_*=1` and specialize at `gamma_0`. Since `E_Z(gamma_0)=0`, the
domain-side complement is

```text
q_0V_0+P_XW_0=0.                                     (4)
```

Factoring as in `(NWT6)` and using coprimality gives

```text
V_0=Phat_0H_0,       W_0=-Qhat_0H_0.                 (5)
```

The other complement reads

```text
R_0Qhat_0A_0+P_cl(gamma_0)B_0=R_0Phat_0B_X.          (6)
```

The scalar `P_cl(gamma_0)` is nonzero, so `R_0` divides `B_0`. Writing
`B_0=R_0J_0` and cancelling gives the middle relation in `(NWT7)`. The first
weld identity at `gamma_0` now gives `K_0=-H_0J_0`.

The exceptional specialization has `r-1` distinct roots in `D\S`. At most
the `c` roots of `B_X` lie outside the saturated-row set, so

```text
a_0>=r-1-c.
```

Since `r-1=2e_*`, `e_*=e-b`, and here `c<=C_*=e-5b`, this is at least
`e+3b`. Also `deg q_0<=r`, hence `deg Qhat_0<=r-a_0<=c+1`. The strict bound
`deg_X V<D_0-c=deg P_X` in the complement theorem and `(5)` give
`deg H_0<a_0`. This proves `(NWT8)`.

## 3. Exhaustive descent

If every defect-row trace `K_x` vanishes, each distinct linear factor of
`B_X` divides `K`. If `D_*=1` and the exceptional trace also vanishes, the
linear factor `E_Z` divides `K`. These factors are pairwise coprime, so
`B_XE_Z|K`. The quotient `K_1` is nonzero because `K` is nonzero, and the
degree bounds in `(NWT12)` follow from the original box.

Reduce the first weld identity modulo any linear factor of `B_XE_Z`. Both
the separated term and `QK` vanish, so that prime factor divides `WB`, hence
divides `W` or `B`. Allocate every factor to one of them, obtaining
`(NWT10)`. Substitute `(NWT9),(NWT10)` into the first weld identity and
cancel the nonzero product `B_XE_Z`; this gives the first equation in
`(NWT11)`. Substitute into the second identity and cancel `Z_B`; this gives
the second equation. If some listed trace does not vanish, the active-trace
alternative applies instead. The two alternatives are exhaustive. QED.
