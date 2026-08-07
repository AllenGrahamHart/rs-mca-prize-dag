"""rl_lib -- round-22 f2_rlocality pilot: the R-locality deficit, made exact.

DRAFT ONLY (notes/pilots_20260807/f2_rlocality/).  Every functional here is
NAMED in PREREG.md section A (CATCH-19C).  Nothing in this file touches
dag.json, nodes/, or tools/.

Official row (tern_route_b/PROOFS.md:58-61):
    p = 18446735827372343297, e_p = 39, S = 2**38,
    R = 4294967340 (banked)  or  4294967339 (exact balance),
    log2 p = 63.999999355 ,  R/S = 1/log2 p  (saturation).
"""

import math

# ---------------------------------------------------------------- constants
P_OFF = 18446735827372343297
S_OFF = 2 ** 38
R_OFF = 4294967340            # banked reading, R = ceil(t/2)
R_OFF_BAL = 4294967339        # exact-balance reading
L_OFF = math.log2(P_OFF)      # = 63.999999355...

LOG2E = 1.0 / math.log(2.0)
CSTAR = 1.0 / math.log(2.0) - 1.0       # 0.4426950409... (COROLLARY ZM)


# ------------------------------------------------------- the local cost d(c)
def d_cost(c, p):
    """d(c) = -2 log2|cos(pi c / p)|  (tail_count THEOREM 1)."""
    return -2.0 * math.log2(abs(math.cos(math.pi * c / p)))


def rho_interval(D):
    """rho(D) = |A(D)|/p -> (2/pi) arccos(2^{-D/2})   (tail_count THEOREM 9)."""
    if D <= 0.0:
        return 0.0
    x = 2.0 ** (-D / 2.0)
    if x >= 1.0:
        return 0.0
    return (2.0 / math.pi) * math.acos(x)


# ---------------------------------------- the flat model (p -> infinity CGF)
def Lambda_flat(theta):
    """Lambda(theta) = log2 C(2t,t) - t   (tail_count THEOREM 7).

    X = log2(1+cos(2 pi c/p)) = 1 - d(c);  Lambda(1) = 0, Lambda'(1) = c*.
    """
    return (math.lgamma(2.0 * theta + 1.0)
            - 2.0 * math.lgamma(theta + 1.0)) / math.log(2.0) - theta


def Lambda_flat_prime(theta):
    # d/dt [ lgamma(2t+1) - 2 lgamma(t+1) ]/ln2 - 1
    return (2.0 * _digamma(2.0 * theta + 1.0)
            - 2.0 * _digamma(theta + 1.0)) / math.log(2.0) - 1.0


def _digamma(x):
    """psi(x), x > 0 (Lanczos-free recurrence + asymptotic series)."""
    r = 0.0
    while x < 12.0:
        r -= 1.0 / x
        x += 1.0
    f = 1.0 / (x * x)
    return (r + math.log(x) - 0.5 / x
            + f * (-1.0 / 12.0 + f * (1.0 / 120.0 + f * (-1.0 / 252.0
                   + f * (1.0 / 240.0 + f * (-1.0 / 132.0))))))


def I_FLAT(c, L=L_OFF, tol=1e-14):
    """I_FLAT(c): flat-model rate (per S) of {P >= 2^{cS}} = {cost <= (1-c)S}.

    Continuum (p->oo) Cramer rate, capped at L: at finite p the event at
    c = 1 is {all c_s = 0}, probability p^{-S}, so I_FLAT(1) = L EXACTLY.
    """
    if c >= 1.0:
        return L
    lo, hi = 1e-12, 1.0
    while Lambda_flat_prime(hi) < c:
        hi *= 2.0
        if hi > 1e12:
            break
    while hi - lo > tol * max(1.0, hi):
        mid = 0.5 * (lo + hi)
        if Lambda_flat_prime(mid) < c:
            lo = mid
        else:
            hi = mid
    th = 0.5 * (lo + hi)
    return min(th * c - Lambda_flat(th), L)


# ------------------------------------------- the V_1 statistic's flat rate
def _bessel_I(nu, x, tol=1e-17):
    """I_nu(x) for x >= 0 by the ascending series, term-ratio iteration
    (no factorials, no overflow)."""
    if x == 0.0:
        return 1.0 if nu == 0 else 0.0
    t = (x / 2.0) ** nu / math.gamma(nu + 1.0)
    s = t
    k = 0
    q = (x / 2.0) ** 2
    while True:
        t *= q / ((k + 1.0) * (k + nu + 1.0))
        s += t
        k += 1
        if t < tol * s or k > 100000:
            break
    return s


def _log_I0(x):
    return math.log(_bessel_I(0, x))


def _ratio_I1_I0(x):
    return _bessel_I(1, x) / _bessel_I(0, x)


def J_FLAT(eta, L=L_OFF, tol=1e-14):
    """J_FLAT(eta): flat-model rate (per S) of {V_1/|H| >= eta}.

    V_1(u)/|H| = (1/S) sum_s cos(2 pi c_s/p) (route_b LEMMA 2 + LEMMA 5).
    Continuum: Lambda_cos(theta) = log2 I_0(theta ln2).  Capped at L:
    at finite p, {mean cos = 1} = {all c_s = 0}, rate L.
    """
    if eta >= 1.0:
        return L
    if eta <= 0.0:
        return 0.0
    lo, hi = 1e-12, 1.0
    while _ratio_I1_I0(hi) < eta and hi < 1e6:
        hi *= 2.0
    while hi - lo > tol * max(1.0, hi):
        mid = 0.5 * (lo + hi)
        if _ratio_I1_I0(mid) < eta:
            lo = mid
        else:
            hi = mid
    t = 0.5 * (lo + hi)
    return min((t * eta - _log_I0(t)) / math.log(2.0), L)


# --------------------------------------------- the ONE executable instrument
def eta_of_c(c):
    """eta_c = 2^c - 1 (route_b LEMMA 5 / tail_count THEOREM 11)."""
    return 2.0 ** c - 1.0


def I_INSTR(c, L=L_OFF):
    """Exponent per S certified by AM-GM(Lemma 5) -> V_1 -> Z-2 moment
    N_k <= (2k-1)!!|H|^k -> Chebyshev, k = min(R, eta^2 S).

    tail_count THEOREM 11:  (1/L) log2(e eta^2 L)   [branch k = R]
                            log2(e) eta^2           [branch k = eta^2 S]
    """
    eta = eta_of_c(c)
    if eta * eta <= 1.0 / L:
        return LOG2E * eta * eta
    return math.log2(math.e * eta * eta * L) / L


def DEF_INSTR(c, L=L_OFF):
    """THE INSTRUMENT DEFICIT at layer c: required c over certified I_INSTR."""
    v = I_INSTR(c, L)
    return float("inf") if v <= 0.0 else c / v


# ------------------------------------- the four named per-step loss factors
def THETA(c, L=L_OFF):
    """LAYER factor: requirement c vs the flat truth at layer c."""
    return c / I_FLAT(c, L)


def AMGM(c, L=L_OFF):
    """Lemma-5 (AM-GM) linearization loss: flat rate of the true event
    over flat rate of the relaxed event {V_1 >= eta_c |H|}."""
    return I_FLAT(c, L) / J_FLAT(eta_of_c(c), L)


def GAUSS(c, L=L_OFF):
    """Gaussian/(2k-1)!! moment-shape loss: true flat rate of the V_1 event
    over the free-k Chebyshev (= sub-Gaussian) exponent log2(e) eta^2."""
    eta = eta_of_c(c)
    return J_FLAT(eta, L) / (LOG2E * eta * eta)


def CAP(c, L=L_OFF):
    """LOCALITY CAP loss: free-k exponent over the k <= R capped exponent.

    SELF-CORRECTION (2026-08-07, after PREREG section A was written): the
    formula registered in PREREG is the k = R branch only.  When the free
    optimum k = eta^2 S already satisfies k <= R (i.e. eta^2 <= 1/L, i.e.
    c <= 0.16993 at L = 64) the cap is INACTIVE and the factor is exactly 1.
    Both layers named in the registrations (c* and c = 1) lie in the k = R
    branch, so no registered prediction is affected.
    """
    eta = eta_of_c(c)
    if eta * eta <= 1.0 / L:
        return 1.0
    return LOG2E * eta * eta * L / math.log2(math.e * eta * eta * L)


# ----------------------------------------------------- D2 candidate supplies
def I_TYPE(c, L=L_OFF, kmul=1.0):
    """A1 DROP-AMGM: type/binomial-moment bound with locality radius k = kmul*R.
    min{D(nu||mu) : E_nu[d] <= 1-c} = I_FLAT(c)  (Sanov contraction), so the
    exponent per S is (k/S) I_FLAT(c) = kmul * I_FLAT(c)/L."""
    return kmul * I_FLAT(c, L) / L


def var_d_flat():
    """Var(d) under the flat model, closed form:
    E[d] = 2, E[d^2] = 4[(ln2)^2 + pi^2/12]/(ln2)^2."""
    e2 = 4.0 * ((math.log(2.0) ** 2) + (math.pi ** 2) / 12.0) / (math.log(2.0) ** 2)
    return e2 - 4.0


def I_MOM(c, L=L_OFF, kmul=1.0, exact_cgf=True):
    """A2 TRUNCATED-MOMENT: the k-th centred-moment bound on the cost sum,
    k = kmul*R, evaluated through the exact centred CGF

        Lambda2(theta) = log2 E[2^{theta (X - EX)}] = log2 C(2 theta, theta).

    Pr <= k! (theta ln2 t)^{-k} 2^{S Lambda2(theta)},  t = (c - EX) S,
    EX = -(1 - 2/p) -> -1, so exponent per S =
        (k/S) log2( theta ln2 (1+c) e L / kmul ) - Lambda2(theta),  maximised.
    """
    ks = kmul / L                    # k/S
    best = -1e30
    lo, hi = 1e-6, 0.45              # Lambda2 finite for theta > -1/2; upper tail
    n = 4000
    for i in range(n + 1):
        th = lo + (hi - lo) * i / n
        lam2 = ((math.lgamma(2.0 * th + 1.0) - 2.0 * math.lgamma(th + 1.0))
                / math.log(2.0)) if exact_cgf else (th * th * var_d_flat()
                                                    * math.log(2.0) / 2.0)
        arg = th * math.log(2.0) * (1.0 + c) * math.e * L / kmul
        if arg <= 0.0:
            continue
        val = ks * math.log2(arg) - lam2
        if val > best:
            best = val
    return best


def I_BINOM(c, S=S_OFF, R=R_OFF, ngrid=20000):
    """A3 NO-POSITION-ENTROPY: tail_count THEOREM 10 repaired.  Replace the
    union bound |U_c| <= C(S,R) m^R by the binomial-moment bound
        Pr[N_A >= m] <= E[C(N_A,R)] / C(m,R) = C(S,R) rho^R / C(m,R),
    with m = (1-delta)S and A = A(D), D = (1-c)/delta (tail_count THEOREM 9).
    Exponent per S = (1/S)[ log2 C(m,R) - log2 C(S,R) - R log2 rho(D) ].
    """
    L = math.log2(2.0) * 0 + S / R          # = log2 p at saturation
    best, bestd = -1e30, None
    for i in range(1, ngrid):
        delta = i / ngrid
        m = (1.0 - delta) * S
        if m < R + 1:
            continue
        D = (1.0 - c) / delta
        rho = rho_interval(D)
        if rho <= 0.0 or rho >= 1.0:
            continue
        val = (_lchoose(m, R) - _lchoose(S, R) - R * math.log2(rho)) / S
        if val > best:
            best, bestd = val, delta
    return best, bestd, L


def _lchoose(n, k):
    """log2 C(n,k) for real n >= k >= 0 via lgamma."""
    return (math.lgamma(n + 1.0) - math.lgamma(k + 1.0)
            - math.lgamma(n - k + 1.0)) / math.log(2.0)


# ------------------------------------------------------ the pattern LP floor
def OPTPAT_asym(rho, L, kmul):
    """Hermite/Chebyshev-system asymptotics for the two-bin pattern LP
        max{ Pr[N=S] : E[C(N,j)] = C(S,j) rho^j, j = 0..k },  k = kmul*R.
    Exponent per S = (kmul/(2L)) log2( 2 e L (1-rho) / (kmul rho) ).
    (Derived in PROOFS.md section 5; validated against exact LP at small S.)
    """
    return (kmul / (2.0 * L)) * math.log2(2.0 * math.e * L * (1.0 - rho)
                                          / (kmul * rho))


def FLOOR_asym(c, L=L_OFF, kmul=1.0):
    rho = rho_interval(1.0 - c)
    e = OPTPAT_asym(rho, L, kmul)
    return c / e, e, rho
