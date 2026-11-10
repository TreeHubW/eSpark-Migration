---
type: formula
output: "[[Month]]"
excel_column: F
kind: "calculated"
variables: ["[[Date]]"]
tags: [formula, identity-calendar]
---

# Month (formula)

Produces [[Month]]  |  Excel column F  |  Group: Identity & Calendar

## In plain English

Month number of Date, formatted with a leading zero.

## Inputs

- [[Date]] (date)

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =TEXT(MONTH([Date]),"00")
> ```
