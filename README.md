# CSI-Geometric-Bounds
# CSI Geometric Information Bounds

This repository contains the Python implementation used in the paper:

"Geometric Information-Theoretic Bounds for CSI-Based Spatial Inference"

## Description

The code reproduces:

- ULA geometry and channel simulation
- Channel manifold generation
- PCA-based 3D embedding
- Jacobian norm visualization
- Mutual information bound validation

## Files

- `ULA.py`  
  Simulates a Uniform Linear Array (ULA) and generates the channel response over a spatial grid.

- `Manifold.py`  
  Generates the CSI manifold, applies PCA for dimensionality reduction, and visualizes the embedding and Jacobian-based information structure.

## Requirements

Python ≥ 3.9

Install dependencies:

```bash
pip install -r requirements.txt
