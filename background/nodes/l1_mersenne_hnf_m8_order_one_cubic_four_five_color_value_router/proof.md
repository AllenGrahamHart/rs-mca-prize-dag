# Proof - L1 Mersenne HNF m=8 order-one cubic four/five-color value router

The root formula gives

```text
V_E(X)=product_(x:L(x)=0)(X-E(x))
      =product_(epsilon used)(X-epsilon)^n_epsilon.  (1)
```

Since the eight colors are exactly the roots of `X^8-1`, multiplying (1)
by the missing-color product gives

```text
V_E M
 =(product_(epsilon in mu_8)(X-epsilon))
   product_(epsilon used)(X-epsilon)^(n_epsilon-1)
 =(X^8-1)D,                                          (2)
```

which proves (FFV3).

A cubic fiber contains at most three roots. The partitions of six into
exactly five or four positive parts bounded by three are precisely

```text
2+1+1+1+1,
3+1+1+1,
2+2+1+1.                                             (3)
```

Their excess factors `D` are exactly those in the table.

For the first profile, mark the repeated color and choose three missing
colors from the other seven. Translating the marked color to `1` is unique,
leaving `binom(7,3)=35` packets. The same argument for the marked triple
color and four missing colors gives `binom(7,4)=35` packets for the second
profile.

For `2+2+1+1`, choose the unordered pair of repeated colors and then four
missing colors from the other six. There are

```text
binom(8,2)binom(6,4)=420                              (4)
```

raw configurations. Under cyclic translation, only the identity and the
half-turn can fix one. The identity fixes all 420. For the half-turn, the
repeated pair is one of four antipodal pairs and the missing set is a union
of two of the other three antipodal pairs, giving `4*binom(3,2)=12` fixed
configurations. Burnside's lemma gives

```text
(420+12)/8=54.                                       (5)
```

This proves all packet counts. The conic is inherited, and exact
multiplicities are imposed by the corresponding fiber-gcd subresultants.
Every displayed degree is fixed independently of the official exponent.
QED.
