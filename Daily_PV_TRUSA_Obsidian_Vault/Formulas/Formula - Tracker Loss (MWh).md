---
type: formula
output: "[[Tracker Loss (MWh)]]"
excel_column: BN
kind: "calculated"
variables: ["[[Tracker AVL(%)]]", "[[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]]"]
tags: [formula, availability-loss-breakdown]
---

# Tracker Loss (MWh) (formula)

Produces [[Tracker Loss (MWh)]]  |  Excel column BN  |  Group: Availability & Loss Breakdown

## Math

[[Tracker Loss (MWh)]] = ([[Tracker AVL(%)]] − 1) × [[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]]

## In plain English

Availability minus one (a negative number when availability is below 100%) times the energy baseline.

## Inputs

- [[Tracker AVL(%)]] (ratio)
- [[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]] (MWh)

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =([Tracker AVL(%)]-1)*[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]
> ```
