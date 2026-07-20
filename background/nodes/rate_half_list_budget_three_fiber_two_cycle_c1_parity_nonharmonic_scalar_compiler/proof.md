# Proof

The signed flat-root coloring in the even-factorization dependency is
parameter-uniform in the two-antipodal denominator. At quotient order `L` its
primitive cyclotomic resultant gives

```text
p=1 mod L  ==> p<4L^2,
p=-1 mod L ==> p<2L.                                 (1)
```

The maximal-field dependency leaves a prime field with
`p=1 mod 2^41`, or a quadratic field with `p=+/-1 mod 2^40`. The prime-field
case contradicts `p=q_field>=3*2^128>4L^2`; the negative quadratic case
contradicts `p^2<(2L)^2<3*2^128`. This proves the field line in `(CNS1)`.

Because `2L` divides `p-1`, every element of `mu_L` lies in `F_p` and is a
square there. In particular `t=r^4` lies in `F_p`, even when the top lift
`r` is anti-invariant under Frobenius. The canonical truncation recurrence
and normalized secondary-square-root uniqueness put the square-pencil
directions in `F_p[x]`. Each normalized outer factor is a product of roots
from `mu_L`, hence lies in `F_p[x]`; comparison in the two factor identities
puts their nonzero scalars `lambda,mu` in `F_p`. Root evaluation, exactly as
in the even-factorization field argument, makes `-lambda,-mu` squares.
Thus

```text
q_out=mu/lambda in mu_L\{1} subset F_p.              (2)
```

Since `-1` is a square, `lambda` and `mu` are squares as well. The constant
ODE is parameter-uniform at `M=2^36`; applying it to
`D_0=(x-1)(x-t)` proves `(CNS2)`, including uniqueness and descent of the
monic `U_0`. Therefore all Euclidean data in `(CNS3)` lie in `F_p[x]`.

The parity Mobius router proves that completion-root matching is equivalent
to one of the six equalities

```text
q_out+q_out^(-1)=tau(z_Xj).                           (3)
```

It does not require `r in F_p`; a source cross ratio may first be evaluated
in the quadratic field. On a matching branch its trace in `(3)` equals the
outer unordered trace and therefore lies in `F_p`. The harmonic-exclusion
dependency gives `q_out!=-1`, while distinct outer factors give `q_out!=1`.
This proves the exclusions in `(CNS5)`.

If `y_0=q_out+q_out^(-1)` and `y_(m+1)=y_m^2-2`, induction gives

```text
y_m=q_out^(2^m)+q_out^(-2^m).                        (4)
```

Thus `q_out^L=1` implies `y_39=2`. Conversely, if a value `y in F_p`
satisfies the terminal equation, either root of
`X^2-yX+1` obeys

```text
(q_out^L-1)^2/q_out^L=0.
```

Both roots therefore lie in `mu_L`, hence in `F_p`; the excluded traces
remove `+/-1`. This proves the exact torsion assertion in `(CNS5)`.

Write the even square pencil as

```text
Q=(A+Z)(A+q_out Z),       Z=lambda V_0^2.            (5)
```

The square class of `lambda` makes `Z` a polynomial square. Since the outer
ratio is nonharmonic, subtracting `A^2` and dividing uniquely by the monic
polynomial `A` gives

```text
S=(1+q_out)Z,       T=q_out Z^2.                     (6)
```

Putting `y=q_out+q_out^(-1)` in `(6)` yields

```text
S^2=(q_out+q_out^(-1)+2)T=(y+2)T,                   (7)
T/q_out=Z^2.                                         (8)
```

If `Z` is a square, `(8)` is a fourth power. Conversely, if
`T/q_out=W^4`, unique factorization gives `Z=+/-W^2`; because `-1` is a
square, `Z` is a polynomial square. Equations `(6)--(8)` then reconstruct
`(5)`, and taking outer scalars `1,q_out` is admissible because both
`-1,-q_out` are squares. Equation `(3)` invokes the converse of the Mobius
router, proving that `(CNS5)--(CNS7)` are sufficient as well as necessary.

The fourth-power test is independent of the reciprocal root. Replacing
`q_out` by its inverse multiplies `T/q_out` by `q_out^2`. Since `q_out` is a
square in `F_p`, this multiplier is a fourth power. Degree comparison in
`(6)--(8)` gives `deg W=M-1`.

It remains to prove the two rejection gates. The parameter-uniform
constant-coefficient Legendre collapse gives

```text
S(0)=2H_(4M-1)(t),       T(0)=-1/t.                  (9)
```

Evaluating `(7)` at zero and substituting `(9)` gives
`4tH^2+y+2=0`, proving `(CNS8)`.

Finally, differentiating `D_0Q=x^L-1` and using `(CNS2)` gives the exact
identity

```text
2xD_0R'=P_aux+2(LD_0-xD_0')R.                       (10)
```

On an accepted branch, `(6)` and `(CNS7)` make `S` a nonzero scalar
multiple of `W^2`, while `T=q_outW^4`. Hence `W^2` divides
`R=AS+T`, and `W` divides `R'`. Solving `(10)` for `P_aux` gives
`W|P_aux`; consequently `S|P_aux^2` and
`deg gcd(S,P_aux)>=deg W=M-1`. This proves `(CNS9)--(CNS10)` and all
claims. QED.

