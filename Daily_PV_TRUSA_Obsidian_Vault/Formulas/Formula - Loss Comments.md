---
type: formula
output: "[[Loss Comments]]"
excel_column: BP
kind: "calculated"
variables: ["[[Actual Irradiation GHI (kWh-m2)]]", "[[Actual Irradiation GPOA (kWh-m2)]]"]
tags: [formula, comments-qa]
---

# Loss Comments (formula)

Produces [[Loss Comments]]  |  Excel column BP  |  Group: Comments & QA

## Math

[[Loss Comments]] = [[Actual Irradiation GHI (kWh-m2)]] ÷ [[Actual Irradiation GPOA (kWh-m2)]]

## In plain English

Actual GHI divided by actual POA.

## Inputs

- [[Actual Irradiation GHI (kWh-m2)]] (kWh/m2 per day)
- [[Actual Irradiation GPOA (kWh-m2)]] (kWh/m2 per day)

> [!warning] The column header says 'Loss Comments' but the formula computes a GHI/POA ratio, so the header and content do not match. See [[Audit Notes]].

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =[Actual Irradiation GHI [kWh/m2]]/[Actual Irradiation GPOA [kWh/m2]]
> ```
