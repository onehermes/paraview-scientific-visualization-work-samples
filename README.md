# Scientific Visualization & ParaView Work Samples

<p align="center">
  <img src="assets/hero.svg" alt="Scientific Visualization and ParaView Work Samples banner" width="100%" />
</p>

This repository is a self-directed, public work-sample portfolio built to demonstrate practical understanding of ParaView workflows, scientific visualization documentation, and quality review of AI-generated technical instructions.

> Honest scope: these are not client deliverables, lab reports, or production simulation studies.
> They are intentionally synthetic examples created to show workflow reasoning, reproducibility habits, and visual communication skill.

## Portfolio Pillars

<table>
<tr>
<td width="33%" valign="top">
<strong>Workflow documentation</strong><br><br>
Step-by-step ParaView procedures that can be repeated, checked, and compared.
</td>
<td width="33%" valign="top">
<strong>Scalar and vector reasoning</strong><br><br>
Inspection of structured datasets, contour and slice choices, glyphs, stream tracers, and color mapping.
</td>
<td width="33%" valign="top">
<strong>AI output review</strong><br><br>
Evaluation of generated ParaView guidance for missing arrays, unclear sequence, and unsupported claims.
</td>
</tr>
</table>

## Core Concepts Referenced

- ParaView
- VTK-style datasets
- Scientific visualization pipelines
- Scalar fields
- Vector fields
- Contour, Slice, Clip, Glyph, Stream Tracer, and Calculator filters
- Color maps
- Screenshot and export workflows
- AI-generated ParaView instruction evaluation

## Skills Demonstrated

- Scientific visualization workflow documentation
- Dataset inspection
- Filter and pipeline reasoning
- Scalar and vector field interpretation
- Reproducible technical documentation
- Quality review of AI-generated visualization instructions
- Attention to assumptions, edge cases, and scope limits

## Featured Previews

<table>
<tr>
<td width="33%" valign="top">
<a href="projects/01-volume-contour-visualization/README.md"><img src="assets/previews/scalar-preview.svg" alt="Scalar field preview" width="100%" /></a><br>
<strong>Volume & Contour</strong><br>
Slice, contour, color mapping, and export discipline.
</td>
<td width="33%" valign="top">
<a href="projects/02-vector-field-flow-visualization/README.md"><img src="assets/previews/vector-preview.svg" alt="Vector field preview" width="100%" /></a><br>
<strong>Vector Field & Flow</strong><br>
Glyphs, magnitude scaling, and streamline reasoning.
</td>
<td width="33%" valign="top">
<a href="projects/03-paraview-ai-output-quality-review/README.md"><img src="assets/previews/review-preview.svg" alt="AI review preview" width="100%" /></a><br>
<strong>AI Output Review</strong><br>
Find defects, rewrite clearly, and document limitations.
</td>
</tr>
</table>

## Project Map

| Project | Focus | Key Files |
| --- | --- | --- |
| [01. Volume & Contour Visualization](projects/01-volume-contour-visualization/README.md) | Scalar field slicing, contouring, and export discipline | [workflow](projects/01-volume-contour-visualization/workflow.md), [pipeline notes](projects/01-volume-contour-visualization/pipeline-notes.md), [expected outputs](projects/01-volume-contour-visualization/expected-outputs.md), [quality checklist](projects/01-volume-contour-visualization/quality-checklist.md) |
| [02. Vector Field & Flow Visualization](projects/02-vector-field-flow-visualization/README.md) | Glyphs, flow interpretation, and vector-field review | [workflow](projects/02-vector-field-flow-visualization/workflow.md), [vector field notes](projects/02-vector-field-flow-visualization/vector-field-notes.md), [expected outputs](projects/02-vector-field-flow-visualization/expected-outputs.md), [quality checklist](projects/02-vector-field-flow-visualization/quality-checklist.md) |
| [03. ParaView AI Output Quality Review](projects/03-paraview-ai-output-quality-review/README.md) | Evaluating a flawed AI-generated ParaView answer and rewriting it clearly | [fake answer](projects/03-paraview-ai-output-quality-review/fake-ai-generated-answer.md), [review findings](projects/03-paraview-ai-output-quality-review/review-findings.md), [improved answer](projects/03-paraview-ai-output-quality-review/improved-answer.md), [evaluation checklist](projects/03-paraview-ai-output-quality-review/evaluation-checklist.md) |

## Why This Matters For AI Research And Digital Asset Evaluation

Scientific visualization instructions are easy to make sound convincing while still missing the details that matter: dataset format, array selection, filter sequence, reproducibility, and limitations. This portfolio demonstrates how I review technical content for those failure modes and rewrite it into a workflow that is testable, honest, and reusable.

That same discipline is useful when evaluating AI-generated technical content or digital assets:

- verify the data model before trusting the explanation
- check whether the pipeline can be reproduced from the instructions alone
- separate visual appearance from scientific meaning
- record what the visualization supports and what it does not
- avoid overstated conclusions that the dataset cannot justify

## Repository Link

- GitHub: https://github.com/onehermes

## Repository Layout

```text
paraview-scientific-visualization-work-samples/
  assets/
    hero.svg
    previews/
  README.md
  projects/
  scripts/
  docs/
  LICENSE
  .gitignore
```
