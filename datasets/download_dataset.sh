#!/bin/bash
set -e

# ==============================================================================
# Script: download_dataset.sh
# Purpose: Automatically download and unpack Kaggle Olist E-commerce Dataset
# ==============================================================================

TARGET_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/data"
mkdir -p "$TARGET_DIR"

DATASET_NAME="olistbr/brazilian-ecommerce"

echo "=========================================================="
echo "📦 Downloading Kaggle Dataset: $DATASET_NAME"
echo "📂 Target Directory: $TARGET_DIR"
echo "=========================================================="

# Check if kaggle CLI is installed
if ! command -v kaggle &> /dev/null; then
    echo "⚠️ Warning: 'kaggle' CLI not found."
    echo "Installing kaggle CLI via pip..."
    pip install kaggle
fi

# Check for ~/.kaggle/kaggle.json
if [ ! -f "$HOME/.kaggle/kaggle.json" ] && [ -z "$KAGGLE_USERNAME" ]; then
    echo "❌ Error: Kaggle credentials not found!"
    echo "Please place your 'kaggle.json' in ~/.kaggle/ or set KAGGLE_USERNAME and KAGGLE_KEY."
    echo "Alternatively, datasets/seed_data.py will automatically generate synthetic data."
    exit 1
fi

echo "🚀 Fetching dataset files..."
kaggle datasets download -d "$DATASET_NAME" -p "$TARGET_DIR" --unzip

echo "✅ Dataset successfully downloaded and extracted into $TARGET_DIR"
ls -lh "$TARGET_DIR"
