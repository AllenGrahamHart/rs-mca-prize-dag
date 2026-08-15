# Statement

For one exact support `S`, let `I_d(S)` count rank-`(10-d)` eleven-subsets.
For every `3<=d<=9`, put

```text
s_d=C(d+2,2),
L_d=C(67472+d,2),
E_d=C(K'-d-9,2),
Q_d=C(11-d,2).
```

Then

```text
(s_d L_d/E_d) I_d(S) <= Q_d I_(d-2)(S).                 (H_d)
```

If `E_d=0`, the source incidence is absent.  These seven inequalities couple
the odd and even kernel-corank chains two ranks at a time.
