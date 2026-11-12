---
type: formula
output: "[[Combiner AVL (%)]]"
excel_column: BH
kind: "site-data pull"
variables: ["[[Site Name]]", "[[Date]]"]
sources: ["[[Site Data Source Map]]"]
tags: [formula, availability-loss-breakdown]
---

# Combiner AVL (%) (formula)

Produces [[Combiner AVL (%)]]  |  Excel column BH  |  Group: Availability & Loss Breakdown

## Math

[[Combiner AVL (%)]] = value from the site's own data sheet on the matching [[Date]]

## In plain English

Nested IF on Site Name, AVERAGEIFS on Date, wrapped in IFERROR. See [[Site Data Source Map]].

## Inputs

- [[Site Name]] (text)
- [[Date]] (date)

## Data sources

- [[Site Data Source Map]]

> [!abstract]- Original Excel formula (structured references shortened)
> ```excel
> =IFERROR(IF([Site Name]="Oberon 1A",AVERAGEIFS(Oberon[Combiner AVL (%)],Oberon[Date],[Date]),IF([Site Name]="Rayos del Sol",AVERAGEIFS(Rayos[Combiner AVL (%)],Rayos[Date],[Date]),IF([Site Name]="Ellis",AVERAGEIFS(Ellis[Combiner AVL (%)],Ellis[Date],[Date]),IF([Site Name]="Myrtle",AVERAGEIFS(Myrtle[Combiner AVL (%)],Myrtle[Date],[Date]),IF([Site Name]="Danish",AVERAGEIFS(Danish[Combiner AVL (%)],Danish[Date],[Date]),IF([Site Name]="Skysol",AVERAGEIFS(Skysol[Combiner AVL (%)],Skysol[Date],[Date]),IF([Site Name]="Hill",AVERAGEIFS(Hill1Data!K:K,Hill1Data!A:A,[Date]),IF([Site Name]="Big Sky",AVERAGEIFS(BigSkyData!K:K,BigSkyData!B:B,[Date]),IF([Site Name]="Cottonwood",AVERAGEIFS(CottonwoodData!K:K,CottonwoodData!A:A,[Date]),IF([Site Name]="Brazoria",AVERAGEIFS(BrazoriaData!K:K,BrazoriaData!B:B,[Date]),IF([Site Name]="Clinton",AVERAGEIFS(ClintonData!K:K,ClintonData!B:B,[Date]),IF([Site Name]="Montpelier",AVERAGEIFS(MontpelierData!K:K,MontpelierData!B:B,[Date]),IF([Site Name]="Hill 2",AVERAGEIFS(Hill2Data!K:K,Hill2Data!B:B,[Date]),"!"))))))))))))),"!")
> ```
