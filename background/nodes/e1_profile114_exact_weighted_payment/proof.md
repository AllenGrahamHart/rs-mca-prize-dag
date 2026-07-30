# Proof

The profile-(1,14) router proves that the ten pure cofactor families and the
128 cofactor-514 prime-ideal families are the only possible families once
cofactor 1538 is excluded and cofactor 1028 is empty. The energy-two,
energy-three, energy-five/six, and energy-four exclusions prove that last
premise. Hence

```text
T_114<=10+128=138,
|D_114|<=256*138=35328.                             (1)
```

The weighted-kernel dictionary gives

```text
E_114<=M_33(1,14)|D_114|/2.                        (2)
```

The factor one half converts oriented differences to unordered class pairs.
Since

```text
M_33(1,14)=1154418456451360735963226152798543872,
```

substitution of `(1)` in `(2)` gives

```text
E_114<=M_33(1,14)*35328/2
     =20391647614756836040054426763033478955008.    (3)
```

Subtracting `(3)` from the residual after profile `(2,10)`,

```text
22622986807805210095050326195532090878375,
```

leaves

```text
R=2231339193048374054995899432498611923367.         (4)
```

Exact regeneration of the eligible dictionary profiles identifies the next
one as

```text
(0,18,S=18),
M_next=M_33(0,18)=1117325838856821897682125205459304448.  (5)
```

For all later oriented collision vectors `D_res`, monotonicity of the sorted
dictionary gives `E_later<=M_next|D_res|/2`. Exact division yields

```text
floor(2R/M_next)=3994,
M_next*3994<=2R<M_next*3995.                        (6)
```

Equations `(1)--(6)` prove the payment and the next residual cap. QED.
