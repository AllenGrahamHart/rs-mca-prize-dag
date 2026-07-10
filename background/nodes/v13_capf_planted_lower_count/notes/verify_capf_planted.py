#!/usr/bin/env python3
"""
Exact-arithmetic verifier for thm:capf-planted (v13 raw, lines 6060-6110):
the "image-fiber list-side correction" core claim (petal lane / sec:capf-l1).

CLAIM (verbatim math): D = alpha*H subset F^x a multiplicative coset of a cyclic
subgroup H of order n; C = RS[F,D,k]; M | gcd(n,k); 1 <= sigma < M;
k/M <= n/M - 1.  Then there is a received word U: D -> F with at least
P_M(n,k) = C(n/M - 1, k/M) DISTINCT codewords in F[X]_{<k} agreeing with U on
at least k+sigma positions.

PRE-REGISTERED CRITERIA (falsification-first):
  CONFIRM iff on every untampered instance:
    (i)   deg R_A < k for every A            (degree bookkeeping of the proof)
    (ii)  every planted P_A agrees with U on >= k+sigma points of D (exact count)
    (iii) #distinct codeword evaluation vectors == C(N-1, k/M), N = n/M
    (iv)  brute-force instance: planted family is a subset of the full list
          ImgFib_U^{<k}(k+sigma) enumerated over ALL q^k polynomials, and
          #full list >= planted count
    (v)   non-vacuity: sigma >= 1, planted count >= 2, every fiber of
          x -> x^M on D has size exactly M, |D| == n
  REFUTE if any of (i)-(v) fails on an untampered instance.
  The TAMPER run must FAIL (detector power); if it passes, the harness is vacuous.

All arithmetic exact: python ints mod p, and GF(16) as GF(2)[x]/(x^4+x+1).
"""
import itertools, math, sys

FAILURES = []
def check(cond, label):
    if not cond:
        FAILURES.append(label)
        print("    FAIL:", label)
    return cond

# ---------- field abstractions ----------
class PrimeField:
    def __init__(self, p):
        self.p = p; self.q = p
    def add(s,a,b): return (a+b)%s.p
    def sub(s,a,b): return (a-b)%s.p
    def mul(s,a,b): return (a*b)%s.p
    def neg(s,a):   return (-a)%s.p
    def zero(s): return 0
    def one(s):  return 1
    def elements(s): return range(s.p)
    def units(s): return range(1,s.p)
    def name(s): return f"GF({s.p})"

class GF16:
    """GF(2^4) = GF(2)[x]/(x^4+x+1); elements = ints 0..15 (bit i = coeff of x^i)."""
    def __init__(self):
        self.q = 16
    def add(s,a,b): return a^b
    def sub(s,a,b): return a^b
    def neg(s,a):   return a
    def mul(s,a,b):
        r = 0
        while b:
            if b & 1: r ^= a
            b >>= 1
            a <<= 1
            if a & 0x10: a ^= 0x13   # reduce by x^4+x+1
        return r
    def zero(s): return 0
    def one(s):  return 1
    def elements(s): return range(16)
    def units(s): return range(1,16)
    def name(s): return "GF(16)"

# ---------- polynomial helpers (coeff list, index = degree) ----------
def ptrim(F,a):
    while a and a[-1]==F.zero(): a.pop()
    return a
def padd(F,a,b):
    n=max(len(a),len(b)); r=[F.zero()]*n
    for i,c in enumerate(a): r[i]=F.add(r[i],c)
    for i,c in enumerate(b): r[i]=F.add(r[i],c)
    return ptrim(F,r)
def psub(F,a,b):
    n=max(len(a),len(b)); r=[F.zero()]*n
    for i,c in enumerate(a): r[i]=F.add(r[i],c)
    for i,c in enumerate(b): r[i]=F.sub(r[i],c)
    return ptrim(F,r)
def pmul(F,a,b):
    if not a or not b: return []
    r=[F.zero()]*(len(a)+len(b)-1)
    for i,c in enumerate(a):
        if c==F.zero(): continue
        for j,d in enumerate(b):
            r[i+j]=F.add(r[i+j],F.mul(c,d))
    return ptrim(F,r)
def pdeg(a): return len(a)-1 if a else -1
def peval(F,a,x):
    r=F.zero()
    for c in reversed(a): r=F.add(F.mul(r,x),c)
    return r
def fpow(F,x,e):
    r=F.one()
    for _ in range(e): r=F.mul(r,x)
    return r

def mult_order(F,x):
    r=F.one(); o=0
    while True:
        r=F.mul(r,x); o+=1
        if r==F.one(): return o

def find_order_element(F,n):
    for g in F.units():
        if mult_order(F,g)==(F.q-1):
            return fpow(F,g,(F.q-1)//n), g
    raise RuntimeError("no generator")

# ---------- the planted construction (verbatim from the proof) ----------
def run_instance(F,n,alpha,k,M,sigma,brute=False,tamper=False,label=""):
    global FAILURES
    pre = len(FAILURES)
    N = n//M
    print(f"[{label}] {F.name()}, n={n}, k={k}, M={M}, sigma={sigma}, "
          f"alpha={'nontrivial' if alpha!=F.one() else '1'} -> "
          f"expect count C({N-1},{k//M})={math.comb(N-1,k//M)}, threshold k+sigma={k+sigma}")
    # hypotheses
    assert n % M == 0 and k % M == 0, "M | gcd(n,k) violated"
    assert 1 <= sigma < M, "sigma range violated"
    assert k//M <= N-1, "k/M <= n/M - 1 violated"
    assert (F.q-1) % n == 0, "n must divide |F^x|"
    h,_ = find_order_element(F,n)
    H = []
    x = F.one()
    for _ in range(n): H.append(x); x = F.mul(x,h)
    D = [F.mul(alpha,y) for y in H]
    check(len(set(D))==n, f"{label}: |D|=n")
    # quotient map and fibers
    Q = sorted(set(fpow(F,x,M) for x in D))
    check(len(Q)==N, f"{label}: |Q|=n/M")
    fibers = {b:[x for x in D if fpow(F,x,M)==b] for b in Q}
    check(all(len(v)==M for v in fibers.values()), f"{label}: all fibers size M (non-vacuity v)")
    b0 = Q[0]
    T = fibers[b0][:sigma]
    # E_T
    E = [F.one()]
    for t in T: E = pmul(F,E,[F.neg(t),F.one()])
    # U_0 = X^k * E_T ; received word U on D
    U0 = [F.zero()]*k + E
    U = [peval(F,U0,x) for x in D]
    if tamper:
        # corrupt U at one point lying in a planted agreement set: the first
        # point of the fiber over Q[1] (touched by every A containing Q[1])
        idx = D.index(fibers[Q[1]][0])
        U[idx] = F.add(U[idx], F.one())
        print(f"    (tampered U at one point)")
    ell = k//M
    vecs = set(); planted = []
    ok_deg = True; ok_agree = True
    for A in itertools.combinations(Q[1:], ell):
        # L_A = E_T * prod (X^M - b)
        L = E[:]
        for b in A:
            binom_poly = [F.neg(b)] + [F.zero()]*(M-1) + [F.one()]
            L = pmul(F,L,binom_poly)
        R = psub(F,L,U0)              # R_A = L_A - U_0, so P_A = -R_A
        if pdeg(R) >= k: ok_deg = False
        P = [F.neg(c) for c in R]
        pv = tuple(peval(F,P,x) for x in D)
        agree = sum(1 for i in range(n) if pv[i]==U[i])
        if agree < k+sigma: ok_agree = False
        vecs.add(pv); planted.append(pv)
    cnt = math.comb(N-1,ell)
    check(ok_deg,   f"{label}: (i) deg R_A < k for all A")
    check(ok_agree, f"{label}: (ii) all planted agree >= k+sigma")
    check(len(vecs)==cnt, f"{label}: (iii) distinct codewords == C(N-1,k/M) "
                          f"[got {len(vecs)} vs {cnt}]")
    check(cnt >= 2, f"{label}: (v) planted count >= 2 (non-vacuity)")
    if brute:
        # enumerate ALL P in F[X]_{<k}: q^k of them
        full = set()
        for coeffs in itertools.product(list(F.elements()), repeat=k):
            pv = tuple(peval(F,list(coeffs),x) for x in D)
            agree = sum(1 for i in range(n) if pv[i]==U[i])
            if agree >= k+sigma: full.add(pv)
        check(vecs <= full, f"{label}: (iv) planted subset of full ImgFib list")
        check(len(full) >= cnt, f"{label}: (iv) #ImgFib_U(k+sigma) >= planted count")
        print(f"    brute force: #ImgFib_U^<k({k+sigma}) = {len(full)} "
              f"(>= planted {cnt}) over {F.q**k} polynomials")
    inst_failed = len(FAILURES) > pre
    print(f"    -> {'FAILED' if inst_failed else 'PASS'} "
          f"({len(vecs)} distinct codewords, min agreement "
          f"{min(sum(1 for i in range(n) if p[i]==U[i]) for p in planted)}, "
          f"threshold {k+sigma})")
    return not inst_failed

# ---------- instances (pre-registered) ----------
F31 = PrimeField(31); F61 = PrimeField(61); F13 = PrimeField(13); F16g = GF16()

# nontrivial coset rep for I1: a generator g of GF(31)^x (order 30, not in H of order 15)
_, g31 = find_order_element(F31, 15)
results = []
results.append(run_instance(F31, 15, g31 % 31, 6, 3, 2, label="I1 p=31 coset"))
results.append(run_instance(F61, 30, 1, 12, 6, 5, label="I2a p=61 M=6"))
results.append(run_instance(F61, 30, 1, 12, 2, 1, label="I2b p=61 M=2 count=3003"))
results.append(run_instance(F13, 12, 1, 4, 2, 1, brute=True, label="I3 p=13 BRUTE"))
results.append(run_instance(F16g, 15, 1, 6, 3, 1, label="I4a GF(16) char2"))
results.append(run_instance(F16g, 15, 1, 6, 3, 2, label="I4b GF(16) sigma=2"))

# tamper run: must FAIL (detector power)
pre_t = len(FAILURES)
tamper_ok = run_instance(F31, 15, g31 % 31, 6, 3, 2, tamper=True, label="T1 TAMPER")
tamper_detected = not tamper_ok
# remove tamper-run failures from the ledger (they are expected)
FAILURES = FAILURES[:pre_t]

print()
print("="*70)
print("TAMPER RUN DETECTED:", tamper_detected, "(must be True for a non-vacuous harness)")
if FAILURES:
    print("VERDICT: REFUTED — failures on untampered instances:")
    for f in FAILURES: print("  -", f)
    sys.exit(1)
elif not tamper_detected:
    print("VERDICT: HARNESS VACUOUS — tamper not detected")
    sys.exit(2)
else:
    print("VERDICT: CONFIRMED on all pre-registered instances (exact arithmetic)")
