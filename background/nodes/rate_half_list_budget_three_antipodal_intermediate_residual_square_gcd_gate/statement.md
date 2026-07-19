# Budget-three antipodal intermediate residual-square gcd gate

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_list_adjacent_crossing`
- **dependency:**
  `rate_half_list_budget_three_antipodal_intermediate_cube_part_router`

Retain the maximal intermediate boundary in original coordinates:

```text
s=2^37,       d=4s,       r=s-1,
h=(s+1)/3,    v=deg V=2h-2=(2^38-4)/3.               (IRG1)
```

Thus `e_2=0,e_3!=0`,

```text
F=(Y^d-1)/D=product_i(U+c_iV)=U^4+V^3K,
K=e_3U+e_4V,                                          (IRG2)
```

and the proved differential residual

```text
T=dDU-Y(D'U+4DU')                                    (IRG3)
```

has exact degree two. Define two polynomials determined only by the deleted
divisor `D` and its canonical monic direction `U`:

```text
P=TU^3+d,       W=T'U+3TU'.                          (IRG4)
```

Every valid intermediate direction satisfies

```text
V^2 | P,
P'=U^2W,
gcd(P,P')=gcd(P,W),
V | gcd(P,W).                                        (IRG5)
```

Here gcds are monic. In particular,

```text
deg gcd(P,W)>=v=(2^38-4)/3.                          (IRG6)
```

The gcd has a uniform low-degree annihilator. Define

```text
A=4YDT'+3T(dD-YD'),       J=dA^3+27T^7.              (IRG7)
```

Then

```text
gcd(P,W) | J,       deg J=18,
deg gcd(P,W)<=18.                                        (IRG8)
```

Since `(2^38-4)/3>18`, `(IRG6)` and `(IRG8)` are incompatible. Therefore
the complete maximal intermediate boundary is empty.

The ambient degrees are exact:

```text
deg P=3r+2,       deg W=r+1,       (r+1)-v=h+1.      (IRG9)
```

This rejects the intermediate boundary before any Hensel recursion,
cube-part factorization, outer-scalar test, or split/Mobius matching. The
generic, pure, higher-degree, and non-antipodal branches remain, so this
theorem does not close the adjacent crossing.
