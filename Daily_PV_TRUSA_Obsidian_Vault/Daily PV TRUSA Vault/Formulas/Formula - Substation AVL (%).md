---
type: formula
output: "[[Substation AVL (%)]]"
excel_column: BF
kind: "site-data pull"
variables: ["[[Site Name]]", "[[Date]]"]
sources: ["[[Site Data Source Map]]"]
tags: [formula, availability-loss-breakdown]
---

# Substation AVL (%) (formula)

Produces [[Substation AVL (%)]]  |  Excel column BF  |  Group: Availability & Loss Breakdown

## Math

$$
A_{sub} = \text{value from the site's own data sheet on the matching Date}
$$

## In plain English

Nested IF on Site Name, AVERAGEIFS on Date, wrapped in IFERROR. See [[Site Data Source Map]].

## Inputs

- [[Site Name]] (text)
- [[Date]] (date)

## Data sources

- [[Site Data Source Map]]

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =IFERROR(IF([Site Name]="Oberon 1A",AVERAGEIFS(Oberon[Substation AVL (%)],Oberon[Date],[Date]),IF([Site Name]="Rayos del Sol",AVERAGEIFS(Rayos[Substation AVL (%)],Rayos[Date],[Date]),IF([Site Name]="Ellis",AVERAGEIFS(Ellis[Substation AVL (%)],Ellis[Date],[Date]),IF([Site Name]="Myrtle",AVERAGEIFS(Myrtle[Substation AVL (%)],Myrtle[Date],[Date]),IF([Site Name]="Danish",AVERAGEIFS(Danish[Substation AVL (%)],Danish[Date],[Date]),IF([Site Name]="Skysol",AVERAGEIFS(Skysol[Substation AVL (%)],Skysol[Date],[Date]),IF([Site Name]="Hill",AVERAGEIFS(Hill1Data!I:I,Hill1Data!A:A,[Date]),IF([Site Name]="Big Sky",AVERAGEIFS(BigSkyData!I:I,BigSkyData!B:B,[Date]),IF([Site Name]="Cottonwood",AVERAGEIFS(CottonwoodData!I:I,CottonwoodData!A:A,[Date]),IF([Site Name]="Clinton",AVERAGEIFS(ClintonData!I:I,ClintonData!B:B,[Date]),IF([Site Name]="Brazoria",AVERAGEIFS(BrazoriaData!I:I,BrazoriaData!B:B,[Date]),IF([Site Name]="Montpelier",AVERAGEIFS(MontpelierData!I:I,MontpelierData!B:B,[Date]),IF([Site Name]="Hill 2",AVERAGEIFS(Hill2Data!I:I,Hill2Data!B:B,[Date]),"!"))))))))))))),"!")
> ```
