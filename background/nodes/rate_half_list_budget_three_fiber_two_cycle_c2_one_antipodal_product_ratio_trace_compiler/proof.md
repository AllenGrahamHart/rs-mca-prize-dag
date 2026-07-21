# Proof

From `(PRT1)--(PRT2)`,

```text
P(Z+2)=cd(c/d+d/c+2)=c^2+d^2+2cd=(c+d)^2=X,
```

which proves `(PRT3)`.

The trace doubling identity gives inductively

```text
P_j=P^(2^j),
Z_j=t^(2^j)+t^(-2^j).                                 (1)
```

If `c,d in mu_N`, then `P^N=t^N=1`. At half order put

```text
epsilon_c=c^(N/2),       epsilon_d=d^(N/2).
```

Both signs lie in `{1,-1}`, and

```text
P_39=epsilon_c epsilon_d,
t^(N/2)=epsilon_c/epsilon_d=epsilon_c epsilon_d.
```

Equation `(1)` therefore gives `(PRT5)`.

Conversely suppose `(PRT5)` holds. Let `t,t^(-1)` be the roots of
`T^2-ZT+1`. Equation `(1)` and `(PRT5)` imply

```text
P^N=1,
t^(N/2)+t^(-N/2)=2P^(N/2).
```

Writing `epsilon=P^(N/2) in {1,-1}`, the second equation is

```text
(t^(N/2)-epsilon)^2/t^(N/2)=0.
```

Hence `t^(N/2)=epsilon` and in particular `t^N=1`. The full group `mu_N`
lies in the official base field, so `P,t in mu_N`. Moreover

```text
(Pt)^(N/2)=epsilon^2=1.
```

In a cyclic group of order `N`, this says exactly that `Pt` is a square.
Choose `c in mu_N` with `c^2=Pt` and put `d=P/c`. Then

```text
cd=P,       c/d=c^2/P=t.
```

The other square root replaces both roots by their negatives; replacing
`t` by `t^(-1)` swaps them. This proves exact reconstruction modulo common
sign and order.

Using `(PRT3)`, the previous primary equations become the first line of
`(PRT6)`. Its distinctness factor is the old factor rewritten as

```text
X(X-4P)((1+P)^2-X)
 =P^2(Z+2)(Z-2)(1+P^2-PZ).
```

Torsion makes `P` nonzero, so its nonvanishing is exactly the last line of
`(PRT6)`. This also shows that no independent square condition on `X` is
needed: reconstruction already gives `X=(c+d)^2`.

Finally use the official torsion-field router. In the fixed chamber, `c,d`
are fixed by Frobenius, proving `(PRT7)`. In the reciprocal chamber,

```text
P^p=c^pd^p=c^(-1)d^(-1)=P^(-1),
t^p=c^p/d^p=c^(-1)/d^(-1)=t^(-1).
```

Therefore `Z^p=t^p+t^(-p)=t^(-1)+t=Z`, proving `(PRT8)`. QED.
