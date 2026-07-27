import modal
img = (modal.Image.debian_slim(python_version="3.11")
       .apt_install("libgmp-dev","libmpfr-dev","libqd-dev","pkg-config")
       .pip_install("cython","cysignals").pip_install("sympy","fpylll"))
app = modal.App("rs-mca-e1-cert")

@app.function(image=img, cpu=8.0, memory=16384, timeout=7200)
def certify(Np):
    """E1 folded no-vector cert at the NAMED field p = 562949953421383*2^200+1.
    L = {w in Z^n : sum_x w_x zeta^x == 0 mod p}, n=Np/2, zeta = primitive Np-th
    root. Box collision: w in {-2..2}^n \\ 0. lambda_1 > 2 sqrt(n) => CERTIFIED
    (no non-cyclotomic collision); else the short vector IS a collision — report
    its coordinates to inspect signed-core vs prize-shape structure."""
    import sympy, math
    from fpylll import IntegerMatrix, LLL, BKZ, SVP, GSO
    c = 562949953421383
    p = c * (2**200) + 1
    assert sympy.isprime(p) and p % Np == 1 and p < 2**256
    n = Np // 2
    g = sympy.primitive_root(p)
    zeta = pow(g, (p - 1) // Np, p)
    assert pow(zeta, Np, p) == 1 and pow(zeta, Np // 2, p) == p - 1
    a = [pow(zeta, x, p) for x in range(n)]
    B = IntegerMatrix(n, n)
    B[0, 0] = p
    for i in range(1, n):
        B[i, i] = 1
        B[i, 0] = (-a[i]) % p
    LLL.reduction(B)
    BKZ.reduction(B, BKZ.Param(block_size=min(40, n), max_loops=8))
    def norm2(row): return sum(int(x) * int(x) for x in row)
    bkz_short = min(range(n), key=lambda i: norm2(B[i]))
    bkz_vec = [int(x) for x in B[bkz_short]]
    M = GSO.Mat(B); M.update_gso()
    gso_min = min(M.get_r(i, i) for i in range(n))
    thr2 = (2.0 * math.sqrt(n)) ** 2
    short_vec = bkz_vec; short_n2 = norm2(B[bkz_short])
    try:
        v = SVP.shortest_vector(B)
        if sum(int(x)**2 for x in v) < short_n2:
            short_vec = [int(x) for x in v]; short_n2 = sum(int(x)**2 for x in v)
    except Exception:
        pass
    is_box = max(abs(x) for x in short_vec) <= 2
    verdict = "CERTIFIED (no box collision)" if short_n2 > thr2 else ("BOX COLLISION" if is_box else "short<thr but not box")
    return dict(Np=Np, n=n, p_bits=p.bit_length(),
                threshold_norm=round(2*math.sqrt(n), 3),
                shortest_norm=round(math.sqrt(short_n2), 3),
                gso_lower_norm=round(math.sqrt(gso_min), 3),
                shortest_is_box=is_box,
                shortest_inf_norm=max(abs(x) for x in short_vec),
                shortest_support=sum(1 for x in short_vec if x),
                shortest_vec_head=short_vec[:24],
                verdict=verdict)

@app.local_entrypoint()
def main():
    import json
    jobs=[certify.spawn(128), certify.spawn(256)]
    out=[j.get() for j in jobs]
    print("E1_CERT_RESULTS_START"); print(json.dumps(out)); print("E1_CERT_RESULTS_END")
