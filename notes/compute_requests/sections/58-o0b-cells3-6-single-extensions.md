## Preregistered O0b cells-3/6 single-equation extensions

- **decision:** search for a tractable ordering of the four equations hidden
  behind the first-prefix `q4` bottleneck
- **scope:** case `(cell=3,S0,sigma_o=-1,epsilon=(-1,-1),xi=2,pairing=0)`;
  independently extend the retained `q3` basis by one of `q4,q5,q6,q7`
- **launcher SHA-256:**
  `97dc167ee95336920cf54acccb30f09d381aa8f69b429448a39ef70d4e8bb577`
- **outcome-neutral checker SHA-256:**
  `af1029828d47963ecbfa1d93a68668903281c554f8536df1d16a6b63cd1595e0`
- **initial-prefix result SHA-256:**
  `486c36b63335f0b30aa17008481df341869f5d37b32456d58fc40438deb7daa6`
- **cached common input SHA-256:**
  `28c97e75aa1fd80565ad926e95ab2eacf4ce62a692520ca2662de6845ee0ddd8`
- **cached outside compiler SHA-256:**
  `048e38650d7ab98ee9c21d081d4908ed067f57fe483a6e4b6890fab3fa755b03`
- **envelope:** at most four one-CPU workers, 4 GiB each, 180-second
  Singular child wall and 230-second container wall; projected cost below
  `$0.20`
- **local safety:** unordered result streaming with immediate checkpoints
  under one RAM-guarded Modal client and a 300-second external hard stop

Each worker begins with the exact retained 51-polynomial basis of the common
ideal plus `q3`, reduces its one new equation modulo that basis, records the
normal-form degree and term count when available, and retains the exact new
basis on completion. An easy `q5`, `q6`, or `q7` extension authorizes a staged
ordering experiment from that basis; a timed `q4` row merely confirms the
localized computational obstruction. No row proves emptiness, and this run
does not authorize another representative or a full campaign.

Launch command:

```text
tools/ramguard modal -- timeout --signal=TERM --kill-after=15s 300s \
  ~/.venvs/modal/bin/modal run \
  experiments/prize_resolution/rate_half_kb_positive_433_1b_o0b_split_cells3_6_single_extensions_modal.py
```
