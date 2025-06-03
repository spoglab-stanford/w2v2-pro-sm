# Employing self-supervised learning models for cross-linguistic child speech maturity classification

```
/path/to/w2v2-pro-sm/speechbrain/recipes/W2V2-LL4300-Pro-SM
├── 2025 (example seed)
│   ├── myst_checkpoints
│   │   ├── CKPT+2025-02-09+02-37-58+00 (from https://huggingface.co/spoglab/w2v2-pro-sm)
│   │   │   ├── ...
|   |   ├── CKPT+2025-02-08+21-43-25+00 (from https://huggingface.co/spoglab/w2v2-pro-sm)
│   │   │   ├── ...
│   │   ├── wav2vec_asr.ckpt (from https://huggingface.co/spoglab/w2v2-pro-sm)
│   ├── predictions.csv
├── checkpoint_best.pt (from https://huggingface.co/spoglab/w2v2-pro-sm)
├── convert_to_json.py
├── environment.yaml
├── fairseq_wav2vec.py
├── hparams
│   └── train_1_w2v2_2dnn_WA_LL4300_asr_bbcor_concat.yaml
├── Readme.md
├── sample_json
│   └── sample_sm.json
└── train_1_w2v2_WA_2dnn_combine_asr_features_bbcor.py
```
## Steps for running inference with W2V2-LL4300-Pro-SM
The following steps are to be followed if you wish to use W2V2-LL4300-Pro-SM for inference on your data.

1. Clone this repository:
```
git clone https://github.com/spoglab-stanford/w2v2-pro-sm
```
2. Navigate to the W2V2-LL4300-Pro-SM folder in the repository
```
cd ../w2v2-pro-sm/speechbrain/recipes/W2V2-LL4300-Pro-SM
```
3. Create and activate a new conda virtual environment using the required packages to run the model
```
conda env create -f environment.yaml
conda activate w2v2-ll4300-pro-sm
```
4. Create a new directory named after the seed you set in ../hparams/train_1_w2v2_2dnn_WA_LL4300_asr_bbcor_concat.yaml that will hold your model outputs with a subdirectory named myst-checkpoints. Refer to the file tree at the top of this page for more details.

5. Download the requisite model checkpoints from https://huggingface.co/spoglab/w2v2-pro-sm and place them in the correct locations according the file tree above.

6. (If needed) Convert your CSVs to JSON. You can refer to the convert_to_json.py code or refer to the expected format in the sample_json folder.
    - If you are doing inference, you can set the label to a random label (i.e. Junk) and ignore the statistical metrics the output will produce

7. Update all the paths and seed in ../hparams/train_1_w2v2_2dnn_WA_LL4300_asr_bbcor_concat.yaml and train_1_w2v2_WA_2dnn_combine_asr_features_bbcor.py 

8. Run the model. Your predicted labels will be in the file you set in train_1_w2v2_WA_2dnn_combine_asr_features_bbcor.py and the label mapping is: "Non-Canonical": 1, "Canonical": 2, "Laughing": 3, "Crying": 4,"Junk": 0
```
python train_1_w2v2_WA_2dnn_combine_asr_features_bbcor.py train_1_w2v2_2dnn_WA_LL4300_asr_bbcor_concat.yaml
```
### Paper/BibTex Citation
If you found this recipe or our paper helpful, please cite us as

```
@article{zhang2025employing,
  title={Employing self-supervised learning models for cross-linguistic child speech maturity classification},
  author={Zhang, Theo and Suresh, Madurya and Warlaumont, Anne and Hitczenko, Kasia and Cristia, Alejandrina and Cychosz, Margaret},
  booktitle={Interspeech},
  year={2025}
}
```

### Acknowledgement
Thank you to Jialu Li (jialuli3@illinois.edu) for providing the foundational work for this model, including the code (https://github.com/jialuli3/speechbrain/tree/ef9038cd076dd2789755f48c0f95955c8570be5a/recipes/BabbleCor) and the pretrained model we finetuned. Jialu's enthusiastic assistance allowed us to utilize her code to create the new state-of-the-art model for this task.

### Contact
Theo Zhang

E-mail: theo.zhang@ucla.edu