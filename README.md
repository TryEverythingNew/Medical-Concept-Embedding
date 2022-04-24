# Introduction

This project aims at reproducing the work of "Medical Concept Embedding using TeSAN model" proposed in paper "Xueping Peng, Guodong Long, Tao Shen, Sen Wang, Jing Jiang, and Michael Blumenstein. 2019. Temporal self-attention network for medical concept embedding. In 2019 IEEE International Conference on Data Mining (ICDM), pages 498–507. IEEE."

# Prerequisite of Running the Code

1. python version 3.6.x-3.7.x is good, and tensorflow version around 1.13. is good.
2. Due that github doesn't allow file size > 100Mb, one raw data file is not uploaded although other raw files are uploaded.
You need to download "PRESCRIPTIONS.csv" from MIMIC III dataset and put it into "dataset\mimic3" folder.

# How to Run
## Step 1: process raw file
python data_preparation.py
## Step 2: To train tesan model
python train_tesan.py --data_source mimic3 --model tesa --gpu 1 --max_epoch 30 --train_batch_size 64 --num_samples 10 --reduced_window True --skip_window 6 --verbose True --is_scale False --is_date_encoding False --task embedding --visit_threshold 1

You can adjust "--model tesa" to other arguments to test other models like "--model normal"
