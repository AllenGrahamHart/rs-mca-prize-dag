## Preregistered O0b `FFI` kernel-lifted boundary diagnostic

- **decision:** compare a genuinely sparse graph-lifted formulation against
  the timed substituted-kernel boundary ideal
- **scope:** case `(cell=3,S0,sigma_o=-1,epsilon=(-1,-1),xi=2,pairing=0)`;
  chart mask `FFI` only
- **launcher SHA-256:**
  `aa6ddf1a87175b4e9d238189bc91f952e2e4db73b0b6d191a898cb0ba555cf44`
- **outcome-neutral checker SHA-256:**
  `74783c856fffb0c1aed80bf139193be0bef28621371df729e1d35e32451e9529`
- **lifted boundary-program core SHA-256:**
  `af075097d890859b5ce077d2fafa77d8c4eb2755853217e46fb691f7dde21f62`
- **direct boundary result SHA-256:**
  `9e5dd9324b1fe7575c7d16135465bd1c560f3cce9d3effbee5ecece6391109c6`
- **cached common input SHA-256:**
  `28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8`
- **global common basis SHA-256:**
  `bda163ed7bdb961c115cebbe910dd3d991307bd53cddf4770925697d1a5e7c4e`
- **cached outside compiler SHA-256:**
  `048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03`
- **envelope:** one CPU, 4 GiB, 240-second Singular child wall and
  300-second container wall; projected cost below `$0.06`
- **local safety:** one RAM-guarded Modal client under a 360-second external
  hard stop; no local CAS

The program introduces variables `z0,...,z7` and the eight exact graph
equations `zi=ki(t,r,c,b)`. All outside equations are then written sparsely in
the `zi`, with two finite root variables and the Rabinowitsch inversion of
`b+1`. Projection along the graph variables is an isomorphism with the direct
substituted system, so a unit result is an exact chart proof. Completion
authorizes transport to the other three multi-finite masks. A timeout retires
this lifting architecture; it does not authorize a larger run.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 360s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_chart_ffi_lifted_boundary_modal.py
```
