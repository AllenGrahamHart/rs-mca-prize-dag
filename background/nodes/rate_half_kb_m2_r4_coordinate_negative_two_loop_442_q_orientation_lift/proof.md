# Proof

At the `A` loop, orient the `AB` and `AC` edges so both contain `A`.  The
proof of the antipodal-label classifier reduces their exact weld to

```text
x_AB(k_AC-k_B)=x_AC(k_AB-k_B).                    (1)
```

The first identity `(KB44-1)` is exactly the result of squaring `(1)` and
cancelling the distinct-label factor.  Therefore the ratio in `(KB4Q-1)`
has square one.  In odd characteristic it is `+1` or `-1`.  Reversing the
assignment of the `AC` deck orbit negates `x_AC` in this shared-endpoint
orientation and realizes the required sign in `(1)`.

The same argument at the `B` loop gives `(KB4Q-2)`.  The edge in the `AB`
orbit that contains `B` is either the same edge as the one containing `A`
or its deck conjugate; this accounts for the printed fixed sign between
`x_AB^(A)` and `x_AB^(B)`.  Reversing the `BC` orbit changes only the second
equation.  Choose the `AB` orientation freely.  Equation `(1)` then fixes
the `AC` orientation, and its `B` analogue fixes the `BC` orientation.
This gives two and only two triples among the eight.

Each shared-loop equation is a specialization of `(KBNW-2)`.  The Mobius
difference identity in the product-to-q theorem makes it equivalent to
equality of `q_sB_2(s)/R(s)` for that pair of nonloop labels.  The two
equations form a connected tree on `AB,AC,BC`, so all three values agree.
The converse part of that theorem reconstructs the nonzero scalar `c_1`
and all five equations `(KB4Q-3)`. QED.
