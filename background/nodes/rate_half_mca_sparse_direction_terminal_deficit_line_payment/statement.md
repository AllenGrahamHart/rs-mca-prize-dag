# Sparse-direction terminal-deficit line payment

- **status:** PROVED
- **closure:** affine-codeword-line cap for the exact terminal deficit
- **scope:** one shortened support-wise MCA-bad family after a codeword
  direction gauge

## Terminal-line lemma

Use

```text
N=R+K,       m=d+K,       c=K-1,
r_1=b+q,     E=supp(q),   |E|=e<d,       n=N-e.
```

Assume `e>=K`.  Let `L_e` be the number of transformed explanations that
own a selected slope and have exact outside deficit `e`.  Then

```text
L_e <= floor((n-c)/(m-e-c)).                         (TL1)
```

Here the denominator is positive on both applications below.  The bound is
also valid when there are zero or one terminal explanations.

## Prefix-plus-terminal profile

For `1<=h<e`, let `C_h` be any proved cumulative cap on the number `N_h`
of explanations with outside deficit at most `h`.  Put

```text
B_0=0,       B_h=min_(h<=v<e) C_v.
```

Then

```text
|Z| <= sum_(h=1)^(e-1) (B_h-B_(h-1))*floor(e/h)
       + floor((n-c)/(m-e-c)).                       (TL2)
```

Using the Johnson/mean-centered raw caps from the preceding node, `(TL2)`
expands the complete certified walls to

```text
KoalaBear K=14:   e<=64048,   j=R-e>=984528;
Mersenne K=6:     e<=65455,   j=R-e>=983121.
```

The new endpoint bounds are respectively `181326343` and `16100647`.
At the next KoalaBear support the cumulative cap at `h=e-1` is unavailable.
At the next Mersenne support `(TL2)=17119507>16777215`.

## Nonclaims

This does not pay either adjacent support, bound any nonterminal exact layer
by an affine-line argument, use the full-lift near-MDS extension structure,
or close an official row.

## Falsifier

Two terminal explanations not lying on the asserted affine codeword line,
a legal terminal family exceeding `(TL1)`, a selected family exceeding
`(TL2)`, or an incorrect endpoint or adjacent computation.
