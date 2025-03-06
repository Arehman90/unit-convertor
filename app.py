import streamlit as st

st.title("🌏 Unit Converter App")
st.markdown("### Converts Length, Weight, and Time Instantly")
st.write("Welcome! Select a category, enter a value, and get the result in real-time.")

# Category selection
category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

# Function to convert units
def convert_units(category, value, from_unit, to_unit):
    if category == "Length":
        if from_unit == "Kilometers" and to_unit == "Miles":
            return value * 0.621371
        elif from_unit == "Miles" and to_unit == "Kilometers":
            return value / 0.621371

    elif category == "Weight":
        if from_unit == "Kilograms" and to_unit == "Pounds":
            return value * 2.20462
        elif from_unit == "Pounds" and to_unit == "Kilograms":
            return value / 2.20462

    elif category == "Time":
        if from_unit == "Seconds" and to_unit == "Minutes":
            return value / 60
        elif from_unit == "Minutes" and to_unit == "Seconds":
            return value * 60
        elif from_unit == "Minutes" and to_unit == "Hours":
            return value / 60
        elif from_unit == "Hours" and to_unit == "Minutes":
            return value * 60
        elif from_unit == "Hours" and to_unit == "Days":
            return value / 24
        elif from_unit == "Days" and to_unit == "Hours":
            return value * 24

    return 0  # Default return value

# Unit selection based on category
if category == "Length":
    units = ["Kilometers", "Miles"]
elif category == "Weight":
    units = ["Kilograms", "Pounds"]
elif category == "Time":
    units = ["Seconds", "Minutes", "Hours", "Days"]

# Layout for unit selection
col1, col2, col3 = st.columns([2, 1, 2])

with col1:
    from_unit = st.selectbox("From", units)

with col2:
    st.write("=")  # Display "=" in the middle

with col3:
    to_unit = st.selectbox("To", units)

# Value input
value = st.number_input("Enter the value to convert")

# Convert button
if st.button("Convert"):
    result = convert_units(category, value, from_unit, to_unit)
    st.success(f"The result is {result:.6f}")