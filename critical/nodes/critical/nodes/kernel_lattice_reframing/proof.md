# kernel_lattice_reframing proof

Since `p = 1 mod N'`, the finite field contains an element `zeta` of order
`N'`. For a class indicator `1_B`, the elementary sum is

```text
e1(B) = sum_{x in B} zeta^x in F_p.
```

For two classes `B,B'`, define the ternary difference vector

```text
v_x = 1_B(x) - 1_{B'}(x) in {-1,0,1}.
```

Then

```text
e1(B) - e1(B') = sum_x v_x zeta^x.
```

Thus `e1(B) = e1(B') mod p` if and only if `v` lies in the explicit kernel

```text
K_p = { v : sum_x v_x zeta^x = 0 mod p }.
```

The support of `v` has size at most `2l'`, because it is the symmetric
difference of two `l'`-classes. Known cyclotomic or quotient relations are
the already-classified kernel vectors; every additional finite-field
collision is exactly an additional sparse ternary vector in `K_p`.

Therefore the per-prime value-set certification problem is precisely a
sparse-short-vector exclusion problem in this explicit lattice/kernel model.
