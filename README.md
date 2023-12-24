# Diamond Price Prediction Project

## Overview 

This repository contains the code and resources for a data science project focused on predicting diamond prices. The goal of this project is to develop a machine learning model that can accurately predict the price of diamonds based on various features.

## Project Structure

The project is organized into the following directories:

- **data:** Contains the dataset used for training and testing the model.
  
- **notebooks:** Jupyter notebooks that document the various stages of the data science pipeline, including data exploration, preprocessing, feature engineering, model training, and evaluation.

- **src:** Source code for the machine learning model and any custom functions or utilities used in the project.

- **models:** Saved model files or checkpoints generated during the training process.

- **reports:** Reports or documentation related to the project, such as the final analysis report or presentation slides.

## Getting Started

1. **Clone the Repository:**
   ```
   git clone https://github.com/praj2408/diamond-price-prediction.git
   cd diamond-price-prediction
   ```

2. **Install Dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Download the Dataset:**
   - The dataset is available in the `data` directory. If needed, replace it with your own dataset.

4. **Explore the Notebooks:**
   - The `notebooks` directory contains Jupyter notebooks that guide you through the different steps of the project. Start with `1_data_exploration.ipynb` and follow the numerical order.

5. **Run the Model:**
   - Once you've gone through the notebooks and are ready to train the model, use the code in the `src` directory. Adjust hyperparameters as needed.

6. **Evaluate the Model:**
   - After training, use the evaluation notebooks to assess the model's performance and fine-tune as necessary.

## Dependencies

- Python 3.x
- Jupyter Notebooks
- pandas
- NumPy
- scikit-learn
- matplotlib
- seaborn

Install these dependencies using the provided `requirements.txt` file.

## Model

The machine learning model used in this project is a Linear Regression. The model is trained on the provided dataset and can be fine-tuned based on your specific requirements.

## Results
Linear Regression with 93.7% r2 score

## Contributing

If you'd like to contribute to this project, please follow the standard GitHub workflow:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make changes and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

Feel free to reach out with any questions or suggestions!
