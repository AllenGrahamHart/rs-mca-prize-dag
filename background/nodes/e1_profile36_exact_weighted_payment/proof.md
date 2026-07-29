# Proof

The weighted-kernel dictionary gives, for profile `(3,6,S=18)`,

```text
E_36=128 M_33(3,6) T_36(p,r).                        (1)
```

The factor `128` is one half of the `256` oriented vectors in each
negacyclic shift/sign orbit: the dictionary counts oriented differences and
then divides by two to count unordered class pairs.

The two height-collapse nodes prove `T_36(p,r)<=4`. Substitution in `(1)`
gives

```text
E_36 <= 512 M_33(3,6)
     = 709758113888498314287146042668908462080.       (2)
```

Subtracting `(2)` from the binding edge budget

```text
65127585921474870475467050631501738502567
```

leaves

```text
E_res=64417827807586372161179904588832830040487.       (3)
```

The profile `(4,2,S=18)` is already empty. Exact enumeration of all 271
eligible dictionary profiles, with `(4,2)` removed and `(3,6)` paid
separately, shows that the largest remaining multiplicity is

```text
M_next=M_33(2,10)
      =1227527050040565145269313275179180544.         (4)
```

If `D_res` is the set of all remaining oriented collision vectors, the
dictionary therefore gives

```text
E_remaining <= M_next |D_res|/2.
```

Exact division yields

```text
floor(2 E_res/M_next)=104955,
M_next*104955 <= 2 E_res < M_next*104956.             (5)
```

This proves the stated residual uniform cap. QED.

