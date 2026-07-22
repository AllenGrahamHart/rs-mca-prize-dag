# Claim contract - L1 pullback coverage/kernel tradeoff

## Inputs

- degree cap `k`, pullback degree `s`, and `b` complete domain fibers;
- the component dimensions and kernel exponent from the general pullback
  descent;
- a listed codeword at threshold `k+ell-1` and its partial loss `z`.

## Outputs

The exact kernel identity `(CK2)`, the loss coupling `(CK4)`, and the automatic
fixed-kernel consequences `(CK5)` and `(CK6)`.

## Falsifier

Parameters for which the residue-class sum in `(CK1)` differs from
`max(0,k-sb)`, or a listed codeword violating `z>=ell-1+kappa` when
`kappa>0`.

## Nonclaims

The theorem does not bound `z-ell+1`, prove the Johnson gate, or count wild
and unanchored maps.
