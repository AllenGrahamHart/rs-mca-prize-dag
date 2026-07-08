# F3 h=3 consecutive-core family rates

Status: MACHINE-CHECKED RATE TABLE for the structural families found in the
complete `A=[0,1,2]` consecutive-core census.

## Statement

Inside the oriented slice

```text
A = [0,1,2],  B subset {3,...,95}, |B|=3,
```

the complete census has:

```text
total shapes                  = 129766
fixed-pair family {17,81}     = 91
antipodal-pair family         = 4095
overlap                       = 2
union                         = 4184
outside union                 = 125582
```

Activation counts:

```text
all activations               = 44
fixed-pair activations        = 18 / 91
antipodal-pair activations    = 28 / 4095
overlap activations           = 2 / 2
union activations             = 44 / 4184
outside-union activations     = 0 / 125582
```

Thus the two structural families are not merely descriptive: they are an exact
cover of all common-root activations in this complete subfamily, and the
complement is activation-free.

## Replay

```text
python3 critical/nodes/u1_x4_direct_column_budget/notes/f3_h3_consecutive_core_family_rates.py
```

Expected digest:

```text
H3_CONSECUTIVE_CORE_FAMILY_RATES_PASS
```

