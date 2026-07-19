# `A=1` core-one nonzero-weld trace descent

- **status:** PROVED
- **closure:** proof
- **consumer:** `rate_half_band_closure`
- **dependency:**
  `rate_half_ca_hankel_a1_core_one_zero_weld_exclusion`

Retain the official core-one maximal-degree sharp-cap notation and the exact
two-sided weld

```text
W B-B_X E_Z=Q K,       V B+A E_Z=-P_X K,             (NWT1)
```

where `K!=0`, `c=deg B_X`, `D_*=deg E_Z`, and

```text
1<=c<=C_*=e-5b-1+D_*,       D_* in {0,1}.            (NWT2)
```

## 1. Every nonsaturated domain row

Let `x` be a root of `B_X`. Put

```text
q_x=Q(U,V;x),       R_x=gcd(q_x,P_cl),
q_x=R_x Qhat_x,     P_cl=R_x Phat_x.                 (NWT3)
```

The gcd is taken over a splitting field and is monic up to the fixed
homogeneous normalization. There are homogeneous forms `H_x,J_x` such that

```text
A_x= Phat_x H_x,       B_x=-Qhat_x H_x,
W_x= R_x J_x,
P_X(x)J_x=Phat_x E_Z-Qhat_x V_x,
K_x=-H_x J_x.                                           (NWT4)
```

Let `a_x=deg R_x`, let `delta_x=e_*-v_x>=1` be the component deficit of this
row, and let `epsilon_x` be one when the exceptional supported slope is a
root of `q_x` and zero otherwise. Then

```text
a_x=e_*-delta_x-epsilon_x,
deg Qhat_x=delta_x+epsilon_x,
deg H_x<=a_x-1,       sum_(x:B_X(x)=0)delta_x=C_*.    (NWT5)
```

In particular an active trace `K_x!=0` factors through a quotient of degree
exactly `delta_x+epsilon_x`, and the sum of those row deficits is the already
proved small capacity `C_*`.

## 2. The exceptional supported slope

Suppose `D_*=1`, and let `gamma_0` be the root of `E_Z`. Put

```text
q_0=Q(gamma_0;X),       R_0=gcd(q_0,P_X),
q_0=R_0 Qhat_0,          P_X=R_0 Phat_0.              (NWT6)
```

There are `H_0,J_0` such that

```text
V_0= Phat_0 H_0,       W_0=-Qhat_0 H_0,
B_0= R_0 J_0,
Qhat_0 A_0+P_cl(gamma_0)J_0=Phat_0 B_X,
K_0=-H_0 J_0.                                           (NWT7)
```

Writing `a_0=deg R_0`, the unique root deficit at `gamma_0` gives

```text
a_0>=r-1-c>=e+3b,
deg Qhat_0<=c+1<=e-5b+1,       deg H_0<a_0.           (NWT8)
```

Thus the exceptional trace also has a high-degree saturated gcd and a
capacity-sized complementary quotient.

## 3. Trace-or-descent alternative

Exactly one of the following exhaustive alternatives applies.

1. **Active trace.** Some root `x` of `B_X` has `K_x!=0`, or `D_*=1` and
   `K_(gamma_0)!=0`. Its factorization is given by `(NWT4)` or `(NWT7)`.
2. **Factor descent.** Every listed trace vanishes. Then

   ```text
   B_X E_Z divides K,       K=B_X E_Z K_1,       K_1!=0. (NWT9)
   ```

   The distinct factors can be allocated as

   ```text
   B_X=X_W X_B,       E_Z=Z_W Z_B,
   W=X_W Z_W W_1,     B=X_B Z_B B_1,             (NWT10)
   ```

   and cancellation in `(NWT1)` gives the reduced weld

   ```text
   W_1B_1-1=QK_1,
   V X_B B_1+A Z_W=-P_X X_W X_B Z_W K_1,          (NWT11)
   deg_X K_1<=D_0-1-c,
   deg_(U,V)K_1<=T-1-D_*.                          (NWT12)
   ```

This theorem is an exact local and global router for the nonzero weld. It
does not exclude either alternative and does not close the sharp-cap face or
`rate_half_band_closure`.
