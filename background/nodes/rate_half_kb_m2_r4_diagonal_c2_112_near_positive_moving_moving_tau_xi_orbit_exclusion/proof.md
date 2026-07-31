# Proof

Use `a=2`, `(eta,ell)=(c,d)`, `w=1/c`, source edges
`{2,b},{2,1/b}`, and the three allocations in `(KBMMT-1)`.

For square-xi, the four primitive source-core digests are

```text
358028760cd7cba0 9f5ab54f14b259c8
72568ee71be7f479 48c4bf1306aae34b,
```

and their reciprocal trace digests are

```text
05c2e7899b89ec0e c627b196276df586
f0bba9bf4f23b8d2 2414ff4e8cdee299.
```

The parent eliminants have digests `1c20140f6e4a7549` and
`43a8347e92f7f81d`.  After forbidden-factor binding they leave three
components on each side.  The nine pair projections route to exactly 15
nonstandard modular factors of degrees `1,2,3,6` dividing six.  All 15
forbidden saturations are unit.

For square-ell, the core digests are

```text
a3c2f655933d7fa4 f9448c2c1e47ba1b
eb61169143695dcb 1dc3011fa04a0715,
```

and the trace digests are

```text
162035e9c06a96e0 a4fe8c32d48892ac
5d8fbd6b0b3f749d 5e2df8c7faca28bc.
```

The parent digests are `4b4738172d468601` and `48395b300501d597`.
The resulting `3x2` router has six pinned characteristic-zero projections.
Only four nonstandard modular factors have residue degree dividing six, and
all four forbidden saturations are unit.

For mixed, the core digests are

```text
7989027e9c1d34fd 2e50b8c81db25ee2
54ced314ef2e355e 0c28c5e953424d27,
```

and the trace digests are

```text
b3fe3e2204921ff2 c3cb520e5c94e733
788ff68c772c7958 4e3f87d61395b853.
```

The parent digests `610f5b1189c150ce` and `8173c0db21c9e654`
leave one component each.  Their degree-128 projection has digest
`6c0e718979cba2e1`; its complete characteristic-zero factor degrees are
standard powers plus `2,12,12,32`.  Modulo `p=2130706433`, exactly four
linear, five quadratic, and one cubic factor can meet `F_(p^6)`.  All ten
forbidden saturations are unit.

In every chart, the saturation product includes zero and collision loci,
`c,d in {2,1/2,1,-1}`, `c=d`, `cd=1`, `2s=5`, `s^2=4`, both reciprocal
fixed-point equations, the `z=1` equation, and the finite-incidence equation.

The primary reconstructs the source by direct matrix inversion and uses
resultants.  The independent no-import audit proves a fraction-free source
identity with `DomainMatrix.solve_den`, reverse-lifts every trace, and uses
terminal subresultants at both elimination layers.  Both implementations
pin the full parent and pair factor multiplicities and all 29 unit
saturations.  Therefore no admissible deployed-field point exists in any
of the three charts.  QED.
