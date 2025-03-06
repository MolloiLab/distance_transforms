# distance_transforms
[![Documentation][docs-img]][docs-url]

Python bindings for the Julia [DistanceTransforms.jl](https://github.com/MolloiLab/DistanceTransforms.jl) package, providing efficient Euclidean distance transforms for arrays.

## Installation

```bash
pip install distance_transforms
```

## Requirements

- Python 3.11+
- Julia 1.10+ or 1.11
- Required Julia packages will be automatically installed on first use

## Usage

### Basic Example

```python
import numpy as np
import distance_transforms as dts

# Create a binary array (1's for foreground, 0's for background)
arr = np.zeros((5, 5), dtype=np.uint8)
arr[2, 2] = 1  # Set center point as foreground

# Compute distance transform
# Returns squared distances from each point to the nearest foreground point
distances = dts.transform(arr)
print(distances)
```

### CUDA Example (Optional)

If you have CUDA available and PyTorch installed:

```python
import torch
import distance_transforms as dts

# Create a binary tensor on GPU
tensor = torch.zeros((5, 5), dtype=torch.bool, device="cuda")
tensor[2, 2] = True

# Compute distance transform on GPU
distances = dts.transform_cuda(tensor)
print(distances)
```

## About

This package is a Python wrapper around [DistanceTransforms.jl](https://github.com/MolloiLab/DistanceTransforms.jl), which provides efficient implementations of Euclidean distance transforms. The distance transform computes, for each pixel in an image, the squared Euclidean distance to the nearest non-zero pixel.

On first use, the package will set up the required Julia environment automatically.

## Features

- Fast CPU implementation using the Felzenszwalb algorithm
- Optional GPU acceleration with CUDA support
- Simple, NumPy-compatible API
- Support for multidimensional arrays

## Documentation

For comprehensive documentation on the algorithms and detailed usage, please refer to the [DistanceTransforms.jl documentation](https://molloilab.github.io/DistanceTransforms.jl/).

## License

MIT

[docs-img]: https://img.shields.io/badge/docs-dev-blue.svg
[docs-url]: https://molloilab.github.io/DistanceTransforms.jl/