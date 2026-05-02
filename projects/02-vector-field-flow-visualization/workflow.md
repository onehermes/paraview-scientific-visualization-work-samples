# Workflow

## 1. Load the vector field dataset

Generate the sample data:

```bash
python scripts/generate_sample_vector_field.py --output generated-data/vector_field.vtk
```

Open `generated-data/vector_field.vtk` in ParaView.

## 2. Inspect the vector array

Verify that the `velocity` vector array is present and available for coloring, glyphing, or stream tracing.

If you generate the CSV fallback instead, make sure the vector components are present and that you convert them into a usable vector array before interpreting the result.

## 3. Apply `Glyph`

Use `Glyph` to show vector direction and relative magnitude.

Recommended practice:

- choose a glyph type that makes arrow direction obvious
- reduce glyph density if the scene becomes cluttered
- keep the scale factor readable instead of making the arrows dominate the entire image

## 4. Scale glyphs by vector magnitude

Scale glyphs by the vector magnitude so longer arrows represent stronger vectors. Keep the scaling bounded so the visualization remains readable.

## 5. Use color mapping

Color by magnitude when the goal is to communicate strength, not just direction.

Recommended practice:

- use a color map that does not exaggerate the data
- avoid assigning meaning to a color transition that the field does not support
- if you color by a component, say so explicitly in the notes

## 6. Apply `Stream Tracer` if applicable

If a streamline view helps, add `Stream Tracer` with a clear seed source.

Useful notes:

- choose seed placement that intersects the most interesting part of the field
- make sure the chosen seed source is documented
- state whether the tracer is forward, backward, or bidirectional

## 7. Export the screenshot

Capture a screenshot once glyph size, color map, and streamline settings are stable.

## Interpretation Notes

- The vector field describes a rotational pattern with a weak vertical component.
- Glyph orientation shows direction; glyph size suggests magnitude only when the scaling is documented.
- Streamlines can help reveal the rotational structure, but they should not be described as evidence of a real instrumented flow without real data.

