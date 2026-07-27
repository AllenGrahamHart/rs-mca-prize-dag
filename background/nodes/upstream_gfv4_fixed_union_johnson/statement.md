# Fixed-union RS ray and list compilers

- **status:** PROVED
- **closure:** proof
- **source:** `experimental/grande_finale.tex` at upstream pin `b13de811`
- **upstream labels:** `thm:fixed-union-ray`,
  `thm:single-mds-circuit-ray`, `thm:fixed-union-list-johnson`

Let `H` be an RS parity check of redundancy `R` and let `U` contain

```text
N=R+nu
```

evaluation coordinates.

## Transverse syndrome ray

Assume `nu>=1`, `t<R`, and let `Z` be distinct finite slopes on a syndrome
line `y_0+gamma y_1`. For every `gamma in Z`, suppose there is an error
`e_gamma` supported in `U`, of weight at most `t`, and transverse in the
sense that `y_0,y_1` are not both spanned by the columns on
`supp(e_gamma)`. Then

```text
|Z| <= floor(C(R+nu,nu+1)/(R-t)).                    (FU1)
```

At `nu=1` this is

```text
|Z| <= floor(R(R+1)/(2(R-t))).                       (FU2)
```

## Fixed-syndrome list

For `t<R`, fix a syndrome `y`, put `h=N-t`, and let `L_U(y,t)` be the errors supported
in `U`, of weight at most `t`, with syndrome `y`. If `nu=0`, then
`|L_U(y,t)|<=1`. If `nu>=1` and

```text
h^2>N(nu-1),
```

then

```text
|L_U(y,t)| <= floor(N(h-nu+1)/(h^2-N(nu-1))).       (FU3)
```

Equivalently, `(FU3)` bounds the codewords in one RS list whose error
supports all lie in the fixed union `U`.
