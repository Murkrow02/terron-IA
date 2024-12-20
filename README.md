# Terron-IA
A simple LLM create using IBM InstructLab

## Instructions
### Create env with PYTHON3.11 (brew install python@3.11)
Make sure to use exactly this python version as it's a requirement of ilab
```bash
python3.11 -m venv venv
```
### Install ilab
```bash
CMAKE_ARGS="-DCMAKE_OSX_ARCHITECTURES=arm64" pip install --upgrade --verbose --force-reinstall --no-cache-dir instructlab
```

### Init ilab
*Important!* do not edit the standard configuration as in beta it may break
```bash
ilab config init
```

### Download default model
```bash
ilab model download --hf-token=
```

### Serve chat model
```bash
ilab model serve --model-path ./models/granite-7b-lab-Q4_K_M.gguf
```

### Update mac RAM usage for faster generate (this will reset to 0 at reboot)
```bash
sudo sysctl iogpu.wired_limit_mb=12288
```

### Generate data from provided taxonomy
```bash
ilab data generate --gpus=1 --pipeline simple
```

### TRAIN
```bash
ilab -v model train --pipeline simple --local --num-epochs 1 --iters 10 --optimize-memory
```
### Convert model to GGUF
```bash
ilab model convert --model-dir /Users/murkrow/.local/share/instructlab/checkpoints/-Users-murkrow-.cache-instructlab-models-instructlab-granite-7b-lab-mlx-q/ --model-name jolie -sd
```

### Serve the newly created model
```bash
ilab model serve --model-path ./jolie-trained/jolie-Q4_K_M.gguf
```

### Chat with the model and enjoy!
```bash
ilab model chat
```
