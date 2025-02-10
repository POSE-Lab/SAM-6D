## Steps to follow for BOP Evaluation.

Getting Started:

Install SAM-6D env and the model checkpoints:

```
cd SAM-6D
bash prepare.sh
```

## Data preparation

Download BOP Datasets inside /Data.

Structure should be:

```bash
Data/BOP
├── lmo
    ├──models           # object CAD models 
    ├──test             # bop19 test set
    ...
```

## Render templates:

```
cd ../Render/
blenderproc run render_bop_templates.py --dataset_name $DATASET
```

The string "DATASET" could be set as lmo, icbin, itodd, hb, tless, tudl or ycbv. Rendered templates can also be downloaded from the SAM-6D repo.


## Instance Segmentation

Run Instance Segmentation with SAM or FastSAM.

```
cd Instance_Segmentation_Model

export CUDA_VISIBLE_DEVICES=0

python run_inference.py dataset_name=$DATASET or python run_inference.py dataset_name=$DATASET model=ISM_fastsam.
```

The string "DATASET" could be set as lmo, icbin, itodd, hb, tless, tudl or ycbv.

## Pose Estimation

Evaluation on BOP Datasets:

```
cd Pose_Estimation_Model

python test_bop.py --gpus 0 --model pose_estimation_model --config config/base.yaml --dataset $DATASET --view 42
```

The string "DATASET" could be set as lmo, icbin, itodd, hb, tless, tudl or ycbv. 