# proof: m720_official_norm_gate_case_manifest_soundness

Let `C` be the set of official-shape primitive `h=7..20` norm-gate cases.

The manifest covers `C`, so every primitive case appears exactly once or in a
declared disjoint case class with accounted multiplicity. Each case is
discharged in one of the accepted ways.

If the entry cites a uniform nonvanishing theorem, then that theorem excludes
the primitive norm-gate obstruction for the covered case or case class.

If the entry is a certificate record, the record has `complete=true` and zero
unpaid non-toral survivors. Thus it is a complete zero certificate for the
case under the payload schema.

Since every official primitive case is covered by one accepted discharge, the
manifest supplies either a uniform theorem or complete zero certificate
payload covering every official-shape primitive norm-gate case. That is
exactly `m720_official_h7_20_norm_gate_payload`.
