# Proof

The weighted-kernel dictionary gives, for profile `(2,10,S=18)`,

```text
E_210<=M_33(2,10)|D_210|/2.                         (1)
```

The factor one half converts oriented differences into unordered class
pairs. The split-prime router starts with 394 shift/sign orbits. The proved
cofactor-1538 exclusion removes its 128 prime-ideal families, leaving

```text
T_210<=266,
|D_210|<=256*266=68096.                             (2)
```

Since

```text
M_33(2,10)=1227527050040565145269313275179180544,
```

substitution in `(1)--(2)` gives

```text
E_210<=M_33(2,10)*68096/2
     =41794840999781162066129578393300739162112.    (3)
```

Subtracting `(3)` from the residual after the profile-(3,6) payment,

```text
64417827807586372161179904588832830040487,
```

leaves

```text
R=22622986807805210095050326195532090878375.        (4)
```

Exact enumeration of all 271 eligible dictionary profiles, with `(4,2)`
empty and `(3,6)`, `(2,10)` paid, identifies the next multiplicity as

```text
M_next=M_33(1,14)
      =1154418456451360735963226152798543872.        (5)
```

For the set `D_res` of all later oriented collision vectors,

```text
E_later<=M_next |D_res|/2.
```

Exact division gives

```text
floor(2R/M_next)=39193,
M_next*39193<=2R<M_next*39194.                       (6)
```

This proves the payment and the next residual cap. QED.
