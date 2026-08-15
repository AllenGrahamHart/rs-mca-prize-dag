# Proof

Import the residual owner geometry from the parent node. For a fixed
rank-nine chart, the common core `J` and disjoint owner petals satisfy

```text
9<=j:=|J|<=K'-1,
0<=s_p:=|P_p|<=m'-j-1,
sum_p s_p<=n'-j,
q_j(s)=s(j-9)+C(s,2),
W_B<=981105*sum_p q_j(s_p).                         (1)
```

## Exact convex packing

Set

```text
D_1=981105,       a=m'-j-1.
```

Then `67472<=a<=67462+K'` and `n'-j=D_1+a`. The charge is
nondecreasing, and moving mass toward a larger petal never lowers it. More
precisely,

```text
q_j(x+y)-q_j(x)-q_j(y)=xy                         (2)
```

when `x+y<=a`, while for `x,y<a<x+y`,

```text
q_j(a)+q_j(x+y-a)-q_j(x)-q_j(y)=(a-x)(a-y).       (3)
```

Both right sides are nonnegative. Saturating the relaxed total budget and
repeating (2)--(3) leaves full petals and at most one remainder. Therefore

```text
sum_p q_j(s_p)<=r q_j(a)+q_j(b),
r=1+floor(D_1/a),       b=D_1 mod a.               (4)
```

This is an upper bound even when the affine owner plane has fewer petal
slots, because (4) optimizes over the larger unrestricted partition class.

## Optimize the petal ceiling

Substitute `j=K'+67471-a` into (4). For each integer `a`, the exact packed
charge is the line

```text
G_a(K')=(D_1+a)K'+I_a,
I_a=(D_1+a)(67462-a)
    +[r a(a-1)+b(b-1)]/2.                          (5)
```

On `10<=K'<=15634`, the admissible range is
`67472<=a<=83096`, and `floor(D_1/a)` has only four blocks:

```text
q=14: 67472..70078,       q=13: 70079..75469,
q=12: 75470..81758,       q=11: 81759..83096.       (6)
```

Within a block with fixed quotient `q`, (5) is a quadratic in `a` with
leading coefficient

```text
(q^2+q-1)/2>0.                                     (7)
```

It is therefore convex, so its maximum over each integer block occurs at
an endpoint. At `K'=15634`, subtracting all eight endpoint values from
`G_67472` gives

```text
a:       67472  70078      70079      75469       75470
gap:         0  676268727  676325879  3265037774  3265407519

a:       81758       81759       83096
gap:     6322001175  6322245154  7515065748.        (8)
```

For every `a>67472`, the difference
`G_67472(K')-G_a(K')` decreases with `K'`, since the candidate has the
larger slope `D_1+a`. Hence the nonnegative endpoint comparison at the
largest row proves that `a=67472` is a maximizer at every earlier
admissible row. Here

```text
r=15,       b=36497,
G_67472(K')=1048577*K'+34798536326.                 (9)
```

Equations (1), (4), and (9) give the integral cap

```text
U(K')=981105*(1048577*K'+34798536326).              (10)
```

## Exact crossing and persistence

The weighted selector demand is

```text
L(K')=(495405467/10^9) N_min
      *C(m',9)C(m'-9,2)/C(n',9),
N_min=274980728111260126.                           (11)
```

Exact adjacent-row arithmetic gives

```text
K'=15528: ceil(L)=50114371326035640,
           U       =50115667510540110;

K'=15529: ceil(L)=50120589875892136,
           U       =50116696274677695.              (12)
```

Before rounding, the cross-products `numerator(L)-U*denominator(L)` are

```text
-6248068483868188405542620968591685205454118996921498723724119393820000
```

and

```text
18768695900816242246861589677573925951586796317153282240839542295982000,
```

respectively.

The ratio of (11) to (10) is a positive constant times the nine increasing
Reed--Solomon factors `(m'-i)/(n'-i)`, `0<=i<=8`, and

```text
H(K')=(K'+67463)(K'+67462)
      /(1048577*K'+34798536326).                    (13)
```

The numerator of `H(K'+1)-H(K')` after clearing positive denominators is

```text
P(K')=1048577*K'^2+69598121229*K'-77044697164886.
```

Writing `K'=15529+x` gives

```text
P=1048577*x^2+102164825695*x+1256608704226512>0     (14)
```

for every `x>=0`. Thus the raw ratio strictly increases after the first
crossing, proving the contradiction through `K'=15634`. The parent node
then covers `15635..20617`, and the separate high-row theorem covers all
larger rows.
