# Proof - L1 official Newton cofactor-window router

## 1. The characteristic is at least 3583

The power-of-two order argument in
`l1_official_reserve_tame_refinement_router` gives

```text
f>=n/(p+1).                                            (1)
```

For `5<=x<=251`, the function `log(x)/(x+1)` is decreasing. At the right
endpoint,

```text
8192 log_2(251)/252>256
```

because this is equivalent to `251^8>2^63`. The case `p=3` is larger still.
Thus `(1)` and the strict field cap exclude every prime `p<=251`, so
`p>=257`.

Now `8192|p^f-1`, hence `ord_(8192)(p)|f`. Since `log_2 p>8`, the cap gives

```text
ord_(8192)(p)<32.
```

This order is a power of two, so it is at most `16`. The exact order formula
on powers of two then forces

```text
p=1 or -1 mod 512.                                    (2)
```

The only positive integers in `[257,3582]` satisfying `(2)` are

```text
511, 513, 1023, 1025, 1535, 1537,
2047, 2049, 2559, 2561, 3071, 3073.
```

They have the explicit factors

```text
511=7*73,       513=27*19,      1023=3*11*31,
1025=25*41,     1535=5*307,     1537=29*53,
2047=23*89,     2049=3*683,     2559=3*853,
2561=13*197,    3071=37*83,     3073=7*439.
```

None is a characteristic. This proves `p>=3583`.

## 2. Uniform reserve gap below the characteristic

The official-reserve router proves

```text
ell_0<=ceil(5(p+1)/(4 log_2 p))+1.                    (3)
```

Since `p>=3583>2^11`, equation `(3)` gives

```text
ell_0<=ceil(5(p+1)/44)+1.                             (4)
```

For `p>=3583`, direct integer arithmetic gives

```text
5(p+1)/44<=p-3175
```

because it is equivalent to `139705<=39p`. The right side is an integer, so
`(4)` yields `ell_0<=p-3174`. This proves `(NW3)`.

## 3. Newton transport

Let `a>=a_0` be a nonempty exact shell. The fixed-cofactor transport gives
cofactor degree `e=h-a` and locator-prefix depth

```text
d=min(a,h-k).
```

Under `(NW4)`,

```text
h-k=(a_0+e_0)-k=ell_0-1+e_0<=p-1,
```

so `d<p` for every such shell.

Put `E_j(A)=(-1)^j l_j`, the elementary symmetric function of the roots.
For `1<=j<=d`, Newton's identity is

```text
j E_j=sum_(i=1)^j (-1)^(i-1) E_(j-i) S_i,
E_0=1.                                                 (5)
```

Every integer `j<=d` is nonzero in characteristic `p`. Equation `(5)`
therefore recovers `E_j` successively from `S_1,...,S_j`; the reverse Newton
recursion recovers `S_j` from `E_1,...,E_j`. This proves the bijection
`(NW6)` and preserves every locator-prefix fiber cardinality exactly.

The fixed-cofactor theorem places each shell cell in one prescribed locator
prefix, with equality for the scalar top shell. Applying `(NW6)` proves the
power-sum formulation. Equation `(NW7)` follows from `(NW3)`. Finally, if
`p>=n-k`, then `h-k<=n-k-1<p` for every `h<n`, so all received words lie in
the window.
