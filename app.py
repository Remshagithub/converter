import streamlit as st

def convert_units(value, from_unit, to_unit, unit_type):
    if unit_type == "Length":
        conversion_factors = {
            "Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Inch": 39.3701, "Foot": 3.28084, "Yard": 1.09361
        }
    elif unit_type == "Weight":
        conversion_factors = {
            "Kilogram": 1, "Gram": 1000, "Milligram": 1e6, "Pound": 2.20462, "Ounce": 35.274
        }
    elif unit_type == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        else:
            return value  # No conversion needed
        
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

# Streamlit UI 🖥
st.title("🔄 Unit Converter")
unit_type = st.selectbox("Choose unit type 🏷", ["Length", "Weight", "Temperature"])

if unit_type == "Length":
    units = ["Meter", "Kilometer", "Centimeter", "Millimeter", "Inch", "Foot", "Yard"]
elif unit_type == "Weight":
    units = ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"]
elif unit_type == "Temperature":
    units = ["Celsius", "Fahrenheit"]

value = st.number_input("Enter value 🔢", min_value=0.0, format="%.2f")
from_unit = st.selectbox("From Unit 🏁", units)
to_unit = st.selectbox("To Unit 🎯", units)

if st.button("Convert ⚡"):
    result = convert_units(value, from_unit, to_unit, unit_type)
    st.success(f"🎉 Converted Value: {result:.2f} {to_unit}")