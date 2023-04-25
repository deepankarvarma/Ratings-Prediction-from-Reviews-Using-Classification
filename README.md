# Rating Review Classification Using CNN
## Rank 1 (Adshed) in Kaggle Wars hosted by ACM Thapar.
### Kaggle Competition Link :- https://www.kaggle.com/competitions/kaggle-wars-eclipse
This repository contains the code for a multiclass classification model that predicts the rating of a review based on its text content. The model was built using Python, Keras and Tensorflow.<br>
### Dataset
The dataset used in this project was obtained from the Kaggle Wars competition hosted by ACM Thapar. The original dataset contained reviews and their corresponding ratings ranging from 1 to 5 stars. The dataset was preprocessed to remove noise, including punctuations, emojis, numbers and stop words. The words were also lemmatized and stemmed to normalize the text. The preprocessed dataset was split into training and testing datasets.<br>
### Model Architecture
The model used for this project is a convolutional neural network (CNN). The CNN model consisted of an embedding layer, two convolutional layers, two max-pooling layers, and two dense layers. The embedding layer was used to convert text inputs into numerical embeddings. The convolutional layers were used to learn relevant features from the text data. The max-pooling layers were used to downsample the output of the convolutional layers. Finally, the dense layers were used to produce the output predictions.<br>
### Results
The CNN model achieved an accuracy of 97.21% on the training dataset and an accuracy of 96.68% on the testing dataset. The model was able to accurately predict the rating of the reviews based on their text content.<br>
### Usage
To use this code, follow these steps:
<br>
1. Clone the repository<br>

2. Install the required dependencies using `pip install -r requirements.txt`<br>

3. Download the `train (1).csv` and `test (2).csv` files. <br>
4. Run the `.ipynb` file cell by cell file to evaluate the model on the testing dataset and generate the classification report.<br>
### Conclusion
The CNN model was able to effectively classify the reviews into their respective ratings with high accuracy. The model can be useful in sentiment analysis applications, where the goal is to determine the sentiment of a text input.
