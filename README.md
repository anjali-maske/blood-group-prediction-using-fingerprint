# blood-group-prediction-using-fingerprint

###  Project Overview
This project introduces a non-invasive approach to blood group prediction using fingerprint image processing and machine learning. By leveraging Convolutional Neural Networks (CNNs), it classifies fingerprint patterns into eight common blood groups (A+, A-, B+, B-, AB+, AB-, O+, O-), offering a quick and accessible alternative to traditional methods.  

![Screenshot 2025-03-05 001626](https://github.com/user-attachments/assets/486dad12-1b91-434b-963e-1f97e7acbb46)

### Objectives
-Rapid Blood Group Identification – Provides a fast and accurate alternative to traditional methods.

-Accessibility in Remote Areas – Enables blood group prediction without lab facilities or skilled personnel.

-Integration with Portable Devices – Supports point-of-care diagnostics in clinics and mobile units.

-Safety and Scalability – Reduces contamination risks and ensures adaptability across healthcare settings.

-Biometric and Medical Synergy – Combines biometrics and machine learning for improved diagnostics.
  
### Tech Stack
#### Frontend: 
- HTML, CSS, JavaScript
#### Backend: 
- Flask, SQLAlchemy, SQLite
#### Machine Learning (Model Development): 
- TensorFlow/Keras,  Google Colab

### Model Performance
| Model                                | Testing Accuracy | Validation Accuracy |
|--------------------------------------|-----------------|---------------------|
| VGG16                                | 88.72%          | 89.50%              | 
| AlexNet                              | 12.47%          | 12.49%              | 
| ResNet50                             | 61.19%          | 62.70%              |
| Hybrid Model (EfficientNetB0 + SVM)  | 22.29%          | 22.81%              

### Dataset 
[Fingerprint-dataset](https://www.kaggle.com/datasets/rajumavinmar/finger-print-based-blood-group-dataset) 

![Screenshot 2025-03-05 002114](https://github.com/user-attachments/assets/764ddf3e-9f88-4734-802e-0e8d0f25f58d)

### Screenshots
#### Signup Page
![Screenshot (278)](https://github.com/user-attachments/assets/f716115e-7875-4c65-b9cc-943c3faeb4cc)
![log_in](https://github.com/user-attachments/assets/0344bdc4-cc05-4b28-889f-12fc61970dcf)

#### Predicting Result Page
![Screenshot 2025-03-05 223335](https://github.com/user-attachments/assets/b5701d15-8837-46b8-aa13-c200625b0d35)
![Screenshot 2025-03-05 223538](https://github.com/user-attachments/assets/40453f3f-d631-424b-82df-258843e445d8)
![Screenshot 2025-03-05 223633](https://github.com/user-attachments/assets/63c77e96-f082-4c9c-9f53-02cf3b76cd3b)

###  Future Improvements
- Expand the dataset for better generalization.
- Experiment with other models for further accuracy improvements.
- Deploy model in live environment

### Contact 
#### Anjali Maske  
Email: [aamaske50@gmail.com](mailto:aamaske50@gmail.com)  
[LinkedIn](https://www.linkedin.com/in/anjali-maske/)
