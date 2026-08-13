# Proof

Fix an anchor `(gamma_0,c_0)` in `D`.  For every other member put

```text
p_gamma=(c_gamma-c_0)/(gamma-gamma_0).
```

On the intersection of their chosen size-`H` inside agreement sets,
`p_gamma` equals the gauged direction.  That intersection has size at least
`A=2H-e`.  Hence the intrinsic set

```text
U_p={x in E:q(x)=p(x)}
```

has size at least `A` for every represented direction `p`.

Every represented `p` is nonzero.  Indeed, `p=0` would make the member and
the anchor the same codeword, whereas on their nonempty inside intersection
that codeword would have to equal the two received words whose difference is
`(gamma-gamma_0)q`.  This is impossible because the slopes are distinct and
`q` is nonzero at every coordinate of its support `E`.

If `p!=p'`, the nonzero degree-`<K` codeword `p-p'` has at most `K-1=c`
zeros.  Thus `|U_p intersect U_p'|<=c`.  The ordinary constant-block
Johnson double count gives `(RZ1)`.

For fixed `p`, all corresponding explanations have the form
`c_0+(gamma-gamma_0)p`; together with the anchor they lie on one affine
codeword line.  The preceding nonzero-direction guard makes its outside
common core a subset of the zero set of `p`, hence of size at most `c`.
Since the layer has exactly `m-H` outside agreements and this number exceeds
`c`, outside-core line packing bounds each such line by `Q`.  The anchor is
common to every line closure, so at most `Q-1` nonanchors occur in each of
the at most `J` classes.  This proves `(RZ2)`.

The independently truncated prefix charges all deficits at most `H-1`.
The top-third theorem puts all deficits greater than `H` on one affine
line, and total-core packing bounds it by `N-m+1`.  This proves `(RZ3)`.

If the whole family exceeds budget, subtracting the exact prefix and
boundary charges gives `|T|>=343071`.  For a line of size `L` with common
core `g`, line packing says `L(m-g)<=N-g`, hence

```text
g>=ceil((Lm-N)/(L-1)).
```

At `L=343071` this is `67452=m-2`.
