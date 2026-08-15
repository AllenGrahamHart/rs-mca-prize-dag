# Proof

Let `A_0` be an attaining independent source deletion, let `Z_0` be all of
its completions, and put `B=A_0 union Z_0`.  Then

```text
|B|=(c-1)+(q-s)=q+c-1-s.                         (1)
```

For any independent target `(d-1)`-deletion `A`, define

```text
H_A={f in V:f|_A=0},       H_0={f in V:f|_(A_0)=0}.
```

Independent evaluation gives dimensions `11-d` and `11-c`.  Each space
vanishes on the complete carrier of its deletion.  Grassmann therefore
gives

```text
dim(H_A intersect H_0) >= (11-d)+(11-c)-10 = 12-c-d.    (2)
```

This is positive under `c+d<=11`.  The intersection vanishes on `U_A union
B`, so the common-root bound and `(1)` give

```text
|U_A setminus B|
 <= K-(12-c-d)-|B|
 = s+d-1.                                                (3)
```

If `s=0`, the attaining source-completion labels span the full
`q`-dimensional annihilator.  Every target circuit label therefore has a
representation on `B`.  Comparing it with its minimal target support uses
at most

```text
|B|+d=q+c+d-1<=q+10=K.
```

Vandermonde independence forces the target circuit support into `B`, giving
the first line of `(XC1)`.

Now suppose `0<s<q`.  A target circuit with exactly `j` points outside `B`
is exposed by deleting each of those `j` points.  The remaining independent
target deletion has `j-1` outside points, so `(3)` permits at most

```text
s+d-1-(j-1)=s+d-j
```

outside completions.  There are at most

```text
C(b,d-j) C(m-b,j-1)
```

such deletions, and each target circuit is counted exactly `j` times.
Multiplication, exact division by `j`, integer flooring, and summation over
`j=1..d`, together with the inside stratum, prove `(XC1)`.  Each target
circuit extends to at most `C(m-d,11-d)` selected eleven-sets.  QED.
