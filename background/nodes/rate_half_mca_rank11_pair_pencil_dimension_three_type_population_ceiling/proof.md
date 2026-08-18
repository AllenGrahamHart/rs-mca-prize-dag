# Proof

Let `J` be the complete received-pair core of the scalar family and shorten
by it. Put `K'=K-|J|`. Every residual pair core has size

```text
s'=67470+K'
```

in a domain of size

```text
n'=1048576+K'.                                     (1)
```

Let `d_x` count retained quotient pair cores through residual coordinate
`x`. Scalar dimension three makes the owner set one affine plane, so the
proved affine-plane cap gives

```text
0<=d_x<=218,
q(67470+K')=sum_x d_x<=218(1048576+K').             (2)
```

Thus, for `q>218`,

```text
(q-218)K'<=A(q):=218*1048576-q*67470.               (3)
```

Distinct residual pair cores intersect in at most `K'-1` coordinates.
Therefore

```text
sum_x C(d_x,2)<=C(q,2)(K'-1).                       (4)
```

For every integer `0<=d<=218`, the exact identity

```text
C(d,2)=217d-C(218,2)+C(218-d,2)                    (5)
```

implies

```text
sum_x C(d_x,2)
 >=217q(67470+K')-C(218,2)(1048576+K').             (6)
```

Combining `(4)` and `(6)` and collecting `K'` gives

```text
P(q)K'>=B(q),                                      (7)
P(q):=C(q,2)-217q+C(218,2),
B(q):=217q*67470-C(218,2)*1048576+C(q,2).
```

Here `P(q)>0` throughout `q>=520`. A necessary condition for `(3)` and
`(7)` to share a real solution is

```text
P(q)A(q)-B(q)(q-218)>=0.                            (8)
```

Twice the left side factors exactly as

```text
2(PA-B(q-218))
 =-109q(q-218)(619q-1962831).                       (9)
```

Since

```text
619*3170-1962831=-601,
619*3171-1962831=18,
```

equation `(9)` is negative for every integer `q>=3171`. Hence `q<=3170`.
The population router already proves `q>=520`, establishing `(TP1)`.

At `q=3170`, exact division in `(7)` and `(3)` gives

```text
P=4358628,
B=4358628*4959+556785,
A=2952*4982+2804.
```

Thus `K'>=4960` and `K'<=4982`. At `q=3171`, the doubled cross-product in
`(9)` equals `-18372095406`, giving the printed adjacent deficit.

Still at `q=3170`, let

```text
Delta=218n'-3170s'=14709668-2952K'.                (10)
```

Every coordinate with `d_x<218` contributes at least one to `Delta`.
Therefore the number `F_218` of maximum-multiplicity coordinates satisfies

```text
F_218>=n'-Delta=-13661092+2953K'.                   (11)
```

The right side increases with `K'`; at `K'=4960` it equals 985,788, and at
`K'=4982` it equals 1,050,754. This proves `(TP4)`.

Finally the `M=255011043` retained records are partitioned by first-owned
pair type. Averaging over at most 3170 types gives

```text
ceil(255011043/3170)=80446.
```

QED.
