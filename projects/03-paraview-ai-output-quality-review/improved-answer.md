# Improved Answer

Use a clearly defined dataset first. If you are working from this portfolio, open `generated-data/scalar_field.vtk` for the scalar example or `generated-data/vector_field.vtk` for the vector example.

## Scalar Example

1. Open the VTK file in ParaView.
2. Inspect the available arrays and select `temperature`.
3. Apply `Slice` to create a 2D cross-section.
4. Apply `Contour` to the slice output if you want contour lines or threshold surfaces.
5. Color by `temperature` and choose a smooth sequential color map.
6. Add a scalar bar so the array name and range are visible.
7. Reset the camera.
8. Export a screenshot at the desired resolution.

## Vector Example

1. Open the VTK file in ParaView.
2. Inspect the vector arrays and select `velocity`.
3. Apply `Glyph` to show vector direction.
4. Scale the glyphs by vector magnitude and keep the scale factor readable.
5. Color by magnitude or another explicitly stated array component.
6. Add `Stream Tracer` only if streamlines help explain the field, and document the seed source.
7. Export a screenshot once the view is stable.

## Review Notes

- The dataset format is named explicitly.
- The selected array is named explicitly.
- The filter order is written in a reproducible sequence.
- The color map is described as part of the workflow, not as decoration.
- The final image is supported by an export step.
- The explanation stays within the limits of the synthetic dataset.

## Limitation Statement

This workflow demonstrates visualization technique, not physical validation. The synthetic field is useful for review and documentation, but it should not be described as evidence of a real experiment or simulation result.

