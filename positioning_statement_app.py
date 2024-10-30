import streamlit as st

# Title and introduction
st.title("Positioning Statement Generator")
st.write("Use this tool to create a positioning statement for your brand. Choose your focus and fill in the details to get a customized positioning statement.")

# Choose between two positioning focuses
focus = st.selectbox(
    "Select your focus:",
    ["Compare to Competitors", "Focus on Customers"]
)

# Inputs for "Compare to Competitors" positioning statement
if focus == "Compare to Competitors":
    st.header("Positioning Statement: Comparing to Competitors")
    
    target_customer = st.text_input("Target Customer/Audience")
    need = st.text_input("Audience Need")
    product_name = st.text_input("Product/Service Name")
    product_category = st.text_input("Define Product Category")
    solution = st.text_input("How does your product solve the customer’s need?")
    competitor = st.text_input("Competitor Name")
    difference = st.text_input("How is your product different from the competition?")

    # Generate positioning statement
    if st.button("Generate Positioning Statement"):
        positioning_statement = (f"For {target_customer} that need {need}, {product_name} is a {product_category} that {solution}. "
                                 f"Unlike {competitor}, our product {difference}.")
        st.subheader("Your Positioning Statement:")
        st.write(positioning_statement)

# Inputs for "Focus on Customers" positioning statement
elif focus == "Focus on Customers":
    st.header("Positioning Statement: Focusing on Customers")
    
    target_customer = st.text_input("Target Customer/Audience")
    product_name = st.text_input("Product/Service Name")
    product_category = st.text_input("Define Product Category")
    problem = st.text_input("Problem your product solves for your customer")
    benefit = st.text_input("Benefit your product brings to your customer")

    # Generate positioning statement
    if st.button("Generate Positioning Statement"):
        positioning_statement = (f"For {target_customer}, {product_name} is the {product_category} that will {problem} "
                                 f"so they can {benefit}.")
        st.subheader("Your Positioning Statement:")
        st.write(positioning_statement)

# Instructions for use
st.write("Fill in each section and click 'Generate Positioning Statement' to see your result.")
