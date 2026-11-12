---
type: formula
output: "[[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]]"
excel_column: AV
kind: "calculated"
variables: ["[[Actual MWp]]", "[[Actual Irradiation GPOA (kWh-m2)]]", "[[Expected Performance Ratio (PR)]]", "[[Other external losses]]"]
tags: [formula, expected-energy-performance-ratio]
---

# Expected Energy - Actual POA & 100% PEA,GEA (MWh) (formula)

Produces [[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]]  |  Excel column AV  |  Group: Expected Energy & Performance Ratio

## Math

[[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]] = [[Actual MWp]] × [[Actual Irradiation GPOA (kWh-m2)]] × ([[Expected Performance Ratio (PR)]] − [[Other external losses]])

## In plain English

Actual MWp times measured POA irradiation times (expected PR minus other external losses). MWp times kWh/m2 per day gives MWh.

## Inputs

- [[Actual MWp]] (MWp)
- [[Actual Irradiation GPOA (kWh-m2)]] (kWh/m2 per day)
- [[Expected Performance Ratio (PR)]] (ratio)
- [[Other external losses]] (ratio)

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =[Actual MWp]*[Actual Irradiation GPOA [kWh/m2]]*([Expected Performance Ratio (PR)]-[Other external losses])
> ```
