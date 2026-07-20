# Proof

All assertions are finite identities in `F_17`; the verifier exhausts every
field slope and every degree-four split locator on `D`.

The coefficient vectors in ascending degree are

```text
A=(10,10,1,0),       B=(10,7,3,1),
q(z)=A+z(0,14,2,1).                                  (1)
```

Direct Hankel multiplication with `(E1F3)` gives

```text
M_0A=0,
M_0(B-A)+M_1A=0,
M_1(B-A)=0,                                           (2)
```

so `M(z)q(z)=0` identically. Row reduction gives rank two at zero and rank
three at every nonzero finite slope. The two padded shifts of `A` span the
exceptional kernel. Direct contraction of `M_1` to that plane proves
`(E1F4)`. Cofactor expansion proves `(E1F5)` entry by entry; checking all
seventeen values proves the polynomial identity because both sides have
parameter degree at most three.

The lift in `(E1F6)` is defined by

```text
y_(k+1)-y_k=h_k,       y_0=0.                         (3)
```

Consequently `(X-1)Q(z;X)` annihilates the full eight-moment sequence.
Exhaustion of all `C(16,4)=1820` squarefree degree-four domain locators finds
no locator common to both endpoints. It finds supported locators only at the
five finite slopes in `(E1F7)`: at zero, the three-point support can be
padded by any fourth domain point; at each ordinary slope the printed
four-point locator including the fixed core is unique. No degree-four split
locator annihilates the infinity endpoint. The split-pencil equivalence
therefore proves the column-far and exact supported-slope assertions.

For the external blocks, each of the nine listed points occurs exactly once
and `14` occurs zero times. Multiplying their monic locators gives the monic
polynomial on those nine points. Including `A` and the internal `B` gives
the monic polynomial on every residual point except `14`, agreeing with the
supported-fiber resultant at `e=1`.

Finally, exhaustive Vandermonde span tests modulo the columns at `2,5` find
no support of size at most two and exactly the four size-three supports
printed in the statement. This proves quotient distance three and records
the deliberate failure of uniqueness at `r=3`. QED.
