# Owner-free weighted Cauchy divisor chart

- **status:** PROVED
- **consumer:** `l1_fpc5_large_source_payment`

Let `T_1,...,T_t` be the disjoint full petals, let `L_i` be their monic
locators, and put

```text
T=disjoint_union_i T_i,       Lambda=product_i L_i,
h=deg Lambda,                 d<h<=2d+1.              (CC1)
```

Fix labels `c_i` and let `chi` be the unique polynomial of degree below
`h` satisfying

```text
chi==c_i (mod L_i).                                  (CC2)
```

For every polynomial `G` of degree at most `d`, define

```text
B_G=rem_Lambda(chi G).                                (CC3)
```

Then `(G,B)` lies in the complete `t`-petal pair slice

```text
deg G,deg B<=d,       B==c_i G (mod L_i)              (CC4)
```

if and only if `B=B_G` and `deg B_G<=d`.

Assume the petals split into distinct field points. For `z in T_i`, write
`c(z)=c_i` and define

```text
M_j(P)=sum_(z in T) c(z) z^j P(z)/Lambda'(z).         (CC5)
```

The degree condition in `(CC4)` is exactly

```text
M_j(G)=0,       0<=j<=h-d-2,                          (CC6)
```

where the range is empty when `h=d+1`. Thus there are exactly `h-d-1`
printed moment equations.

Let `Core` and `Bkg` be disjoint from the petals. If `G` is a monic
squarefree degree-`d` divisor of

```text
L_Core=product_(x in Core)(X-x),                      (CC7)
```

then for each root `x` of `G`,

```text
B_G(x)=-Lambda(x) M_0(G/(X-x)).                       (CC8)
```

Consequently

```text
gcd(G,B_G)=1
iff M_0(G/(X-x))!=0 for every x in Z(G).              (CC9)
```

For every background point `y`, put

```text
C_y(G)=sum_(z in T)
       c(z)G(z)/((y-z)Lambda'(z)).                    (CC10)
```

Then

```text
B_G(y)=Lambda(y) C_y(G),                              (CC11)
```

so every required or forbidden background agreement is exactly a printed
vanishing or nonvanishing Cauchy equation.

Finally, if `A=L_Core/G`, then `(CC6)` is equivalently the reciprocal
divisor system

```text
sum_(z in T)
  c(z) z^j L_Core(z)/(A(z)Lambda'(z))=0,
0<=j<=h-d-2.                                         (CC12)
```

Hence the split, primitive, and background-guarded points in the complete
cell form one owner-free weighted Cauchy divisor census over the
degree-`N-d` divisors `A` of `L_Core`. If the slice contains a saturated
primitive monic anchor, the proved dimension theorem shows that the
unrestricted monic solution chart of `(CC6)` is an affine
`e=2d+1-h` flat.

## Scope

This theorem is an exact anchor-free reformulation. It does not bound the
number of divisors satisfying `(CC12)`, prove base-field-normalized
flatness, pay first-owner chronology, or aggregate source charts.
