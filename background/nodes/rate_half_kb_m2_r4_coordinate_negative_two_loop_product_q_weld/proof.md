# Proof

The complete-fiber compiler proves that `F=N/D=B_0/B_2` is a nonconstant
Mobius map and that all five `p_s` are distinct.  The five `s` are also
distinct.  Three distinct source and image points determine a unique
projective linear map, so any three rows of `(KBNW-1)` have rank three.
The actual coefficient vector lies in the kernel of all five rows.  Hence
the full matrix has rank exactly three and its kernel is the line spanned by
`(D_0,D_1,N_0,N_1)`.  Leading support gives `D(s)!=0` on `K`.

Write

```text
N(W)=N_0+N_1 W,       D(W)=D_0+D_1 W,
Delta=N_1 D_0-N_0 D_1.
```

Nonconstancy gives `Delta!=0`.  For distinct `r,s` direct subtraction gives

```text
p_r-p_s=Delta(r-s)/(D(r)D(s)).                    (1)
```

Apply `(1)` to `(h,i)` and `(h,j)`.  Since all labels and products are
distinct, every factor divided by below is nonzero, and

```text
D(i)/D(j)
 = (h-i)(p_h-p_j)/((h-j)(p_h-p_i)).               (2)
```

The loop-stratified compiler gives `A_1=cR`.  At a nonloop label its sum
equation is

```text
cR(i)+q_iD(i)=0.                                  (3)
```

Two instances of `(3)` imply

```text
q_iD(i)R(j)=q_jD(j)R(i).                          (4)
```

Substituting `(2)` into `(4)` and clearing the nonzero denominator gives
exactly `(KBNW-2)`.

Conversely, suppose the product gate, leading support, and the two welds
against one nonloop label `i_0` hold.  Reverse the calculation using `(2)`.
Then `q_sD(s)/R(s)` has one common value on all three nonloop labels.  Put

```text
c=-q_sD(s)/R(s).
```

The value is independent of `s` and is nonzero.  With `A_1=cR`, equation
`(3)` holds on every nonloop.  At `lambda,mu`, both `R` and `q` vanish, so
the two loop equations hold as well.  This proves the necessity and
sufficiency assertion. QED.
