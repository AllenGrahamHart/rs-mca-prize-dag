#!/usr/bin/env python3
"""THE ROW LIST (deliverable D1), with file:line provenance for every
constant.  Selection rules are the ones registered in PREREG.md P1.

Nothing here is computed; these are literal transcriptions.
"""

# ---------------------------------------------------------------- PINNED
# R1 rows: a DAG node makes the literal folded-kernel certificate over an
# explicitly printed (field, root, quotient order, box) its OWN payload.

# background/nodes/e1_pocklington_250bit_exhibit_field/statement.md:11-12
P250 = 904625697166646869347790708689937759412227977745095982970820953353127723009
# background/nodes/e1_pocklington_250bit_exhibit_field/statement.md:23-24
RHO128 = 440266185830122294862552098878717819794821358702875176198798016633729926114
# background/nodes/e1_pocklington_250bit_exhibit_field/statement.md:26-27
RHO256 = 368095729527972287347366462180303065908636718991804826343652948937354262881

PINNED = [
    dict(cid="E1-128", kind="PINNED",
         Nprime=128, h=64, p=P250, root=RHO128, L=128, boxinf=2,
         node="background/nodes/e1_folded_no_vector_certificate_128_payload",
         prov=[
             ("p", "background/nodes/e1_pocklington_250bit_exhibit_field/"
                   "statement.md:11-12"),
             ("rho_128", "background/nodes/e1_pocklington_250bit_exhibit_field/"
                         "statement.md:23-24"),
             ("N'=128 + box {-2..2}^64",
              "background/nodes/e1_folded_no_vector_certificate_128_payload/"
              "statement.md:9-16"),
             ("same cell restated",
              "background/nodes/e1_folded_certificate_cell_128_payload/"
              "statement.md:14-15,25"),
         ]),
    dict(cid="E1-256", kind="PINNED",
         Nprime=256, h=128, p=P250, root=RHO256, L=256, boxinf=2,
         node="background/nodes/e1_folded_no_vector_certificate_256_payload",
         prov=[
             ("p", "background/nodes/e1_pocklington_250bit_exhibit_field/"
                   "statement.md:11-12"),
             ("rho_256", "background/nodes/e1_pocklington_250bit_exhibit_field/"
                         "statement.md:26-27"),
             ("N'=256 + box {-2..2}^128",
              "background/nodes/e1_folded_no_vector_certificate_256_payload/"
              "statement.md:8-16"),
         ]),
]

# ------------------------------------------------------------- EXTENSION
# R2 rows: REAL deployed prize characteristics.  No node pins them to an
# N'-folded cell; they are certified as EXTENSION rows and labelled so.
# background/nodes/mca_quadratic_prize_rows/statement.md:29-34
PROTH = [
    ("1/2", 2 ** 41,
     132540169958804033333249306710494641010898987122689, 389500552609),
    ("1/4", 2 ** 42,
     411940680852499481698306614369841346700408394874881, 1210584858040),
    ("1/8", 2 ** 43,
     979947269755402568812854322316630667196565607677953, 2879806199253),
    ("1/16", 2 ** 44,
     2121285573237585848299875619011192262679065433997313, 6233898019554),
]

EXTENSION = [
    dict(cid="PROTH-%s" % r.replace("/", "over"), kind="EXTENSION",
         Nprime=128, h=64, p=p, root=None, L=128, boxinf=2,
         rate=r, n=n, Bstar=B,
         node="background/nodes/mca_quadratic_prize_rows",
         prov=[("p", "background/nodes/mca_quadratic_prize_rows/"
                     "statement.md:%d" % (31 + i)),
               ("Proth certificate + witness",
                "background/nodes/mca_quadratic_prize_rows/verify.py:%d-%d"
                % (18 + 13 * i, 22 + 13 * i))])
    for i, (r, n, p, B) in enumerate(PROTH)
]

# ------------------------------------------------------- PRICED, NOT RUN
# R3 rows: the six deployed clean-anchor rows.  Quotient orders N' = 256,
# 512 -> folded dimensions h = 128, 256.  NO PRIME IS PINNED: the spec
# fixes an interval plus a congruence.
#   background/nodes/qfloor_clean_anchor_norm_threshold_route_cut/
#     statement.md:9-13   (rate -> N', ell')
#   background/nodes/e1_pair_feasible_prime_field_reduction/proof.md:20-24
#     I_C = [2^250, 2^250+2^128-1]
#   background/nodes/e1_pair_feasible_prime_field_reduction/proof.md:38-43
#     I_P = [B_P 2^128, (B_P+1) 2^128-1],  B_P = 3174946747754687731830209...
BP = 317494674775468773183020924238786383963
ANCHOR = [
    dict(cid="RowC-1/4", kind="PRICED", Nprime=256, h=128, ell=65, L=130,
         p=2 ** 250, plabel="min I_C = 2^250"),
    dict(cid="RowC-1/8", kind="PRICED", Nprime=256, h=128, ell=33, L=66,
         p=2 ** 250, plabel="min I_C = 2^250"),
    dict(cid="RowC-1/16", kind="PRICED", Nprime=512, h=256, ell=33, L=66,
         p=2 ** 250, plabel="min I_C = 2^250"),
    dict(cid="prize-1/4", kind="PRICED", Nprime=256, h=128, ell=65, L=130,
         p=BP * 2 ** 128, plabel="min I_P = B_P*2^128"),
    dict(cid="prize-1/8", kind="PRICED", Nprime=256, h=128, ell=33, L=66,
         p=BP * 2 ** 128, plabel="min I_P = B_P*2^128"),
    dict(cid="prize-1/16", kind="PRICED", Nprime=512, h=256, ell=33, L=66,
         p=BP * 2 ** 128, plabel="min I_P = B_P*2^128"),
]

# ---------------------------------------------------- corridor literal prime
# critical/nodes/corridor_ledger/verify_corridor_literal_prime.py:22-26
QCORR = 108037839417390090843359763492907651258221714407500997496797919767622829735937

ALLCELLS = {c["cid"]: c for c in PINNED + EXTENSION}
