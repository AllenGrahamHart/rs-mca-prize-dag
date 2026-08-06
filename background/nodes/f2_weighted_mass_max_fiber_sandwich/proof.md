# Proof

The proved collision identity gives

```text
2^m Z(A)=sum_v N(v)^2,
sum_v N(v)=2^m.
```

Choose `v_0` with `N(v_0)=M`. Keeping its term in the collision sum gives

```text
2^m Z(A) >= M^2.
```

For the reverse inequality, `N(v)^2<=M N(v)` pointwise, so

```text
2^m Z(A)=sum_v N(v)^2
          <=M sum_v N(v)
          =M 2^m.
```

Division by `2^m` proves `(MF-1)`. Substitution of `(MF-2)` into its upper
half proves `(MF-3)`.

For a nonempty fiber, choose `x_0` in it. Its binary members are precisely
the vectors in the affine coset `x_0+ker(A)` whose coordinate `i` lies in
the two-element list `{0,1}`. This is binary full-agreement list recovery.
The plus/minus consequence only instantiates this generic identity with the
already proved branch maps. QED.
