#!/bin/bash

echo "🚀 Iniciando configuración del entorno para Gaussian Splatting..."

# 1. Instalar dependencias del sistema
echo "🔧 Instalando dependencias del sistema (requiere sudo)..."
sudo apt-get update && \
sudo apt-get install -y --no-install-recommends \
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
    wget && \
sudo apt-get clean && sudo rm -rf /var/lib/apt/lists/*

# 2. Crear entorno virtual
echo "🐍 Creando entorno virtual Python..."
python3 -m venv gs-env
source gs-env/bin/activate

# 3. Instalar PyTorch y dependencias Python
echo "📦 Instalando PyTorch y librerías requeridas..."
pip install --upgrade pip
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
pip install -r requirements.txt

# 4. Compilar submódulos
echo "⚙️ Compilando submódulos..."
cd submodules/simple-knn
python setup.py develop

cd ../fused-ssim
python setup.py develop

cd ../diff-gaussian-rasterization
python setup.py develop

cd ../../  # Volver a la raíz del repo

echo ""
echo "✅ Entorno listo. Para activarlo más tarde, usa:"
echo "   source gs-env/bin/activate"
