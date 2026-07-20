# Proof

The program works over `QQ` and uses exact symbolic resultants. Its
shifted-product construction is the global resultant formula, and its block
generator is the canonical quotient-orbit resultant manifest. For every
block it reduces each required Hasse derivative modulo the monic block and
computes the odd coefficient content of the Taylor resultant. The Taylor
cutoff theorem identifies the resulting prime support.

The verifier executes every one of the 12 blocks at `n=8` for cutoffs two and
three. It checks the canonical block IDs, degrees, odd contents, coefficient
hashes, the degree-49 product hash, and completeness of the packet.

The support check is independent of those resultant calculations. For each
declared prime it obtains an order-eight root of unity, forms
`A=(1-H)\{0}`, and directly counts

```text
P(t)=#{(a,b) in A^2: ab=t},
R(t)=#{(a,b) in A^2: b/a=t}.
```

It then compares the direct event

```text
exists t!=1: P(t)>=c+1 and R(t)>0
```

with divisibility of at least one computed block content by `p`. All sixteen
prime-cutoff comparisons agree, with both positive and negative cases.

Finally the audit mutates packet shape, block count, cutoff labels, and
content support, and checks that each corruption is rejected. It also forces
a synthetic timeout, exercises partial selection, and verifies rejection of
an exponent above the cap. Thus completion and timeout cannot be confused.
This exhausts the finite claim. QED.
