import modal
img = (modal.Image.debian_slim(python_version="3.11")
       .apt_install("libgmp-dev","libmpfr-dev","libqd-dev","pkg-config")
       .pip_install("sympy","fpylll"))
app = modal.App("rs-mca-lattice-cert")

@app.function(image=img, cpu=8.0, memory=16384, timeout=10800)
def certify(Np, pbits):
    """Folded short-vector certificate for the certifier nodes (integer_code_
    distance_cert, u2_per_row_certifier) + finite e1_fullness. L = {w in Z^n :
    sum_x w_x zeta^x == 0 mod p}, n = Np/2, zeta order Np. A collision has
    |w|_inf <= 2 => |w|_2 <= 2*sqrt(n). So lambda_1(L) > 2*sqrt(n) => CERTIFIED
    (no non-cyclotomic collision at this prime); else a short vector is a
    collision (survivable/charged). Exact SVP = rigorous verdict."""
    import sympy, math
    from fpylll import IntegerMatrix, LLL, BKZ, SVP, GSO
    n = Np // 2
    # stand-in prime p = 1 mod Np, ~pbits bits (Row-C shape: labeled stand-in)
    lo = 1 << (pbits - 1)
    p = lo - (lo % Np) + 1
    while not sympy.isprime(p): p += Np
    # zeta of order Np: g^((p-1)/Np), g a primitive root
    g = sympy.primitive_root(p)
    zeta = pow(g, (p - 1) // Np, p)
    assert pow(zeta, Np, p) == 1 and pow(zeta, Np // 2, p) == p - 1
    a = [pow(zeta, x, p) for x in range(n)]
    # basis of L (det = p): b0 = p e0; b_i = e_i - a_i e0 (i>=1)
    B = IntegerMatrix(n, n)
    B[0, 0] = p
    for i in range(1, n):
        B[i, i] = 1
        B[i, 0] = (-a[i]) % p
    LLL.reduction(B)
    # BKZ for a strong basis
    bs = min(40, n)
    BKZ.reduction(B, BKZ.Param(block_size=bs, max_loops=8))
    # shortest found (upper bound on lambda_1)
    def norm2(row): return sum(int(x) * int(x) for x in row)
    bkz_short = min(norm2(B[i]) for i in range(n))
    # GSO min ||b*_i||^2 (lower bound on lambda_1^2)
    M = GSO.Mat(B); M.update_gso()
    gso_min = min(M.get_r(i, i) for i in range(n))
    thr2 = (2.0 * math.sqrt(n)) ** 2
    verdict = None; exact = None
    try:
        v = SVP.shortest_vector(B)  # exact
        exact = sum(int(x) * int(x) for x in v)
        verdict = "CERTIFIED" if exact > thr2 else "COLLISION"
    except Exception as e:
        # fall back to bounds
        if gso_min > thr2: verdict = "CERTIFIED (GSO lower bound)"
        elif bkz_short <= thr2: verdict = "COLLISION (BKZ found short)"
        else: verdict = "INCONCLUSIVE (%s)" % str(e)[:40]
    return dict(Np=Np, n=n, pbits=pbits, p_hi=str(p)[:14] + "...",
                threshold_norm=round(2 * math.sqrt(n), 3),
                lambda1_exact_norm=round(math.sqrt(exact), 3) if exact else None,
                bkz_shortest_norm=round(math.sqrt(bkz_short), 3),
                gso_lower_norm=round(math.sqrt(gso_min), 3),
                verdict=verdict)

@app.local_entrypoint()
def main():
    import json
    jobs = [
        certify.spawn(16, 40),    # validation: p=60161-ish, expect CERTIFIED
        certify.spawn(32, 40),    # validation: expect COLLISION (MITM found some)
        certify.spawn(128, 250),  # THE REAL ROW-C CELL: dim 64, 250-bit stand-in
        certify.spawn(256, 250),  # stretch: dim 128
    ]
    out = [j.get() for j in jobs]
    print("LATTICE_CERT_RESULTS " + json.dumps(out))
