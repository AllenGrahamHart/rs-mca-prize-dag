# Proof

After rank-eight canonical-basis cancellation, delete all global zero-normal
coordinates and write

```text
t=K'-10-z.
```

The remaining chart has

```text
n=R+t+2,       K=t+2,       m=w+t+2,       s=2,
(R,w)=(1048576,67472).
```

Its incident normal matroid at every selected record is loopless and has
rank three.  For any one-dimensional normal span, support-local
transversality leaves at least

```text
w+s-1=w+1
```

incident normals outside that span.  Hence every parallel class has size at
most

```text
a=m-(w+1)=t+1.
```

Apply `matroid_rank3_bounded_parallel_basis_floor`.  If `b` is the number
of unordered incident bases, then

```text
2b >= (m-1)(m-1-a)
    = (w+t+1)w.
```

Thus every record owns at least `6b>=3w(w+t+1)` ordered independent
coordinate triples.  An independent triple of affine agreement
hyperplanes meets in at most one parameter point, so the number of records
is at most the floor of

```text
H(t)=(R+t)(R+t+1)(R+t+2)/(3w(w+t+1)).              (1)
```

The official range is `0<=t<=R-10`.  The successive ratio satisfies

```text
H(t+1)/H(t)-1 has the sign of 2t+3w+3-R.
```

This affine expression increases with `t`, so `H` first decreases and then
increases.  Its maximum on the official integer interval is therefore at
`t=0` or `t=R-10`.  Exact division gives

```text
floor(H(0))     = 84416263,
floor(H(R-10))  = 40828171.
```

Both next-integer gaps are positive, respectively `10721959296` and
`9846731093898357072`.  Therefore `(UC2)` holds uniformly.  The bounded
Modal replay exhausts all `1048567` integer rows as an arithmetic audit;
the proof uses the one-turn endpoint reduction.
