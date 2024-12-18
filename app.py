import streamlit as st
import pickle
import numpy as np

# Load the model
model = pickle.load(open('fertilizer_type_model.pkl', 'rb'))

# Title of the app
st.title('Fertilizer Type Prediction')

# Inputs for the model
soil_color = st.selectbox('Soil Color', [0, 1])  # Example: Use 0 or 1 for soil color
nitrogen = st.number_input('Nitrogen', min_value=0.0, step=0.1)
phosphorus = st.number_input('Phosphorus', min_value=0.0, step=0.1)
potassium = st.number_input('Potassium', min_value=0.0, step=0.1)
ph = st.number_input('pH', min_value=0.0, step=0.1)
rainfall = st.number_input('Rainfall', min_value=0.0, step=0.1)
temperature = st.number_input('Temperature', min_value=0.0, step=0.1)
crop = st.selectbox('Crop', [0, 1, 2, 3])  # Modify crop options as needed

# When the user clicks the 'Predict' button
if st.button('Predict'):
    try:
        # Create input array for prediction
        features = np.array([[soil_color, nitrogen, phosphorus, potassium, 
                             ph, rainfall, temperature, crop]])
        
        numpy=features.
        prediction = model.predict(features)[0]

        # Map prediction to fertilizer type
        fertilizer_types = {
            0: 'NPK-10:10:10',
            1: 'NPK-10:26:26',
            2: 'NPK-12:32:16',
            3: 'NPK-13:32:26',
            4: 'NPK-18:46:0',
            5: 'NPK-19:19:19',
            6: 'NPK-20:20:20',
            7: 'NPK-50:26:26',
            8: 'Ammonium Sulphate',
            9: 'Chelated Micronutrient',
            10: 'DAP',
            11: 'Ferrous Sulphate',
            12: 'Hydrated Lime',
            13: 'MOP',
            14: 'Magnesium Sulphate',
            15: 'SSP',
            16: 'Sulphur',
            17: 'Urea',
            18: 'White Potash'
        }

        result = fertilizer_types.get(prediction, 'Unknown Fertilizer Type')
        
        # Display the result
        st.success(f'Recommended Fertilizer: {result}')
        
    except Exception as e:
        st.error(f'Error in prediction: {str(e)}')
