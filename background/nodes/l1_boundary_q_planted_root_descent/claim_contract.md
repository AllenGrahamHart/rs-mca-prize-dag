# Claim contract - L1 boundary-Q planted-root descent

## Inputs

- the proved boundary affine-Q cell;
- one shifted basis with `d_1=w+1,d_2=omega`;
- an exact affine member and its complete agreement locator.

## Outputs

- determinant identity `W_1P-N_1=c_PL`;
- canonical planted owner `D=gcd(W_1,Omega)`;
- exact removal of every domain root of `W_1`;
- at most one member when `deg D>=k`;
- a root-free rational-Q atom of unchanged depth `w` when `deg D<k`.

## Consumer rule

Compute `D` once from the fixed minimal vector.  Charge its roots as planted
agreements, puncture them once, and apply any future Q theorem only to the
root-free residual `(PR5)`.  Do not enumerate subsets of `roots_H(W_1)`.

## Nonclaims

The punctured domain need not be smooth.  A root-free nonconstant `W_1` is
not identified with `W_1=1`; it remains a rational/quotient Q atom.  No Q
constant or finite reserve fit is asserted.

## Falsifier

An exact affine member violating `(PR1)`, a domain root of `W_1` outside its
agreement set, two members when `deg D>=k`, an extra agreement outside the
split reduced locator, or a change in surplus depth.
