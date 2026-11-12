---
type: formula
output: "[[DC Loss (MWh)]]"
excel_column: BM
kind: "calculated"
variables: ["[[Combiner AVL (%)]]", "[[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]]"]
tags: [formula, availability-loss-breakdown]
---

# DC Loss (MWh) (formula)

Produces [[DC Loss (MWh)]]  |  Excel column BM  |  Group: Availability & Loss Breakdown

## Math

[[DC Loss (MWh)]] = ([[Combiner AVL (%)]] − 1) × [[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]]

## In plain English

Availability minus one (a negative number when availability is below 100%) times the energy baseline.

## Inputs

- [[Combiner AVL (%)]] (ratio)
- [[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]] (MWh)

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =([Combiner AVL (%)]-1)*[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]
> ```
