# F2 antipodal-selector prefix transport

- **status:** PROVED
- **closure:** proof

Let `K` be a finite field of odd characteristic `p`, let `theta in K` have
order `2m`, and assume `p>2R`. Put

```text
D=mu_(2m)=H disjoint_union (-H),
H={theta^s:0<=s<m}.
```

For `x in {0,1}^m`, define its F2 odd-prefix syndrome and antipodal
selector by

```text
A(x)_j=sum_(s=0)^(m-1) x_s theta^(s(2j-1)),  1<=j<=R,
E_x={theta^s:x_s=1} union {-theta^s:x_s=0}.
```

Then `x -> E_x` is a bijection from the binary cube to the `m`-subsets of
`D` containing exactly one point from every antipodal pair. If

```text
c_l=sum_(s=0)^(m-1) theta^(sl),
```

its first `2R` power sums are

```text
p_l(E_x)=2 A(x)_((l+1)/2)-c_l   for l odd,
p_l(E_x)=c_l                    for l even.          (AS-1)
```

Consequently every F2 syndrome fiber is exactly the transversal part of
one ordinary central fixed-size power-sum prefix fiber on `D`, and injects
into the full fiber:

```text
#{x:A(x)=v}
 <= max_z #{E subset D: |E|=m and (p_1(E),...,p_(2R)(E))=z}.  (AS-2)
```

Since `p>2R`, Newton identities identify the latter with an ordinary
depth-`2R` split-locator prefix fiber. Thus any subexponential, polynomial,
or exact bound for that full locator fiber transfers without loss to the
F2 binary max fiber and hence, by the weighted collision sandwich, to its
weighted ternary mass.

If `m` is a power of two, every selector `E_x` is aperiodic in upstream's
stabilizer sense. Indeed any nontrivial subgroup of the cyclic group
`mu_(2m)` contains `-1`, whereas `E_x` is disjoint from `-E_x`. Therefore
no transported F2 object lies in the quotient-periodic support bucket.

The plus-branch GRS class maps and the minus-branch coupled root-code maps
have exactly this form, up to invertible row scalings. The transport also
applies to their generated-field ambient images.

This theorem removes the weighted odd-power map mismatch with upstream
`prob:capfr1-master-flatness`. It does not prove that flatness statement,
place the transported parameters inside its normalized band, or supply its
common-divisor removal and first-match owner bookkeeping. The
quotient-periodic removal is vacuous on the selector image by the preceding
aperiodicity corollary.
