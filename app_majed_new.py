
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

- **Majed Alshnifi** - [Majed's LinkedIn Profile](https://www.linkedin.com/in/majed-alshnifi/)
- **Intesar Hejazy** - [Intesar's LinkedIn Profile](https://www.linkedin.com/in/intesar-hejazy/)

Majed and Intesar have been the dynamic duo behind the AutoScout Car Price Prediction Platform, working in lockstep through every stage of its creation. From the initial blueprint to the final touches, they've left no stone unturned:

- **Architectural Design**: Dreaming up the structure and flow of the application.
- **Data Wizardry**: Taming vast datasets to reveal their secrets through meticulous analysis and preprocessing.
- **Algorithmic Alchemy**: Harnessing the predictive powers of the Ridge regression model, ensuring it's well-trained to foresee car valuations.
- **Streamlit Spell casting**: Weaving the code that brings the user interface to life, ensuring every interaction is a breeze.
- **Database and Image Conjuring**: Crafting the behind-the-scenes magic that seamlessly pulls features and visual cues from a treasure trove of data.
- **Quality Questing**: Relentlessly pursuing perfection through thorough testing and refinement, all to deliver a stellar application.

Together, they've engineered more than just a tool; they've created a gateway for users to unlock insights into car values with precision and ease.

---

Delve into their professional realms to discover more about their past exploits and potential future collaborations.


                    """)
    


    
    with tab2:
        
        
        st.markdown("""
                  # AutoScout Car Price Prediction Platform
## Let's tell you how we made this  :star:masterpiece:star:

## Overview
The AutoScout Car Price Prediction Platform is not just an app; it's a marvel in the car pricing cosmos. Crafted with the mystical arts of Streamlit and machine learning, it's where numbers meet ML to predict what your ride's worth.

## Magic Under the Hood

### User Interface
- **Interactive Forms**: The kind where you tell us about your four-wheeled buddy, and we crunch those numbers like a math wiz.

### Machine Learning Sorcery
- **Models**: We experimented multiple models starting with Ridge's magic, but we also have unleashed an ensemble of decision trees to play the numbers game and predict car prices.
- **Model Training with a Twist**: Cross-validation and grid search were our crystal ball, helping us peer into the data's soul to find the hyperparameter nirvana.

### Visual Wizardry
- **Data Scraping Charm**: Our code ninjas conjured a spell to scrape Google images, creating a majestic gallery of car models.

### Database Connectivity
- **Automated Feature Extraction**: We've got a `.csv` database that's like a treasure map, leading us to hidden gems like horsepower and engine size.

## Crystal Ball Details
- **Algorithms**: Ridge Regressor because we always start simple then Random Forest Regressor, because why use one decision tree when you can use a forest?
- **Model Performance**: Our crystal ball's accuracy was measured with metrics more mystical than your average tarot card reading.

## Data Source
The application leans on a `.csv` grimoire filled with arcane knowledge about car models and their mystical features.

## How to Use this Enchantment
1. **Welcome Tab**: A grand hall where you're welcomed with open arms and the promise of future fortunes.
2. **Selecting Car Features**: An alchemy table where you mix and match features to create the elixir of price prediction.
3. **Price Prediction**: Voilà! Your chariot's value revealed with a flourish and a dash of machine learning magic.

## Conjuring the App in Your Realm
1. Clone the repository with a wave of your wand.
2. Command your terminal spirits to install the necessary incantations via `pip install -r requirements.txt`.
3. Summon the app into existence with `streamlit run app.py`.

## Extend the Magic
Fancy casting your own spells to enhance this mystical tool? Here's how to join our circle of wizards:

1. Fork the repository to your own mystical lair (GitHub account).
2. Create a new branch where your magic will unfold.
3. Contribute your enchantments and push them to your fork.
4. Initiate a pull request to discuss your magical enhancements.

## License
This spellbook is covered under the MI (Majed and Intesar) :clown_face: License. See the `CallME.md` for all the secret clauses.

## Self-High-Five!
A round of applause for us, Majed and Intesar, for our mind-bending HARD work and for being our own patrons, therapists, and cheerleaders.

## _________________________________________
###### All rights reserved to MIClown :clown_face:.Inc
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
        st.sidebar.write("Mix the features to create the magic of.. :sparkles: price prediction :sparkles:")
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
            
                
                user_input_df = pd.DataFrame([user_data])

                # Make a prediction using the loaded model
                df1 = pd.DataFrame({
                'energy efficiency':[user_data['energy_efficiency_class']],
                'previous owners':[user_data['previous_owner']],
                'fuel type':[user_data['fuel_type']],
                'gear box':[user_data['gearbox']],
                'Hourse Power':[user_data['power_kW']],
                'full service history':user_data['full_service_history']

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
            else: 
                st.header(':clown_face: please select a car name :clown_face: ')
                st.write("We know you are excited to try this masterpiece, but select a car model first to cast the magic spell :black_joker:")
                 
            
                                        
            

 
