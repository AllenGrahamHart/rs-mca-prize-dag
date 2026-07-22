# Proof

Modulo `D_k`, the summand with index `k` in `(QBC2)` vanishes because it
contains `D_k`. For every `i!=k`, the Lagrange polynomial `L_i(z)` vanishes
at `z=xi_k`, so that summand is divisible by `z-xi_k`. Hence

```text
S(z;X) is divisible by z-xi_k modulo D_k.             (1)
```

The `D_k` are pairwise coprime and have product `A`. The CRT definition of
`delta` turns `(1)` into divisibility by the monic polynomial `z-delta` in
`R_A[z]`. Since `deg_z S<=e-1`, this proves `(QBC3)`.

Let `a` be a root of `D_k`. The pair-Lagrange specialization, normalized by
the leading coefficient `q_e(a)`, is

```text
Q(z;a)=q_e(a) zI(z)/(z-xi_k).                         (2)
```

At `X=a`, the first two terms in `(CLQ6)` vanish and the last term gives

```text
F(z;a)=I(z)q_e(a)S(z;a).                              (3)
```

Evaluate the global weld `(CLQ11)` at `a`, substitute `(2)--(3)`, and
cancel the nonzero polynomial `zI(z)^2`. This gives exactly `(QBC7)`.

The smooth support partition is

```text
X^N-1=(X-s)(X-x_0)A(X)B(X)C(X).                      (4)
```

Differentiate `(4)` and evaluate at a root `a` of the squarefree polynomial
`A`. Since `a^N=1`,

```text
N a^(-1)=(a-s)(a-x_0)A'(a)B(a)C(a).                 (5)
```

Thus, as classes in `R_A`,

```text
C^(-1)=N^(-1)X(X-s)(X-x_0)A'B.                      (6)
```

Equations `(QBC3)`, `(QBC7)`, and `(6)` show that `Omega` and the expression
inside `rem_A` in `(QBC4)` agree at every root of `A`. Because `A` is
squarefree, they are equal in `R_A[z]`. The cleared-lift router gives
`deg_X Omega<=4`, and `e>=3` gives `4<2e=deg A`; hence `Omega` is already
the canonical representative of its class. This proves `(QBC4)--(QBC6)`.
Equation `(QBC8)` is the standard vanishing of the fifth divided difference
of a polynomial of degree at most four, applied coefficientwise in `z`.

For completeness, the degree collapse also reconstructs the weld without
using its asserted existence. Assume the active-row identities through
`(CLQ10)`, construct `(QBC4)`, and suppose its `X`-degree is at most four.
Set

```text
D=FQ-(AB)^2q_eP_Z-CzI^2Omega_A.                      (7)
```

At every root of `C`, `(CLQ8)` and `Q=q_eG_x` show that `D=0`, so `C`
divides `D` coefficientwise. Equations `(2)--(6)` and the definition of
`Omega_A` show that `D=0` at every root of `A`, so `A` also divides `D`.
The factors are coprime. On the other hand,

```text
deg_X D<=6e+7,       deg(AC)=8e+3>6e+7              (8)
```

for `e>=3`. Therefore `D=0`, proving the full weld and its uniqueness.
This establishes the stated equivalence.

Finally let `t` be a root of `B`. Pair-Lagrange specialization gives
`Q(z;t)=q_e(t)I(z)`, while `(CLQ6)` again gives
`F(z;t)=I(z)q_e(t)S(z;t)`. Evaluation of `(7)` at `t` proves `(QBC9)`.
Differentiating `(4)` at `t` proves `(QBC10)` exactly as in `(5)--(6)`.
QED.
