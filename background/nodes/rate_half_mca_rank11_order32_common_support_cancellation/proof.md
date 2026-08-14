# Proof

Let

```text
L_C(X)=product_(x in C)(X-x).
```

Since `c<K`, interpolate the two received columns on `C` by polynomials
`A,B` of degree below `K`:

```text
A(x)=r_0(x),       B(x)=r_1(x)       (x in C).
```

For record `i`, the explanation identity on `C subset S_i` gives

```text
h_i(x)=r_0(x)+gamma_i r_1(x)=A(x)+gamma_i B(x).
```

Thus `L_C` divides `h_i-A-gamma_i B`. Put

```text
h_i'=(h_i-A-gamma_i B)/L_C.
```

Its degree is below `K-c`. On `D'=D\C`, where `L_C` is nonzero, define

```text
r_0'(x)=(r_0(x)-A(x))/L_C(x),
r_1'(x)=(r_1(x)-B(x))/L_C(x).
```

Then, point by point on `D'`,

```text
r_0'(x)+gamma_i r_1'(x)=h_i'(x)
```

if and only if the original slope word equals `h_i` at `x`. Hence the exact
agreement support is `S_i'=S_i\C`, of size `m-c`.

Support-wise MCA-badness is preserved. If degree-below-`K-c` polynomials
`a',b'` simultaneously explained `(r_0',r_1')` on `S_i'`, then

```text
a=A+L_C a',       b=B+L_C b'
```

would have degree below `K`. They agree with the original received columns
on `S_i'` by construction and on `C` by the interpolation identities. Thus
they would simultaneously explain the original pair on all `S_i`, contrary
to the actual record. The converse lifting identity also shows that no
information is added by the transformation.

Because `C` is the complete intersection of the original supports,

```text
intersection_i(S_i\C)=emptyset.
```

Finally,

```text
n'=n-c, K'=K-c, m'=m-c,
```

so both differences `n-K` and `m-K` are invariant. The seed compiler gives
`c<=K-4923`, hence `K'>=4923`. Direct division gives

```text
floor(2*1048576/67472)+1=31+1=32.
```

All transformations are performed on each fixed record without changing
its slope or its position in the received-line chronology. This proves the
adapter.

For the route boundary, the maximal-support slope-degree incidence theorem
on the residual common-support-free row has floor

```text
r_min(K')=ceil(32(K'+67472)/(K'+1048576)).
```

At `K'=4923` this is `ceil(2316640/1053499)=3`. The condition
`r_min(K')>=18` is the strict inequality

```text
32(K'+67472)>17(K'+1048576),
```

or `15K'>15666688`; its first integer solution is `K'=1044446`,
equivalently `c<=4130`. Thus the deployed degree-18 corollary is not a
puncture-uniform consequence of this adapter.
