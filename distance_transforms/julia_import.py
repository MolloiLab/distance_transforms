"""
Initialize Julia and import required packages.
"""
import os
import importlib.resources
from juliacall import Main as jl

# Replace these lines:
# if importlib.resources.is_resource(__package__, "juliapkg.json"):
#     pkg_file = importlib.resources.path(__package__, "juliapkg.json").__enter__()
#     os.environ["JULIA_PROJECT"] = str(pkg_file.parent)

# With this modern approach:
try:
    # For Python 3.9+
    pkg_file = importlib.resources.files(__package__).joinpath("juliapkg.json")
    os.environ["JULIA_PROJECT"] = str(pkg_file.parent)
except AttributeError:
    # Fallback for older Python versions (though you're using 3.11 so this shouldn't be needed)
    with importlib.resources.path(__package__, "juliapkg.json") as pkg_file:
        os.environ["JULIA_PROJECT"] = str(pkg_file.parent)

# Initialize Julia packages
jl.seval("using Pkg; Pkg.status()")
jl.seval("using DLPack")
jl.seval("using DistanceTransforms")

# Optional CUDA support
try:
    jl.seval("using CUDA")
    CUDA_AVAILABLE = True
except Exception:
    CUDA_AVAILABLE = False

# Export Julia modules
DLPack = jl.DLPack
DistanceTransforms = jl.DistanceTransforms

# Check for CUDA capability
def is_cuda_available():
    """Check if CUDA is available in the Julia environment."""
    return CUDA_AVAILABLE and jl.seval("CUDA.functional()")