# Direction-mismatch recursive shortening

- **status:** PROVED
- **closure:** field-general recurrence plus direct-gate official envelopes
- **scope repair:** initialization uses only the proved direction-distance
  gate at `s=1`

Let the shortened row be `(N,K,m)=(R+s,s,d+s)`.  Let the received-line
direction have nonzero syndrome, minimum lift weight `R-j`, and `0<=j<d`.
If every support-wise MCA-bad child family at dimension `s-1` and direction
defect at most `j` has size at most `M_(s-1)(j)`, then

```text
M_s(j) <= floor((R-j) M_(s-1)(j)/(d-j)).             (RS1)
```

At each dimension this may be combined with the direct direction-distance
gate by taking the smaller bound.

## Repaired official envelopes

Initialize at `s=1` separately for every defect paid by the direct gate.
Exact iteration gives:

```text
KoalaBear: base j<=4340; frontier j<=4337 at s=14;
           j<=4330 at s=22; j=0 through s=4992.
Mersenne:  base j<=4337; frontier j<=4334 at s=6;
           j<=4330 at s=10; j=0 through s=4979.
```

The full checkpoints are pinned in `source_contract.json`.  The KoalaBear
frontier at `s=14` is seven defects wider than the former false-base packet;
the later checkpoints coincide.  Mersenne's printed frontier is unchanged.

No all-defect base case is claimed.  Defects above the repaired frontier at
each dimension remain open.

## Falsifier

A child defect exceeding its parent, failure of the incidence floor `d-j`,
a family violating `(RS1)`, or an incorrect repaired checkpoint.
