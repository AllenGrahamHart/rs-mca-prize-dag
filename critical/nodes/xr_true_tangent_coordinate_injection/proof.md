# Proof

Fix one of the stated slopes and a witness support `S`. On `S`, equality of
the line word with its explaining codeword is

```text
e_0+z e_1=0.
```

If `S` were disjoint from `T`, the pair `(c_0,c_1)` would explain `(u,v)` on
all of `S`, contradicting support-wise MCA-badness. Hence `S intersect T` is
nonempty. Choose its first coordinate `i` in a fixed order. Then

```text
e_0(i)+z e_1(i)=0,
```

and `(e_0(i),e_1(i))` is nonzero because `i in T`. A nonzero affine function
of `z` has at most one finite root. Therefore two distinct slopes cannot be
charged to the same coordinate `i`. This injects the genuine tangent slopes
into `T`, proving the bound.

The argument does not assert that an explaining codeword different from
`c_0+z c_1` is tangent-paid. Those are precisely the support-mismatch slopes
retained by the consumer.
