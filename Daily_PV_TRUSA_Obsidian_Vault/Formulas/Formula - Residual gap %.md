---
type: formula
output: "[[Residual gap %]]"
excel_column: BC
kind: "calculated"
variables: ["[[Residual BU Gap (MWh)]]", "[[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]]"]
tags: [formula, residual-gap]
---

# Residual gap % (formula)

Produces [[Residual gap %]]  |  Excel column BC  |  Group: Residual Gap

## Math

[[Residual gap %]] = [[Residual BU Gap (MWh)]] ÷ [[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]]

## In plain English

Residual gap divided by expected energy at actual irradiation.

## Inputs

- [[Residual BU Gap (MWh)]] (MWh)
- [[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]] (MWh)

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =[Residual BU Gap [MWh]]/[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]
> ```
