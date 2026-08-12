# Proof

## 1. The determinantal identity (DET)

With entries in `F_q[x][z]`,

```text
[[f + zg,  k + zf],
 [g - zh,  f + zg]]
```

has determinant `(f+zg)^2 - (k+zf)(g-zh)`. Expanding,

```text
(f^2 + 2fgz + g^2 z^2) - (kg - khz + fgz - fhz^2)
   = (f^2 - kg) + z(2fg + kh - fg) + z^2(g^2 + fh)
   = (f^2 - kg) + z(fg + hk) + z^2(g^2 + hf).
```

This is an identity in `F_q[x][z]`; the verifier re-checks it coefficient by
coefficient on random draws over two fields. Under (PAR) the right-hand side
is `L*Q_z`, which is (DET).

## 2. The syzygies (SYZ)

Write `A = f^2-kg`, `B = fg+hk`, `C = g^2+hf`. Then

```text
f*C - g*B = f(g^2+hf) - g(fg+hk) = fg^2 + hf^2 - fg^2 - ghk
          = h(f^2 - kg) = h*A,
f*B - k*C = f(fg+hk) - k(g^2+hf) = f^2 g + fhk - kg^2 - khf
          = g(f^2 - kg) = g*A.
```

Both are polynomial identities, valid without any hypothesis.

## 3. Two conditions suffice, and the exception is exactly `f(ell)=g(ell)=0`

Suppose `A(ell) = C(ell) = 0`. By the first syzygy `g(ell)B(ell) = 0`; by the
second `f(ell)B(ell) = 0`. Hence `B(ell) = 0` unless `f(ell) = g(ell) = 0`.

Conversely, if `f(ell) = g(ell) = 0` then `A(ell) = -k(ell)g(ell) = 0` and
`C(ell) = g(ell)^2 + h(ell)f(ell) = 0` hold automatically, while
`B(ell) = f(ell)g(ell) + h(ell)k(ell) = h(ell)k(ell)` is free. The exception
is therefore nonempty exactly on `{f(ell) = g(ell) = 0, h(ell)k(ell) != 0}`.
The verifier confirms this **exhaustively** over all `13^4` local value
4-tuples: every tuple with `A = C = 0` and `B != 0` has `f = g = 0`, and there
are `144 = (13-1)^2` of them, matching the free pair `(h,k)` with
`h k != 0`.

Consequently imposing `L | A` and `L | C` imposes `L | B` as well off the
exceptional locus, which is why (PAR) carries exactly two conditions at
`ell`.

## 4. (RES), forward direction

Under (PAR) the linear form `L` divides `A`, `B` and `C` simultaneously, so
`gcd(A,B,C)` is divisible by `L` and in particular is not `1`. The verifier
checks this on the certified witness by exact division.

The converse — that a nonconstant gcd forces `det M(B) = 0`, i.e. membership
— is **not proved here**. The source bank supports it with a `1200/1200`
measurement over two fields.

## 5. Dimension

`(f,g,h,k)` contribute `4 x 5 = 20` coordinates, `ell` one more, the two
conditions at `ell` remove two, and the overall scaling removes one:
`20 + 1 - 2 - 1 = 18`. The fibres of `B -> Q` and of `Q -> B` were both
measured to have nullity `1` on `40/40` draws per field, so the image
dimension is `18` — the same value the round-35 determinantal count gives as
`23 - 5`.

## 6. The certified witness

The verifier rebuilds the banked `q = 97`, `T = 2` object entirely from
`(f,g,h,k,L)`: it forms `A, B, C`, divides by `L`, and recovers
`Q_0, Q_1, Q_2` exactly; then it checks `deg = (7,7,7)`, `s = 0`,
`M(Z)Q_Z = 0` entrywise against the banked `(y_0,y_1)`, `nullity(36x32) = 1`
with `(y_0,y_1)` spanning that kernel, generic rank `7` with a single finite
rank drop at `z = 89` to rank `6` and full rank at infinity, the absence of
any kernel vector of parameter degree `<= 1` (so the minimal index is exactly
`e = m = 2`), and `T = 2` over `mu_32` counting `z = infinity`, with
`|S_0 ^ S_2| = 0`.
