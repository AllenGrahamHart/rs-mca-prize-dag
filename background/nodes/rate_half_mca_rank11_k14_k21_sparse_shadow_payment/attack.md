# Attack notes

The first K'=14 calculation used the valid completion cap but paid low
circuits independently of the rank-nine marks they create.  It failed by
`9995070259076701640612865283374805190095980304653278054869147`.

The joint ledger repairs exactly that duplicated capacity.  It closes not
only K'=14 but the contiguous range through K'=21.  The gap decreases
monotonically across these eight rows and remains positive at K'=21.

At K'=22 the same formula fails by
`2859529280846211417198922209345618432657212793529140162369036`.
The next attack should target this modest boundary deficit.  Candidate
improvements are a sharper completion premium, a stronger shadow weight
for the dominant sparse strata, or coupling kernel incidences to unused
rank-nine marks.  No speculative child premise is introduced here.
