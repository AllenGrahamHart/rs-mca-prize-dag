# Proof

Fix a basis `B` in a corank-`d` decorated kernel incidence and put

```text
z = number of common zero normals of ker(ev_B) outside B,
t = S-z.
```

Every extension `T` of `B` uses `d+1` of those zero normals, so one record
has at most `C(z,d+1)=C(S-t,d+1)` extensions.  The same `z` is deleted in
the support-local chart.  Thus the complete chart `t=0` contributes at most

```text
P_d C(S,d+1),
```

while every noncomplete chart contributes at most

```text
floor(F_d(t)) C(S-t,d+1).
```

For `q=d+1` and every nonzero term with `t>=1`, the unfloored successive
ratio is

```text
 F_d(t+1) C(S-t-1,q)       (R+d+t+1)(w+d+t)(S-t-q)
 --------------------  =  --------------------------------.
 F_d(t)   C(S-t,q)         (R+t)(w+d+t+1)(S-t)
```

It is strictly smaller than

```text
(1+q/(R+t))(1-q/(S-t)) < 1,
```

because `0<q/(R+t)<q/(S-t)`.  Hence every noncomplete weighted chart is
bounded by `F_d(1)C(S-1,q)`.

For `d=1,2,3`, the proved uniform caps are exactly the complete integers
`P_d`, so the larger extension count at `t=0` gives the first line.  For
`d=4,...,9`, exact cross multiplication at `K'=796599` shows

```text
F_d(1) C(S-1,d+1) > P_d C(S,d+1).
```

The ratio of the left side to the right side increases with `S`; therefore
the same branch dominates through `K'=R`.  This proves the displayed
weighted caps.  Finally, the proved all-bases decoration theorem gives at
least `d+2` bases per undecorated incidence, so summing over all fixed bases
and dividing by `d+2` is valid.
