# Proof

The union of the row supports is all of `X`: the zero fibers are disjoint and
there are at least four rows. Hence

```text
v=|X|+|union_i O_i|.                                  (1)
```

For an outside point of multiplicity `m>=1`, the elementary identity

```text
1=m-C(m,2)+C(m-1,2)                                  (2)
```

gives

```text
|union_i O_i|=sum_i|O_i|-sum_x C(m_x,2)+H.           (3)
```

The forced extension sizes give

```text
sum_i|O_i|=sum_i(tau_i-|I_i|)
            =t(h-d-1)+Z-I.                           (4)
```

By definition of `sigma` and the summed pair slack,

```text
sum_x C(m_x,2)
 =(t-1)Z-C(t,2)(d+1)-(t-1)I-sigma.                  (5)
```

Substitute `(4)--(5)` into `(3)`:

```text
|union_i O_i|
 =t(h-d-1)+Z-((t-1)Z-C(t,2)(d+1))
   +(t-2)I+sigma+H.                                  (6)
```

Now use `|X|=a+d+1` in `(1)` and compute `2v-2a-ht` from `(6)`. The terms
independent of `I,sigma,H` are exactly `D_0` in `(MD3)`, and the remaining
terms give twice their displayed charge. This proves `(MD4)`. Expanding and
factoring the baseline verifies the two equal forms in `(MD3)`.

For a full minimal Maxwell core, the shell router gives `Delta=-e<=0`.
Equation `(MD4)` then proves `(MD5)`. If `D_0>0`, no nonnegative defect charge
can make `Delta` nonpositive. If `D_0=0`, every nonnegative term in `(MD4)`
must vanish. Since `t>=4`, this gives `I=0`; `sigma=0` means every individual
nonnegative pair slack is zero; and `H=0` is equivalent to `m_x<=2` at every
outside point. This proves `(MD6)`. QED.
