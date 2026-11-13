---
type: formula
output: "[[Availability BU Gap (MWh)]]"
excel_column: AM
kind: "calculated"
variables: ["[[Actual Plant Availability]]", "[[Expected Plant Availability]]", "[[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]]", "[[Availability BU Gap (%)]]"]
tags: [formula, plant-availability]
---

# Availability BU Gap [MWh] (formula)

Produces [[Availability BU Gap (MWh)]]  |  Excel column AM  |  Group: Plant Availability

## Math

[[Availability BU Gap (MWh)]] =

- −[[Expected Plant Availability]] × [[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]], if [[Actual Plant Availability]] = 0
- [[Availability BU Gap (%)]] × [[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]], otherwise

## In plain English

Availability gap % times the energy potential. If actual availability is zero it instead books the full expected availability as lost energy.

## Inputs

- [[Actual Plant Availability]] (ratio)
- [[Expected Plant Availability]] (ratio)
- [[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]] (MWh)
- [[Availability BU Gap (%)]] (ratio)

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =IF([Actual Plant Availability]=0,-[Expected Plant Availability]*[Expected Energy - Actual POA & 100% PEA,GEA (MWh)],[Availability BU Gap (%)]*[Expected Energy - Actual POA & 100% PEA,GEA (MWh)])
> ```
