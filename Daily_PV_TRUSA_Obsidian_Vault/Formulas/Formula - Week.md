---
type: formula
output: "[[Week]]"
excel_column: G
kind: "calculated"
variables: ["[[Date]]"]
tags: [formula, identity-calendar]
---

# Week (formula)

Produces [[Week]]  |  Excel column G  |  Group: Identity & Calendar

## In plain English

WEEKNUM(Date, 2): week number with Monday as the first day of the week.

## Inputs

- [[Date]] (date)

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =TEXT(WEEKNUM([Date],2),"00")
> ```
