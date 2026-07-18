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

The binding open content is now the exact adjacent location for every branch
`B*>=3`: improve the safe anchor and/or construct an unsafe witness at the
predecessor of a proved safe point until the two meet. The node makes no
MCA/CA claim.
