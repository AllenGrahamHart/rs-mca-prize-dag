# Mersenne linear-factor projective-star router

- **status:** PROVED
- **scope:** the degree-one common-factor branch at Mersenne `e=130237`
- **residual:** an `F`-rational projective star, or factor degree at least two

Suppose the full interpolation gcd has total `(Y,Z)` degree one.  Its at
least 4,982 captured degree-five polynomial sections force its primitive
form to have constant `Y,Z` coefficients:

```text
P(X,Y,Z)=A Y+B Z+C(X),       A,B in F, (A,B)!=(0,0), deg C<=5.
```

If `A!=0`, all captured affine explanation lines pass through the common
finite center

```text
gamma_*=B/A,       c_*=-C/A.
```

If `A=0`, all have the common codeword direction `b_*=-C/B`, the projective
center at slope infinity.  Thus every linear-factor survivor is an
`F`-rational primitive-star configuration.  All nonconstant-coefficient
linear factors are impossible.
