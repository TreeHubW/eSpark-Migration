---
type: formula
output: "[[Tracker AVL(%)]]"
excel_column: BI
kind: "site-data pull"
variables: ["[[Site Name]]", "[[Date]]"]
sources: ["[[Site Data Source Map]]"]
tags: [formula, availability-loss-breakdown]
---

# Tracker AVL(%) (formula)

Produces [[Tracker AVL(%)]]  |  Excel column BI  |  Group: Availability & Loss Breakdown

## Math

$$
A_{trk} = \text{value from the site's own data sheet on the matching Date}
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
> =IFERROR(IF([Site Name]="Oberon 1A",AVERAGEIFS(Oberon[Tracker AVL(%)],Oberon[Date],[Date]),IF([Site Name]="Rayos del Sol",AVERAGEIFS(Rayos[Tracker AVL(%)],Rayos[Date],[Date]),IF([Site Name]="Ellis",AVERAGEIFS(Ellis[Tracker AVL(%)],Ellis[Date],[Date]),IF([Site Name]="Myrtle",AVERAGEIFS(Myrtle[Tracker AVL(%)],Myrtle[Date],[Date]),IF([Site Name]="Danish",AVERAGEIFS(Danish[Tracker AVL(%)],Danish[Date],[Date]),IF([Site Name]="Skysol",AVERAGEIFS(Skysol[Tracker AVL(%)],Skysol[Date],[Date]),IF([Site Name]="Hill",AVERAGEIFS(Hill1Data!L:L,Hill1Data!A:A,[Date]),IF([Site Name]="Big Sky",AVERAGEIFS(BigSkyData!L:L,BigSkyData!B:B,[Date]),IF([Site Name]="Cottonwood",AVERAGEIFS(CottonwoodData!L:L,CottonwoodData!A:A,[Date]),IF([Site Name]="Clinton",AVERAGEIFS(ClintonData!L:L,ClintonData!B:B,[Date]),IF([Site Name]="Brazoria",AVERAGEIFS(BrazoriaData!L:L,BrazoriaData!B:B,[Date]),IF([Site Name]="Montpelier",AVERAGEIFS(MontpelierData!L:L,MontpelierData!B:B,[Date]),IF([Site Name]="Hill 2",AVERAGEIFS(Hill2Data!L:L,Hill2Data!B:B,[Date]),"!"))))))))))))),"!")
> ```
