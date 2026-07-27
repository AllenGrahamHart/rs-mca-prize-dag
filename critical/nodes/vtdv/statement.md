# vtdv

- **status:** see dag.json (single source of truth; dag status PROVED)
- **closure:** proof (transcribed from the upstream proof_sketch source, 2026-07-27)
- **source:** read with `git -C ../rs-mca show origin/main:experimental/notes/roadmaps/proof_sketch/<file>`

## Statement

SUBGROUP HANKELS ARE FOURIER OBJECTS [transcribed 2026-07-27 from proof_sketch/s3b_iii_2_displacement_spectral.md#1, tagged 'elementary, verified'; upstream experimental/notes/roadmaps/]. For u supported on the subgroup H = mu_n with syndrome s_u[m] = sum_{x in H} u(x) x^m, the Hankel factors as H_{t,j}(u) = V_t^T D_u V_{j+1}, where D_u = diag(u(x))_{x in H} and V_m[x,r] = x^r (r < m). Consequently, for a locator l with root set (co-support) T and w_Z = u + Z v: M(Z) l = 0 IFF the function w_Z * l on H has vanishing Fourier coefficients at frequencies 0..t-1. Verified entrywise on the F_13 / mu_12 toy. A constant syndrome-indexing offset x^{c_0} absorbs into D_u (cosmetic). SCOPE: this node is the factorization identity and its Fourier restatement only; the rigidity mechanism (same file, section 3) is SKETCH and is NOT claimed here.
