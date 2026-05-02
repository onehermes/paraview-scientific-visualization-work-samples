# Workflow

This workflow uses the generated scalar dataset as the primary path. If you prefer the built-in `Wavelet` source, the same visual reasoning applies; the main difference is the array name you select in ParaView.

## 1. Open ParaView

Launch ParaView and make sure the standard pipeline browser, properties panel, and render view are visible.

## 2. Load or generate the dataset

Generate the sample data:

```bash
python scripts/generate_sample_scalar_field.py --output generated-data/scalar_field.vtk
```

Then open `generated-data/scalar_field.vtk` in ParaView.

## 3. Inspect available arrays

Check the dataset information and verify that the scalar array is available. In this sample, the array is named `temperature`.

If you use `Wavelet` instead, the equivalent array is typically `RTData`.

## 4. Apply the `Slice` filter

Use `Slice` to cut through the 3D volume and expose a single 2D section.

Recommended practice:

- choose a plane that crosses the center of the dataset
- keep the slice orientation visible enough to explain in notes
- avoid implying that the slice is a physical measurement plane unless the dataset really supports that claim

## 5. Apply the `Contour` filter

Apply `Contour` to the slice output so the contour lines represent the selected scalar thresholds on that 2D section.

Why this order matters:

- `Slice` first reduces the volume to a section
- `Contour` second makes that section easier to read
- this order is easier to explain than contouring a large volume first when the goal is a simple work sample

## 6. Adjust the color map

Color by the scalar array and choose a palette that makes gradients legible.

Recommended practice:

- prefer a perceptually clear map such as Viridis or another smooth sequential palette
- avoid rainbow-style maps when they make the data harder to read
- note the chosen array name in the documentation

## 7. Add a scalar bar

Add a scalar bar so the figure can be read without hidden context.

The scalar bar should support:

- array name
- value range
- immediate visual interpretation

## 8. Reset the camera

Reset the camera after the filters are applied so the dataset is framed cleanly and the screenshot starts from a stable view.

## 9. Export the screenshot

Export an image once the pipeline, colors, and framing are final. Record the export settings in the notes if you want the result to be reproducible later.

## If You Use The Wavelet Source

The pipeline remains the same:

1. create the source
2. inspect the active scalar array
3. apply `Slice`
4. apply `Contour`
5. color by the selected scalar
6. add the scalar bar
7. reset the camera
8. export the image

