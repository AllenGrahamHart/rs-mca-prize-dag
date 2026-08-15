# Joint sparse shadows pay K'=14..21

- **status:** PROVED
- **closed residual rows:** `14<=K'<=21`
- **units:** `(record, eleven-subset)` component incidences

For each row put

```text
n'=1048576+K',       m'=67472+K',       q=K'-10.
```

Rank-deficient incidences are paid by every nonzero canonical-basis corank
term.  For full-rank incidences, all core sizes `9<=j<K'` are scanned to
obtain a global rank-nine mark capacity `G`.  The completion ladder gives
structured and unstructured support caps `L_c`; the joint ledger gives

```text
I_full <=floor((G+R_actual P_*)/45),

P_*=max_branch sum_(c=2)^5 (45-q_c)L_c.
```

Adding the kernel capacity and comparing with

```text
ceil((990810934/10^9) R_actual C(m',11))
```

is strict on every row `K'=14..21`.  The exact gaps are

```text
14: 21650768172043394032492459946400263590275020562192971022865376
15: 18588028475285812265606143363906671348737995144736255147834120
16: 15524989535492821727324938882048706164611583704587475891361669
17: 12461651333490539307570308245171118440833885273861127661424680
18:  9398013850103444858371174848818672822082629043827750046751608
19:  6334077066154944217959550399858581606171131782792291719264278
20:  3269840962466993657882795068981405767940223879562014346498774
21:   205305519860193617784849691734671763401656917434567909452790
```

The same exact payment first fails at `K'=22`, where capacity exceeds
demand by

```text
2859529280846211417198922209345618432657212793529140162369036.
```

Thus the remaining rank-nine interval is `22<=K'<=15528`.

## Falsifier

An omitted kernel corank; a larger honest core-offset chart; a sparse
premium above the completion maximum; reuse of rank-nine marks; a
nonpositive record coefficient; or failure of any exact row comparison.
