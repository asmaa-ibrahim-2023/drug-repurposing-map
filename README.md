# AI-Powered Drug Repurposing Map from Biomedical Literature

CSAI 491 Senior Project · School of Information Technology · New Giza University
Supervisor: Dr. Nehal Ali

## Overview

Developing a new drug takes many years and is very costly. This project suggests existing drugs that could be repurposed to treat other diseases: if drug X is used for disease Y, can it treat disease Z? We build a drug repurposing map from a biomedical knowledge graph, predict new drug–disease links, and use explainable AI to justify each suggestion.

Phase I uses **PrimeKG**, a knowledge graph linking drugs, diseases, genes and other biological entities, and covers all diseases.

## Team

| Member | Role |
| --- | --- |
| Asmaa Ibrahim | Team leader |
| Belal Ehab | |
| Hana Ahmed | |
| Kenzy Ahmed | |

## Repository structure

```
notebooks/
  01_primekg_eda.ipynb   Dataset acquisition and initial exploratory analysis
scripts/
  download_data.py       Downloads PrimeKG into data/
data/                    Downloaded data (not committed)
requirements.txt         Python dependencies
```

## Setup

**Google Colab (recommended):** open `notebooks/01_primekg_eda.ipynb` in Colab and choose Runtime → Run all. The notebook downloads the data itself.

**Local:**

```bash
git clone <repository-url>
cd <repository-folder>
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/download_data.py
jupyter notebook notebooks/01_primekg_eda.ipynb
```

PrimeKG is about 1 GB and is not stored in this repository.

## Dataset

Chandak, P., Huang, K., & Zitnik, M. (2023). Building a knowledge graph to enable precision medicine. *Scientific Data*, 10, 67. Data: [Harvard Dataverse](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/IXA7BM).

## Project status

- [x] Dataset identified and acquired
- [x] Initial exploratory data analysis
- [ ] Baseline drug–disease link prediction
- [ ] Graph neural network model
- [ ] Explainable AI module
- [ ] Web application
