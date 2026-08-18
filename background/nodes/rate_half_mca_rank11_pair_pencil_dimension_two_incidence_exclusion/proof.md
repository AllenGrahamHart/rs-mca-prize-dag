# Proof

Assume for contradiction that the scalar span `W` has dimension two. Use the
coprime-direction normal form and factor the scalar-space gcd:

```text
(a_p,b_p)=(a_0,b_0)+R_p(U,V),
W=C span_F{P,Q},       gcd(P,Q)=gcd(U,V)=1.          (1)
```

For each coordinate `x`, let

```text
d_x=|{p:x in H_p}|.
```

If `C(x)=0`, every selected scalar polynomial vanishes at `x`, so every pair
codeword `(a_p,b_p)` has the same value `(a_0,b_0)`. The received pair either
matches that value, in which case `d_x>=520`, or does not, in which case
`d_x=0`. The matching coordinates form the common received-pair core `J`.

Now suppose `C(x)!=0`. Evaluation at `x` is a nonzero `F`-linear functional
on the two-dimensional scalar space `W`: after removing `C`, it cannot kill
both coprime basis polynomials `P,Q`. If two types `p,q` both contain `x` in
their cores, their pair codewords both equal the received pair there. Since
`U,V` have no common root, `(1)` then forces

```text
R_p(x)=R_q(x).
```

Thus all selected scalar points whose cores contain `x` lie in one affine
fiber of this nonzero evaluation functional. Such a fiber is an affine line
in `W`, and the proved affine-line cap gives

```text
d_x<=15                                                (2)
```

outside `J`.

Pick two distinct quotient types. On `J` their two codeword components agree;
at least one component difference is a nonzero polynomial of degree below
`K`. Hence

```text
j=|J|<=K-1.                                           (3)
```

Count core incidences first by cores and then by coordinates. Using `(2)`
and `(3)`,

```text
520s <= sum_x d_x
     <=520j+15(n-j)
     <=520(K-1)+15(n-K+1).                            (4)
```

The official integers are

```text
520s                                      =580343920,
520(K-1)+15(n-K+1)                        =560987655,
580343920-560987655                       = 19356265.
```

This contradicts `(4)`. Therefore scalar dimension two is impossible. The
preceding router already excludes dimension one and caps the dimension by
four, leaving exactly dimensions three and four. QED.
