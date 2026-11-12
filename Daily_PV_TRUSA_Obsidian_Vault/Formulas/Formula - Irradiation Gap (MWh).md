---
type: formula
output: "[[Irradiation Gap (MWh)]]"
excel_column: AA
kind: "calculated"
variables: ["[[Irradiation Gap (%)]]", "[[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]]"]
tags: [formula, irradiation]
---

# Irradiation Gap [MWh] (formula)

Produces [[Irradiation Gap (MWh)]]  |  Excel column AA  |  Group: Irradiation

## Math

[[Irradiation Gap (MWh)]] = ([[Irradiation Gap (%)]] × [[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]]) ÷ (1 + [[Irradiation Gap (%)]])

## In plain English

Irradiation gap % applied to expected energy at actual irradiation, divided by (1 + gap %) to convert it back to the energy that corresponds to the expected-irradiation baseline.

## Inputs

- [[Irradiation Gap (%)]] (ratio)
- [[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]] (MWh)

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =[Irradiation Gap (%)]*[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]/(1+[Irradiation Gap (%)])
> ```
