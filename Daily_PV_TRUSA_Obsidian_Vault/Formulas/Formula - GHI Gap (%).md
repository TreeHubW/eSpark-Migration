---
type: formula
output: "[[GHI Gap (%)]]"
excel_column: AE
kind: "calculated"
variables: ["[[Actual Irradiation GHI (kWh-m2)]]", "[[Model Irradiation GHI (kWh-m2)]]"]
tags: [formula, irradiation]
---

# GHI Gap (%) (formula)

Produces [[GHI Gap (%)]]  |  Excel column AE  |  Group: Irradiation

## Math

[[GHI Gap (%)]] =

- 0, if [[Actual Irradiation GHI (kWh-m2)]] = 0
- ([[Actual Irradiation GHI (kWh-m2)]] − [[Model Irradiation GHI (kWh-m2)]]) ÷ [[Model Irradiation GHI (kWh-m2)]], otherwise

## In plain English

Actual vs modelled GHI, with the same zero guard as the POA gap.

## Inputs

- [[Actual Irradiation GHI (kWh-m2)]] (kWh/m2 per day)
- [[Model Irradiation GHI (kWh-m2)]] (kWh/m2 per day)

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =IF([Actual Irradiation GHI [kWh/m2]]=0,[Actual Irradiation GHI [kWh/m2]],(([Actual Irradiation GHI [kWh/m2]]-[Model Irradiation GHI [kWh/m2]])/[Model Irradiation GHI [kWh/m2]]))
> ```
