# Proof

Put

```text
P=cd-2c-2d+1,       Q=2cd-c-d+2.
```

Then the negative-factor polynomials are `B=bP+Q` and `C=bQ+P`, so

```text
C(b)=b B(1/b).                                      (1)
```

The moving-moving template is the unordered pair
`{{2,b},{2,1/b}}`; replacing `b` by `1/b` leaves it unchanged and exchanges
its `B` and `C` loci. Thus every retained negative locus may be represented
by `B=0`.

On an actual `B=0` locus, `P` is nonzero. Indeed, `P=Q=0` would give
`2P-Q=-3(c+d)=0`, followed by `P=1-c^2=0`. This puts `c,d` among the
inversion-fixed labels `+1,-1`, contrary to admissibility. Therefore

```text
b=-Q/P.                                             (2)
```

Use `(2)` in the exact negative reconstruction `(KBSR-2)--(KBSR-4)`. At
each root of `q`, divide `G=U^2-WV^2` by the forced factor `(W-w)^2`.
Multiply the two residual quadratics, normalize their nonzero leading
coefficient, and subtract the aligned q-slice target
`((W-1/c)(W-1/d))^2`. If the leading coefficient vanished, the resultant
would have degree below eight and could not pass `(KBQS-1)`, so this monic
normalization loses no passing candidate.

Coefficient expansion gives `(KBNA-1)` for both the fixed-moving and
moving-moving templates. All displayed denominators are nonzero incidence,
label, or monic-normalization factors. A passing candidate has `m_0=0`.
Since `c,d` are nonzero and `cd!=1` by the factor theorem, `(KBNA-1)` forces

```text
cd=-1.                                              (3)
```

The convenient three-row reconstruction minor degenerates on `(3)`, but
this creates no extra solution: the parent reconstruction theorem gives
rank four for the full five-row matrix. Equivalently, clear the minor
denominator in the identities on the dense `B=0` locus and use the unique
full-matrix solution on `(3)`. The independent audit performs that direct
five-row solve.

Now `A=5cd-4c-4d+5=-4(c+d)`. The coefficient expansion on `(3)` gives

```text
m_1-m_3=4(c^2-1)/c
         =4(c-1/c)
         =-A.                                      (4)
```

If `(KBQS-1)` held, both `m_1` and `m_3` would vanish. Equation `(4)` would
then give `A=0`, contradicting the already-proved identity
`z+1=(1+w)A/E` and fixed-point-free labels, which imply `A!=0`. Thus no
aligned negative candidate passes the q-slice. QED.
