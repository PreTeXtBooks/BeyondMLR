# Missing / Divergent Content Report: RMD → PTX Conversion
## Chapters 10, 11, and Backmatter

_Prepared by comparison of R Markdown source files against PreTeXt conversion files._

---

## PAIR 1: Chapter 10 (Three-Level Multilevel Models)

**Files compared:**
- Source: `10-Multilevel-Data-With-More-Than-Two-Levels.Rmd` (1724 lines)
- Target: `pretext/source/ch_3level.ptx` (1360 lines)

---

### 1. Citations — Systematically Removed (Global)

All inline `@citation` keys are removed throughout the PTX chapter. This is a universal pattern
affecting all `@Baer2002`, `@Camill2004`, `@Knops2000`, `@Allison2005`, `@Zak2003`,
`@Angell2010`, `@Sampson1997`, `@Eisinger2011`, `@Bickel2007`, `@Pray2009`, and any other
references cited in the RMD. No reference links or cross-references to the backmatter are
substituted; the text simply has the citation removed.

---

### 2. Missing Prose Paragraphs / Text

**2a. Microbial communities ecological sentence** (RMD line 47):
> "It is important to note that microbial communities in prairie soils have been implicated with
> plant diversity and overall ecosystem function by controlling carbon and nitrogen cycling in
> the soils [@Zak2003]."

Absent from PTX introduction.

**2b. Prairie reconstruction variability paragraph** (RMD line 49):
The full second paragraph about "all of the aforementioned changes associated with cultivation
practices" and prairies reconstructed in different years yielding "disparate prairie communities"
is significantly condensed in PTX (merged into the second paragraph with much less detail).

**2c. Biological species description paragraph** (RMD line 222):
> "Coneflowers are members of the aster family, growing up to 4 feet tall with their distinctive
> gray seed heads and drooping yellow petals. Leadplants, on the other hand, are members of the
> bean family...Leadplants have deep root systems and are symbiotic N-fixers, which means they
> might experience stifled growth in sterilized soil compared with other species."

This entire paragraph is **MISSING** from the PTX.

**2d. Variability analysis paragraph** (RMD line 357):
> "Another way to examine variability due to plant vs. variability due to pot is through summary
> statistics. Plant-to-plant variability can be estimated by averaging standard deviations from
> each pot (.489 for intercepts and .039 for slopes)..."

**MISSING** from PTX.

**2e. Model B numerical interpretation** (RMD line 633):
> "We see that, on average, leadplants have a height of 1.54 mm 13 days after planting...
> producing an average height at the end of the study (Day 28) of 3.22 mm."

**MISSING** from PTX.

**2f. Boundary constraints conceptual walkthrough** (RMD lines 701, 745–755):
Two paragraphs explaining boundary constraints through a simple two-parameter illustration:
> "Consider a model in which we have two parameters..."
> "Graphically, in this simple illustration, the effect of the boundary constraint is to alter
> the likelihood function from a nice hill..."

Both paragraphs are **MISSING** from PTX. The PTX jumps directly to the "what should you do"
bulleted list without these conceptual foundations.

**2g. Three-way interaction colorful note** (RMD line 1187):
> "This means we may have a **three-way interaction** in our final composite model between
> sterilization, remnant prairies, and time. Three-way interactions show that the size of an
> interaction between two predictors differs depending on the level of a third predictor. Whew!"

**MISSING** from PTX.

**2h. Model E complete discussion** (RMD lines 1321–1343):
The full discussion of Model E (an attempt to simplify Model F), including its R code and
likelihood ratio test comparison with Model F, is **MISSING** from PTX. The PTX goes directly
from Model D to Model F in the model-building progression.

**2i. Parametric bootstrap detailed numerical walkthrough** (RMD lines 858–908):
The detailed worked example showing how bootstrapped data is generated for Plants 11 and 12
(with Level Three / Level Two / Level One headings, specific numeric values such as
$\tilde{u}_1 = -.192$) is **SIGNIFICANTLY CONDENSED** in PTX. PTX has only a brief summary
paragraph, not the full worked numerical example.

**2j. Bootstrapped chi-square test output explanation** (RMD lines 985–987):
> "A likelihood ratio test statistic is calculated comparing Model C.1 to Model C. For example,
> after continuing...Model C does have a larger loglikelihood than Model C.1 (−280.54 vs.
> −281.24)..."

**MISSING** from PTX.

**2k. Confidence interval results discussion** (RMD line 1020):
> "From the output below, the 95% bootstrapped confidence interval for $\rho_{\tilde{u}\tilde{v}}$
> (−1, 1) contains 0, and the interval for $\sigma_{\tilde{v}}$ (.00050, .0253) nearly contains 0..."

Present in PTX in altered form, but the `confint()` R code block is different.

**2l. Full Model C_plus write-out** (RMD lines 1036–1096):
The complete level-by-level equations for Model C_plus, including the full 4×4 covariance matrix
at Level Three, are **SIGNIFICANTLY CONDENSED** in PTX.

**2m. Exploding variance components detailed explanation** (RMD lines 1096–1140):
The vivid passage including "even in the absolute simplest case, with only two options for each
parameter, there would be over one billion possible combinations to consider!" and the full
9-parameter simplified random intercepts model discussion are **CONDENSED** in PTX.

---

### 3. Missing Covariance Structure Content (Section 10.7)

**3a.** 4×4 within-plant covariance matrix $\text{Cov}(\mathbf{Y}_{ij})$ (RMD lines 1420–1428)
— **MISSING** from PTX.

**3b.** 4×4 between-plant covariance matrix $\text{Cov}(\mathbf{Y}_{ij}, \mathbf{Y}_{ij'})$
(RMD lines 1430–1440) — **MISSING** from PTX.

**3c.** Discussion that $\tau_k^2$ and $\tau_{kk'}$ are independent of $i$ and $j$
(RMD line 1428) — **MISSING** from PTX.

**3d.** Constrained correlation matrices after Model F constraints
($\sigma_{\tilde{v}}^2 = \sigma_{\tilde{u}\tilde{v}} = 0$): both within-plant and between-plant
matrices (RMD lines 1466–1482) — **MISSING** from PTX.

**3e.** Standard deviation by timepoint discussion (RMD line 1462):
> "Examination of standard deviation terms by timepoint suggests that variability increases over
> time within a plant (estimated SDs of .652, .703, .828, and .999 for Days 13, 18, 23, and 28,
> respectively)."
— **MISSING** from PTX.

**3f.** 24×24 block diagonal complete covariance matrix (RMD lines 1515–1533) — **MISSING**.

**3g.** Correlation matrix conversion formula (RMD line 1535):
$\text{Corr}(Y_{ijk}, Y_{ij'k}) = \tilde{\tau}_{kk}/\tau_k^2$ — **MISSING** from PTX.

**3h.** Alternative covariance structures comparison text (RMD line 1537):
> "We fit both structures, along with the toeplitz structure, and compared the resulting models...
> AIC and BIC from the standard model (615.2 and 651.4, respectively) are considerably lower..."
— **CONDENSED** in PTX.

---

### 4. Missing Tables

| RMD table ID      | Caption                                                        | Status in PTX           |
|-------------------|----------------------------------------------------------------|-------------------------|
| `table1chp10`     | "A snapshot of data (Plants 231–246) in wide format"           | **MISSING**             |
| `table2chp10`     | "A snapshot of data (Plants 236–242) in long format"           | **MISSING**             |
| `table10verb7`    | "Original data for Plants 11 and 12 from Pot 1"               | **MISSING**             |
| `table4chp10`     | "Correlates of collective efficacy from Table 3 of Sampson et al." (exercise table) | **MISSING** |
| `table5chp10`     | "Neighborhood correlates of perceived neighborhood violence from Table 4 of Sampson et al." | **MISSING** |

Exercises 17 and 22 reference the Sampson tables, but the tables themselves are not embedded in
the PTX exercise section.

---

### 5. Missing R Code Blocks

- **`confint(modelcl, method="boot", oldNames = F)`** (RMD line 1027) — **MISSING** from PTX.
- **Single bootstrap sample demonstration** (RMD lines 965–983):
  `set.seed(3333); d <- drop(simulate(modelcl0.ml))...` — **MISSING** from PTX.
- Multiple `echo=FALSE` display-only blocks that show formatted output (VarCorr, coef summary,
  etc.) are consolidated or omitted in PTX; PTX shows only the fitting code, not the separate
  display output blocks.

---

### 6. Equations

- **Bivariate normal distributions for error terms** with full matrices (RMD lines 579–599 and
  1073–1095, for unconditional growth and Model C_plus) — **ABSENT** from the PTX equivalents.
- **Composite model for Model B** (RMD line 574): The RMD has a typo `+{v}_{ij}` which PTX
  correctly renders as `+u_{ij}`.

---

### 7. Exercise Issues (Ch10)

All 22 Conceptual, 2 Guided, and 2 Open-Ended exercises are present in PTX. However:
- Exercises 17 and 22 (referring to Sampson Tables 3 and 4) are rendered without the referenced
  tables being embedded (see §4 above).
- Guided Exercise 2, part (e) optional sub-bullets (5 predicted cases, 2 scatterplots) are
  **MISSING** from the PTX version.

---

---

## PAIR 2: Chapter 11 (Generalized Linear Multilevel Models)

**Files compared:**
- Source: `11-Generalized-Linear-Multilevel-Models.Rmd` (1349 lines)
- Target: `pretext/source/ch_glmm.ptx` (1243 lines)

---

### 1. Citations — Systematically Removed (Global)

Same universal pattern as Ch10: all `@citation` keys removed throughout the PTX. Affected
citations include `@Moskowitz2011`, `@Anderson2009`, `@Noecker2012`, `@Randall2014`,
`@Trinh2018`, `@Mohr2018`, `@Jenkins2006`, `@Fast2011`, and others.

---

### 2. Missing Prose Paragraphs / Text

**2a. Case study intro — Book title and specific details removed** (RMD lines 1–30, before line 100):
The PTX case study introduction omits:
- The specific title *Scorecasting* by Moskowitz and Wertheim
- The phrase "controlling for score differential, conference, and whether or not the home team had the lead"
- The explanation of foul type classification (personal, shooting, offensive)

These details are condensed in PTX.

**2b. Anderson & Pierce methodological justification** (RMD line 455):
> "Anderson and Pierce ran such a model in their 2009 paper, using the results of their multiple
> logistic regression model to support their primary conclusions, while justifying their approach
> by confirming a low level of correlation within games and the minimal impact on fixed effect
> estimates that accounting for clustering would have."

**MISSING** from PTX. The PTX simply says "one potential multiple logistic regression model."

**2c. Home-team variability paragraph and Figure gmu-histmat3** (RMD lines 686–705):
After fitting regression models by home team, the RMD reports detailed summary statistics
(mean=−0.15, SD=0.33 for intercepts; mean=−0.22, SD=0.12 for slopes) and references
Figure gmu-histmat3 (histograms of intercepts and slopes by home team). **Both the detailed
statistics and Figure gmu-histmat3 are MISSING from PTX.** The PTX mentions variability "much
less than game-to-game" but omits the numbers and the figure.

**2d. Dose response — 2004–2005 comparison** (RMD line 1091):
> "Analyses of data from 2004–2005 [@Noecker2012] showed that the tendency to even out foul
> calls was stronger when one team had a large lead, but we found no evidence of a foul
> differential by score differential interaction in the 2009–2010 data, although home team fouls
> are more likely when the home team has a large lead, regardless of the foul differential."

**MISSING** from PTX. The PTX moves directly to the parameter interpretation bullet list.

---

### 3. Missing Tables

| RMD table ID    | Caption                                                                        | Status in PTX                  |
|-----------------|--------------------------------------------------------------------------------|--------------------------------|
| `table3chp11`   | "Key variables from the March 3, 2010, game (Virginia at Boston College, Game 110)" | **MISSING** from PTX — section references it but table not shown |
| `table4chp11`   | "Adjusted rate ratios for individual-level variables from Randall et al. (2014) Table 2" | **MISSING** — exercises 20–24 reference it without embedding |
| `table5chp11`   | "Adjusted rate ratios for area-level variables from Randall et al. (2014) Table 3" | **MISSING** — exercises 25–26 reference it without embedding |

**Note on tables 4 & 5:** Unlike Ch10, Ch11 exercises 19–28 do reference "the Randall et al.
(2014) Table 2" and "Table 3" by name, expecting students to look them up. This differs from the
RMD approach of embedding the tables inline for self-contained exercises.

---

### 4. Missing Figures

- **Figure gmu-histmat3** ("Histograms of intercepts and slopes from fitting logistic regression
  models by home team") — **MISSING** from PTX (as noted above in §2c).

---

### 5. Missing R Code Blocks

- The `bootstrapAnova()` function definition (RMD lines 833–848) is intentionally not displayed
  in PTX (appropriate, since it is `echo=FALSE` in RMD too).
- Multiple `echo=FALSE` output-display blocks (for VarCorr, coef summaries) are consolidated
  or omitted, consistent with the Ch10 pattern.

---

### 6. Exercise Coverage (Ch11)

All 28 Conceptual exercises and 4 Open-Ended exercises are present in PTX. The exercise text
is essentially complete and faithful. The main issue is the missing embedded tables referenced
by exercises 20–28 (Randall et al. 2014, Tables 2 and 3 — see §3 above).

---

---

## PAIR 3: Backmatter / References

**Files compared:**
- Source: `99-References.Rmd` (0 lines — auto-generated by bookdown from `.bib` files)
- Target: `pretext/source/meta_backmatter.ptx` (563 lines)

---

### Overview

The RMD reference list was fully auto-generated from bibliography `.bib` files at build time;
the `99-References.Rmd` file itself is empty. The PTX manually encodes references as
`<biblio type="raw">` entries in `meta_backmatter.ptx`. A direct 1:1 comparison of `.bib`
vs. PTX entries is not performed here, but all citations verified from Chapters 10 and 11 are
present in the PTX backmatter.

---

### Cross-Verification: Citations Used in Ch10 and Ch11

All citations from Chapters 10 and 11 were spot-checked and **confirmed present** in
`meta_backmatter.ptx`:

| Citation key      | Title / Author                                       | Status |
|-------------------|------------------------------------------------------|--------|
| `Baer2002`        | Baer et al. — Changes in Ecosystem Structure         | ✓      |
| `Camill2004`      | Camill et al. — Community- and Ecosystem-level Changes | ✓    |
| `Knops2000`       | Knops & Tilman — Dynamics of Soil Nitrogen           | ✓      |
| `Allison2005`     | Allison et al. — Effects of Climate Change           | ✓      |
| `Zak2003`         | Zak et al. — Plant Diversity, Soil Microbial Communities | ✓  |
| `Angell2010`      | Angell — Effects of Soil Type and Sterilization      | ✓      |
| `Sampson1997`     | Sampson et al. — Neighborhoods and Violent Crime     | ✓      |
| `Eisinger2011`    | Eisinger et al. — Tree Growth Rates and Mortality    | ✓      |
| `Bickel2007`      | Bickel — Multilevel Analysis for Applied Research    | ✓      |
| `Pray2009`        | Pray — Effects of Rainfall and Sun Exposure          | ✓      |
| `Randall2014`     | Randall et al. — Acute Myocardial Infarction (Aboriginal Australians) | ✓ |
| `Noecker2012`     | Noecker & Roback — NCAA Basketball Officials         | ✓      |
| `Moskowitz2011`   | Moskowitz & Wertheim — *Scorecasting*                | ✓      |
| `Anderson2009`    | Anderson & Pierce — Officiating Bias in NCAA Basketball | ✓   |
| `Trinh2018`       | Trinh & Ameri — Airbnb Price Determinants            | ✓      |
| `Mohr2018`        | Janusz & Mohr — Yelp Star Ratings                    | ✓      |
| `Jenkins2006`     | Jenkins — Book Challenges and Young Readers          | ✓      |
| `Fast2011`        | Fast & Hegland — Book Challenges: A Statistical Examination | ✓ |

---

### PTX Backmatter Structure

The PTX backmatter contains two elements:
1. `<references>` — manual bibliography (all entries confirmed above)
2. `<index>` with `<index-list/>` — auto-generated from `<idx>` tags throughout the PTX source

This structure is appropriate for PreTeXt output. The RMD had only an auto-generated reference
list; there was no index in the bookdown version.

---

### Potential Gap: Full `.bib` Coverage

Since the `.bib` source files were not enumerated, it is possible that some references cited in
Chapters 1–9 are present in the `.bib` files but absent from `meta_backmatter.ptx`. This report
covers only the citations verified for Chapters 10, 11, and their exercises. A complete audit
would require comparing all `@key` citations across all 12 RMD chapters against all `xml:id`
entries in the PTX backmatter.

---

---

## Summary Table of Missing Content by Type

| Category                           | Ch10  | Ch11  | Backmatter |
|------------------------------------|-------|-------|------------|
| Citations removed (systematic)     | All   | All   | N/A (backmatter has full refs) |
| Prose paragraphs missing           | 13    | 4     | N/A        |
| Tables missing                     | 5     | 3     | N/A        |
| Figures missing                    | 0     | 1     | N/A        |
| R code blocks missing              | 3+    | 1+    | N/A        |
| Equations / covariance matrices    | 8     | 0     | N/A        |
| Exercise content issues            | 3     | 2     | N/A        |
| Index                              | —     | —     | Added (new in PTX) |

