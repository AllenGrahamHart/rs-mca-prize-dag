# Fiber-two cycle c=1 parity harmonic characteristic screen

Modal app `ap-Js6Im9DeoBlc0di05YG2WE` completed all 32 preregistered
shards. It processed every

```text
p=1+k*2^40,       29058991<=k<33554432,
```

including composite moduli, for a total of `4,495,441` candidates.
`899,088` multiples of five were rejected as composite before forming
`8/5`. Every other modulus was tested against both exact terminals:

```text
H_P: 41 updates from 8/5,
H_R: 40 updates from 16.
```

There were no hits. The longest shard took 3.121 seconds, well below the
60-second hard timeout and the preregistered `$0.50` ceiling.

The compact result packet stores exact contiguous shard ranges, rolling
digests, processed counts, factor-five counts, and timings. Replay with

```text
tools/ramguard local -- python3 +  experiments/prize_resolution/+rate_half_list_fiber_two_cycle_c1_parity_harmonic_characteristic_check.py
```

The no-hit verdict excludes both residual harmonic `c=1` parity classes
after the proved field router. It says nothing about the six nonharmonic
trace tests or the nonparity normalized chamber.

