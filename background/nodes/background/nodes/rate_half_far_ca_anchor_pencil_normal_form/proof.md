# Proof

For a non-anchor bad slope `gamma`, choose a close codeword `c_gamma` and put

```text
lambda=gamma-gamma_0,
p=(c_gamma-c_0)/lambda in C.
```

Since

```text
f_1+gamma f_2-c_gamma
 =e_0+lambda(f_2-p),                                  (1)
```

the right side has weight at most `r`. Conversely, any nonzero `lambda` and
`p in C` satisfying this weight bound give the close codeword
`c_0+lambda p` at slope `gamma_0+lambda`. The received pair is column-far, so
every close slope is CA-bad. This proves the set equality `(AP1)`.

Consider the code pair

```text
(c_0-gamma_0 p,p).
```

Its difference from the received pair is

```text
(e_0-gamma_0(f_2-p),f_2-p).
```

A coordinate column vanishes exactly when both `e_0` and `f_2-p` vanish.
Thus its column disagreement set is `E_0 union supp(f_2-p)`, of size `s+t`.
Column farness gives `s+t>r`, proving the lower half of `(AP2)`. Outside
`E_0`, the word in `(1)` is nonzero at every point of `T`, so `t<=r`, proving
the upper half.

The `t` forced errors outside `E_0` leave at most `r-t` nonzero coordinates
inside the `s`-point anchor support. Hence at least

```text
s-(r-t)=s+t-r
```

anchor coordinates cancel. At a cancelling coordinate,
`e_0+lambda(f_2-p)=0`, which is exactly the interpolation condition in
`(AP3)`.

Finally, if two codewords `p,p'` work for the same `lambda`, then the two
corresponding close codewords `c_0+lambda p` and `c_0+lambda p'` are each
within radius `r` of the same received word. Their difference has weight at
most `2r<d_min(C)`, so it is zero and `p=p'`. QED.
