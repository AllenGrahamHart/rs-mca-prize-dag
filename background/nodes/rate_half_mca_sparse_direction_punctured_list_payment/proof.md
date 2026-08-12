# Proof

For each selected slope choose an explanation `c_gamma` and exact
pair-noncontained agreement support `S_gamma` of size `m`.  Put

```text
a_gamma=c_gamma-gamma b in C.
```

Outside `E`, the direction equals `b`, so `a_gamma` agrees with `r_0` on
`S_gamma\E`, a set of size at least

```text
m-e=s+(d-e)>s.
```

Puncture `E`.  Evaluation remains injective because `N-e>=s`, and the
selected `a_gamma` belong to an ordinary Reed-Solomon list in row

```text
(N-e,s,m-e)=(R+s-e,s,d+s-e).
```

Applying the affine-span list compiler to the complete dimension-`s` code
gives at most

```text
L_e=floor(C(R-e+s,s)/C(d-e+s,s))
```

distinct punctured codewords.

It remains to control the slope multiplicity over one such codeword `a`.
Every witness must meet `E`: otherwise `r_1=b` on the whole witness and
`(a,b)` would give a simultaneous explanation of the received pair there.
Choose `x in S_gamma intersect E`.  Agreement at `x`
gives

```text
a(x)-r_0(x)=gamma q(x).
```

Since `q(x)!=0`, a fixed pair `(a,x)` determines at most one slope.  There
are `e` choices of `x`, so one punctured codeword owns at most `e` slopes.
Multiplying by `L_e` proves `(SP1)`.

Exact binomial evaluation at the two first-unpaid dimensions gives the
contract boundaries.  The bound is increasing over the checked `e` interval,
so the adjacent last-paid/first-unpaid comparison certifies the whole prefix.
