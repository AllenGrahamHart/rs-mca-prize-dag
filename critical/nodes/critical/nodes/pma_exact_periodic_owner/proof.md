# Proof - PMA exact-periodic source owner

## 1. Canonical owner at one exact scale

Fix `M|n` with `1<M<n` and a listed codeword `P` whose full agreement set
`A_P` has exact stabilizer order `M`. A cyclic group has a unique subgroup
`K_M` of order `M`. Stabilizer invariance says that `A_P` is a union of
`K_M`-cosets. Since its stabilizer is proper, `A_P` is not all of `H`.

Let `N=n/M` and order the `N` cosets of `K_M` once and for all. The set
`A_P` contains at least

```text
h_M=ceil(a/M)
```

cosets because `|A_P|>=a`. It contains at most `N-1` cosets because it is
proper. In particular, the exact-`M` class is empty when `h_M=N`.

When `h_M<N`, let `I_M(P)` be the union of the first `h_M` contained cosets.
Suppose two listed codewords `P` and `P'` of exact scale `M` have the same
owner. Both agree with `U` on every point of that owner, so `P-P'` has at
least

```text
M h_M >= a = k+sigma > k-1
```

distinct roots. Since both polynomials have degree less than `k`, this forces
`P=P'`. Their full agreement sets are then equal as well. Hence

```text
P -> I_M(P)
```

is injective, and there are only `binom(N,h_M)` possible owners.

Put `A_M=M h_M`. Pascal's ratio gives

```text
binom(N,h_M)
  = N/(N-h_M) binom(N-1,h_M)
  = n/(n-A_M) binom(N-1,h_M).
```

For `M=n`, an invariant nonempty agreement set is all of `H`; at most one
degree-`<k` polynomial can agree with `U` everywhere. Finally, `M(P)` is a
function of the full agreement set, so exact-scale classes are pairwise
disjoint. This proves `(QOWN)` and the global first-match assertion.

The proof uses the actual full agreement set of the source codeword. It never
chooses a PMA defect chart, auxiliary polynomial, or sunflower presentation.
Consequently multiple source charts for one codeword do not create multiple
owners.

## 2. Official `sigma=1` allowance

Now let `n=2^j`, `k=rho n`, and `a=k+1` on the grid in the statement. Put
`M_cut=(n-k)/2`. For each dyadic `2<=M<=M_cut`, the proved QA.22 extension
gives

```text
A_M=M ceil((k+1)/M)<=n-M,
n/(n-A_M)<=4,
sum_(2<=M<=M_cut) Q_M(A_M)
  <= (1+2^-690) Q_2(k+2).
```

Applying `(QOWN)` scale by scale therefore gives

```text
sum_(2<=M<=M_cut) #{P:M(P)=M}
 <= 4(1+2^-690) Q_2(k+2).                         (1)
```

Because `rho<=1/2`, one has `n/4<=M_cut<n/2`. The only dyadic divisors greater
than `M_cut` are `n/2` and `n`. At `M=n/2`, the quotient length is two. If
`rho=1/2`, then `h_M=2`, so the exact-`M` class is empty. At the other three
rates, `h_M=1`, so `(QOWN)` bounds it by `binom(2,1)=2`. The exact-`n` class
has size at most one. Thus all scales above `M_cut` contribute at most three.
Together with `(1)`,

```text
#QOWN_per <= 4(1+2^-690) Q_2(k+2)+3.              (2)
```

QA.22 also proves `Q_2(k+2)>=1`. Therefore

```text
4(1+2^-690) Q_2(k+2)+3
 <= 719(1+2^-690) Q_2(k+2),
```

since already `4(1+2^-690)+3<719(1+2^-690)`. This proves `(FINITE)`.

The bound counts all exact-periodic codewords for the received word before
any structural router is applied. It therefore replaces, rather than adds to,
chart-local charges for the same codewords.
