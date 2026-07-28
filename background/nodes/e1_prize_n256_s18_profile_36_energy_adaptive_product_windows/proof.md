# Proof

Let the 64 conjugate squares be `y_u=|F(zeta^u)|^2`. The imported profile
identities give mean 18 and average squared deviation `V`. Write the positive
half negacyclic autocorrelation as `(A_d)_(1<=d<64)` and put

```text
E=sum_d A_d^2=V/2,       L=sum_d |A_d|.
```

Every `A_d` is an integer, so `L<=E`. Fourier expansion therefore gives

```text
y_u <= 18+2L <= 18+2E = 18+V.                       (1)
```

Together with the existing coefficient bound, (1) gives
`y_u<=min(144,18+V)`.

## Exact product envelope

The bounded-product parent proves that, for fixed mean, variance, and upper
cap, a product maximum has some entries at the cap and at most two remaining
levels. The certificate enumerates every capped count `k=0,...,63` and every
lower-level multiplicity. Each square root is enclosed between consecutive
rationals with denominator `2^192`; monotonic endpoint substitution gives a
rigorous product interval.

There are 6273 exact rational comparisons. Every extremum is below the
collision threshold in

```text
m=256: V=48,50,...,60,
m=514: V=24,26,...,34.                              (2)
```

At `V=46` and `V=22`, respectively, a lower endpoint remains above the
threshold, so (2) is sharp for this relaxation. This proves the displayed
new cofactor windows.

## Multiplicity-one residue

The cofactor `514=2*257` forces binary multiplicity one. The exact
multiplicity-one child already proves that no profile coefficient vector has
`E=2,...,6`. Hence only `E=7,...,11` remains after (2).

Modulo two, the autocorrelation parity polynomial is
`P(X)P(X^-1)`. Since `P` has `(X+1)`-multiplicity one, this product has
multiplicity two and is nonzero modulo `X^128-1=(X+1)^128`. Thus its positive
half parity mask has weight `q>0`.

For `E<=11`, let `n_j` count autocorrelation entries of magnitude `j`. Exact
integer partitioning of

```text
n_1+4n_2+9n_3=E
```

gives the maximum `L=n_1+2n_2+3n_3` at each parity weight
`q=n_1+n_3`:

```text
E=7:  (q,L)=(3,5),(7,7)
E=8:  (q,L)=(4,6),(8,8)
E=9:  (q,L)=(1,5),(5,7),(9,9)
E=10: (q,L)=(2,6),(6,8),(10,10)
E=11: (q,L)=(3,7),(7,9),(11,11).
```

Rerunning the same exact envelope with `y_u<=18+2L` excludes
`(9,1),(10,2),(11,3),(11,7)`. Every other row has an exact lower interval
above the threshold for this relaxation, leaving precisely the nine pairs in
`statement.md`.
