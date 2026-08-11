# Proof

For `u=1`, the cubic router gives

```text
O=e-1,
I_E=Delta-1-I_0,
C_E=sum c_i=e+2+I_0.                                 (1)
```

The root rows consume excess degree `I_E+epsilon`, where
`epsilon=sum epsilon_i`, and every ordinary incidence consumes at least two.
The remaining excess degree is therefore

```text
R_out=C_tot-I_E-epsilon-2I_0
     =1-w-I_0-epsilon>=0.                            (2)
```

If `I_0=0` and `R_out=1`, its supported root lies away from the three
residual roots. The residual scalar is a unit there, and one excess copy
gives horizontal multiplicity one or two according as the root is new or
overlaps the minimal locator. Both contradict ordinary cube divisibility.
Thus `R_out=0`. Equation `(2)` proves `(SGN1)`. In the last regime the
ordinary incidence spends exactly two excess copies, overlaps the minimal
locator, and has horizontal/contact multiplicities three and one.

There is no new excess root outside the residual-root rows: the only
possible outside charge is the overlapping ordinary incidence. The
omission identity hence gives

```text
sum t_i=C_tot-O=e-w.                                  (3)
```

At every simple residual-root row, the vertical estimate and correction
congruence say

```text
0<=q_i=c_i+epsilon_i-t_i,       3|q_i.               (4)
```

Using `(1)`, `(3)`, and `(SGN1)` gives

```text
sum q_i=C_E+epsilon-(e-w)
       =2+I_0+epsilon+w=3.                           (5)
```

Thus exactly one `q_i` is three and the other two vanish, proving `(SGN4)`.

We now calculate locally. Write `R=R_i`, `N=N_i`, `c=c_i`, `t=t_i`, and
`q=q_i`. With no augmented incidence, the horizontal multiplicity divisor
on `R` is `2R-N`: an overlapping root has multiplicity two and a new root
has multiplicity one. The local simple-root cube identity makes the least
vertical divisor `R+N`. Since

```text
deg(R+N)=e-c+t=e-q,                                  (6)
```

the complete degree-`e` vertical divisor is `R+N+3P`, with
`deg P=q/3`. Dividing the sum of horizontal and vertical multiplicities by
three gives contact divisor `R+P`. This is `(SGN5)`.

Suppose now that the unique extra copy occurs at `J`. If `J` is new, the
horizontal divisor is `2R-N+J`. Its vertical residue changes from two to
one at `J`, and exact degree gives

```text
V=R+N-J+3P,       deg P=q/3.                         (7)
```

The contact divisor is again `R+P`, proving `(SGN6)`.

If `J` overlaps the minimal locator, its horizontal multiplicity rises from
two to three. Its positive vertical multiplicity must rise from one to
three, so the least vertical divisor is `R+N+2J`. Its degree is `e+3-q`.
Exact vertical degree and `(SGN4)` force `q=3`, with no further correction,
and the contact divisor is `R+J`. This proves `(SGN7)`.

Only the corrected row contributes one contact degree beyond its reduced
distinguished divisor. Together with the ordinary contact when `I_0=1`,
the displayed divisor has degree

```text
I_E+1+I_0=Delta.                                     (8)
```

It therefore exhausts the contact section, proving `(SGN8)`.

Finally, the three vertical fibres have class `O_C(3,0)`. Substitute
`R_i=V_i-Z_i` into `(SGN8)` and use
`O_C(div(s_F))=O_C(-rho-1,e+1)`. Rearrangement gives `(SGN9)`. Its degree
is

```text
(rho+4)e-(e+1)rho=4e-rho=e+1,                        (9)
```

because `rho=3e-1`. QED.
