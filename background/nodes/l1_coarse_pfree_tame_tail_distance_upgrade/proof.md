# Proof - L1 coarse p-free tame-tail distance upgrade

## 1. Lower degree below the characteristic

Suppose `t<p` and, toward a contradiction, `deg W<=t-2`. At infinity,

```text
F_X'/F_X-F_Y'/F_Y = W/(F_X F_Y)=O(Z^(-t-2)).        (1)
```

The logarithmic-derivative expansions are

```text
F_X'/F_X=t/Z+sum_(j>=1) S_j(X)/Z^(j+1),
F_Y'/F_Y=t/Z+sum_(j>=1) S_j(Y)/Z^(j+1).              (2)
```

Equations `(1)--(2)` force

```text
S_j(X)=S_j(Y),       1<=j<=t.                        (3)
```

Because `t<p`, every integer `1,...,t` is invertible in `F`. Newton
identities therefore recover equality of all `t` elementary symmetric
functions. The monic degree-`t` locators are equal, contradicting disjoint
nonempty `X,Y`. Hence `deg W>=t-1`, proving `(TTD2)`.

## 2. Distance dichotomy

The Wronskian distance supplier gives

```text
deg W<=2t-d-2.                                       (4)
```

If `t<p`, combining `(TTD2)` and `(4)` yields

```text
t-1<=2t-d-2,
```

and therefore `t>=d+1`. Consequently a collision with
`t<min(d+1,p)` is impossible, so `t>=min(d+1,p)`. Combining this with the
supplier's `t>=ceil((d+2)/2)` proves `(TTD3)--(TTD4)`.

At a checkpoint depth `d>=p`, `(TTD3)` gives `t>=p`. The official router
proves `p>n/24`, yielding `(TTD5)`.

## 3. Packing and sharpness

Distinct fiber members intersect in at most `a-tau_p` points. No
`s_p=a-tau_p+1` subset can lie in two members, so the same constant-weight
double count as the supplier proves `(TTD6)`.

For the fixture over `F_5`, both pairs sum to one. Their locators are

```text
F_X=Z^2-Z,       F_Y=Z^2-Z+3.
```

They have the same derivative `2Z-1`, and direct substitution gives

```text
F_X'F_Y-F_XF_Y'=3(2Z-1)=Z+2 mod 5.
```

Thus `t=2=d+1<p` and `deg W=1=t-1`, proving sharpness.
