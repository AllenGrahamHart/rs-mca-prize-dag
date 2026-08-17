# Proof

Restrict the original evaluation matroid of `V` to the `N=m-u` points
outside `D`.  Let an independent original-matroid triple span a rank-three
flat.  Its annihilator in `V` has dimension seven, so intersection with
`W` has dimension at least `g-3`.  Every polynomial in this intersection
vanishes on `D` and on the complete original-matroid closure of the triple.
After dividing the squarefree locator of `D`, we obtain at least `g-3`
independent polynomials of degree at most `K-1-u`.

An `r`-dimensional polynomial subspace of degree at most `e` has common
factor degree at most `e-r+1`: after removing its gcd, the quotient space
still has dimension `r`, so its maximum degree is at least `r-1`.  Therefore
the rank-three flat has at most

```text
(K-1-u)-(g-3)+1=K-u-g+3=B
```

outside points.  Repeating the argument for an independent four-set leaves
dimension at least `g-4` and gives rank-four flat size at most `B+1`.

Let `C_4,C_5` count entirely-outside circuits in this original restricted
matroid.  The rank-five flat-circuit coupling theorem gives

```text
5 C_5<=R C(N,4)-(N-B)C_4.                          (1)
```

Ordinary completion exposure gives

```text
C_4<=floor(R C(N,3)/4).                            (2)
```

Equation `(1)` also forces
`C_4<=floor(R C(N,4)/(N-B))`, hence `C_4<=X_4`.

Write `S_4=C(m-4,7)` and `S_5=C(m-5,6)`.  Increasing `C_4` by one lowers
the integer upper envelope for `C_5` by at most
`ceil((N-B)/5)`.  Since `21S_4=3(m-4)S_5` and

```text
15 ceil((N-B)/5) S_5<=3(N-B+4)S_5,
3[(m-4)-(N-B+4)]=3(K-g-5)>=0,
```

the weighted envelope is nondecreasing in `C_4`.  It is maximized at
`C_4=X_4`, where `(1)` gives `C_5<=X_5`.

For a circuit with exactly `j<d` points outside `D`, expose each outside
point in turn.  The completion-stratified fixed-union theorem leaves at most
`R` outside completions, yielding exactly `(FU2)`.  Add these lower strata
to `X_4,X_5` and multiply by the selected-eleven-set extension factors.
This proves `(FU4)`. QED.
