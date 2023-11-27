
import streamlit as st
from joblib import load
import pandas as pd
import os 

def get_car_image_path(car_model):
    # Assuming the base directory 'photos' is in the current working directory
    base_dir = 'photos'
    
    # Construct the path to the car's folder
    car_folder_path = os.path.join(base_dir, car_model)
    
    # Assuming there is only one image per folder and its extension is known
    # This will list all files in the directory
    try:
        for file in os.listdir(car_folder_path):
            if file.endswith(('.png', '.jpg', '.jpeg','webp')):
                return os.path.join(car_folder_path, file)
    except FileNotFoundError:
        return f"No directory found for {car_model}."

# Example usage:

st.set_page_config(page_title= "AutoScout Platform",page_icon='icon.png')

df = pd.read_csv('Ready_to_ML.csv')
# Load the pre-trained Ridge model
ridge_model_loaded = load('majed_model.joblib')
st.markdown("""
        <style>
            .main_container {
                background-color: #FFFFFF;
            }

            h1 {
                text-align: center;
                color: #FF3131;
            }
            h2{
                text-align: center;
            }
            .sidebar .sidebar-content {
                background-color: #F2F2F2;
            }
            
            .sidebar .sidebar-button{
                 color: #ffffff;
                background-color: #FF3131;
                border: none;
                border-radius: 4px;
                padding: 0.75rem 1.5rem;
                margin: 0.75rem 0;
                position: absolute;
                left: 10% ;
            }
            
            .stButton>button {
                color: #ffffff;
                background-color: #FF3131;
                border: none;
                border-radius: 4px;
                padding: 0.75rem 1.5rem;
                margin: 0.75rem 0;
                position: absolute;
                left:40%;

            }
            .stButton>button:hover {
                background-color:  #FF4B4B;
                text-align: center;
                color: #FFFFFF;
            }
           
            
          
            body {
            background-color: #F2F2F22;}
        </style>
    """, unsafe_allow_html=True)

if 'submitted' not in st.session_state:
    st.session_state['submitted'] = False
    

# Define the welcome page form
if not st.session_state['submitted']:
    
        # st.write("Welcome to Eng.Majed AutoMobile Shop! Please submit to continue.")
        col1,col2,col3 = st.columns([0.2,0.4,0.2])
        col2.image("Auto Scout.jpg",width=300,)
        st.markdown("----", unsafe_allow_html=True)
        st.subheader("Welcome to..")
        st.title('AutoScout Car Prices Platform')
        st.subheader("The PERFECT place to find car prices with the touch of machine learning")
        st.markdown("----", unsafe_allow_html=True)
        submitted = st.button("Let's GO")

        # Form fields go here
        # ...Nsooooooooo here please

        # Submit button for the form
        
        if submitted:
            st.session_state['submitted'] = True
            st.experimental_rerun()  # Rerun the app to update the state

# Define your tabs
if st.session_state['submitted']:
    tab1, tab2,tab3 = st.tabs(["Predict", "Details","Authors :sunglasses:"])
    
    with tab3:
        st.markdown("""


## Authors
- **Majed** - [Majed's Profile](https://www.linkedin.com/in/majed-alshnifi/)
- **Intesar** - [Intesar's Profile](https://www.linkedin.com/in/intesar-hejazy/)



As co-developers, Majed and Intesar have both contributed to every aspect of the AutoScout Car Price Prediction Platform. Their collaboration spans across the entire development lifecycle of the project, including:

- Conceptualization and design of the application's architecture.
- Data analysis and preprocessing to prepare the dataset for machine learning.
- Training, evaluation, and integration of the Ridge regression model.
- Development of the Streamlit interface to ensure a user-friendly experience.
- Implementation of the database and image scraping functionalities.
- Rigorous testing and refinement to optimize the application's performance.

Their partnership has been a cornerstone of the project's success, embodying a shared vision for creating a powerful and intuitive tool for car price prediction.

---

We encourage you to explore their profiles for more information about their professional experience and other collaborative ventures.

                    """)
    


    
    with tab2:
        
        
        st.markdown("""
                   # AutoScout Car Price Prediction Platform
## Let's tell you how we made this  :star:masterpiece:star:
## Overview
The AutoScout Car Price Prediction Platform is an advanced web application built on the Streamlit framework that offers users a seamless experience in estimating car prices. By harnessing the power of machine learning through a pre-trained Ridge regression model, the platform provides accurate price predictions based on a comprehensive set of car features. With a robust back-end that connects to a `.csv` database and an image scraping module, the application presents both visual and data-driven insights into car valuation.

## Features

### User Interface
- **Interactive Forms**: The application includes forms that allow users to input various car features. These inputs are then used to predict prices.
- **Tabbed Navigation**: Users can navigate between different sections of the app, including a welcome tab and a prediction tab, for organized interactions.

### Machine Learning Integration
- **Ridge Regression Model**: The core of our prediction capability, providing reliable price estimates.
- **Model Training**: The model is trained on a rich dataset that captures the nuances of the automotive market.

### Image Display
- **Data Scraping**: A built-in functionality to scrape and display images corresponding to the user’s car selection.
- **Visual Feedback**: Enhances the user experience by providing visual confirmation of the car being queried.

### Database Connectivity
- **Automated Feature Extraction**: Direct connectivity to a `.csv` file allows the app to pull relevant features like horsepower, engine size, etc.
- **Data-Driven Predictions**: Ensures that the user is not burdened with inputting technical details that can be fetched from the database.

## Model Details
- **Algorithm**: Ridge Regression, chosen for its effectiveness in handling multicollinearity in data.
- **Model Performance**: Evaluated using standard metrics such as R-squared, RMSE, etc., to ensure accuracy.

## Data Source
The application relies on a `.csv` database that contains detailed information about various car models and their associated features. This database is pivotal in enabling the model to make precise predictions.

## Usage Instructions
Follow these steps for a typical user journey through the app:

1. **Welcome Tab**: Users are greeted and provided with introductory information about the platform.
2. **Selecting Car Features**: Users can specify the car's make and model, mileage, seller type, among other attributes.
3. **Price Prediction**: After the features are submitted, the platform calculates and displays the estimated price along with a relevant car image.

## Setup and Installation
To run the application on your local environment, please follow these steps:

1. Clone the project repository from GitHub to your local machine.
2. Navigate to the project directory and install dependencies via `pip install -r requirements.txt`.
3. Launch the application using `streamlit run app.py` in your terminal.

## How to Contribute
We encourage contributions that can help enhance the application's functionality or user experience. Please adhere to the following process:

1. Fork the repository to your GitHub account.
2. Create a new branch for your feature or bug fix.
3. Develop your feature and push the changes to your fork.
4. Open a pull request for discussion and review.

## License
This project falls under the MI (Majed and Intesar) :clown_face: License. Refer to the `CallME.md` file in the project's repository for full details.

## Acknowledgments
We would like to thank ourselves for our great HARD work and our own emotional, mental :otter:, financial, and physical support

## _________________________________________
###### All rights reserved to MIClown:clown_face:.Inc
 
                    """)
        
        

    # Prediction tab content

    with tab1:
            
        # Set page title and background color

        # Define the main title and description
        st.title('Car Price Prediction')
        st.header('The prediction will be shown here :magic_wand:')
        user_data = {}

        # Create a sidebar for additional information (optional)
        st.sidebar.title('Car Features')
        st.sidebar.write("Here you can choose the features of the car you want to predict its price")
        st.sidebar.markdown("---", unsafe_allow_html=True)
        names = ['','Volvo V40', 'Ford Mondeo', 'Renault Megane', 'Opel Astra',
            'Opel Adam', 'SEAT Leon', 'Nissan Pulsar', 'Hyundai i30',
            'Skoda Scala', 'Ford Focus', 'Dacia Sandero', 'Fiat Panda',
            'Ford Mustang', 'Fiat 500X', 'Renault Captur', 'Nissan Qashqai',
            'Renault Talisman', 'Peugeot 308', 'Volvo XC40', 'Ford Fiesta',
            'Renault Kadjar', 'Fiat 500C', 'Toyota Yaris', 'Skoda Fabia',
            'Renault Clio', 'Opel Insignia', 'Peugeot 2008', 'SEAT Ibiza',
            'Opel Cascada', 'Dacia Duster', 'Skoda Karoq', 'Hyundai i20',
            'Peugeot 206', 'Volvo XC60', 'Toyota RAV 4', 'Opel Corsa',
            'Toyota Corolla', 'Peugeot 3008', 'Hyundai TUCSON', 'Peugeot 208',
            'Fiat 500', 'SEAT Arona', 'Volvo S60', 'Opel Grandland X',
            'Dacia Logan', 'Peugeot RCZ', 'Nissan Micra', 'Skoda Kodiaq',
            'Toyota C-HR', 'Skoda Superb', 'SEAT Ateca', 'Hyundai IONIQ',
            'Skoda Octavia', 'Toyota Auris', 'Volvo V90', 'Fiat Tipo',
            'Peugeot 207', 'Volvo XC90', 'Volvo S90', 'Volvo C30',
            'Nissan 370Z', 'Volvo C70', 'Nissan Juke', 'Nissan X-Trail',
            'Mercedes-Benz A 180', 'Toyota Aygo', 'Volvo V60', 'Peugeot 508',
            'Nissan 350Z', 'Ford Kuga']
        names = sorted(names)
        

        user_data['make_model'] = st.sidebar.selectbox('Make and Model', options=names)        
        user_data['warranty'] = st.sidebar.radio('Warranty', options=['Yes', 'No'])
        st.write("---")
        user_data['mileage'] = st.sidebar.number_input('Mileage', min_value=0.0, max_value=df['mileage'].max(), value=0.0, step=500.0)
        user_data['seller'] = st.sidebar.selectbox('Seller', options=['Dealer', 'Private seller'])

        user_data['full_service_history'] = 'Yes'
        user_data['upholstery'] = st.sidebar.selectbox('Upholstery', options=['Part/Full Leather', 'Cloth'])
        user_data['comfort_&_convenience_Package'] = st.sidebar.selectbox('Comfort & Convenience Package', options=['Standard', 'Premium', 'Premium Plus'])
        user_data['entertainment_&_media_Package'] = st.sidebar.selectbox('Entertainment & Media Package', options=['Standard', 'Plus'])
        user_data['safety_&_security_Package'] = st.sidebar.selectbox('Safety & Security Package', options=['Safety Standard Package', 'Safety Premium Package', 'Safety Premium Plus Package'])


        # Create a multi-column layout for better organization


        user_data['body_type'] ='Compact'
        user_data['type'] = 'Used'
        user_data['gearbox'] = 'Semi-automatic'
        user_data['fuel_type'] = 'Benzine'
        user_data['engine_size'] = 1500.0
        user_data['gears'] = 6.0
        user_data['co_emissions'] = 500
        user_data['drivetrain'] = 'Front'
        user_data['extras'] = 8
        user_data['empty_weight'] = 1280.0
        user_data['full_service_history'] = 'Yes'
        user_data['previous_owner'] =1.0
        user_data['energy_efficiency_class'] ='efficient'
        user_data['age'] = 2.0
        user_data['power_kW'] = 88.0
        user_data['cons_avg'] = 3.6
        # user_data['comfort_&_convenience_Package'] = st.selectbox('Comfort & Convenience Package', options=['Standard', 'Premium', 'Premium Plus'])
        # user_data['entertainment_&_media_Package'] = st.selectbox('Entertainment & Media Package', options=['Standard', 'Plus'])
        # user_data['safety_&_security_Package'] = st.selectbox('Safety & Security Package', options=['Safety Standard Package', 'Safety Premium Package', 'Safety Premium Plus Package'])

        # Submit button
        st.markdown(
            """
        <style>
          
            
            .stButton>button {
                color: #ffffff;
                background-color: #FF3131;
                border: none;
                border-radius: 4px;
                padding: 0.75rem 1.5rem;
                margin: 0.75rem 0;
                position:  absolute;
                top:10px;
                left:25%;
                
                

            }
            .stButton>button:hover {
                background-color:  #FF4B4B;
                text-align: center;
                color: #FFFFFF;
            }
           
            
          
        </style>
    """, unsafe_allow_html=True
        )
        submit_button = st.sidebar.button('Predict Price')

        # Prediction and display in col2

       
        if submit_button:
            # Create a DataFrame with user input
            #df[df['make_model'] == dic['ii']].head(1)['price'].values[0]
            if user_data['make_model'] != '':
                # print(df[df['make_model'] == user_data['make_model']].head(1)['gearbox'].values[0])
                user_data['gearbox']=df[df['make_model'] == user_data['make_model']].head(1)['gearbox'].values[0]
                user_data['energy_efficiency_class']=df[df['make_model'] == user_data['make_model']].head(1)['energy_efficiency_class'].values[0]
                user_data['power_kW']=df[df['make_model'] == user_data['make_model']].head(1)['power_kW'].values[0]
                user_data['cons_avg']=df[df['make_model'] == user_data['make_model']].head(1)['cons_avg'].values[0]
                user_data['previous_owner']=df[df['make_model'] == user_data['make_model']].head(1)['previous_owner'].values[0]
                user_data['full_service_history']=df[df['make_model'] == user_data['make_model']].head(1)['full_service_history'].values[0]
                user_data['body_type']=df[df['make_model'] == user_data['make_model']].head(1)['body_type'].values[0]
                # user_data['extras']=df[df['make_model'] == user_data['make_model']].head(1)['extras'].values[0] ### we need to deal with this or it will be fixed value -----
                user_data['fuel_type']=df[df['make_model'] == user_data['make_model']].head(1)['fuel_type'].values[0]
                user_data['engine_size']=df[df['make_model'] == user_data['make_model']].head(1)['engine_size'].values[0]
                user_data['gears']=df[df['make_model'] == user_data['make_model']].head(1)['gears'].values[0]
                user_data['co_emissions']=df[df['make_model'] == user_data['make_model']].head(1)['co_emissions'].values[0]
                user_data['drivetrain']=df[df['make_model'] == user_data['make_model']].head(1)['drivetrain'].values[0]
                user_data['empty_weight']=df[df['make_model'] == user_data['make_model']].head(1)['empty_weight'].values[0]
                user_data['previous_owner']=df[df['make_model'] == user_data['make_model']].head(1)['previous_owner'].values[0]
                user_data['age']=df[df['make_model'] == user_data['make_model']].head(1)['age'].values[0]
            else: pass
                
            user_input_df = pd.DataFrame([user_data])

            # Make a prediction using the loaded model
            df1 = pd.DataFrame({
            'Age':[user_data['age']],
            'previous owners':[user_data['previous_owner']],
            'fuel type':[user_data['fuel_type']],
            'gear box':[user_data['gearbox']],
            'Hourse Power':[user_data['power_kW']],

        })

        # Convert the DataFrame to a Markdown table string
            markdown_table = df1.to_markdown(index=False)
            
            predicted_price = ridge_model_loaded.predict(user_input_df)[0]
            car_model = user_data['make_model']  # Replace with user's choice
            # This should be replaced with the user's choice
            image_path = get_car_image_path(car_model)
            print(image_path)
            
            st.image(image_path,use_column_width=True)
            table_style = """
<style>
table {
    width: 100%;
    border-collapse: collapse;
}
th {
    background-color: #808080;
    color: white;
}
th, td {
    padding: 8px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}
tr:hover {
   
}




</style>
"""

# Convert your DataFrame to a Markdown table string without index
            st.write('---')
            markdown_table = df1.to_markdown(index=False)

# Render the styled Markdown table in Streamlit
     
            st.markdown(table_style + markdown_table, unsafe_allow_html=True)  
            st.write('---')             
            st.header(f'${predicted_price:.2f}')
            st.write('---')
                                    
            

 
