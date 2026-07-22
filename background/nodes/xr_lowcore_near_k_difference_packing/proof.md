# Proof - XR low-core near-K oriented-difference packing

## 1. Unique subset ownership

Take distinct `I,J in R_(X,Y)`. The two members `X union I` and `X union J`
of `mathcal F` share the fixed set `X`, so `(NK1)` gives

```text
t+|I intersect J|<=K-1.                               (1)
```

With `c=K-t`, this is

```text
|I intersect J|<=c-1.                                 (2)
```

Every residual has size

```text
a-t=K+h-(K-c)=H+c-1=w                                 (3)
```

inside the `v=N-2t=N-2K+2c` coordinates outside `X union Y`. Since `c>=1`
and `w>=c`, each residual owns `binom(w,c)` distinct `c`-subsets. Equation
`(2)` says that these owned subsets are disjoint between residuals. There are
only `binom(v,c)` ambient `c`-subsets, hence

```text
|R_(X,Y)| binom(w,c)<=binom(v,c).                      (4)
```

Taking the integer floor proves `(NK4)`.

## 2. Aggregate energy

For every nonzero oriented difference, its fiber size counts the ordered
support pairs producing that difference. Therefore

```text
sum_((X,Y) nonzero) |R_(X,Y)|=M(M-1).                 (5)
```

Restricting to widths indexed by `C` and applying `(NK4)` gives

```text
E_C=sum_(c in C) sum_(width K-c fibers) |R_(X,Y)|^2
   <=max_(c in C)R_c
       sum_(c in C) sum_(width K-c fibers)|R_(X,Y)|
   <=max_(c in C)R_c M(M-1).                          (6)
```

This is `(NK5)`. If the maximum is at most `8n` and `M>8n^3`, then

```text
E_C<=8nM(M-1)<8nM^2<M^3/n^2,                         (7)
```

which proves `(NK6)`.

## 3. Official arithmetic and maximality

Write `A_0=N-2K`. Before taking floors, define

```text
U_c=binom(A_0+2c,c)/binom(H+c-1,c).                   (8)
```

Direct cancellation gives

```text
U_(c+1)/U_c
 =((A_0+2c+2)(A_0+2c+1))/((A_0+c+1)(H+c)).           (9)
```

All six rows have `A_0+1>H`. Each numerator factor in `(9)` is then strictly
larger than its paired denominator factor, so `U_c`, and therefore
`floor(U_c)=R_c`, is nondecreasing. Exact integer evaluation gives the table
in the statement: every printed `R_(C_0)` is at most `8n`, while the next
value is greater than `8n`. This proves both the paid prefixes and their
maximality for `(NK6)`.
