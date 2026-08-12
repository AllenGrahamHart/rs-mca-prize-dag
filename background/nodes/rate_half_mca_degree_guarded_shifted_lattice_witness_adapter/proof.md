# Proof

Use `deg 0=-infinity`.  For any nonzero lattice vector, put

```text
a=deg W,  b=deg N-k.
```

Then

```text
s_k+1=max(a,b),  s_k=max(a,b+1).
```

Therefore `s_k+1<=s_k<=s_k+1+1`.  Taking minima gives
`d1^(k+1)<=d1^(k)`.  If a vector minimizes the effective shift, its code
shift is at most one larger, so `d1^(k)<=d1^(k+1)+1`.

Let `W` have the properties in the statement and write `N=Wc`.  Since
`deg W=omega`, the effective cap is exactly

```text
deg N<=omega+k,
```

or `deg c<=k`.  The code-shift cap is exactly

```text
deg N<=omega+k-1,
```

or `deg c<k`.  These assertions also hold for `N=0`.  This proves the three
guard conditions equivalent.

The roots of `W` are `omega` distinct points of `D`, so
`T=D\Z(W)` has size `m`.  At every `x` in `T`, `W(x)` is nonzero.  The lattice
identity and `N=Wc` therefore imply

```text
U(x)=N(x)/W(x)=c(x).
```

Under the guard, `deg c<k`, giving an actual Reed-Solomon explanation.

Conversely, suppose `h` of degree below `k` explains `U` on an `m`-set `T`.
Set

```text
W=product_{x in D\T}(X-x),  N=Wh.
```

On `T` the lattice identity holds because `U=h`; off `T` it holds because
`W=0`.  The polynomial `W` is the unique monic locator of `D\T`, and `N` is
then forced by `h`.  It satisfies every guard above.  Since `m>=k`, two
degree-`<k` polynomials agreeing with `U` on `T` are equal, so the two
constructions are inverse.

Finally, every function on `T` has a unique interpolating polynomial of
degree below `m`.  A degree-`<k` polynomial agrees with `u` on `T` exactly
when the interpolant of `u|T` has degree below `k`, and similarly for `v`.
Hence simultaneous pair explanation is equivalent to both degree tests.
Failure of at least one test is exact same-support pair noncontainment.
Together with the reconstructed explanation of `u+gamma v`, this is exactly
an actual support-wise MCA-bad witness.  QED.
