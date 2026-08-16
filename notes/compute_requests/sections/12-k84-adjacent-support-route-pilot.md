## Preregistered K'=84 adjacent-support route pilot

- **decision:** determine whether the first new row already breaks the
  proved K'=83 adjacent-support router, and identify the exact first
  obstruction if it does
- **scope:** `ordinary`, exact offsets `1`, `2`, `7`, and the new terminal
  offset `73`, in both primary and independent implementations
- **primary wrapper SHA-256:**
  `a3f55cf0627f63b9786d3f44f526bb44c62d223152424099f1039df04d272a20`
- **audit wrapper SHA-256:**
  `a9a323316bcbef966ad97ca3e24f66220aa41baf8d5115e7ca3f3205e3e37249`
- **hash-pinned K'=83 code archive SHA-256:**
  `327c677b870233b5b43609203a45c12ca478a719da3b9391c61860d9ddbe6b49`
- **dependency archive SHA-256:**
  `5ee5d10a20f1e47b1e5400d10177e33bafdc83c0e9b516d6d12dfe0fad93aaf8`
- **batch runner SHA-256:**
  `bbe9f1100d8d6add611794e24e02d57ab0f57903a15195a944e6fe640ca98922`
- **envelope:** ten remote containers, one CPU and 1 GB each, 645-second
  child wall; projected cost below `$0.20`
- **local safety:** one RAM-guarded Modal client; no local enumeration

The wrappers change only the row parameters to `K'=84`, `q=74`,
`m'=67556`, and `n'=1048660`. The theorem and router sources imported by
the wrappers are the unchanged hash-pinned K'=83 implementations. The five
lanes are route-locating, not an exhaustive row certificate.

```text
PASS:       both implementations agree and all five lanes are safe;
            analyze the active templates symbolically before authorizing
            any remaining-lane wave
FAIL:       both implementations agree on an unsafe lane; retain its exact
            branch as the next analytic wall and do not launch broadly
INCOMPLETE: any timeout, missing lane, or implementation disagreement;
            retain no mathematical conclusion
```

No outcome of this pilot promotes `K'=84` or changes a DAG status.

**Outcome:** `PASS` as a route-locating pilot, with no row promotion.
Modal app `ap-Srv9CDnQL721xYGzAUZoR6` completed all ten jobs without a
timeout at 58--62 MB peak RSS. The raw capture SHA-256 is
`4024f6ad84c050540bfa3c32088e4768a3ca5abf798f95bc8624d054178f9ff4`.
Primary and audit agree exactly on every maximum:

```text
ordinary:  41388798786059119503097492734939028640066114130
           margin 44581160171407926086602515730765812413619
offset 1:  41388509655129434578015936172698056050247199551
           margin 333712089856333007643164756703355631328198
offset 2:  41387937303860893532474667943101838831996305858
           margin 906063358397378548911394352920573882221891
offset 7:  41388695386454290912259500164616925968496091874
           margin 147980764999998764079172837833437382435875
offset 73:   207313827489437078117773167012308731551794440
           margin 41181529539729853832905806170442450674326733309
```

The new leading branch is

```text
s2=74/s3=55/s4=45/s5=37/ordinary-single/
c6d3/c7d2/c8d1/c9d0/raw-safe.
```

Thus the adjacent-support router has not failed at the first new row, but
the maximizer changed from K'=83's offset-two/full-fallback template to an
ordinary single-support-three template. Analyze this branch and the
unsampled-offset domination problem symbolically before any full K'=84
wave.

## Preregistered one-sided raw-template scan

- **decision:** determine whether the new ordinary one-sided support-2/3
  envelope has a short stable family of active defect templates, and
  whether its exact ceiling margin crosses near the K'=84 frontier
- **interval:** every integer `K'=83..128`
- **script SHA-256:**
  `7946d6aa8174768494322aaae67b2472f351dd42fc2d9e82d07c698a23de84f1`
- **scope:** exact raw maximum over both one-sided branches, all
  support-4/5 Pareto vectors, and all support-6/9 Pareto vectors
- **envelope:** one remote CPU, 1 GB, 645-second wall; projected cost below
  `$0.02`

```text
CROSS:      report the first negative margin as the next raw analytic wall
STABLE:     extract the finitely many active affine defect templates and
            prove their binomial/floor margins on maximal intervals
PROLIFERATE: stop the scan route if active templates do not compress;
             do not replace proof by longer row enumeration
INCOMPLETE: retain no conclusion after timeout or malformed output
```

This scan ignores geometry-required cells and cannot close any row.

**Outcome:** `INCOMPLETE`, and the scan exposed a wrong endpoint rather
than a ceiling crossing. Modal app `ap-Rzy1Aw2D71418NHszc7XLf` reached its
645-second child wall at 61 MB peak RSS after printing complete rows
`K'=83..105`; the raw capture SHA-256 is
`20add11719a44044c14fe93d44a31ee3cc6068b6fac1e351b9a9fe9cf2a09787`.
All 23 completed rows have the same parity family

```text
source=3,
M3=floor(q/2),
s2=q,
s3=s4=s5=ceil(q/2),
c6d2/c7d1/c8d1/c9d0.
```

Its *raw* premium already exceeds the ceiling at `K'=83`; for example at
`K'=84` it is
`46986000759234275253755854037693521002636288520`, with margin
`-5597157392014984342732274700238761596757760771`. This is not a
counterexample to the adjacent-support route. The family lies in the
geometry-required support-three cell, where the theorem mandates the
single-completion carrier `(u,g)=(M3+2,8)`. The scan omitted exactly that
charge. Consequently no first-crossing or interval-stability conclusion is
retained, and extending this raw scan would test the wrong quantity.

The useful route information is the compressed parity family itself. The
next preregistered object must be its **post-charge** adjacent-support
premium, compared with the raw-safe ordinary leader and the other charged
families. A row or interval can be promoted only after that charged envelope
is bounded analytically and independently replayed.

## Preregistered support-three post-charge parity evaluation

- **decision:** identify the active adjacent-pair charge and exact margin of
  the isolated parity family after its mandatory single-completion carrier
- **interval:** every integer `K'=83..128`; this is 46 evaluations of one
  explicit template, not a frontier enumeration
- **script SHA-256:**
  `e91052c09731a4e472468aeb046fcee2d35565538c75da8b63798f368acdb13d`
- **template:** `q=K'-10`, `M3=floor(q/2)`,
  `s2=q`, `s3=s4=s5=ceil(q/2)`, high branch
  `c6d2/c7d1/c8d1/c9d0`, carrier `(M3+2,8)`
- **envelope:** one remote CPU, 1 GB, 120-second child wall; projected cost
  below `$0.01`

```text
STABLE:     one adjacent-charge choice per parity; extract and prove the
            corresponding exact floor/binomial inequalities
SWITCH:     finitely many charge changes; split the symbolic interval there
UNSAFE:     a negative post-charge margin is a genuine route obstruction
INCOMPLETE: retain no mathematical conclusion
```

This evaluation can reject or simplify the proposed symbolic route. It
cannot establish domination over the remaining K'=84 lane families and
cannot promote a row by itself.
