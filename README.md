## Capped Lips Research and Code Repository

Welcome to my Capped Lips Research and Code Repository! This repository contains the code used for my Master's Thesis Research, titled "Capped Lips", which focuses on investigating the effectiveness of capsule networks for machine lipreading. This research was submitted in 2018 as part of the requirements for my degree of Master of Science in Software Development at Boston University.

The proposed method has been evaluated on a lipreading dataset and the results have shown that capsule networks outperform the traditional convolutional neural network-based models in terms of accuracy and robustness to noise.

This repository contains the code used to implement and evaluate the proposed method. The code is organized as follows:

- `data/`: This folder contains the dataset used in the experiments.
- `preprocessing/`: This folder contains the code used for data preprocessing.
- `train/`: This folder contains the code to implement the training loop for the capsule network model for lipreading.
- `models/`: This folder contains the implementation of the proposed method using capsule networks.
- `evaluation/`: This folder contains the code used for evaluating the proposed method.
- `compare/`: This folder ontains the code for comparing the effectiveness of the capsule network model against a baseline model
- `results/`: This folder contains the results obtained from the experiments.


### Usage

To run the code, please follow these steps:

1. Clone this repository: `git clone https://github.com/your_username/capped-lips.git`
2. Install the dependencies: `pip install -r requirements.txt`
3. Preprocess the data: `python preprocessing/main.py`
4. Train the model: `python models/main.py`
5. Evaluate the model: `python evaluation/main.py`
6. View the results: `python results/main.py`


