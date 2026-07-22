# L1 m=4, h=3 colored cyclic-code equivalence

- **status:** PROVED
- **dependencies:** `l1_mersenne_checkpoint_cyclotomic_normal_form`,
  `l1_official_max_split_value_complement_census`
- **consumer:** `l1_mixed_petal_amplification`

Fix one of the four official Mersenne rows with

```text
N=p+1,       n=4N,       p=1 mod 3,                    (CC3-1)
```

and choose `omega in F_p` with `omega^2+omega+1=0`. Let `C_M` be the
prime-field cyclic code of exponent words whose Fourier transform vanishes
on the exact cyclotomic closure `S` from
`l1_mersenne_checkpoint_cyclotomic_normal_form`.

There is a normalized degree-`p` split pencil with exactly three complete
fibers in the order-`n` domain if and only if there is a coefficient word
`b=(b_i)` satisfying all of the following:

```text
b_i in {0,1,omega,omega^2};
# {i:b_i=1}=# {i:b_i=omega}=# {i:b_i=omega^2}=p;
b in C_M;
b^[2] in C_M,                                           (CC3-2)
```

where `b^[2]` denotes coefficientwise squaring. Equivalently, the two
Fourier transforms vanish on all of `S`. The three color classes are the
three complete fibers, and every triple is represented after assigning its
three classes the three colors.

The coefficientwise cube is the union indicator:

```text
b^[3]=1_(X_0 union X_1 union X_2),
# {i:b_i=0}=n-3p=p+4=N+3.                              (CC3-3)
```

Thus the `m=4,h=3` frontier is exactly a two-Schur-section problem inside the
explicit low-weight Mersenne cyclic code, with a complement only four points
larger than one `p`-fiber. The embedded odd pencils cannot occur here because
their split-value degree is even.

This equivalence does not prove that the section is empty, classify its
components, bound nonembedded `h=2`, treat `m=8,16`, or close L1.
