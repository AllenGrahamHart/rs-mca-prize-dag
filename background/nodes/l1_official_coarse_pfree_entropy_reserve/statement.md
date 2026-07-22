# L1 official coarse p-free entropy reserve

- **status:** PROVED
- **role:** show that forgetting Frobenius checkpoints creates no ambient-
  average obstruction on official rows
- **consumer:** `l1_mixed_petal_amplification`

## Setup

Use the official generated-field setup. Write `q=|F|`, let

```text
d_0=sigma_0=ell_0-1,       a_0=k+d_0,
```

and use the proved bounds

```text
n>=2^13,       n | q-1,       k/n in {1/2,1/4,1/8,1/16},
ell_0<=p-3174,       p>n/24.                         (CER1)
```

For a depth `d_0<=d<=n-k`, put `a=k+d` and `r=floor(d/p)`. On the
`binom(n,a)` degree-`a` split locators supported on the evaluation domain,
let the mixed prefix map retain all `d` Newton coordinates and let the coarse
p-free map forget the `r` elementary checkpoints. Their ambient target
averages are

```text
mu_mix(d)=binom(n,k+d)/q^d,
mu_free(d)=binom(n,k+d)/q^(d-r).                     (CER2)
```

## Checkpoint-depth reserve

At every depth containing a checkpoint, `d>=p`. With
`Delta=d-d_0`, one has

```text
Delta>=3175,       r<=23,
mu_free(d)/mu_mix(d_0)
  <=15^Delta/q^(Delta-r)
  <2^(-28276).                                      (CER3)
```

The canonical reserve gives `mu_mix(d_0)<=1`, hence

```text
mu_free(d)<2^(-28276).                               (CER4)
```

If

```text
K_d=max_s |Fib_free(d,s)|/mu_free(d)                 (CER5)
```

is the ambient max-to-average inflation, then the finite sufficient condition

```text
K_d<=q 2^28148                                       (CER6)
```

implies `max_s |Fib_free(d,s)|<q/2^128`. Every mixed locator-prefix
fiber at that depth is a subset of one such coarse fiber.

## Per-condition endpoint

The generated-field structure gives a sharper route-specific conclusion.
Write `q=p^f`. If a checkpoint depth exists then `p<=d<=n-k`, so `p+1<n`
and the integer order bound forces `f>=2`. Moreover the canonical reserve
estimate gives

```text
log_2 q>22,
d_0<=ceil(5(p+1)/44)<=5(p+1)/44+1.                  (CER7)
```

Let `Exc_d(s)` be a nonnegative owner-pruned extras count after an exact
structured subtraction. Consequently any such residual satisfying

```text
max_s Exc_d(s)<=2^(15(d-r)) mu_free(d)               (CER8)
```

obeys the stronger absolute estimate

```text
max_s Exc_d(s)<2^-3393<1,                            (CER9)
```

and hence `Exc_d(s)=0` for every target. Thus the `2^15` per-p-free-condition
endpoint printed by the F2 campaign is **arithmetically sufficient** for an
owner-pruned L1 residual on the official checkpoint range. This is only a
constant/budget compatibility statement: F2's zero-target structured-extras
census is not a uniform arbitrary-target, received-word, first-owner
subtraction. The structured fibers are not bounded by `(CER8)` and must stay
in their separate paid owners.

## Scope

This theorem proves an average reserve and sufficient full-fiber and extras
targets. It does not prove `(CER6)` or `(CER8)`, construct the structured
subtraction, transport the F2 map or owner, bound a Pade-graph intersection,
coalesce positive-cofactor targets, or close L1. It applies only once `d>=p`;
the checkpoint-free Newton window retains its existing Q obligation.
