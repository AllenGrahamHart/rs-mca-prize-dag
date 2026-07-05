# frontier: aqb_averaged_quotient_box

The finite arithmetic part is now separated from the real mathematical leaf
and promoted as `aqb_deficit_arithmetic`.

Verified by `verify.py`:

- `B_I = 429,645,546.773...` bits at `Q = 256`;
- the claimed 429,645,547-bit averaged gain clears that deficit;
- per-fiber gain is `0.000390760348...` bits over `2^40` fiber coordinates;
- the unamplified equality threshold is `Qcrit = 255.90000002...`, matching
  the q-threshold note.

Still open as wired predicates:

- `aqb_c2_family_certificate_payload`: provide the concrete averaged c=2
  quotient-box family certificate;
- `aqb_box_charge_amortization`: prove the box charge amortizes over that
  family by at least the verified bit deficit;
- or prove a tightness/obstruction result showing this route cannot work.

No broad local computation is needed for the remaining step. The live family
payload is an additive-combinatorics/second-moment certificate, not a
constants problem.
