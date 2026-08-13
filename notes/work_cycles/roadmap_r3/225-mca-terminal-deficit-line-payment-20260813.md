# Cycle 225: MCA terminal-deficit line payment (2026-08-13)

The support-only Delsarte screen erased the slope data and gave no saving.
Returning to slope ownership exposes a rigid exact endpoint layer.  At
outside deficit `h=e`, an explanation has exactly `m-e` outside agreements,
so a selected slope forces agreement on every coordinate of `E=supp(q)`.

When `e>=K`, evaluation on `E` is injective for degree-`<K` codewords.
Consequently, all exact-terminal explanations lie on one affine codeword
line.  Outside `E`, their agreement sets are disjoint after deleting a
common zero core of size at most `c=K-1`.  With

```text
n=N-e,       A=m-e,
```

the exact terminal layer therefore has size at most

```text
floor((n-c)/(A-c)).
```

For deficits below `e`, retain the preceding Johnson/mean-centered
cumulative caps and take suffix minima only over the prefix `h<e`.  Adding
the terminal line cap pays one new support in each official row:

```text
KoalaBear e=64048:   prefix 181326056 + line 287 = 181326343;
Mersenne e=65455:    prefix  16100154 + line 493 =  16100647.
```

The next KoalaBear support has no cumulative cap at `h=e-1`.  The next
Mersenne profile is valid but equals `17119507`, exceeding budget by
`342292`.  Thus this is a clean one-cell structural gain, not a closure of
the remaining middle-support interval.

```text
start:                   bb43a4db0
canonical prize:         c8d48cd4b (no newer Fable commit at discovery)
upstream export head:    #1165 @ bb9df40b; import note posted to #1164
result:                  NARROWED + EXPORTED; one PROVED field-general
                         endpoint lemma
DAG delta:               +1 PROVED node, +2 edges
critical status delta:   none; replacement target remains TARGET
full-lift residuals:     KoalaBear 64049<=e<=1044238;
                         Mersenne 65456<=e<=1044241
delta-star movement:     none
compute:                 exact local integer arithmetic under RAMguard;
                         no Modal
next route action:       control the last several high-deficit layers
                         jointly, or retain full-lift near-MDS extension
                         structure throughout the profile
```
