# Proof

The field-router dependency gives `(PFC1)`, puts all normalized source and
outer data in `F_p`, and proves

```text
q_out=mu/lambda in mu_N\{1},
-lambda,-mu in (F_p^*)^2.                            (1)
```

Since `2N | p-1`, `-1` and every element of `mu_N` are squares in `F_p`.
In particular `lambda,mu`, and `q_out` are squares. This square-class ledger,
rather than the stronger and unavailable assertion `4N | p-1`, will be used
throughout.

We first close the harmonic branch. Substitution of `q_out=-1` in the three
matching equations gives

```text
r^2-r+1=0,       r=-1,       r^2-4r+1=0.             (2)
```

The middle alternative contradicts `r^4!=1`. The first makes `r` have order
six in characteristic greater than three, contradicting `r^(4N)=1`. In the
last alternative, `r+r^(-1)=4`. Define

```text
c_0=4,       c_(j+1)=c_j^2-2.                        (3)
```

Then `c_j=r^(2^j)+r^(-2^j)`. If the order of `r` is `2^s`, where
`3<=s<=41`, one has `c_(s-2)=0`. The hash-pinned arithmetic certificate in
the old harmonic dependency covers every official `p=1 mod 2^40` and proves
that no `c_j` vanishes for `1<=j<=38`.

Only `s=41` could remain. Such a root lies in `F_p` only in the split class
`p=1 mod 2^41`, equivalently for even `k` in

```text
p=1+k*2^40,       29058991<=k<33554432.              (4)
```

The preregistered level-39 campaign checked all `2,247,720` even values in
`(4)`. All 16 shards completed with exact contiguous coverage and no value
satisfied `c_39=0`, even before primality filtering. Its launcher, result,
and independent checker are hash-pinned in this node packet. This proves
`(PFC2)`.

The constant-ODE dependency is parameter-uniform in `M`. The transferred
boundary has `d=16M`, generic lower degree `2M-2`, and linear odd residual,
so direct substitution gives `(PFC3)`, including uniqueness of the monic
`U_0` and `kappa!=0`.

The even square-pencil norm has the form

```text
Q=(A+Z)(A+q_out Z),       Z=lambda V_0^2.             (5)
```

Because `lambda` is a square, `Z` is a polynomial square. Since harmonicity
has been excluded, subtracting `A^2` and dividing by the monic `A` gives the
unique Euclidean data

```text
S=(1+q_out)Z,       T=q_out Z^2.                     (6)
```

Conversely, if `(6)` holds and `Z=S/(1+q_out)` is a nonzero square, then
`(5)` is reconstructed. Taking outer scalars `lambda=1`, `mu=q_out` is
admissible because both `-1` and `-q_out` are squares. The field router's
matching equations then reconstruct the completion-root Mobius weld. Thus
`(6)` plus the square class of `Z` is still an exact classifier under the
weaker congruence.

Write the three matching equations uniformly as

```text
a_j(1+q_out)^2=4q_out b_j.                           (7)
```

Every displayed `a_j,b_j` is nonzero on a nonharmonic survivor. Combining
`(6)--(7)` gives `(PFC6)`. Division of `(7)` by `a_jq_out` gives

```text
q_out+q_out^(-1)=4b_j/a_j-2=y_0.                    (8)
```

The recurrence in `(PFC7)` therefore gives
`y_m=q_out^(2^m)+q_out^(-2^m)`. Necessity of `y_39=2` follows from
`q_out^N=1`. Conversely, `y_39=2` implies

```text
(q_out^N-1)^2/q_out^N=0,
```

for either root of the reciprocal quadratic, so both lie in `mu_N`. The
excluded traces `+/-2` remove `q_out=+/-1`. Since `N | p-1`, both roots lie
in `F_p`.

It remains to replace the old fourth-power step without losing the nonsplit
field class. Equation `(6)` gives the identity

```text
T/q_out=Z^2.                                         (9)
```

Because `-1` is a square in `F_p`, unique factorization proves that `Z` is a
polynomial square if and only if `Z^2` is a polynomial fourth power. Thus
`(9)` proves the exact criterion `(PFC8)` and its converse.

This criterion does not depend on the reciprocal-root choice. Replacing
`q_out` by its inverse multiplies `T/q_out` by `q_out^2`. The scalar
`q_out` is a square by `(1)`, so `q_out^2` is a fourth power. Multiplication
by it preserves the polynomial fourth-power class.

The old unscaled test is now audited precisely. If `4N | p-1`, every
`q_out in mu_N` is a fourth power. In the nonsplit class,
`v_2(p-1)=v_2(2N)`, and cyclicity of `F_p^*` gives

```text
q_out is a fourth power  iff  q_out^(N/2)=1.          (10)
```

If instead `q_out^(N/2)=-1`, its order is exactly `N`; multiplying the
fourth power in `(PFC8)` by `q_out` places `T` in the nontrivial quartic
coset. This proves the warning following `(PFC8)`.

We next transfer the constant gate. Put `a=4M-1` and `s=2M-2`. Reversing
`R=AS+T` shows that `S(0)` is the coefficient of degree `s` in the unique
truncated quotient `R_rev/A_rev`. The fourth-root truncation argument is
formal for every `M` in characteristic greater than `16M` and gives

```text
S(0)=2H_(4M-1)(t).                                   (11)
```

Evaluating the three cleared identities in `(PFC6)` at `x=0`, using
`T(0)=-1/t`, and substituting `(11)` gives exactly `(PFC10)`. The source
torsion `r^(4N)=r^(2^41)=1` gives `chi_41=2`. This proves the complete
doubled-order constant/Legendre gate.

Finally, differentiating `D_0Q=x^N-1` and using `(PFC3)` gives the same
parameter-uniform identity

```text
2xD_0R'=P+2(ND_0-xD_0')R.                           (12)
```

On an accepted branch, `(PFC8)` and `(9)` give `Z=+/-W^2`. Equation `(6)`
then makes `S` a nonzero scalar multiple of `W^2`, while `T=q_outW^4`.
Hence `W^2` divides `R=AS+T` and `W` divides `R'`. Solving `(12)` for `P`
shows `W|P`; consequently `S|P^2` and
`deg gcd(S,P)>=deg W=M-1`. This proves `(PFC11)--(PFC12)` and all claims.
QED.
