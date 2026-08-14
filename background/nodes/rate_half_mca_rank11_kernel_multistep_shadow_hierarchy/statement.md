# Statement

For one exact support `S`, let `I_d(S)` count rank-`(10-d)` eleven-subsets.
For every `3<=d<=9` and `2<=t<=d-1`, put

```text
s_(d,t)=C(d+2,t),
L_(d,t)=C(67472+d,t),
E_(d,t)=C(K'-d-11+t,t),
Q_(d,t)=C(9-d+t,t).
```

Then

```text
(s_(d,t)L_(d,t)/E_(d,t)) I_d(S) <= Q_(d,t) I_(d-t)(S).   (H_(d,t))
```

If `E_(d,t)=0`, the source incidence is absent.  The 28 inequalities include
the two-step nine-shadow hierarchy and add six three-step eight-shadow rows.
