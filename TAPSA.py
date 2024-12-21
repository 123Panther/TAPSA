import streamlit as st
from PIL import Image
import base64
import pandas as pd
import numpy as np
import altair as alt

# Set up the primary page configuration
st.set_page_config(page_title='TAPSA MUHAS', layout='wide')


# Load background image for the first page
def set_background(image_path):
    with open(image_path, "rb") as image_file:
        image = image_file.read()
    bin_str = "data:image/jpeg;base64," + base64.b64encode(image).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{bin_str}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


# Custom CSS to style the Streamlit app
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .sidebar .sidebar-content {
        background-image: linear-gradient(#2e7bcf,#2e7bcf);
        color: white;
    }
    h1 {
        color: #2e7bcf;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Define navigation
pages = ['Home', 'Profile', 'Dashboard', 'Registration', 'TAPSA FEE', 'Updates', 'Documents']
if 'page' not in st.session_state:
    st.session_state['page'] = 'Home'

page = st.sidebar.selectbox('Navigation', pages, index=pages.index(st.session_state['page']))

# Sidebar Title
st.sidebar.title("Navigation")

# Home Page
if page == 'Home':
    set_background('C:\\Users\\OGARE\\PycharmProjects\\TAPSAMUHAS\\students.jpg')  # Updated with your image path
    st.markdown("<h1 style='text-align: center; color: #00072d;'>Welcome to Your Website</h1>", unsafe_allow_html=True)
    st.write("This website is designed to provide an interactive and user-friendly experience.")

    # Creating space between the title and the buttons
    st.markdown("<br><br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        if st.button('Profile'):
            st.session_state['page'] = 'Profile'


    with col2:
        if st.button('Dashboard'):
            st.session_state['page'] = 'Dashboard'


    with col3:
        if st.button('Registration'):
            st.session_state['page'] = 'Registration'


    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        if st.button('TAPSA FEE'):
            st.session_state['page'] = 'TAPSA FEE'


    with col2:
        if st.button('Updates'):
            st.session_state['page'] = 'Updates'


    with col3:
        if st.button('Documents'):
            st.session_state['page'] = 'Documents'


# Profile Page
if page == 'Profile':
    st.title('Profile')
    st.write('User profile information goes here.')
    # Additional fields
    age = st.number_input('Age', min_value=18, max_value=100, value=25)
    bio = st.text_area('Bio', 'Enter a brief biography here...')
    if st.button('Save'):
        st.success('Profile updated!')

# Dashboard Page
if page == 'Dashboard':
    st.title('Dashboard')
    st.write('Dashboard contents go here.')

    # Sample data for visualization
    data = pd.DataFrame(
        np.random.randn(1000, 3),
        columns=['a', 'b', 'c']
    )

    chart = alt.Chart(data).mark_circle().encode(
        x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
    ).interactive()

    st.altair_chart(chart, use_container_width=True)

# Registration Page
if page == 'Registration':
    st.title('Registration')
    st.write("Please fill in the registration form below:")

    with st.form(key='registration_form'):
        name = st.text_input('Name')
        email = st.text_input('Email')
        password = st.text_input('Password', type='password')
        confirm_password = st.text_input('Confirm Password', type='password')
        year_of_study = st.selectbox('Year of Study', [1, 2, 3, 4])

        # Check if the passwords match
        if password and confirm_password and password != confirm_password:
            st.error("Passwords do not match")
        else:
            submit_button = st.form_submit_button(label='Register')
            if submit_button:
                st.success(f'Registration Successful: {name}, {email}, Year {year_of_study}')

# Enhanced TAPSA FEE Page
if page == 'TAPSA FEE':
    st.title('TAPSA FEE')
    st.subheader('Payment Information')

    st.write("""
    The TAPSA FEE is mandatory for all students and supports various activities and resources.
    Below you'll find the details on how to make your payment, deadlines, and other important information.
    """)

    st.markdown("""
    **Payment Methods:**
    - **Bank Transfer**: Transfer the fee to the following bank account:
        - Account Name: TAPSA
        - Bank: National Bank of Tanzania
        - Account Number: 123456789
        - SWIFT Code: NBTZTZT
    - **Mobile Payment**: Pay via mobile money services:
        - M-Pesa: Dial *150*00#, Enter Business Number 12345, Account Number TAPSA Fee
        - Mix by Yas: Dial *150*01#, Enter Business Number 54321, Account Number TAPSA Fee
    - **In-Person Payment**: Visit the TAPSA officers, stationary on campus and pay directly.
    """)

    st.markdown("""
    **Deadlines:**
    - Semester 1: 31st January 2024
    - Semester 2: 30th June 2024
    """)

    st.markdown("""
    **Contact Information:**
    For any queries regarding the TAPSA Fee, please contact:
    - Email: tapsamuhas2019@gmail.com
    - Phone: +255 695 509 587
    - Office Hours: Monday to Friday, 9 AM - 5 PM
    """)

    st.subheader('Payment Confirmation')
    st.write("After making the payment, please fill in the following form to confirm your payment:")

    with st.form(key='payment_confirmation_form'):
        name = st.text_input('Full Name')
        email = st.text_input('Email')
        payment_method = st.selectbox('Payment Method', ['Bank Transfer', 'Mobile Payment', 'In-Person'])
        transaction_id = st.text_input('Transaction ID')
        upload_receipt = st.file_uploader('Upload Payment Receipt', type=['jpg', 'jpeg', 'png', 'pdf'])
        submit_button = st.form_submit_button(label='Confirm Payment')

        if submit_button:
            st.success('Payment Confirmation Received. Thank you!')

    st.subheader('Fee Breakdown')
    st.write("Here's a breakdown of how the TAPSA Fee is utilized:")

    st.markdown("""
    - **Academic Support**: 40%
    - **Extracurricular Activities**: 30%
    - **Student Welfare**: 20%
    - **Administrative Costs**: 10%
    """)

    st.write("For more detailed information, visit our [official TAPSA website](https://www.tapsa-university.edu).")

# Updates Page
if page == 'Updates':
    st.title('Updates')
    st.write('Latest updates in rows go here.')
    # Example updates
    updates = [
        "Update 1: Important notice regarding exams.",
        "Update 2: New research articles added to the library.",
        "Update 3: Upcoming events and seminars.",
        "Update 4: Changes in the academic calendar.",
        "Update 5: New courses available next semester."
    ]
    for update in updates:
        st.write(update)

# Documents Page
if page == 'Documents':
    st.title('Documents')
    st.write('Documents related to pharmacy and articles go here.')
    documents = [
        "Pharmacy Guidelines 2024",
        "Research Articles on Clinical Trials",
        "Pharmaceutical Case Studies",
        "Medicine Safety Reports",
        "New Drug Approvals"
    ]
    for doc in documents:
        st.write(f"- {doc}")
    if st.button('View Documents'):
        st.write('Documents content will be displayed here.')

# Add a dashboard icon to the sidebar (left top corner)
st.sidebar.markdown("<h2 style='color: #00072d;'>Dashboard</h2>", unsafe_allow_html=True)
