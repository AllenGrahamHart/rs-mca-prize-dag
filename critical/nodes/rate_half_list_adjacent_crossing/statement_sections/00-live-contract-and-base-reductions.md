# Rate-half ordinary-list adjacent crossing

- **status:** TARGET
- **consumer:** `list_adjacency_closing`
- **object:** ordinary Reed-Solomon worst-list size (`m=1`)

For every admissible official rate-`1/2` row `C=RS[F,D,k]`, put

```text
q=|F|,
B*=floor(q/2^128),
L_1(a)=max_u #{c in C: agr(c,u)>=a}.
```

There is an agreement index `a_L(C)` such that

```text
L_1(a_L(C)) <= B* < L_1(a_L(C)-1).                 (RHL-ADJ)
```

This is the ordinary-list rate-half input needed by
`list_adjacency_closing`. The proved `list_large_m_scope_closure` theorem then
transports the same pair to every constant common-support interleaving arity.

At the prize-max razor row

```text
n=2^41,    k=2^40,    q<2^256,
```

the proved cyclically rotated prefix floor gives

```text
L_1(k+17,179,869,183)>B*,
```

so any valid crossing satisfies

```text
a_L(C)>=k+17,179,869,184 = k+2^34.                  (RHL-LB)
```

The proved exact-integer Johnson anchor gives the first nontrivial safe
bracket. For `ell=B*+1`, define `a_IJ(C)` as the least `a` for which, on
writing `ell*a=nd+r`,

```text
n binom(d,2)+r*d > binom(ell,2)(k-1).
```

Then

```text
L_1(a_IJ(C))<=B*,       a_L(C)<=a_IJ(C).             (RHL-UB)
```

At the prize-max row, `a_IJ=3n/4` for `B*=1,2,3`, and

```text
a_IJ=floor(sqrt(n(k-1)))+1=1554944255988
```

once `B*>=332114441762`.

The first two low-budget branches are now exact. For every official
rate-half multiplicative-coset row with

```text
B* in {1,2},
```

the explicit low-budget theorem proves

```text
a_L(C)=3n/4,       L_1(3n/4)<=B*<L_1(3n/4-1).       (RHL-B12)
```

The predecessor witnesses contain respectively two and three explicit
degree-`<k` codewords. No inference is made for `B*=3` merely because its
Johnson safe anchor has the same value.

The imported affine-span compiler and its exact equality analysis give one
new necessary condition at the budget-three predecessor. For every `d>=3`,
four distinct words of `RS[F,D,2d]`, `|D|=4d`, that all agree with one
received word on at least `3d-1` coordinates must be affinely independent.
The rank-two equality case would require `2d+2` active coordinates to be
covered by only six pairwise crossings of affine-linear quotients. Hence all
thirteen chambers now carry **codeword affine rank three**. No chamber is
closed: the existing Grassmann-line/scroll rank is locator geometry, and no
bridge identifying it with codeword affine rank is proved.

The official `c=2` parity route now has a separate exact-one-antipodal
reducer. If the denominator already contains one antipodal pair, common
scaling gives

```text
Omega={1,-1,c,d},       S=c+d,       P=cd,       X=S^2.
```

Coefficient parity writes the two primary-gap terms as

```text
a_(2H-2)=F_H(X,P),       a_(2H-1)=S G_H(X,P).
```

Thus the exactly-one-pair branch has `X!=0` and requires `F_H=G_H=0`.
Complementary-root torsion is simultaneously the sign-free circuit

```text
U_0=X-2P,       V_0=P^2,
U_(j+1)=U_j^2-2V_j,       V_(j+1)=V_j^2,       0<=j<39,
U_39=2,          V_39=1.
```

The preferred coordinates separate product and ratio. Put

```text
t=c/d,       Z=t+t^(-1),       X=P(Z+2).
```

If `P_j=P^(2^j)` and `Z_(j+1)=Z_j^2-2`, complementary torsion is exactly

```text
P_39^2=1,       Z_39=2P_39.
```

The primary equations become `F_H(P(Z+2),P)=G_H(P(Z+2),P)=0`, and
distinctness is `(Z^2-4)(1+P^2-PZ)!=0`. This circuit reconstructs the roots
without a separate square test. Moreover `Z` is always in `F_p`; in the
reciprocal quadratic chamber only `P` may remain outside, with
`P^p=P^(-1)`.

These are exact two-variable representations modulo common sign and root
swap. They do not prove the circuit empty or use the secondary gap. C2-PAR
is now split into this
one-antipodal cyclotomic exclusion and a genuinely antipodal-free stratum;
neither exclusion is claimed here.

The binding open content is now the exact adjacent location for every branch
`B*>=3`: improve the safe anchor and/or construct an unsafe witness at the
predecessor of a proved safe point until the two meet. The node makes no
MCA/CA claim.
