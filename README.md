## PIG: Prompt Images Guidance for Night-time Scene Parsing
by Zhifeng Xie, Rui Qiu, Sen Wang, Xin Tan, Yuan Xie
## Overview
Night-time scene parsing aims to extract pixel-level semantic information in night images, aiding downstream tasks in understanding scene object distribution. Due to limited labeled night image datasets, **unsupervised domain adaptation (UDA)** has become the predominant method for studying night scenes. 
UDA typically relies on paired day-night image pairs to guide adaptation, but this approach hampers dataset construction and restricts generalization across night scenes in different datasets. Moreover, UDA, focusing on network architecture and training strategies, faces difficulties in handling classes with little domain similarities.

We leverage **Prompt Images Guidance (PIG)** to enhance UDA with supplementary night knowledge. We propose a **Night-Focused Network (NFNet)** to learn night-specific features from both target domain images and prompt images. To generate high-quality pseudo-labels, we propose **Pseudo-label Fusion via Domain Similarity Guidance (FDSG)**. We utilize the LPIPS to assess the domain similarity between day and night images for the single class.
Classes with less domain similarities are predicted by NFNet, which excels in parsing night features, while classes with more domain similarities are predicted by UDA, which has rich labeled semantics. Additionally, we propose two data augmentation strategies: the **Prompt Mixture Strategy (PMS)** and the **Alternate Mask Strategy (AMS)**, aimed at mitigating overfitting of the NFNet to few prompt images.

We conduct extensive experiments on four night-time datasets: **NightCity**, **NightCity+**, **Dark Zurich**, and **ACDC**. The results indicate that utilizing PIG can enhance the parsing accuracy of UDA.

![PIG compare](resources/PIG_compare.png)
