# Create env with PYTHON3.11 IMPORTANT!
python3.11 -m venv venv

# Ma che cazzo ne so fai cosi e basta che a me si rompeva
CMAKE_ARGS="-DCMAKE_OSX_ARCHITECTURES=arm64" pip install --upgrade --verbose --force-reinstall --no-cache-dir instructlab

# Init ilab
ilab config init

# Download default model
ilab model download --hf-token=

# Serve chat model
ilab model serve --model-path ./models/granite-7b-lab-Q4_K_M.gguf

# Update mac RAM usage for faster generate (this will reset to 0 at reboot)
sudo sysctl iogpu.wired_limit_mb=12288

# Generate data from provided taxonomy
ilab data generate --gpus=1 --pipeline simple

# TRAIN
