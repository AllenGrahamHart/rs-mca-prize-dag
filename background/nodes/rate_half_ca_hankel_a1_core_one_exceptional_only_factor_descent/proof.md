# Proof

In `(EFD1)`, the active-core capacity theorem says that `x_0` is the only
nonsaturated residual-domain row and that its exceptional-incidence bit is
zero. The component norm theorem says that the exceptional fiber `q_0` is
squarefree and has exactly `r-1` residual-domain roots. None is `x_0`, so all
of them are saturated rows. This proves `q_0|P_X`. Since

```text
deg P_X=D_0-1,       deg q_0=r-1,
```

the quotient `H=P_X/q_0` has degree `D_0-r`, proving `(EFD3)`.

Put `p_0=P_cl(gamma_0)`. The supported slopes are distinct, so `p_0!=0`.
Specializing the second equation of `(EFD2)` gives

```text
q_0 A(gamma_0;X)+p_0B(gamma_0;X)=q_0H.               (1)
```

Therefore `q_0|B(gamma_0;X)`. This defines the unique `J` in `(EFD4)`.
The two-sided partition theorem gives

```text
deg_X A=D_0-r-z=D_0-r-1.                             (2)
```

After dividing `(1)` by `q_0`,

```text
A(gamma_0;X)+p_0J=H.                                 (3)
```

The right side has degree `D_0-r`, while the first term on the left has
strictly smaller degree by `(2)`. Hence `deg J=D_0-r`, including its nonzero
leading coefficient. This proves all of `(EFD4)`.

The polynomial `B-QJ` vanishes modulo the linear form `E`: its specialization
at `gamma_0` is zero by construction. Hence

```text
B-QJ=E B_1                                             (4)
```

for a biform `B_1`. Substitute `(4)` into the second equation of `(EFD2)`:

```text
Q(A+P_clJ)+P_clE B_1=P_X.
```

With `A_1=A+P_clJ` and `P=P_clE`, this is the first equation of `(EFD6)`.
Equation `(3)` also gives `A_1(gamma_0)=H`. Since `A` has the smaller degree
in `(2)` and `J` has degree `D_0-r`, this proves `(EFD7)`.

Substituting `(4)` into the third equation of `(EFD2)` gives

```text
QWJ+E(WB_1-1)=QK,
E(WB_1-1)=Q(K-WJ).                                   (5)
```

The linear form `E` does not divide `Q`, because its specialization is the
nonzero polynomial `q_0`. Thus `gcd(E,Q)=1`, and `(5)` proves

```text
WB_1-1=QK_1,       K-WJ=E K_1                        (6)
```

for one biform `K_1`. This proves `(EFD5)` and the second equation of
`(EFD6)`.

Finally use the first equation of `(EFD2)`, the first equation of `(EFD6)`,
and `(6)`:

```text
P_X=QA_1+PB_1
   =QA_1+(QV+P_XW)B_1
   =Q(A_1+VB_1)+P_X(1+QK_1).
```

Cancellation gives `A_1+VB_1+P_XK_1=0`, the last equation of `(EFD6)`.

The earlier trace-free contradiction used the strict global bound
`deg_X A_1<=D_0-r-1`. Here `(EFD7)` proves equality at `D_0-r`, so that
argument cannot be imported. The descent is exact but is not a closure. QED.
