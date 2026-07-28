# E1 m16 primitive closure packet

## Status

Candidate theorem, not yet a DAG node. The complete primary census passes.
The independent reverse audit passes on 24,576 of 39,936 affine support
orbits and is source-pinned and resumable. Modal disabled the workspace before
the remaining 15,360 orbits ran.

Promotion is forbidden until the reverse packet is complete, all 1,009
primary high-side representatives are replayed, and the source-pinned node,
DAG, and harness verifiers pass.

## Candidate statement

There is no prize-envelope `N=256`, profile-`(3,6,S=18)` collision with
cofactor `m=16` whose six-singleton binary support has exact multiplicity four
at `X=1` and contains both parities.

Together with the proved once-divided and twice-divided children, this would
exclude cofactor 16 completely for profile `(3,6,S=18)`.

## Imported facts

1. Cofactor 16 forces exact singleton-support multiplicity four.
2. The exact support atlas splits into 39,936 primitive, 9,080 once-divided,
   and 903 twice-divided affine orbits.
3. The product certificate has 967 live `(E,q,L)` chambers, all with `E<=89`,
   and uses the proved chord inequality `4L<=E+117`.
4. The fixed root table has a separate 256-bit Arb audit proving every scaled
   real and imaginary component error strictly below one.

## Free sign involution

Every primitive support contains an odd exponent. Atlas normalization puts a
singleton at exponent zero and global sign normalization gives its coefficient
sign `+1`. Let `j` be the first odd singleton exponent. The Galois automorphism

```text
zeta -> zeta^129 = -zeta
```

sends `F(X)` to `F(-X)`, leaves every support position fixed modulo 128, and
negates exactly the coefficients at odd positions. It preserves norm. It
changes positive-half autocorrelation `A_d` to `(-1)^d A_d`, so it also
preserves `E`, `L`, `q`, and every product-window decision.

The action is free on normalized sign patterns because it flips the sign at
the odd singleton `j`. Therefore the 32 normalized singleton-sign patterns
split into 16 two-element orbits. Choosing the representative with sign `+1`
at `j`, while retaining all eight heavy-sign patterns, is exhaustive up to
Galois conjugacy. The omitted partner of a heavy-sign pattern is obtained by
flipping every odd heavy position as well.

The old direct engine and the optimized engine agree exactly on one orbit in
every primitive odd-chord class; every downstream optimized count is exactly
half of the unquotiented count.

## Exact Walsh energy ledger

For fixed singleton signs and heavy positions, write the lag-`d`
autocorrelation for heavy signs `x,y,z in {+1,-1}` as

```text
A_d(x,y,z)=B_d+x a_d+y b_d+z c_d
             +xy d_d+xz e_d+yz f_d.                 (1)
```

Here `B` is the singleton autocorrelation, `a,b,c` are twice the three
singleton-heavy cross vectors, and `d,e,f` are the three sparse heavy-pair
vectors. Squaring (1) and summing over lags gives

```text
E(x,y,z)=C_0+x C_1+y C_2+z C_4
            +xy C_3+xz C_5+yz C_6+xyz C_7,          (2)
```

where, writing angle brackets for lag-vector dot products,

```text
C_0 = ||B||^2+||a||^2+||b||^2+||c||^2
      +||d||^2+||e||^2+||f||^2,
C_1 = 2(<B,a>+<b,d>+<c,e>),
C_2 = 2(<B,b>+<a,d>+<c,f>),
C_4 = 2(<B,c>+<a,e>+<b,f>),
C_3 = 2(<B,d>+<a,b>+<e,f>),
C_5 = 2(<B,e>+<a,c>+<d,f>),
C_6 = 2(<B,f>+<b,c>+<d,e>),
C_7 = 2(<a,f>+<b,e>+<c,d>).                         (3)
```

Equations (2)--(3) are the XOR convolution square of the seven occupied
characters `{0,1,2,4,3,5,6}` of `(Z/2Z)^3`. The engines precompute the dense
cross-vector dot products, evaluate (2) in constant time, and replay all 63
lags for every energy survivor. The primary asserts that the replayed energy
equals (2); the reverse engine additionally reconstructs the complete
nine-term integer autocorrelation and checks both energy and `L`.

## Independent norm caps

The primary and reverse engines use different strict-below prechecks.

The primary computes all 64 certified upper squared-modulus factors. It rounds
each factor upward to a 16-bit dyadic mantissa. Multiplying these mantissas and
their powers of two gives an exact upper bound for the fixed-root product. It
returns below only when that upper bound is below

```text
16 B_P 2^128 2^(96*64).
```

Every residual receives the original full lower/upper interval.

The reverse engine does not use dyadic mantissas. It multiplies the 64 integer
upper squared-modulus factors exactly, with the original outward product
normalization, and returns below only after exact comparison with the same
floor. Every residual again receives the original full interval. Thus the
two engines share the separately audited root table but not their accelerated
upper-product arithmetic.

## Complete primary ledger

Modal app: `ap-tkhXMEdMpCXgm2LWUnXkEZ`.

```text
affine support orbits:                 39936
sign representatives:                638976
raw heavy triples:                11790704640
sign-distance tests:             188651274240
radius matches:                  184336208507
exact heavy-sign tests:         1474689668056
low-energy representatives:       29756245802
product-live representatives:       5651872006
fixed below:                         5651870997
fixed above:                               1009
fixed unresolved:                            0
```

All 1,009 high-side representatives are retained in the result packet. The
free involution supplies the omitted conjugate partner and does not require a
second norm computation.

## Reverse checkpoint

Modal app: `ap-bvisSxyx7641bXRImfOwy8`.

```text
completed batches:                768 / 1248
completed orbits:               24576 / 39936
per-orbit primary comparisons: 24576 PASS
product-live representatives:     3477665782
fixed below:                       3477665087
fixed above:                              695
fixed unresolved:                           0
worker seconds:                    35110.543061
```

Resume with

```bash
./tools/ramguard modal -- modal run \
  experiments/prize_resolution/e1_profile_36_mu4_m16_primitive_reverse_upper_audit_modal.py
```

The launcher verifies all source and primary hashes, reads the atomic packet,
and submits only batches 768 through 1247. Do not run until Modal is enabled
and credit is confirmed.

## Provisional source pins

These are final for the primary. The reverse result hash must be replaced after
resume because its packet is intentionally incomplete.

```text
primary launcher: b4f2a92cd5399a46a6d0f696439c1855262b8f762f7b49545ea90910b810d106
primary result:   e9a85530e2902ad75d3450762e22a104abdef72c789d6ddf1a4e2586b8975a36
no diagnostic:    cbebea748fa3eb70894edf02a8a86b64b72057fed0d11f0bb964d6c6eb4f3f1c
primary Walsh:    12fb8c254ea862709917bf86d6348b487f7612a4fbe2e4102196ce8f22942e40
primary twist:    ef0e88602425e840fb4041934f48f58d7ef691fc6ded5ebb873192da47077432
primary cap:      dc3caef2ecfed85ef3c9db2731ed3a4f15de55ef4c6c9524615e08fd76d7bf81
reverse launcher: 20f2064a9c2df53a4674ed9afc0556e69857ee310cd819f519b1c5309bdd9baf
reverse partial:  e161b8ceb13e0ce0165fab5843a8d05806a9a434bc3497335b40a22821c14a9c
reverse twist:    f39a23496d74c0253ab2f1618a439c1c9690b633df6c72433c7dcc7abd4f6e21
reverse Walsh:    2582aecf405435057e2ecc5750ee99ea77751f347eb703bd9d94d72711d4e2db
reverse cap:      d08e453e633b5a86a3169b7df89d76bf268ff34cd36d0b299a42e759cb767e88
```

## Final promotion checklist

1. Resume and complete the 480 remaining reverse batches.
2. Require exact agreement with every primary orbit and the full aggregate
   and `live_E` / `above_E` ledgers.
3. Re-enumerate the 39,936-orbit primitive atlas in the node verifier.
4. Replay the integer autocorrelation, live product chamber, primitive support
   condition, and fixed-root lower product for all 1,009 high representatives.
5. Add the primitive `PROVED` node and its evidence edges.
6. Promote a separate full cofactor-16 node from the three proved support
   children.
7. Refresh the manifest and run the node, DAG, and critical-harness verifiers
   on Modal.
