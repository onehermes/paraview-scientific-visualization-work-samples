# Vector Field Notes

## What The Field Represents

The synthetic field is defined as:

- `vx = -y`
- `vy = x`
- `vz = 0.1 * z`

That means:

- vectors rotate around the z-axis
- vector direction changes smoothly across the plane
- the vertical component introduces a gentle upward or downward drift depending on the sign of `z`

## Why This Is Useful

This is a compact way to test whether a ParaView workflow can show:

- vector direction
- relative magnitude
- how glyph scaling affects readability
- whether stream tracers reinforce or obscure the story

## Review Caution

This field is not a physical measurement. It is useful for documentation, not for claiming turbulence, pressure behavior, or experimental validation.

