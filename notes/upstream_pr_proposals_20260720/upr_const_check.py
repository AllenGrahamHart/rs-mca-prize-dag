# Cheap exact crosswalk constant checks (no giant binomials)
n = 2**21
# KoalaBear sextic
pk = 2**31 - 2**24 + 1
qk = pk**6
Bk = qk >> 128            # floor(q/2^128), eps*=2^-128
# Mersenne-31 quartic (circle)
pm = 2**31 - 1
qm = pm**4
Bm = qm >> 100            # floor(q/2^100), eps*=2^-100
print("KoalaBear p        =", pk)
print("KoalaBear q=p^6    =", qk, " log2 ~", qk.bit_length()-1)
print("KoalaBear B_*      =", Bk, "  (paving node prints 274980728111395087:", Bk==274980728111395087, ")")
print("Mersenne  q=p^4    =", qm, " log2 ~", qm.bit_length()-1)
print("Mersenne  B_*      =", Bm, "  (Danny #993 prints 16777215:", Bm==16777215, ")")
# a0 radius crosscheck vs his 0.1 table 981105/2097152
a0_kb_mca = 1116047
print("KB MCA radius n-a0 =", n-a0_kb_mca, " (his 0.1 numerator 981105:", n-a0_kb_mca==981105, ")")
print("KB MCA delta       = 981105/2097152 =", 981105/2097152)
# adjacency spacing of his four a0
print("a0s:", 1116047,1116046,1116023,1116022, " KB-M31 gap =", 1116047-1116023)
