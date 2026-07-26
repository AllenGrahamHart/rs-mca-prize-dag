# Proof - L1 Mersenne HNF m=16 order-zero even-quadratic exclusion

The dependencies remove every `m=8` quadratic, the collision-free
`m=16` branch, and the exactly-one-repeat `m=16` branch. The quadratic
collision router says that every remaining candidate is even. Assume one
exists:

```text
E_s(W)=A W^2+C,       A!=0,                           (1)
```

with at least two repeated colors.

## 1. Antipodal pairs as an odd/even gcd

If distinct locator roots `a,b` have the same color under `(1)`, then
`a^2=b^2`; the odd characteristic gives `b=-a`. Conversely every antipodal
locator pair repeats its color.

Put `Y=W^2`, `b_r=binom(s+r-1,r)`, and split

```text
P_s(W)=W O_s(Y)+V_s(Y),
O_s(Y)=sum_(j=0)^7 b_(2j)Y^(7-j),
V_s(Y)=sum_(j=0)^7 b_(2j+1)Y^(7-j).                 (2)
```

Each antipodal pair `+-a` gives the common root `a^2` of `O_s,V_s`.
Different pairs give different nonzero squares because `P_s|W^n-1` is
squarefree. Therefore at least two repeated colors imply

```text
deg gcd_Y(O_s,V_s)>=2.                               (3)
```

Replace `V_s` by

```text
R_s=V_s-sO_s.                                        (4)
```

The leading term cancels and

```text
[Y^6]R_s=-s(s-1)(s+1)/3.                            (5)
```

It is nonzero because `s notin F_p`, so the degrees of `O_s,R_s` are exactly
seven and six. Their gcd equals the gcd in `(3)`.

## 2. First-subresultant obstruction

Let

```text
Sres_1(O_s,R_s)=c_1(s)Y+c_0(s).                     (6)
```

For polynomials of degrees seven and six, `(3)` forces the complete first
subresultant `(6)` to vanish. Exact subresultant arithmetic over `Q[s]`, then
coefficientwise reduction modulo `p=8191`, gives

```text
gcd_(F_p[s])(c_0,c_1)
 = s^6(s-3)(s-2)(s-1)^6(s+1)^6
   (s+2)^5(s+3)^5(s+4)^4(s+5)^4
   (s+6)^3(s+7)^3(s+8)^2(s+9)^2(s+10)(s+11).       (7)
```

The right side has degree 50 and every one of its roots lies in `F_p`.
All input denominators divide products of `1!,...,15!` and are invertible
modulo 8191, so the reduction introduces no undefined coefficient. The
primary verifier reconstructs `(6)` with an exact subresultant sequence and
checks `(7)` both over `Q` and after modular reduction.

The independent audit does not use a computer-algebra subresultant routine.
For each of 161 base-field values of `s`, it builds the 11-by-12 first-
subresultant coefficient matrix (five shifts of `O_s`, six of `R_s`). The
two 11-by-11 determinants obtained by deleting the degree-one and degree-zero
columns are `-c_0` and `-c_1`. A determinant has degree at most

```text
5*14+6*15=160,                                       (8)
```

so interpolation from those 161 values is exact. A standalone finite-field
Euclidean algorithm then reproduces precisely the degree-50 polynomial in
`(7)`.

If `(3)` held, both coefficients in `(6)` would vanish at `s`; hence `s`
would be a root of `(7)` and would lie in `F_p`. This contradicts `(ME1)`.
The even multi-repeat chamber is empty, proving `(ME2)` and the stated
five-row quadratic exclusion. QED.
