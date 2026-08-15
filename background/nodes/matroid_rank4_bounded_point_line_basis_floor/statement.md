# Rank-four bounded point/line basis floor

Let `M` be a loopless rank-four matroid on `m=a+r` elements, where `a>=1`
and `r>=3`.  Suppose every parallel class has size at most `a` and every
rank-two flat has size at most `a+1`.

Define

```text
h_a(r)=min(floor((a+1)/2),floor((a+r)/4)),
C_a(r)=(a+r-1)(r-1)(r-2),
L_a(r)=3(a+r-h_a(r)-1)(r-2),
Q_a(3)=6,
Q_a(r)=min(C_a(r),Q_a(r-1)+L_a(r))  for r>=4.
```

If `b(M)` is the number of unordered bases, then

```text
6 b(M) >= Q_a(r).                                  (BPL)
```

The recursive integer floor is explicitly evaluable: its coloop-reset
candidates have successive difference with sign `3h_a(x)-a-2`, so only the
base path and the one reset adjacent to that sign change can minimize.
