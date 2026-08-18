# Proof

Write the scalar span in gcd-normalized form

```text
W=C W_0,       dim_F W=4,       gcd(W_0)=1,
```

and let `J` be the coordinates where `C` vanishes and the received pair
matches the common pair-codeword value. At a root of `C`, a coordinate lies
in all 520 pair cores exactly when it lies in `J`; otherwise it lies in none.
Two selected pair codewords are distinct, so their agreement set contains
`J` and has size at most `K-1`. Hence

```text
j=|J|<=K-1.                                          (1)
```

For a coordinate `x` outside the roots of `C`, evaluation on `W_0` is a
nonzero linear functional. If at least one selected pair core contains `x`,
the coprime pair direction shows that all scalar points whose cores contain
`x` have one fixed evaluation value. They therefore lie in one affine
hyperplane of `W`, which has dimension three. Put

```text
d_x=|{p:x in H_p}|.
```

The proved affine-plane cap says that every affine plane contains at most
233 selected scalar points.

Suppose first that `d_x<=233` at every coordinate outside `J`. Counting the
incidences of the 520 cores, each of size `s=m-2=1116046`, gives

```text
520s<=520j+233(n-j).                                 (2)
```

The exact integer solution of `(2)` is

```text
j>=ceil((520*1116046-233*2097152)/(520-233))
  =319539.                                           (3)
```

This is output 1. The already proved common-core construction subtracts the
common pair, punctures `J`, and divides both received values and polynomial
explanations by the locator of `J`. It is reversible and preserves every
first-owner label, quotient deficiency two, and `m-K=67472`.

Otherwise some coordinate outside `J` has `d_x>=234`. It cannot be a
nonmatching gcd root, where the multiplicity is zero, and if it were a
matching gcd root it would belong to `J`. It is therefore outside the scalar
gcd, and its owners lie in the affine three-space evaluation fiber described
above. They cannot lie in an affine plane, because every affine plane has at
most 233 selected points. Their affine span is consequently exactly three.

Every selected quotient type owns at least 29 records. First ownership makes
the record currencies of distinct types disjoint, so the fiber owns at least

```text
234*29=6786
```

records. The coordinate lies in each type's complete core and hence in the
exact support of every one of those records. This is output 2. QED.
