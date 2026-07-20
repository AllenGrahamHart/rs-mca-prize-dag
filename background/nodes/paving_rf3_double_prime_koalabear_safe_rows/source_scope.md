# Source scope

The imported proof packet is pinned to
`przchojecki/rs-mca@999b8f3a1da959b8002ecf1819d37725af56d383`:

```text
experimental/notes/audits/paving_v9_2_rf3_global_degree_bridge.md
  sha256 284b4cb81f308499eb91d5d2470c71c097d2fd36e4bbfebfe2d6432b683e5092

experimental/notes/audits/paving_v9_2_rf3_bridge_ordinary_audit.md
  sha256 fb2400cd2ed67178cc5ef0d58d7565236f33af9ffadbeeed0b4ea4abd7cdcf75
```

They are vendored byte-for-byte as `upstream_bridge.md` and
`upstream_ordinary_audit.md`. The former contains the full corrected paper
proof. The latter records an independent six-lane adversarial re-derivation,
primary-source hash verification, exact row recomputation, and the remaining
formalization boundary.

The immutable Paving v9.2 paper states the weaker RF3 threshold as an
assumption. This node does not relabel that historical statement. It combines
the paper's elementary interpolation proof with the later proved RF3-double-
prime replacement and uses the replacement's larger exact row ceilings.
