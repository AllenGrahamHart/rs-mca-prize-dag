# Proof

## The heavy cores cannot coalesce

Fix the heavy ruling orientation from the parent router and fix the chosen
low pair attached to every one of its records. There are at most
`Q_4=58361` pair types. A singleton type owns one record, so deleting all
singletons leaves the mass in `(D24-1)` on heavy types.

For a pair `p=(a,b)`, write

```text
H_p={x:r_0(x)=a(x), r_1(x)=b(x)}.
```

Every chosen low pair has `|H_p|>=m-11`. Let `J` be the intersection of
`H_p` over the heavy types. Suppose `|J|>=K-2`, and choose exactly `K-2`
coordinates from `J`. Subtract one anchor pair, cancel their squarefree
locator from every pair difference, and delete them. The residual code has

```text
(n',K',m')=(1048578,2,67474),
```

and every residual pair agrees with the residual received pair on at least

```text
(m-11)-(K-2)=67463
```

coordinates. The dimension-two ordinary list bound is

```text
Q_2=floor(C(1048578,2)/C(67463,2))=241.
```

Since `Q_2^2` is below the deployed field size, the sub-square interleaving
collapse gives at most 241 ordered pair types. Pair noncontainment injects
the slopes owned by one fixed pair into the coordinates outside its core,
giving at most

```text
n-(m-11)=981115
```

owners. Heavy types therefore own at most `241*981115=236448715` records.
Even after restoring all possible singleton types, the orientation has at
most `236507076`, contradicting its mass by `85969283`. This proves
`(D24-2)` and `(D24-3)`.

The average over at most `Q_4` heavy types proves `(D24-4)`.

## Recover the common core with at most five pair types

Let `p_0=(a_0,b_0)` be a densest heavy type. In the reversible affine
gauge, write its correction components as `(A_0,B_0)`. For all heavy types
put

```text
W=span{A-A_0,B-B_0}.
```

Every component belongs to the heavy four-dimensional correction space, so
`dim W<=4`. Greedily choose heavy types `p_1,...,p_t` until their component
differences span `W`; then `t<=4`. Also `t>=1`, since otherwise there is
only one heavy pair type, whose `981115`-record ceiling is below
`M_heavy`.

The selected pair cores recover the complete heavy intersection:

```text
intersection_(i=0)^t H_(p_i)=J.                       (1)
```

The reverse inclusion is immediate. For the forward inclusion, a point in
all selected cores makes every selected component difference vanish. Those
components span `W`, so every heavy pair difference vanishes there; the
point lies in every heavy core.

Choose two distinct owned records from each `p_i`, `i>=1`, and choose
`32-2t` records from `p_0`. This is possible because `p_0` owns at least
5525 records. For two distinct slopes owned by one fixed pair, the
intersection of their exact supports lies in that pair core: outside the
core, subtracting the two scalar agreement equations first forces equality
of the second received column and then of the first. Hence the complete
selected-support intersection `C` lies in the right side of (1), proving
`(D24-5)`.

The two records from `p_1` cannot both have explanations on the parameterized
line of `p_0`. If they did, subtracting the identities at two distinct
slopes would give `b_1=b_0` and then `a_1=a_0`. Thus the packet contains an
off-line explanation.

## Exact cancellation and the degree pin

Let `c=|C|<K-2` and let `L_C` be its squarefree locator. Interpolate the two
received columns on `C` by degree-below-`K` polynomials `R_0,R_1`. For every
selected slope `gamma_i`, the polynomial

```text
h_i-R_0-gamma_i R_1
```

vanishes on `C` and is divisible by `L_C`. Division and deletion give an
exact shortened record on

```text
(n-c,K-c,m-c),       K-c>=3.
```

Pointwise division off `C` preserves exact supports; an explaining pair on
the shortened support lifts by multiplication with `L_C` and addition of
`(R_0,R_1)`, so support-wise MCA-badness is preserved. The shortened
supports have empty common intersection by definition of `C`.

Because `C subset H_(p_0)`, both `a_0-R_0` and `b_0-R_1` are divisible by
`L_C`. Thus the `L_0=32-2t>=24` anchor explanations remain on one affine
codeword line after division. The off-line explanation remains off that
line, since a shortened polynomial identity would multiply back to the
excluded original identity.

Let `H'(X,Z)` be the unique coefficientwise interpolation of the 32
shortened explanations, with `deg_Z H'<=31`. If
`deg_Z H'<=L_0-1`, subtract the anchor affine line. The difference has
degree at most `L_0-1` and vanishes at the `L_0` distinct anchor slopes, so
it is identically zero. This contradicts the off-line explanation. Hence

```text
deg_Z H'>=L_0>=24.
```

Subtracting the residual received line, which is affine in `Z`, does not
change a degree at least two. This proves `(D24-6)`. QED.
