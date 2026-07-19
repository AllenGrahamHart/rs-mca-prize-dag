# Claim contract

- **claim:** canonical official rows on the proved `B*=1,2` rate-half branches
  compile to exact ordinary and all-arity list certificates;
- **inputs:** one exact `prize-row-input-v1` object and an explicit `LIST` or
  `INTERLEAVED_LIST` selector;
- **requirements:** `compiler`, `rate_half_list_low_budget_exact_crossing`, and
  `rate_half_list_low_budget_all_arity_crossing`;
- **implementation evidence:** the canonical `descriptor` tool and its pinned
  implementation; its repository status remains TARGET under the wave-10
  artifact-semantics policy and is not a logical requirement here;
- **output:** a self-contained wrapper around the exact compiler input and
  prize-facing compiler output;
- **refusal surface:** malformed or augmented row inputs, unsupported object,
  wrong rate, `4` not dividing `n`, or `B*` outside `{1,2}`;
- **external preconditions:** primality and realization of the stated
  multiplicative subgroup remain printed public-row obligations;
- **nonclaim:** the generator does not decide `B*>=3`, MCA/CA, primality, or
  whether an arbitrary supplied code actually realizes the descriptor;
- **falsifier:** an accepted out-of-scope row, a wrong endpoint, missing
  provenance, or compiler output not equal to the theorem's adjacent pair.
