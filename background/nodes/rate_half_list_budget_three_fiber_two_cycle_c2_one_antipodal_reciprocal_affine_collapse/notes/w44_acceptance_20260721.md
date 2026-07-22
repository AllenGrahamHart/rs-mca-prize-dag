# w44 acceptance record (2026-07-21)

The reciprocal-affine screen ran under the existing route-deciding,
sub-five-minute remote-compute policy. Modal app
`ap-Ifv7cgmA0WCon3SfgP1aSo` covered all `4,495,442` registered progression
moduli in sixteen disjoint shards and found no hit. The longest shard took
`3.13` seconds under `512 MiB`; no retry was used.

The prior 2026-07-21 maintainer ruling for exact remote no-hit screens applies:
the launcher, banked packet, and deterministic checker are hash-pinned by
`verify_screen_certificate.py`, while `verify_screen_remote.py` is registered
as a remote launcher. Re-execution spends Modal credit and is not part of the
local verifier battery.
