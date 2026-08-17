## Preregistered O0b `FFF` R76 coefficients

- **decision:** form `R76(s)=Res_E(q7,q6)` by the exact quadratic
  resultant identity and reduce its nine possible `s)-coefficients
  separately modulo the admissible base graph
- **scope:** a necessary common-`E` equation for the last open canonical
  `FFF` chart; no equation is adjoined
- **launcher SHA-256:**
  `dd023822f098b72c15504e8176417a21b75b7882fb0451ecaf1029aa51849130`
- **outcome-neutral checker SHA-256:**
  `0e9f1a2c44907dc58b74c40bf28c63d045cfb7acae0f98b58ab285d939199370`
- **program core SHA-256:**
  `7cb0d1b17e2c8175afd59a90be30b84f9409fdad457f3df454119fe2262a22f6`
- **generated Singular SHA-256:**
  `0cf19ceb9bba5f6c2b604f8d352a36c924bc34015538ee7cffe66565768c8d59`
- **source graph result SHA-256:**
  `5a2ecd10e0be462a9a695d0a880227cd995de5952f999fc93ec17282b9fe94c1`
- **source graph basis SHA-256:**
  `7f59b5557597f429a3a56914cd5aad5c988902af6d88a3ef01580aaacbdd5d9e`
- **input ledger:** base variables `x,t,r,c,b`; both input equations
  have `E)-degree 2; coefficient order `0,...,8`; maximum
  `s)-degree 8; 48-element dimension-one graph basis
- **envelope:** one CPU, 4 GiB, 240-second Singular child wall and
  300-second container wall; projected cost below `$0.07`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; no local CAS

The core reconstructs `q6` from coefficient convolutions, applies

```text
Res(p,q) = (p2*q0-p0*q2)^2
           - (p2*q1-p1*q2)*(p1*q0-p0*q1)
```

to `q7,q6`, and independently verifies the resulting degree-eight bound
symbolically. Each completed coefficient is retained in full with its own
hash. Completion supplies exact input for eliminating `s` against the
banked quadratic `q5`; timeout retains a checked prefix. Neither outcome
alone closes `FFF`.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_fff_r76_coefficients_modal.py
```

**Outcome:** preregistered; not yet run.
