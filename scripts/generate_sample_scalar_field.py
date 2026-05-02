"""Generate a small synthetic scalar field for ParaView.

The default output is an ASCII VTK legacy file that ParaView can open directly
without any third-party Python packages.

Optional CSV output is included as a fallback for table-based inspection.

Field definition:
    temperature = sin(x) * cos(y) + z

The script uses only the Python standard library.
"""

from __future__ import annotations

import argparse
import csv
import math
from pathlib import Path


def build_grid(nx: int, ny: int, nz: int, x_min: float, x_max: float, y_min: float, y_max: float, z_min: float, z_max: float):
    """Return coordinate ranges and spacing for a regular grid."""

    if nx < 2 or ny < 2 or nz < 2:
        raise ValueError("nx, ny, and nz must each be at least 2")

    dx = (x_max - x_min) / (nx - 1)
    dy = (y_max - y_min) / (ny - 1)
    dz = (z_max - z_min) / (nz - 1)
    return dx, dy, dz


def temperature(x: float, y: float, z: float) -> float:
    """Synthetic scalar field used for the sample."""

    return math.sin(x) * math.cos(y) + z


def write_vtk(path: Path, nx: int, ny: int, nz: int, x_min: float, y_min: float, z_min: float, dx: float, dy: float, dz: float) -> None:
    """Write an ASCII VTK structured-points dataset."""

    total_points = nx * ny * nz
    lines = [
        "# vtk DataFile Version 3.0",
        "Synthetic scalar field for ParaView",
        "ASCII",
        "DATASET STRUCTURED_POINTS",
        f"DIMENSIONS {nx} {ny} {nz}",
        f"ORIGIN {x_min:.6f} {y_min:.6f} {z_min:.6f}",
        f"SPACING {dx:.6f} {dy:.6f} {dz:.6f}",
        f"POINT_DATA {total_points}",
        "SCALARS temperature float 1",
        "LOOKUP_TABLE default",
    ]

    for k in range(nz):
        z = z_min + k * dz
        for j in range(ny):
            y = y_min + j * dy
            for i in range(nx):
                x = x_min + i * dx
                lines.append(f"{temperature(x, y, z):.6f}")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_csv(path: Path, nx: int, ny: int, nz: int, x_min: float, y_min: float, z_min: float, dx: float, dy: float, dz: float) -> None:
    """Write a CSV fallback with coordinates and scalar values."""

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["x", "y", "z", "temperature"])
        writer.writeheader()
        for k in range(nz):
            z = z_min + k * dz
            for j in range(ny):
                y = y_min + j * dy
                for i in range(nx):
                    x = x_min + i * dx
                    writer.writerow(
                        {
                            "x": f"{x:.6f}",
                            "y": f"{y:.6f}",
                            "z": f"{z:.6f}",
                            "temperature": f"{temperature(x, y, z):.6f}",
                        }
                    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="generated-data/scalar_field.vtk", help="Output file path.")
    parser.add_argument(
        "--format",
        choices=("vtk", "csv"),
        default="vtk",
        help="Output format. VTK is the recommended ParaView path.",
    )
    parser.add_argument("--nx", type=int, default=21, help="Grid points along x.")
    parser.add_argument("--ny", type=int, default=21, help="Grid points along y.")
    parser.add_argument("--nz", type=int, default=11, help="Grid points along z.")
    parser.add_argument("--x-min", type=float, default=-math.pi, help="Minimum x coordinate.")
    parser.add_argument("--x-max", type=float, default=math.pi, help="Maximum x coordinate.")
    parser.add_argument("--y-min", type=float, default=-math.pi, help="Minimum y coordinate.")
    parser.add_argument("--y-max", type=float, default=math.pi, help="Maximum y coordinate.")
    parser.add_argument("--z-min", type=float, default=-1.0, help="Minimum z coordinate.")
    parser.add_argument("--z-max", type=float, default=1.0, help="Maximum z coordinate.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    dx, dy, dz = build_grid(args.nx, args.ny, args.nz, args.x_min, args.x_max, args.y_min, args.y_max, args.z_min, args.z_max)
    output_path = Path(args.output)

    if args.format == "vtk":
        write_vtk(output_path, args.nx, args.ny, args.nz, args.x_min, args.y_min, args.z_min, dx, dy, dz)
    else:
        write_csv(output_path, args.nx, args.ny, args.nz, args.x_min, args.y_min, args.z_min, dx, dy, dz)

    print(f"Wrote {args.format.upper()} scalar field to {output_path}")


if __name__ == "__main__":
    main()

