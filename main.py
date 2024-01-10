import streamlit as st
from generate_csv import generate_csv
from linear_regression import linear_model, inference


# Generate the CSV file
generate_csv('data.csv', 10000)


# Model definition 
model = linear_model()


def main():
    """
    Main function to run the House Price Prediction application.
    """
    # Create the Streamlit interface
    st.title("House Price Prediction")
    
    # Input fields
    bedrooms = st.number_input("Bedrooms", value=1, min_value=1, max_value=5, step=1)
    floor = st.number_input("Floor", value=1, min_value=1, max_value=20, step=1)
    neighborhood = st.number_input("Neighborhood", value=1, min_value=1, max_value=50, step=1)
    
    if st.button("Calculate"):
        # Calculate the number
        prediction = inference(model, bedrooms, floor, neighborhood)
        formatted_prediction = "{:,.2f}".format(prediction[0])
        st.write(f"House with {bedrooms} bedrooms, on floor {floor} in neighborhood {neighborhood} is worth:")
        st.success(f"Predicted price:  ${formatted_prediction}")
        
if __name__ == "__main__":
    main()
