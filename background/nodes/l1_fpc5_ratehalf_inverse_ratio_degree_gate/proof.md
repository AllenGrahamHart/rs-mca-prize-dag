# Proof: inverse source-ratio degree gate

## 1. Inverse degree

From `DE==V mod M`, multiplication by the canonical inverse `F` gives

```text
D=rem_M(FV),                                           (1)
```

because `deg D=j<2ell`. Suppose `f=deg F<ell+a`. Since
`deg V<=s=ell-a`, one has `deg(FV)<2ell`; hence no modular reduction occurs
in `(1)` and `D=FV`. On the live branch `a<=ell/2`,

```text
f<ell+a<=2ell-a=j.
```

As `deg D=j`, the factor `V` is nonconstant. It divides both `D` and `V`,
contradicting `gcd(D,V)=1`. This proves `(RG1)` for every multiplier degree.

## 2. Exact source form of the inverse

The complement-slice source residues are

```text
E==L_1^(-1)          mod L_2,
E==lambda L_1^(-1)   mod L_3.
```

Inverting them proves `(RG2)`. The first congruence in `(RG2)` writes the
unique degree-below-`2ell` representative as

```text
F=L_1+L_2A,       deg A<ell.                          (2)
```

Reducing `(2)` modulo `L_3` and using the second congruence gives

```text
A==(lambda^(-1)-1)L_1L_2^(-1) mod L_3,
```

which is `(RG4)` by uniqueness of the degree-below-`ell` representative.

If `deg A>=1`, then `deg F=ell+deg A`; if `A` is constant, `deg F<=ell`.
Since `a>=1`, the inequality `deg F>=ell+a` is therefore equivalent to
`deg A>=a`. Multiplication by the nonzero scalar `lambda^(-1)-1` preserves
degree, so this is equivalent to `(RG5)`.

## 3. Short syzygy and common pencils

By `(RG3)`, `L_1-U L_2` is divisible by `L_3`; write it as `R L_3`.
If `u=deg U<a`, then `deg(L_1-U L_2)<=ell+u`, so `deg R<=u<a`. This proves
`(RG6)`.

For `L_i=P-z_i`, reduction modulo `L_3=P-z_3` gives

```text
U=(z_3-z_1)/(z_3-z_2),
```

a nonzero constant. It violates `(RG5)` for every `a>=1`, proving the final
claim. QED.
