---
type: formula
output: "[[Plant Performance (PR) gap %]]"
excel_column: BA
kind: "calculated"
variables: ["[[Plant Performance (PR) Act]]", "[[Expected Performance Ratio (PR)]]"]
tags: [formula, expected-energy-performance-ratio]
---

# Plant Performance (PR) gap % (formula)

Produces [[Plant Performance (PR) gap %]]  |  Excel column BA  |  Group: Expected Energy & Performance Ratio

## Math

[[Plant Performance (PR) gap %]] = ([[Plant Performance (PR) Act]] − [[Expected Performance Ratio (PR)]]) ÷ [[Expected Performance Ratio (PR)]]

## In plain English

(Actual PR - expected PR) / expected PR (0 if anything errors).

## Inputs

- [[Plant Performance (PR) Act]] (ratio)
- [[Expected Performance Ratio (PR)]] (ratio)

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =IFERROR(([Plant Performance (PR) Act]-[Expected Performance Ratio (PR)])/[Expected Performance Ratio (PR)],0)
> ```
