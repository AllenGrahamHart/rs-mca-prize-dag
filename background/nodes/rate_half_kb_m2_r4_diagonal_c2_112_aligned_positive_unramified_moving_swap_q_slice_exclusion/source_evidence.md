# Source evidence

Pinned exact sources:

```text
unramified compiler
988e60a010ea2793049505b5e9b0ff6d5c28b300e4a00a4b8a3724849ede09f0

moving router at closure commit `2cb1206a`
1309bd5e7366ce9852fd0f7f030059d0ecafa2685370b8935af19665e7bcf933

moving swap minor cache
cafb0e48b2be45a98e72dbe5a1689f3ffe9a6bda64e685ea152873af48ab3d86

moving swap conic cache
aacf8976e2fe3933055fb8e7d1a90d2b176dad8699ce37cbf2c0f7f3d6fd521e
```

The cache payloads pin the corrected q-slice generator hash and all decoded
polynomial digests. The historical router hash identifies the closure
snapshot; `verify_exact.py` replays the current compatible router and checks
all three terminal PASS contracts. No captured console output is trusted as
a certificate.
