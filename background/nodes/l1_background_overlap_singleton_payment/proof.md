# Proof - L1 background-overlap singleton payment

Let two compatible codewords have background agreement sets `R_1,R_2`.
The list threshold gives, for each word,

```text
h+|R_j|>=d+ell,
|R_j|>=ell-s.                                           (1)
```

Both sets lie in the fixed `b=ell-g` point background. Inclusion-exclusion
therefore gives

```text
|R_1 intersect R_2|
 >=2(ell-s)-b
 =ell-2s+g.                                             (2)
```

The two codewords already agree on all `h=d+s` points of `X`. Their
difference has degree at most `k-1=N=d+a`, so if it is nonzero, `(2)` forces

```text
d+s+ell-2s+g<=d+a,
a+s>=ell+g.                                             (3)
```

Notice that under the negation `(BO2)`, the lower bound in `(2)` exceeds
`N-h=a-s>=0`, so it is positive; no use of a negative set-size bound is
hidden in `(3)`. Thus `(BO2)` makes every difference zero and the cell is a
singleton.

At `p<=P`, there are at most `2^M(P+1)n^P` exact petal-support patterns and
at most `n` defect degrees. Multiplying the singleton bound and using
`2^M<=n^(1/c_0)` proves `(BO3)`.

On the surviving side of `(BO2)`, substitute `s=a-c` to obtain

```text
c<=2a-ell-g.                                            (4)
```

The nonpositive-Johnson condition is `a^2<=Nc`, so `(4)` gives `(BO4)`.
The explicit equality fixture in the verifier has two distinct contributors,
which proves the strictness claim `(BO5)`.
