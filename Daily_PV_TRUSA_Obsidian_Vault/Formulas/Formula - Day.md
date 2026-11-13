---
type: formula
output: "[[Day]]"
excel_column: E
kind: "calculated"
variables: ["[[Date]]"]
tags: [formula, identity-calendar]
---

# Day (formula)

Produces [[Day]]  |  Excel column E  |  Group: Identity & Calendar

## In plain English

Day-of-month of Date, formatted with a leading zero (note: this is not the weekday name).

## Inputs

- [[Date]] (date)

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =TEXT(DAY([Date]),"00")
> ```
