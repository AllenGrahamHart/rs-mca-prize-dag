# DLI first-junction split-Pell normal form

- **status:** PROVED
- **closure:** exact polynomial bijection
- **consumer:** `dli_c2pp_joint_reserve`

Let `n=2h`, `t=2L`, `1<=L<h`, and let `zeta` have exact order `n` in an
odd-characteristic field. Put

```text
x_i=zeta^i,       y_i=x_i^2,       H={y_i:0<=i<h}.
```

For a binary word written in antipodal pairs `(a_i,b_i)`, let `A,W` be the
unique polynomials of degree below `h` satisfying

```text
A(y_i)=a_i+b_i-1,       W(y_i)=x_i(a_i-b_i).              (SP1)
```

Then the first `t` moments vanish if and only if

```text
deg A <= h-L-1,
W(0)=0,       deg W <= h-L.                               (SP2)
```

The binary alphabet is equivalent to the two split-Pell congruences

```text
Y^h-1 divides A(A^2-1),
Y^h-1 divides W^2+Y A^2-Y.                                (SP3)
```

Conversely, every pair `A,W` satisfying `(SP2)` and `(SP3)` recovers one
binary word through `(SP1)`. The word is primitive under antipodal
first-owner deletion if and only if `W` is nonzero.

Consequently the primitive first-junction numerator `Z_0-C_1` is exactly the
number of nonzero-`W` solutions of `(SP2)`--`(SP3)`. Moreover, if `L<=h/2`,

```text
W^2+Y A^2-Y=(Y^h-1)Q,       deg Q<=h-2L.                 (SP4)
```

If `L>h/2`, the left side is identically zero.

No bound on the number of such pairs is asserted.
