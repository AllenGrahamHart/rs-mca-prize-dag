# Cycle 147: rate-half `A=1` paired first-jet transversality (2026-08-11)

## Audit correction

The first attempted tangent continuation was invalid: the Forney constant
is proved on nonincidences, and substituting it at an actual-support root
silently deletes the nonzero actual error. Keeping

```text
b(delta)=e_delta+g_delta
```

gives the exact opposite conclusion.

## First jet

At every actual-support root of a selected zero-excess fiber,

```text
G_t/Q_t-G_X/Q_X
 =(x-s_0)v_x L_U0'(x)e_delta(x)/Lambda(delta) !=0.
```

Thus the full locator and split-biform curves are smooth and transverse at
all such points. This is an exact field-valued identity, not a genericity
claim.

## Common-factor reduction

A common component cannot pass through these transverse points. On a
selected fiber it can therefore use only padded-heavy roots. If its
bidegree is `(a,b)`, then

```text
(|Z_0|-b)a<=sum_(delta in Z_0)r_delta.
```

For the extremal carrier, `|Z_0|=2e`, `b<=e-2`, and the padding total is at
most `e-6-d_A`; hence `a=0`, and the classified row-root dictionary also
rules out a parameter-only factor. The two curves are coprime.

For the first strict carrier, `|Z_0|=p+2`, `b<=e-1`, and the padding total
is at most `e-6-r_A`. A nonconstant gcd is forced to have

```text
a=1,       b>=(e+15)/2+r_A,       r_A<=(e-17)/2.
```

Its selected-fiber root is always padding, never actual support.

The linear factor cannot survive the classified incidence count. Its
parameter-leading coefficient can drop on at most one classified row, so
it supplies at least `b(2p+r_A-1)` row-slope pairs. Each of the `3e+1`
off-line slopes can lie above at most one classified row of an `X`-linear
factor. Hence

```text
b(2p+r_A-1)<=3e+1,
```

contradicting the displayed lower bound on `b`. The strict curves are
coprime too.

## Burn-down

```text
result:                  PROVED paired first-jet transversality
extremal consequence:   Q and G coprime
strict consequence:     Q and G coprime
DAG delta:               +1 PROVED leaf
critical status delta:   none
compute:                 integer arithmetic + finite-field sign tamper
new assumptions:         none
```

The next route-deciding task is therefore the coprime resultant/intersection
ledger in both profiles, with the selected first jets kept explicit.
