---
type: formula
output: "[[Actual Grid Availability]]"
excel_column: AP
kind: "calculated"
variables: ["[[Grid Availability Loss (MWh)]]", "[[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]]"]
tags: [formula, grid-availability]
---

# Actual Grid Availability (formula)

Produces [[Actual Grid Availability]]  |  Excel column AP  |  Group: Grid Availability

## Math

[[Actual Grid Availability]] = 1 + [[Grid Availability Loss (MWh)]] ÷ [[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]]

## In plain English

One plus grid loss divided by expected energy. Because the loss is stored as a negative number, availability falls below 1 as losses grow.

## Inputs

- [[Grid Availability Loss (MWh)]] (MWh)
- [[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]] (MWh)

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =1+([Grid Availability Loss [MWh]]/[Expected Energy - Actual POA & 100% PEA,GEA (MWh)])
> ```
