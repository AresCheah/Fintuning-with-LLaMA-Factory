# Fine-tuning and Deployment of LLaMA-Factory with FastAPI

This guide covers the full pipeline of fine-tuning a language model using [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory), and deploying it with FastAPI for serving inference.

## 1. Clone LLaMA-Factory Repository

```bash
git clone https://github.com/hiyouga/LLaMA-Factory.git
cd LLaMA-Factory
```

---

## 2. Set Up Conda on Data Disk(optional)

```bash
mkdir -p /root/autodl-tmp/conda/pkgs
conda config --add pkgs_dirs /root/autodl-tmp/conda/pkgs

mkdir -p /root/autodl-tmp/conda/envs
conda config --add envs_dirs /root/autodl-tmp/conda/envs
```

---

## 3. Create Conda Environment for LLaMA-Factory

```bash
conda create -n llama-factory python=3.10 -y
conda activate llama-factory

pip install -e ".[torch,metrics]"
```

---

## 4. Launch LLaMA-Factory WebUI

```bash
llamafactory-cli webui
```

---

## 5. Download Pretrained Model from HuggingFace

```bash
mkdir -p /root/autodl-tmp/Hugging-Face
export HF_HOME=/root/autodl-tmp/Hugging-Face

pip install -U huggingface_hub

huggingface-cli download --resume-download <your-model-name>
```

---

## 6. Prepare Your Dataset

- Place your training data in the `data` directory:
  
```bash
LLaMA-Factory/data/your_data.json
```

- Update the dataset configuration `dataset_info.json`:

```json
"your_data": {
    "file_name": "your_data.json"
}
```

---

## 7. Start Fine-Tuning

- Launch the WebUI:
  
```bash
llamafactory-cli webui
```

- In the WebUI:
  - Set your model path to the **unique hash** inside the downloaded model folder.
  - Select `your_data` as your training dataset.
  - Configure your training parameters as needed.
  - Click **Start Training**.

---

## 8. Export Merged Model

After training completes:

```bash
mkdir -p Models/<your-model-name>-merged
```

- In the WebUI:
  - Set the export path accordingly.
  - Click **Start Export**.

---

## 9. Deploy Model with FastAPI

### Create FastAPI Environment

```bash
conda create -n fastapi python=3.10 -y
conda activate fastapi

conda install -c conda-forge fastapi uvicorn transformers pytorch -y
pip install safetensors sentencepiece protobuf
```

---

### Set Up FastAPI Project Structure

```bash
mkdir App
cd App
touch main.py test.py
```

- Paste your **FastAPI app code** into `main.py`.
- Paste your **test script** into `test.py` (modify as needed for your use case).

---

### Start FastAPI Service

```bash
uvicorn main:app --reload --host 0.0.0.0
```

In a new terminal, run the test script:

```bash
python test.py
```

---

## Directory Structure Overview

```
├── LLaMA-Factory/
│   ├── data/
│   │   ├── your_data.json
│   │   └── dataset_info.json
├── Models/
│   └── your-model-name-merged/
├── App/
│   ├── main.py
│   └── test.py
```

---

## Notes

- Adjust paths according to your environment setup.
- Ensure that ports are open for API access if running on a remote server.
- You can use `nohup` or `screen` for long-running services.

---

## License

This project combines open-source tools. Please refer to each respective repository for licensing details.