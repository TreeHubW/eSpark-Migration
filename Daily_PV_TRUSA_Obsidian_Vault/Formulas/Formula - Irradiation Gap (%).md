---
type: formula
output: "[[Irradiation Gap (%)]]"
excel_column: AB
kind: "calculated"
variables: ["[[Actual Irradiation GPOA (kWh-m2)]]", "[[Expected Irradiation P50 POA (kWh-m2)]]"]
tags: [formula, irradiation]
---

# Irradiation Gap (%) (formula)

Produces [[Irradiation Gap (%)]]  |  Excel column AB  |  Group: Irradiation

## Math

[[Irradiation Gap (%)]] =

- 0, if [[Actual Irradiation GPOA (kWh-m2)]] = 0
- ([[Actual Irradiation GPOA (kWh-m2)]] − [[Expected Irradiation P50 POA (kWh-m2)]]) ÷ [[Expected Irradiation P50 POA (kWh-m2)]], otherwise

## In plain English

Actual vs expected POA irradiation. If actual irradiation is zero it returns zero (no gap), unlike Production Gap % which returns -1.

## Inputs

- [[Actual Irradiation GPOA (kWh-m2)]] (kWh/m2 per day)
- [[Expected Irradiation P50 POA (kWh-m2)]] (kWh/m2 per day)

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =IF([Actual Irradiation GPOA [kWh/m2]]=0,[Actual Irradiation GPOA [kWh/m2]],(([Actual Irradiation GPOA [kWh/m2]]-[Expected Irradiation P50 POA [kWh/m2]])/[Expected Irradiation P50 POA [kWh/m2]]))
> ```
