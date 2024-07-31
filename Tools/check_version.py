import torch
import sys
from torch.utils.cpp_extension import CUDA_HOME

# Print Python and PyTorch versions
print("Python version:",sys.version)
print("torch version:",torch.__version__)

# Check if CUDA is available
if torch.cuda.is_available():
    # If CUDA is available, print its details
    print("Installation path of CUDA:", CUDA_HOME)
    print("CUDA version:", torch.version.cuda)
    print("CUDA device count:", torch.cuda.device_count())
else:
    # If CUDA is not available, provide a message
    print("CUDA is not available.")


