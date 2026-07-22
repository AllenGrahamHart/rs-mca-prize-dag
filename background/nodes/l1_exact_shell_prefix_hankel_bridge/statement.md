# L1 exact-shell prefix/Hankel bridge

- **status:** PROVED
- **role:** identify the mixed L1 residual with exact first-match prefix shells
- **consumers:** `l1_mixed_petal_amplification`, `imgfib`

## Exact prefix shells

Let `H` be an ordered `n`-point evaluation domain, let `U:H->F_q`, and fix
`k<a<=n`. For every `a`-subset `A` let `I_A(U)` be the unique polynomial of
degree below `a` agreeing with `U` on `A`. Put `w=a-k` and define

```text
Phi_(U,a)(A)=([X^k]I_A(U),...,[X^(a-1)]I_A(U)) in F_q^w. (EH1)
```

Define the exact first-match zero shell

```text
E_a(U)={A subset H: |A|=a, Phi_(U,a)(A)=0,
         Agr(U,I_A(U))=A}.                               (EH2)
```

Then `A |-> I_A(U)` is a bijection from `E_a(U)` to the degree-below-`k`
codewords having exact agreement `a` with `U`. Consequently, for every
threshold `s>k`,

```text
|ImgFib_U(s)|=sum_(a=s)^n |E_a(U)|.                     (EH3)
```

This is the exact-shell first-owner correction to the raw support fiber: a
codeword with more than `a` agreements owns only its maximal shell and does
not contribute all of its `a`-subsets to `(EH3)`.

## Sunflower/Hankel chart

Fix an admissible source layout with core `C`, `|C|=k-1`, base polynomial
`Q`, and label function `alpha:H\C->F_q` defined by

```text
U(x)=Q(x)+alpha(x)L_C(x).                               (EH4)
```

For any `A in E_a(U)` put

```text
D=C\A,       d=|D|,       X=A\C,       F=L_D.
```

Then

```text
|X|=d+w+1,       I_A(U)-Q=L_(C\D) J,
J=I_X(alpha F),                                            (EH5)
```

and multiplication by the monic locator `L_(C\D)` gives a unitriangular
isomorphism

```text
([X^(d+1)]J,...,[X^(d+w)]J)
       <-> Phi_(U,a)(A).                                (EH6)
```

Hence the global prefix zero condition is equivalent to

```text
T_(X,d)(F)=0,       deg J<=d,                           (EH7)
```

where `T_(X,d)` is the existing saturated mixed-support Hankel map. Exactness
adds precisely

```text
J(z)!=0                         for z in D,
J(y)!=alpha(y)F(y)              for y in (H\C)\X.       (EH8)
```

In particular `gcd(F,J)=1`. Conversely, `(D,X)` satisfying `(EH5)--(EH8)`
reconstructs one member of `E_a(U)`.

At the L1 threshold `s=k+sigma` with `ell=sigma+1`, the shell
`a=s+lambda` has the matching depths

```text
w=a-k=sigma+lambda=ell+lambda-1.                        (EH9)
```

## Consequence

The mixed-petal target can be attacked globally by a new row-sharp bound on
the primitive received-word exact-shell residuals `(EH2)`, with
quotient-periodic shells paid separately. This route needs no enumeration of
maximal source layouts or internal quotient/Forney recharts. The direct
fixed-source payment route remains valid as an alternative.

## Scope

The theorem supplies the exact object and a chart equivalence, not a max-fiber
bound. Existing toy power-sum Q data and the special F2 growing-order Myerson
statement do not automatically bound `(EH2)`; a received-word prefix theorem
or an explicit chart-transport theorem is still required.
`l1_received_word_barycentric_q_scope_fence` gives the exact moving-weight
formula and proves that direct consumption of upstream locator Q is not typed.
On multiplicative-coset domains,
`l1_exact_shell_complement_toeplitz_normal_form` further cancels those moving
weights into a fixed received-word Toeplitz coefficient window on the
complement locator. That is still not the same as a locator-prefix atom.
