# Source evidence

- Common-five horizontal fibers:
  `rate_half_kb_q6_s6_common_five_outgoing_fiber_pin`.
- Coordinate-stabilized preserving lift and source-star equivariance:
  `rate_half_kb_m2_v4_outer_recurrence_router`.
- The one-exchange facets and two-regular pole graph are Corollaries
  9.25--9.28 of the pinned equality-wall source theorem identified in the
  common-five node.

The verifier reconstructs the abstract survivor from records rather than
trusting the printed edge list.

## Upstream custody

The coordinate result and the companion diagonal compiler are exported
together in draft PR `przchojecki/rs-mca#1132` at
`ff133334419f0f1244ae2ab3cbbea515cc33031d`:

```text
note blob:        6302221c51e404f6aa0c0e7f471873e42102e9e6
verifier blob:    8c1fd1318b180f27a3114a3a3beedd7e2ed3efbd
certificate blob: c0f6f9496e4bf43b60358133372ce47bc9b5c8dd
payload SHA-256:  96c47c813c41f4b268b9826ed4866e14d44c5a8187487266a3de6f550cbbf6b6
```

The upstream verifier binds both parents, reconstructs the coordinate
census, profiles, and aligned fixture, replays the diagonal `35 x 12`
kernel, and rejects 17 of 17 hostile mutations.
