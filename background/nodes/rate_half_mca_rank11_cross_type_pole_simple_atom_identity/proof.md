# Proof

Write the two certificates on their shared indexed explanations as

```text
Qh_i +(c_0+c_1 gamma_i)Lambda_i =A +gamma_iB,
Q'h_i+(c'_0+c'_1 gamma_i)Lambda_i=A'+gamma_iB'.       (1)
```

## Independent scalar pairs

Assume first that `s=(c_0,c_1)` and `s'=(c'_0,c'_1)` are independent. At a
point of the collision set `H`, the equations

```text
Q'(x)s=Q(x)s'
```

force `Q(x)=Q'(x)=0`. Pole-simplicity therefore lets a point of `H` occur in
at most one shared support. Outside `G`, the affine collision equation also
allows at most one shared slope. With `z=|G\H|`, the `rm'` support incidences
satisfy

```text
rm' <= (n'-|G|)+r|G\H|+|H| = n'+(r-1)z.             (2)
```

Thus

```text
z >= ceil((rm'-n')/(r-1))=Z_r-c,                     (3)
Z_r=ceil((rm-n)/(r-1)).
```

Every point of `G\H` lies in at least `r-1` shared supports. At most one
support is absent, and each of the two distinguished pair types contributes
at least three supports. Hence the point lies in at least two supports from
each type and therefore in both exact pair cores. Since the types are
distinct,

```text
z<=K'-1=K-c-1.                                       (4)
```

For the official row,

```text
n=2097152,       m=1116048,       K=1048576.
```

Direct integer division gives `Z_16=1050642>K-1=1048575`; moreover `Z_r` is
nondecreasing in `r`. Equations `(3)` and `(4)` contradict one another for
every `r>=16`.

## Proportional scalar pairs

It remains to consider `s'=lambda s`. Scale the second certificate by
`lambda^{-1}` and write

```text
D=Q'-Q,       E_0=A'-A,       E_1=B'-B.
```

Subtracting `(1)` cancels the locator term exactly:

```text
D h_i=E_0+gamma_iE_1.                                (5)
```

If `D` is nonzero, subtract `(5)` at two distinct slopes `gamma_i,gamma_j`.
It follows that

```text
b=(h_i-h_j)/(gamma_i-gamma_j)=E_1/D
```

is a polynomial codeword. Then `a=h_i-gamma_i b=E_0/D` is also a codeword,
and cancellation in the polynomial integral domain gives

```text
h_k=a+gamma_k b
```

for every shared slope. Two shared records from one saturated pair type
identify `(a,b)` with that type's parameterized explanation line. Doing the
same for the second type identifies the two types, a contradiction.

Therefore `D=0`. Equation `(5)` at two distinct slopes gives `E_0=E_1=0`.
After the initial projective scaling, all four certificate components agree,
so the certificates are projectively identical. QED.
