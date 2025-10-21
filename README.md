# Crop Prediction And Disease Classification 🌿

A Streamlit web app that predicts the most suitable crop based on soil and weather parameters and classifies plant diseases from uploaded images using machine learning and deep learning models.

## MOTIVATION 💪

Agriculture is a vital sector for any country's economy. By integrating technology, we can help farmers make more informed decisions, increasing their efficiency and yield. This project aims to provide a simple, accessible tool for farmers to get recommendations on crop selection and identify potential plant diseases early, helping to secure better harvests.

This application implements two main features:
1.  **Crop Recommendation:** Users can input soil and weather data (like N, P, K, pH, temperature, humidity, and rainfall) to get a prediction for the most suitable crop to grow.
2.  **Plant Disease Classification:** Users can upload an image of a plant leaf, and the application will identify the disease, helping them take appropriate action.

## DATA SOURCE 📊

The datasets used for training the models are located within the repository:
* **Crop Recommendation Dataset:** Found in the `/data` directory.
* **Disease Classification Dataset:** The image dataset used for training is located in the `/data` directory.

## Notebooks 📓

All experimentation, model training, and data analysis were performed in Jupyter Notebooks, which are available in the `/notebooks` directory.

* **Crop Prediction Model:** [View Notebook](/notebooks/crop_prediction.ipynb)
* **Disease Classification Model:** [View Notebook](/notebooks/disease_classification.ipynb)

*(Note: Please update the notebook filenames above to match your repository)*

## Built with 🛠️

* **[Streamlit](https://streamlit.io/)** - For building the interactive web application.
* **[Scikit-learn](https://scikit-learn.org/stable/)** - For the Crop Prediction (Machine Learning) model.
* **[TensorFlow](https://www.tensorflow.org/) & [Keras](https://keras.io/)** - For the Disease Classification (Deep Learning) model (MobileNetV2/CNN).
* **[Pandas](https://pandas.pydata.org/)** - For data manipulation and analysis.
* **[NumPy](https://numpy.org/)** - For numerical operations.

## How to use 💻

1.  **Crop Recommendation System:**
    * Navigate to the "Crop Prediction" page.
    * Enter the values for Nitrogen (N), Phosphorous (P), Potassium (K), soil pH, temperature, humidity, and rainfall.
    * Click "Predict" to see the recommended crop.

2.  **Disease Detection System:**
    * Navigate to the "Disease Classification" page.
    * Upload an image of a plant leaf (e.g., from the `/test_images` folder).
    * The algorithm will analyze the image and display the predicted disease name and confidence.

## How to run locally 🛠️

Before following these steps, make sure you have Git and Python (3.8+) installed on your system.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/swarnabhaghosh/Crop-Prediction-And-Disease-Classification.git](https://github.com/swarnabhaghosh/Crop-Prediction-And-Disease-Classification.git)
    cd Crop-Prediction-And-Disease-Classification
    ```

2.  **Create and activate a virtual environment (Recommended):**
    ```bash
    # For Unix/Mac
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit app:**
    *(Assuming your main app file is `app.py` inside the `app` folder)*
    ```bash
    streamlit run app/app.py
    ```
    Open the local URL (e.g., `http://localhost:8501`) provided in your terminal to use the project locally.

## DEMO

Check out the live demo of the application:
**[https://plantiq.streamlit.app/](https://plantiq.streamlit.app/)**

![Crop Recommendation](demo\crop_recommendation_demo.png "Crop Suggestion Output")
![Crop Recommendation](demo\disease_classification_demo.png "Disease Classification Output")


## Contribute 👨‍💻

Contributions are welcome! Please read `CONTRIBUTING.md` (if available) for details on the code of conduct and the process for submitting pull requests.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/NewFeature`)
3.  Commit your Changes (`git commit -m 'Add some NewFeature'`)
4.  Push to the Branch (`git push origin feature/NewFeature`)
5.  Open a Pull Request

## Usage ⚙️

You can use this project for educational purposes, to build upon it, or to integrate it into a larger agricultural platform. If you use this project in your work, please kindly provide attribution by mentioning the original source and linking to this repository.

## Further Improvements 📈

* Add a "Remedies" section for the classified plant disease.
* Integrate a real-time weather API for the crop prediction feature.
* Expand the disease classification model to support a wider variety of plants and diseases.
* Improve the UI/UX of the Streamlit application.

## License 📝

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## Contact 📞

Swarnabha Ghosh - [swarnabhaghosh@example.com](mailto:swarnabhaghosh@example.com) - [LinkedIn](https://www.linkedin.com/in/your-profile)

Project Link: [https://github.com/swarnabhaghosh/Crop-Prediction-And-Disease-Classification](https://github.com/swarnabhaghosh/Crop-Prediction-And-Disease-Classification)

*(Please update the contact details above)*
