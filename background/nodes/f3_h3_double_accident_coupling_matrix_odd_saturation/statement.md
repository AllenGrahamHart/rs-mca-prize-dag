# H3 double-accident coupling-matrix odd saturation

- **status:** PROVED
- **closure:** proof
- **consumer:** `f3_h3_mobius_excess_half`
- **dependencies:** `f3_h3_double_accident_coupling_batch_odd_saturation`,
  `f3_h3_shifted_product_sidon`

Let `m,r>=2`. Let `E_0,...,E_(m-1)` be distinct unordered shifted-root pairs
with products `beta_i`, and let `Q_0,...,Q_(r-1)` be distinct ordered
nonidentity quotient lifts `Q_j=(u_j,v_j)`. Put

```text
pi=1-zeta_n,       c_a=(1-zeta_n^a)/pi,
alpha_i=(beta_i-beta_0)/pi^2,
lambda_(i,j)=beta_i c_(u_j)-c_(v_j),
theta_(0,j)=c_(v_j)c_(u_0)-c_(v_0)c_(u_j).        (CM1)
```

The coupling matrix obeys the two exact difference identities

```text
lambda_(i,j)-lambda_(0,j)=pi^2 c_(u_j)alpha_i,    (CM2)
c_(u_0)lambda_(0,j)-c_(u_j)lambda_(0,0)
  =-theta_(0,j).                                   (CM3)
```

Every coefficient inverted below has 2-power norm. Define

```text
I_joint=(lambda_(0,0),
         alpha_i:i>0,
         theta_(0,j):j>0),

I_cross=(lambda_(i,0):0<=i<m,
         lambda_(0,j):1<=j<r),

I_rect=(lambda_(i,j):0<=i<m,0<=j<r).              (CM4)
```

Then

```text
I_joint O[1/2]=I_cross O[1/2]=I_rect O[1/2].       (CM5)
```

Thus the usual product-collision generators, quotient-collision generators,
and one product-to-quotient coupling are odd-locally equivalent to a coupling
cross, and also to the full coupling rectangle. All three ideals have the same
valuations at odd prime ideals and the same odd part of their absolute ideal
norms.

The characteristic-zero zero entries of the matrix form a partial matching:
each row and each column contains at most one zero. Hence

```text
#{(i,j):lambda_(i,j)!=0} >= mr-min(m,r).           (CM6)
```

On a positive `Y_18` target, taking all
`m=U(t)=(P(t)+D(t))/2>=10` unordered product lifts and all `r=R(t)>=2`
quotient lifts gives an exact coupling rectangle contained in the row-prime
ideal, with at least `mr-min(m,r)` nonzero entries. The low-distance star is
the three-row submatrix used for coarse candidate generation.

The full rectangle does not provide `mr` independent ideal generators:
`(CM5)` proves that one row and one column generate it after inverting two.
This theorem gives no ideal-index lower bound and no bound for the surviving
row primes.
