# Review Findings

| Issue | Why It Matters | Recommended Fix |
| --- | --- | --- |
| Unclear dataset format | The answer does not say whether the input is VTK, CSV, or something else | Name the file type and how it is loaded |
| Missing array selection | The answer does not identify which scalar or vector array should be used | Explicitly state the active array |
| Wrong or unclear filter sequence | The response suggests filters without explaining the order | Describe the filter chain step by step |
| No pipeline reproducibility | A reader cannot recreate the workflow from the answer alone | Include file names, filter order, and key settings |
| No screenshot/export guidance | The answer does not explain how to produce a shareable artifact | Add export instructions and any relevant image settings |
| No color-map explanation | "Make it look scientific" is not a technical rule | Explain the color map and why it fits the field |
| Overclaiming scientific meaning | Visual appeal is mistaken for scientific proof | Limit claims to what the dataset can actually support |
| Missing limitations | The answer does not say what the visualization cannot establish | Add a limitations section |

## Bottom Line

The response sounds plausible, but it is not yet a reliable ParaView workflow. It needs explicit data assumptions, filter logic, export guidance, and careful wording about what the visualization proves.

