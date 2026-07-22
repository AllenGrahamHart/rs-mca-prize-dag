# Proof

Either a joint codeword-pair explanation on an `A`-support exists or it does
not.

In the second case the pair is in the original globally generic scope. The
proved strip rung makes all distinct selected support intersections at most
`K`. Declaring a slope high when it participates in an intersection of size
exactly `K` and low otherwise gives a disjoint exhaustive partition. Every
low member intersects every other selected support in at most `K-1`. These
are P-A1 and P-B by definition.

Now suppose a joint explanation `(c_0,c_1)` exists. For every selected ray,
`q_z` is either zero or nonzero. If zero, the proved coordinate injection
pays the genuinely recovered-line tangent slope. If nonzero, retain it.

For a retained error `e=u+zv-p_z`, put `E=supp(e)` and `S=D\E`. If both
endpoint syndromes had lifts `a_0,a_1` supported on `E`, then
`u-a_0` and `v-a_1` would be codewords agreeing with `(u,v)` throughout
`S`, contradicting support-wise nontriviality. Conversely, any such codeword
pair gives endpoint lifts on `E`. Thus the retained ray is support-locally
transverse, although another explanation support exists. By definition the
whole retained nongeneric population is P-A2.

The two cases are exhaustive. P-A1 plus P-B costs `8n^3+8n^3` in the generic
case, while P-A2 costs `16n^3` in the nongeneric case. This proves the routing
implication without assuming any numerical target.
