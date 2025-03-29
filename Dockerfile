FROM nvidia/cuda:12.4.0-devel-ubuntu22.04
#FROM nvidia/cuda:12.8.0-devel-ubuntu24.04

# Instalación de dependencias generales
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    git \
    libopencv-dev \
    python3 \
    python3-pip \
    python3-dev \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libglm-dev \
    ninja-build \
    curl \
    wget \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Instalación de PyTorch con CUDA 12.4
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

# Instalación de otras dependencias de Python
RUN pip install tqdm tensorboard pybind11

# Clonación del repositorio de Gaussian Splatting
WORKDIR /workspace
RUN git clone https://github.com/graphdeco-inria/gaussian-splatting.git
WORKDIR /workspace/gaussian-splatting
RUN git submodule update --init --recursive

# Configuración del entorno virtual
RUN python3 -m venv gs-env && \
    . gs-env/bin/activate && \
    pip install -r requirements.txt

# Compilación de submódulos
WORKDIR /workspace/gaussian-splatting/submodules/simple-knn
RUN . /workspace/gaussian-splatting/gs-env/bin/activate && python setup.py develop

WORKDIR /workspace/gaussian-splatting/submodules/fused-ssim
RUN . /workspace/gaussian-splatting/gs-env/bin/activate && python setup.py develop

WORKDIR /workspace/gaussian-splatting/submodules/diff-gaussian-rasterization
RUN . /workspace/gaussian-splatting/gs-env/bin/activate && python setup.py develop

# Establecer el entorno para la ejecución
ENV PATH="/workspace/gaussian-splatting/gs-env/bin:$PATH"

CMD ["/bin/bash"]
