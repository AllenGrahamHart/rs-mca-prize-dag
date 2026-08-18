# DLI first-junction support-overlap identity

Let `n=2h`, `t=2L`, `1<=L<h`, and let `zeta` have exact order `n` in
`F_q`. Put

```text
x_i = zeta^i,  y_i = x_i^2,  0 <= i < h.
```

For `S subset Z/h`, define `E_S` to be the number of vectors
`e in {0,1,2}^h` such that

```text
e_i=1 iff i in S,       sum_i e_i y_i^r=0  (1<=r<=L),
```

and define `O_S` to be the number of vectors `o in {-1,0,1}^h` such that

```text
o_i is in {+1,-1} iff i in S,
sum_i o_i x_i y_i^r=0  (0<=r<L).
```

Then the exact first-junction censuses satisfy

```text
Z_0 = sum_S E_S O_S,              C_1 = E_emptyset,
Z_1 = sum_S 2^|S| E_S,            B_0 = sum_S 2^(h-|S|) O_S.       (1)
```

Consequently

```text
p_S = 2^|S| E_S/Z_1,              q_S = 2^(h-|S|) O_S/B_0
```

are probability distributions and the primitive first-junction ratio is

```text
K_0^prim = 2^n(Z_0-C_1)/(Z_1B_0)
          = 2^h sum_(S nonempty) p_S q_S.                          (2)
```

For `t=2^m`, the full primitive ratio factors exactly as

```text
J_prim = K_0^prim K_tail,
K_tail = 2^(n(m-1)) Z_1/(Z_m product_(1<=j<m) B_j),                (3)
```

with the empty product and `K_tail=1` when `m=1`.

There is also an exact signed-complement description:

```text
E_S = #{epsilon in {+1,-1}^{S^c}:
        sum_(i in S^c) epsilon_i y_i^r=0, 1<=r<=L}.                (4)
```

The distinctness of the `y_i` and Vandermonde rank imply

```text
O_S=0 if 1<=|S|<=L,
E_S=0 if 1<=|S^c|<=L.                                             (5)
```

The empty signed support is an explicit exception in both statements.

