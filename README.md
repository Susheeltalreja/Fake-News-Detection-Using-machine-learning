
# Fake News Detection Using Machine Learning

A Python-based project for detecting fake news using advanced machine learning techniques and natural language processing (NLP). This repository demonstrates a comprehensive approach to text preprocessing, model training, and evaluation, providing accurate predictions for fake and real news articles.

---

## Features

- **Data Cleaning**: Optimized preprocessing using text cleaning functions.
- **Model Training**: Trained with Logistic Regression, Decision Tree, Random Forest, and Gradient Boosting.
- **Evaluation**: Models evaluated with precision, recall, F1-score, and accuracy.
- **User Interaction**: Input a news article and test its authenticity against trained models.
- **Confidence Check**: Validates predictions based on model confidence levels.

---

## Requirements

Install the required Python libraries using:
```bash
pip install -r requirements.txt
```
Required libraries include:
- `pandas`
- `numpy`
- `seaborn`
- `matplotlib`
- `scikit-learn`

---

## Dataset

The project uses the following datasets for training and testing:
- **Fake.csv**: Contains fake news samples.
- **True.csv**: Contains real news samples.

---

## How It Works

1. **Data Preprocessing**: 
   - Cleans and reshuffles the data.
   - Removes unnecessary columns like `title`, `subject`, and `date`.

2. **Feature Extraction**: 
   - Converts text data into numerical features using TF-IDF Vectorizer.

3. **Model Training**: 
   - Trains and evaluates the following models:
     - Logistic Regression
     - Decision Tree Classifier
     - Random Forest Classifier
     - Gradient Boosting Classifier

4. **Manual Testing**: 
   - Input your news and verify its authenticity with the trained models.

---

## Usage

Run the following command to start the application:
```bash
python app.py
```
### Manual Testing:
- Enter a news article in the prompt.
- Models will predict if the news is **Fake** or **Real**.

---

## Example

```text
Put your news here! 
"The government announces new reforms in education."
✅ LR Prediction: It is a true news 
✅ DTC Prediction: It is a true news 
✅ RFC Prediction: It is a true news 
✅ GBC Prediction: It is a true news
```

---

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

Special thanks to the open-source community and the creators of the libraries used in this project.
