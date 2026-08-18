# Proof

Write the global normalized atom as `(Q,A,B,c_0,c_1)`. Fix a quotient type
`p` and any other large type `q`. Its canonical `p`-anchored edge packet
contains 18 supports owned by `p`, all containing `H_p`, and its rational
certificate is the global atom.

The packetwise pole-simple theorem says that a domain root of `Q` belongs to
at most one selected support. A point of `H_p` belongs to all 18 anchor
supports, so

```text
H_p intersection Z_D(Q)=empty.                       (1)
```

Take `x in H_p`. On two anchor supports with distinct slopes `gamma_i` and
`gamma_j`, their locators vanish at `x`, while their explanations are
`a_p+gamma b_p`. The atom equations become

```text
Q(x)(a_p(x)+gamma_i b_p(x))=A(x)+gamma_i B(x),
Q(x)(a_p(x)+gamma_j b_p(x))=A(x)+gamma_j B(x).
```

Subtracting and then back-substituting gives

```text
Q(x)b_p(x)=B(x),       Q(x)a_p(x)=A(x).              (2)
```

By definition of the pair core, `(r_0,r_1)=(a_p,b_p)` on `H_p`. Equation
`(1)` permits division by `Q(x)`, so `(2)` places `x` in the atom owner set

```text
G={x in D: r_0(x)=A(x)/Q(x), r_1(x)=B(x)/Q(x)}.
```

Thus every quotient pair core lies in `G`.

Put `s=m-2=1116046` and `c=K-1=1048575`. Distinct codeword pairs can agree
in both components on at most `c` domain points, so distinct cores satisfy
`|H_p intersection H_q|<=c`. For `q` cores let `d_x` count the cores
containing `x`. Then

```text
sum_x d_x=qs,
sum_x d_x^2=qs+2 sum_x binom(d_x,2)
             <=qs+q(q-1)c.
```

Cauchy--Schwarz therefore yields

```text
|union_p H_p| >= (qs)^2/(qs+q(q-1)c)
                =q s^2/(s+(q-1)c).                  (3)
```

The right side increases with `q` because `s>c`. At `q=520`, its exact
value is

```text
647690510540320/545326471 = 1187711.481... .
```

Taking the ceiling in `(3)` gives `|G|>=1187712`. Since
`1187712-1183521=4191`, the claimed improvement follows. QED.
