# Import streamlit library for web app creation
import streamlit as st

# Set the title of the web app
st.title("🧮 Simple Calculator")

def main():
    # Display instruction message
    st.write("✨ Enter two numbers and choose an operation")

    # Create two columns for layout
    col1, col2 = st.columns(2)

    with col1:
        # Input field for first number
        num1 = st.number_input("🔢 Enter first number", value=0.0)

    with col2:        
        # Input field for second number
        num2 = st.number_input("🔢 Enter second number", value=0.0)    

        # Dropdown to select math operation
    operation = st.selectbox("⚡ Choose Operation", ["+", "-", "x", "/"])
        
        # Calculate button and logic
    if st.button("📊 Calculate"):
            try:
                # Addition operation
                if operation == "+":
                    result = num1 + num2
                    symbol = "+"
                    
                # Subtraction operation
                elif operation == "-":
                    result = num1 - num2
                    symbol = "-"

                # Multiplication operation
                elif operation == "x":
                    result = num1 * num2
                    symbol = "x"

                # Division operation
                else:
                    # Check for division by zero
                    if num2 == 0:
                        st.error("❌ ERROR: Division by 0")
                        return
                    result = num1 / num2
                    symbol = "/"

                # Display result
                st.success(f"✅ {num1} {symbol} {num2} = {result}")

            # Handle any errors that occur
            except Exception as e:
                st.error(f"❌ An error occurred: {str(e)}") 

# Run main function when script is executed
if __name__ == "__main__":
    main()
