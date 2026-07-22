# Proof

Choose disjoint sets of field elements

```text
A={a_1,...,a_e},       B={b_1,...,b_(2e)}.
```

Put

```text
K_0(z)=product_(a in A)(z-a),
P(z)=K_0(z) product_(b in B)(z-b),
R_i(z)=K_0(z)/(z-a_i),       i=1,2,3.               (1)
```

The polynomial `P` is squarefree, split, and has degree `3e`. The four
polynomials `K_0,R_1,R_2,R_3` are independent: `K_0` has degree `e`, while
evaluation of a relation among the `R_i` at `a_1,a_2,a_3` isolates one
coefficient at a time. Hence

```text
W=span{K_0,R_1,R_2,R_3}
```

has dimension four.

For `i in {1,2,3}` and `b in B`, define the one-root swap

```text
K_(i,b)(z)=R_i(z)(z-b)
            =K_0(z)+(a_i-b)R_i(z).                  (2)
```

Its roots are `(A\{a_i}) union {b}`, so it is a split squarefree degree-`e`
divisor of `P`. The three pencils in `(2)` meet only at `[K_0]`, and all
their other points are distinct. They therefore supply

```text
1+3|B|=6e+1
```

projective divisor classes.

Use coordinates `[a:b_1:b_2:b_3]` in the displayed basis of `W`. Every swap
pencil is one of the three lines through `[K_0]=[1:0:0:0]` in a coordinate
direction. All three lie on

```text
b_1b_2+b_2b_3+b_3b_1=0.                             (3)
```

The symmetric matrix of the direction conic, scaled by two, has determinant
two. Thus `(3)` is a rank-three quadric cone in odd characteristic. More
explicitly, the invertible coordinate change

```text
A=b_1+b_2,       B=2b_2,       C=b_2+b_3
```

turns `(3)` into `B^2=4AC`, the cone printed in the pair-complement trace.
Since `6e+1>3e-3`, `(AQF1)--(AQF2)` follow. QED.
