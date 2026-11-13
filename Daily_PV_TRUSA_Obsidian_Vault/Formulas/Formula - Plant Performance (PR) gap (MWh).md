---
type: formula
output: "[[Plant Performance (PR) gap (MWh)]]"
excel_column: AZ
kind: "calculated"
variables: ["[[Plant Performance (PR) gap %]]", "[[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]]"]
tags: [formula, expected-energy-performance-ratio]
---

# Plant Performance (PR) gap [MWh] (formula)

Produces [[Plant Performance (PR) gap (MWh)]]  |  Excel column AZ  |  Group: Expected Energy & Performance Ratio

## Math

[[Plant Performance (PR) gap (MWh)]] = [[Plant Performance (PR) gap %]] × [[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]]

## In plain English

PR gap % times the energy potential (0 if anything errors).

## Inputs

- [[Plant Performance (PR) gap %]] (ratio)
- [[Expected Energy - Actual POA & 100% PEA,GEA (MWh)]] (MWh)

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =IFERROR([Plant Performance (PR) gap %]*[Expected Energy - Actual POA & 100% PEA,GEA (MWh)],0)
> ```
