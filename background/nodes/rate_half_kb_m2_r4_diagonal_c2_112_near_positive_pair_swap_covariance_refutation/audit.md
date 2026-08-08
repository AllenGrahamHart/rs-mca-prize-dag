# Audit

The probe loads the independent generic reconstruction used by the proved
inversion theorem; it does not import the PR #1140 explicit inverse.

The symbolic core was split into twelve Modal containers. Every shard
returned `PASS`, zero target failures, and exactly two residual failures.
Wall times ranged from 42.20 to 264.08 seconds; the slowest remained below
the 270-second child cap.

The independent destination search used exact rational arithmetic at three
specializations and returned `PASS` in 130.93 seconds. Every one of its
twelve destination lists is empty.

Pinned SHA-256 values:

```text
probe source       4426a63a1d416de82d5ab0e60e665595f2af7624c45a00ac45e01d55a8656d32
Modal wrapper      45b137a9d98a86588e13f70f9b31e87def7005d428908ae844023dbe40f62373
symbolic shards    385f06b7161391c6393c4a8ad8474e3e33b36301dcf137d4f34a914f446aad82
destination search 8445490be6926ad552a113f831f6ca93ab91e34099456ccbf9681033f3f19728
```

An earlier unsharded localizer attempt reached its 870-second remote cap and
made no claim. Localizer comparison was abandoned after the residual
covariance itself was refuted; computing it cannot repair a failed residual
identity.
