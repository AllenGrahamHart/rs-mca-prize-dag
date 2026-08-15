# Proof

Let `A` be an independent `(c-1)`-set with `q-s` completions.  Their labels
have private coordinates, so they are independent and span a space
`Lambda_0` of dimension `q-s` on a carrier

```text
U=A union {completions},       |U|=q+c-1-s.         (1)
```

Let `W_c` be the span of every support-`c` label.  Starting from
`Lambda_0`, choose at most `s` further support-`c` labels to span `W_c`.
Their union with `U` is a carrier `B` of size at most

```text
q+c-1-s+sc=q+(s+1)(c-1).                           (2)
```

Every support-`c` label has a representation on `B` and its own circuit
representation.  The union of those representations has size at most

```text
q+c-1-s+(s+1)c=q+(s+2)c-s-1.                      (3)
```

Under `(DH)`, (3) is at most `q+10=K`.  Vandermonde independence therefore
forces the circuit support into `B`, proving `(DC)`.

Let `d_c` be the largest nonnegative `s` for which `(DH)` holds.  If the
largest completion count is `q-s` for some `1<=s<=d_c`, use its carrier
cap.  Otherwise every deletion has at most `q-d_c-1` completions.  The
parent deletion count, retaining the maximum over all allowed completion
counts, gives the fallback cap.  Solving `(DH)` gives the four displayed
depths.  Support five has no positive depth and keeps the parent cap.
