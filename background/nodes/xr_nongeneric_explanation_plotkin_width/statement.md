# XR nongeneric-explanation Plotkin width

- **status:** PROVED
- **role:** bound terminal breadth in the support-mismatch descent
- **consumers:** `xr_tangent_support_mismatch_bridge`,
  `xr_lowcore_spread_heart`, `xr_clean_residual_any_gate`

## Statement

Consider one live XR mismatch instance with ambient length `N`, RS dimension
`K`, and agreement

```text
A=K+h,       h>=1,       H=h+1.                         (XW1)
```

Let `mathcal E` be any family of distinct codeword-pair explanations of the
same received pair, each on at least `A` coordinates. Choose canonically an
`A`-subset `Y_e` of every explanation support. Then

```text
|Y_e|=A,
|Y_e intersect Y_f|<=K-1=A-H,
|Y_e triangle Y_f|>=2H.                                (XW2)
```

Consequently:

1. if `N<4H`, then

   ```text
   |mathcal E|<=floor(4H/(4H-N));                       (XW3)
   ```

2. if `N=4H`, then `|mathcal E|<=2N`;
3. for every fixed `C>=0`, if `N-4H<=C log_2 n`, then

   ```text
   |mathcal E|<=8n^(C+1).                               (XW4)
   ```

In particular, once a canonical nongeneric descent enters `N<=4H`, its
entire live subtree has at most

```text
1+104H                                                  (XW5)
```

instances. All genuine-tangent coordinate charges across that subtree cost
at most

```text
420H^2.                                                 (XW6)
```

At the six official clean-rate rows this is below the reserved `16n^3`.

More generally, if for one fixed `C>=0`

```text
N-4H<=C log_2 n,       H>=2C log_2 n,                   (XW7)
```

then the entire live nongeneric subtree has at most

```text
1+200n^(C+1)                                             (XW8)
```

instances, and all genuine-tangent charges across it cost at most

```text
201n^(C+2).                                             (XW9)
```

Thus every fixed logarithmic terminal window is polynomial as a whole, not
only at its first explanation level.

## Scope

This theorem bounds distinct joint explanations and the resulting
nongeneric instance tree. It does not aggregate slopes across generic
full-external-zero charts or bound the slope fiber of one explanation.
Therefore it narrows, but does not promote, the tangent/support-mismatch
bridge.
