# Proof - exceptional-E J-zero role/P4 compiler

Equation (DQR6), specialized to the reconstructed structural values, reads

```text
U_1=9q(c_1R_j+2c_0S_j)+c_0q^2a_d,

U_0=27(c_2R_j^2+c_1R_jS_j+c_0S_j^2)+12c_0qR_j^0.
```

Since `q!=0`, `U_1=0` is exactly `L_Phi=0`. Completing the square as in the
fully proportional parameter reduction shows that, subject to `L_Phi=0`,
`U_0=0` is exactly `W_Phi=0`. Every operation is reversible because
`c_0q!=0`. This proves the first claim in (FJR2).

For the degree ledger, the structural compiler gives uncancelled
numerator/denominator bounds

```text
R_j:(9/6),       S_j:(12/9),                       (1)
```

with numerator `q`-degrees at most four and six. A common denominator for
`L_Phi` therefore gives total degree at most 12 and `q`-degree at most six.
For `W_Phi`, the term `qR_j^0=-q^2P/(2880b)` has total numerator degree
five and `q`-degree three, while `R_j^2` has numerator/denominator bounds
`18/12` and numerator `q`-degree at most eight. A common denominator gives
the second line of (FJR3).

The substitution estimate (4) in the structural compiler says that a
polynomial of total degree `D` and `q`-degree `m` becomes degree at most
`D+2m` after clearing `q=5bM/T`. It gives `12+2*6=24` and
`18+2*8=34`, proving (FJR4)--(FJR5).

It remains to prove the `d` reconstruction. The exact quotient identity
(DQR7) is

```text
27Phi(R_j,S_j+qd/3)+c_0qP_4=U_1d+U_0.             (2)
```

On the two role filters, the right side vanishes identically in `d`. Let
`eta` satisfy (FJR6) and define `d` by (FJR7). The inherited `qR_j!=0`
guards make this legal, and

```text
S_j+qd/3=eta R_j.
```

Therefore `Phi(R_j,S_j+qd/3)=R_j^2(c_2+c_1eta+c_0eta^2)=0`. Equation (2)
and `c_0q!=0` now give `P_4=0`.

Conversely, suppose the original role equation and `P_4=0` hold on the
fully proportional chart. The parameter reduction gives
`L_Phi=W_Phi=0`. Since `R_j!=0`, put

```text
eta=(S_j+qd/3)/R_j.
```

The role equation gives (FJR6), and solving this display for `d` gives
(FJR7). The official role quadratic is separable and irreducible over the
base field, so its two roots lie in the ambient quadratic field and exhaust
the two alternatives. This proves (FJR8). All saturations and arithmetic
lifts not used here remain retained. QED.
