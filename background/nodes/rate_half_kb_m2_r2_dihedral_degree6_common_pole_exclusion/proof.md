# Proof

Work over the geometric closure of the KoalaBear field. Its characteristic
is prime to `2,3,5` and to every integer denominator below.

## 1. The common pole sextic

For `n=6`, the outer map `G` has one pole of order five. Hence all six
distinct order-five poles of `F` form one unramified fiber of each
degree-six dihedral right factor. In a standard coordinate such a fiber is

```text
P_c(x)=x^6-6x^4+9x^2-c=0.                           (1)
```

The excluded values `c=0,4` are the two finite branch fibers of `D_6`.
The internal involution `i(x)=-x` preserves `(1)` and fixes none of its six
roots.

Let `ell` identify the standard coordinate of the second quotient with the
first, and put `j=ell*i*ell^(-1)`. The second fiber is also unramified, so
`j` is another fixed-point-free involution of the same six roots. As
permutations, `i` and `j` are perfect matchings. If they are distinct, the
union of their edges is either one six-cycle or a four-cycle plus one common
edge. Thus `ij` has order three or two, respectively. The action on six
points is faithful, so this is also its projective order.

## 2. Coincident matchings

If `i=j`, then `ell` normalizes `x -> -x`, and hence has form

```text
ell(x)=s*x       or       ell(x)=s/x.               (2)
```

Comparing the four even coefficients in
`P_c(ell(x))=kappa P_(c')(x)` gives

```text
ell=s*x:   s^2=1, c'=c;
ell=s/x:   s^2=9/4, c=c'=27/8.                     (3)
```

Thus the relative coordinate is `+/-x`, or exceptionally
`+/-3/(2x)`.

## 3. Distinct commuting matchings

Suppose `ij` has order two. Then `i` and `j` commute. A distinct projective
involution commuting with `i` is `j(x)=k/x`. Invariance of `(1)` under `j`
gives

```text
k^2=9/4,       c=27/8.                              (4)
```

For `k=3/2`, the fixed points `x^2=3/2` are roots of `(1)`, contrary to
the fixed-point-free second fiber. Hence `k=-3/2`.

Choose `s^2=-3/2` and

```text
L(z)=s(z+1)/(z-1),       L(-z)=-3/(2L(z)).
```

Direct pullback gives, up to a nonzero scalar,

```text
P_(27/8)(L(z)) = 5z^6+11z^4+11z^2+5.               (5)
```

Any other coordinate conjugating `-z` to `j` differs from `L` by a
normalizer from `(2)`. A scaled Dickson-six fiber with even coefficients
`A,B,C,D` satisfies `B^2=4AC`; after inversion it satisfies `C^2=4BD`.
For `(5)`, both left sides are `121` and both right sides are `220`.
Therefore `(5)` is not a Dickson-six fiber in any allowed second coordinate.
The commuting case is impossible.

## 4. Order-three matchings

Now let `g=ij` have order three. The relation `igi=g^(-1)` and a scalar
normalization put its matrix in the form

```text
g_t(x)=t(x+t)/(t-3x).                               (6)
```

Indeed an order-three matrix satisfying the relation is
`[[a,b],[c,a]]` with `bc=-3a^2`; scaling the matrix to `c=-3` gives
`b=a^2`.

The odd coefficients in the identity
`P_c(g_t(x))=kappa P_c(x)` give, with `s=t^2`,

```text
3c+s^3+2s^2-15s=0,
135c+5s^3-6s^2-27s=0,
243c+s^3-30s^2+81s=0.                              (7)
```

Subtracting multiples of the first equation gives
`(s-3)(5s+27)=0`. The first root gives the ramified fiber `c=0`.
The unramified solution is

```text
t^2=-27/5,       c=756/125.                         (8)
```

Substitution verifies all even coefficients as well. Moreover `g_t`
conjugates `i` to `j`. Thus `g_t^(-1)ell` normalizes `i` and maps one
Dickson-six fiber to another. Equations `(3)` and `(8)` leave only

```text
ell in {+/-g_t,+/-g_t^2},       5t^2+27=0.          (9)
```

Changing the sign of `t` exchanges `g_t` and `g_t^2`.

## 5. Source-cover incompatibility

The source-cover classifier specializes at `a=1` to `(KBM6-1)`, with
`d^2=3`. For a projectivity

```text
ell(z)=(Az+B)/(Cz+D),
L_y(z)=(A-yC)z+(B-yD),
```

condition `(KBM6-1)` is equivalent to

```text
L_2(z)L_b(z) proportional to z^2-b*d*z+b^2-1.       (10)
```

For `ell=+/-z`, coefficient comparison gives

```text
b^2-2b-1=0,       (b+2)^2=3b^2,
```

and the second equation is `b^2-2b-2=0`, a contradiction.

For `ell=+/-3/(2z)`, equation `(10)` gives

```text
8b(b^2-1)-9=0,
16b^4-3(b+2)^2=0.
```

Their resultant is `22371648`, nonzero in the KoalaBear field.

It remains to use `(9)`. For `ell=g_t`, clear the two leading linear
coefficients in `(10)` and reduce by `5t^2+27=0`. The middle-coefficient
equation is linear in `d`; eliminating it with `d^2-3=0` gives

```text
H(b)=(-900t-2295)b^4+(3240-1530t)b^3
     +(1260t-459)b^2+(2088t-2592)b
     +1296t-2268/5.                                 (11)
```

The constant-coefficient equation is

```text
E(b)=(25t+150)b^3+(50t-45)b^2
     +(-70t-60)b-140t-198.                          (12)
```

The exact resultant of `(11)` and `(12)`, reduced by `5t^2+27`, is

```text
76527504000(1472792180t+1585334079).                (13)
```

The norm of the primitive linear factor in `(13)` is

```text
5(1585334079)^2+27(1472792180)^2
 =71132574457861006005
 =1274367339 mod 2130706433.
```

It is nonzero. The other three maps in `(9)` are obtained from the same
two equations by `t -> -t` and/or `d -> -d`, so `(13)` excludes all four.
Thus every possible common-pole coordinate contradicts `(KBM6-1)`, and the
`n=6` profile is empty. QED.
