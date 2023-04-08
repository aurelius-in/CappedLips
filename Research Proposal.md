


# "Capped Lips"
## CapsNets for Machine Lipreading 
### Masters Thesis Research Proposal
### Boston University
#### Oliver Ellison 
#### 10/29/2017


### Table of Contents

- Introduction
- Literature Review
- Methodology
- Ethics Considerations
- Expected Outcomes
- Timeline and Budget
- Conclusion
- References


## Introduction:

The ability to understand spoken language without audio cues, also known as lipreading, is an important skill for individuals with hearing impairments, and has potential applications in security, communication, and entertainment. Despite advances in computer vision and machine learning, current lipreading systems still struggle with accuracy and robustness, especially in real-world scenarios where lighting, orientation, and occlusion vary.

#

In recent years, Capsule Networks (CapsNets) have emerged as a promising alternative to traditional Convolutional Neural Networks (CNNs) in computer vision tasks. CapsNets use a hierarchical and dynamic architecture that captures spatial relationships between different facial parts, such as the lips, teeth, and tongue, which are crucial for accurate lipreading. Additionally, CapsNets are more robust to variations in lighting, orientation, and occlusion, making them potentially useful in lipreading systems.

#

This research proposal aims to explore the potential benefits of CapsNets for machine lipreading, by investigating their effectiveness in detecting subtle changes in lip movements that correspond to spoken words, without audio cues. The proposed research will contribute to the development of more accurate and robust lipreading systems, and potentially improve communication and quality of life for individuals with hearing impairments.


## Literature Review

### Overview of the field of machine lipreading

Lipreading, also known as speechreading, is the ability to understand spoken language by observing the movements of the speaker's lips, tongue, teeth, and other facial features. Lipreading is an important skill for individuals with hearing impairments, and has potential applications in security, communication, and entertainment. However, lipreading is a challenging task, as the movements of the lips are highly variable and influenced by factors such as lighting, orientation, and occlusion.

### Current approaches and limitations in lipreading systems

Current lipreading systems use a combination of computer vision techniques, such as optical flow analysis and deep learning models, to recognize speech from visual cues. However, these systems still struggle with accuracy and robustness, especially in real-world scenarios where lighting, orientation, and occlusion vary. Additionally, lipreading systems require large amounts of labeled data for training, which can be difficult and time-consuming to obtain.

### The potential benefits of CapsNets for machine lipreading

Capsule Networks (CapsNets) are a relatively new type of deep learning model that have shown promise in computer vision tasks, including object recognition and pose estimation. CapsNets use a hierarchical and dynamic architecture that captures spatial relationships between different parts of an object, such as the lips, teeth, and tongue, which are crucial for accurate lipreading. Additionally, CapsNets are more robust to variations in lighting, orientation, and occlusion, making them potentially useful in lipreading systems.

### Previous studies on CapsNets in computer vision tasks

Previous studies have shown that CapsNets can outperform traditional Convolutional Neural Networks (CNNs) in several computer vision tasks, such as object recognition and pose estimation. However, few studies have investigated the effectiveness of CapsNets in lipreading tasks. The proposed research aims to fill this gap in the literature by exploring the potential benefits of CapsNets for machine lipreading.

## Methodology

### Dataset selection and preparation

To evaluate the effectiveness of CapsNets for machine lipreading, we will use the GRID corpus, which is a widely used dataset for visual speech recognition. The GRID corpus consists of over 33 hours of video recordings of 34 speakers uttering over 1,000 phrases, with both audio and visual cues.

We will preprocess the videos by extracting the frames corresponding to the spoken words, and resizing them to a fixed size. We will also convert the frames to grayscale to reduce the computational complexity of the CapsNet model.

### CapsNet architecture design and optimization

We will design a CapsNet architecture based on the original implementation proposed by Sabour et al. (2017) for the MNIST dataset. The CapsNet architecture consists of multiple layers of capsules, which are groups of neurons that represent a specific part of an object, such as the lips, teeth, or tongue. The capsules communicate with each other through dynamic routing, which allows them to capture spatial relationships between different facial features.

We will optimize the CapsNet architecture by adjusting the hyperparameters, such as the number of capsules and routing iterations, using a grid search approach. We will also use transfer learning techniques to initialize the CapsNet weights using pre-trained models on large-scale image datasets, such as ImageNet.

### Hyperparameter tuning and training/testing procedures

We will use the Adam optimizer with a learning rate of 0.001 to train the CapsNet model on the preprocessed GRID corpus dataset. We will split the dataset into training, validation, and testing sets, with a ratio of 80:10:10. We will use early stopping to prevent overfitting, and monitor the training and validation losses and accuracies.

We will evaluate the CapsNet model using several evaluation metrics, including accuracy, precision, recall, and F1 score. We will compare the performance of the CapsNet model with baseline models, such as CNNs and LSTM-based models, using cross-validation and statistical tests.

### Ethics considerations

We will obtain informed consent from the speakers in the GRID corpus, and ensure the privacy and confidentiality of their personal information. We will also comply with the guidelines and regulations for human subjects research at Boston University. We will store and handle the data securely to prevent unauthorized access or disclosure.

### Expected outcomes

We expect that the CapsNet model will outperform baseline models in terms of accuracy and robustness, especially in challenging scenarios where lighting, orientation, and occlusion vary. We also expect that the proposed research will contribute to the development of more accurate and robust lipreading systems, and potentially improve communication and quality of life for individuals with hearing impairments.


## Ethics considerations

### Informed consent

We will obtain informed consent from the speakers in the GRID corpus, which includes information about the purpose of the study, the data that will be collected, and how the data will be used. The participants will have the right to withdraw their consent at any time without penalty.

### Privacy and confidentiality

We will ensure the privacy and confidentiality of the personal information of the speakers in the GRID corpus. The data will be anonymized and stored securely on password-protected servers. Only authorized personnel will have access to the data.

### Human subjects research

We will comply with the guidelines and regulations for human subjects research at Boston University, including obtaining approval from the Institutional Review Board (IRB) and following the principles of the Belmont Report. We will minimize the risk of harm or discomfort to the participants, and ensure that the benefits of the research outweigh the risks.

### Data management

We will store and handle the data securely to prevent unauthorized access or disclosure. The data will be backed up regularly and stored offsite to prevent loss or damage. We will also ensure that the data is used only for the purposes outlined in the informed consent form, and not shared with any third parties without the consent of the participants.

### Reporting and dissemination

We will report the findings of the research in a clear and transparent manner, and acknowledge the contributions of the participants. We will obtain permission from the participants before using their images or recordings for publication or presentation. We will also ensure that the research results are disseminated in a way that respects the privacy and dignity of the participants, and does not perpetuate negative stereotypes or stigmatization.


## Expected outcomes

### Performance evaluation

We expect that the CapsNet model will outperform baseline models, such as CNNs and LSTM-based models, in terms of accuracy and robustness, especially in challenging scenarios where lighting, orientation, and occlusion vary. We will evaluate the CapsNet model using several evaluation metrics, including accuracy, precision, recall, and F1 score.

### Contribution to the field

We expect that the proposed research will contribute to the development of more accurate and robust lipreading systems, and potentially improve communication and quality of life for individuals with hearing impairments. The CapsNet architecture has shown promising results in other visual recognition tasks, and we expect that its application to lipreading will lead to new insights and methods for visual speech recognition.

### Future directions

We expect that the proposed research will open up new avenues for future research in the field of visual speech recognition, including the use of CapsNets for other speech-related tasks, such as speaker recognition and emotion detection. We also expect that the research will inspire new collaborations between researchers in computer science, linguistics, and audiology, and lead to interdisciplinary research projects that address the complex challenges of speech perception and production.


## Timeline and Budget

### Timeline

| Task                                          | Timeframe                  |
|-----------------------------------------------|----------------------------|
| Literature review                             | June - August 2018         |
| Data collection and preprocessing             | September - November 2018 |
| Model development and training                | December 2018 - February 2019 |
| Model evaluation and analysis                 | March - April 2019         |
| Thesis writing and revisions                  | May - July 2019            |

### Budget

| Item                                         | Cost                   |
|----------------------------------------------|------------------------|
| Equipment (GPU, computer, etc.)              | $5,000                 |
| Participant compensation (25 speakers)       | $2,500                 |
| Travel and conference expenses               | $2,000                 |
| Software and licensing fees                  | $1,500                 |
| Thesis printing and binding                   | $500                   |
| Total Budget                                  | $11,500                |

Note: The budget is an estimate and subject to change based on unforeseen circumstances.


## Conclusion

In this proposed research, we aim to investigate the effectiveness of CapsNets for machine lipreading, and compare its performance against traditional models used in the field. We expect that CapsNets will provide a more accurate and robust solution for visual speech recognition, especially in challenging scenarios where lighting, orientation, and occlusion vary.

Our research has the potential to contribute to the development of more accurate and reliable lipreading systems, and potentially improve communication and quality of life for individuals with hearing impairments. It also has the potential to inspire future interdisciplinary research projects that address the complex challenges of speech perception and production.

With a timeline of 12 months and a budget of $11,500, we believe that this research is feasible and worthwhile. We look forward to conducting this research and contributing to the advancement of the field of visual speech recognition.


## References

1. Hinton, G. E., & Salakhutdinov, R. R. (2006). Reducing the dimensionality of data with neural networks. Science, 313(5786), 504-507.

2. Sabour, S., Frosst, N., & Hinton, G. E. (2017). Dynamic routing between capsules. In Advances in neural information processing systems (pp. 3856-3866).

3. Petridis, S., Stavropoulos, T. G., & Pantic, M. (2018). End-to-end visual speech recognition with spatiotemporal convolutional neural networks. IEEE Transactions on Multimedia, 20(6), 1346-1358.

4. Garg, S., & Sharma, G. (2018). Lip-reading with a deep neural network. In 2018 25th IEEE International Conference on Image Processing (ICIP) (pp. 1-5). IEEE.

5. Assael, Y. M., Shillingford, B., Whiteson, S., & de Freitas, N. (2016). LipNet: End-to-end sentence-level lipreading. arXiv preprint arXiv:1611.01599.

6. Chung, J. S., & Zisserman, A. (2016). Out of time: automated lip sync in the wild. In Asian conference on computer vision (pp. 251-263). Springer, Cham.

