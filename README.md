# MIMIC-NLE Dataset

This repository contains the scripts to extract the MIMIC-NLE dataset from the MIMIC-CXR radiology reports. In order to download MIMIC-CXR, head [here](https://physionet.org/content/mimic-cxr-jpg/2.0.0/). More details on the dataset are provided in our MICCAI 2022 paper:

*Explaining Chest X-ray Pathologies in Natural Language* ([arxiv](https://arxiv.org/abs/2207.04343))

## Extracting the dataset

To run our extraction script, please first a create an environment by running `conda env create -f environment.yml`.

After you downloaded MIMIC-CXR, get the path of the radiology reports, which should be given in the following structure: 

```
mimic_reports
└───p10
│   └───p10000032
│   │     s50414267.txt
│   │     s53189527.txt
│   │     ...
│   └───p10000764
│   ...
└───p11
...
└───p19
```

You can then generate MIMIC-NLE by simply running: 
```
python extract_mimic_nle.py --reports_path path/to/your/reports
```
The train, dev, and test set will be stored in the `mimic-nle` folder.

## Dataset details

For each Natural Language Explanation (NLE), we get the following information: 

```
{
"sentence_ID": "s51038639#2",                                   // unique NLE identifier
"nle": "Subtle lower lobe opacities may reflect atelectasis.",  // the NLE
"patient_ID": "p11662490",                                      // unique patient ID
"report_ID": "s51038639",                                       // unique radiology report ID
"diagnosis_label": [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],              // one-hot encoding of the diagnosis label, i.e. the label that is being explained
"evidence_label": [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],               // one-hot encoding of the evidence label, i.e. the label that is evidence for another label
"img_labels": [[0, 1, 0], [1, 0, 0], ..., [1, 0, 0]]            // image-wide labels, given as [negative, uncertain, positive] for each class
}
```

The diagnosis and evidence labels apply only specifically to the NLE at hand, while the `img_labels` apply to the whole image and may contain labels not referred to in the NLE. Dictionaries to uncode the one-hot encoding are provided in `encodings.py`.


