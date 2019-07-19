#!/bin/sh
#SBATCH -o gpu-job-%j.output
#SBATCH -p NV100q
#SBATCH --gres=gpu:1
#SBATCH -n 1
module load cuda90/toolkit

python3 main.py --gpu --batchsize 32 --epoch 50
