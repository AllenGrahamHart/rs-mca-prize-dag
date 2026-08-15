# Weighted split-pencil capacity with a common-core offset

- **status:** PROVED
- **scope:** distinct affine lines with selected petal mass `P`
- **parameters:** `P>=3`, `r>=0`, total petal mass at most `S`

Let affine owner points have integral weights `0<=s_p<=P-1`, with
`sum_p s_p<=S`.  Every distinct selected affine line `L` carries integral
masses `0<=x_(L,p)<=s_p`, supported on its owner points, with exact sum `P`.
Charge

```text
R_L=sum_p C(x_(L,p),2)+rP.
```

Put

```text
h=floor(S/(floor(P/2)+1)),       M=floor(P^2/4),
C_clean=max_(0<=ell<=S) floor(ell*((P-2)(S-ell)/2+h*r*P)).
```

Then

```text
sum_L R_L
 <= C_clean
    +floor((M+rP)C(S,2)/M)
    +C(h,2)(C(P-1,2)+rP).                         (SPO)
```

The theorem uses selected masses only.  It neither assumes that selected
support is the complete agreement set nor allows duplicate affine lines.

## Falsifier

A weighted affine-line family satisfying the printed hypotheses whose total
charge exceeds `(SPO)`; a balanced line with cross charge below `M`; a clean
dominant line reusing light-owner mass through one heavy point; or a failed
specialization in the source contract.
