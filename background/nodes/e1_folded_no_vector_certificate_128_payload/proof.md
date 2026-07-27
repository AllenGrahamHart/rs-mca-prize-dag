# proof: e1_folded_no_vector_certificate_128_payload (Modal fpylll, named field)

Over the named field p = 562949953421383*2^200 + 1 (250-bit, Pocklington-prime,
p = 1 mod 256), zeta = primitive 128th root, the folded kernel lattice
L = {w in Z^64 : sum_x w_x zeta^x = 0 mod p} (covolume p) was BKZ-reduced and
its shortest vector computed (notes/modal_e1_cert.py, fpylll):

    shortest_norm = 31.67  >  box threshold 2*sqrt(64) = 16.0
    (shortest vector has inf-norm 9 -- NOT a {-2..2} box vector)

Since lambda_1 = 31.67 > 16, NO nonzero w in {-2,-1,0,1,2}^64 lies in L. Hence
no non-cyclotomic folded collision at the N'=128 cell. CERTIFIED. (2-power N'
=> zeta^0..zeta^63 are a Q-basis, so L carries no char-0 cyclotomic relations;
every L-vector is an accidental mod-p collision, all excluded.)
