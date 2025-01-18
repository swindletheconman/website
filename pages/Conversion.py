import streamlit as st


st.set_page_config(layout='wide')
st.title("converter")

#dictionaryfor units of conversion factor. unit name is key, factor is the value.
conversion_factor = {'distance' : {'milimeter':1,
                                   'centimeter':0.1,
                                   'meter':0.001,
                                   'kilometer':0.000001,
                                   'inch':0.0393701,
                                   'feet':0.00328084,
                                   'yards':0.00109361,
                                   'miles':6.2137e-7},
                     'weight' : {'gr':1,
                                 'mg':1000,
                                 'kg':0.001},
                     'time' : {'hour':1,
                               'minute':60,
                               'second':3600,
                               'days':1/24,
                               'week':1/(24*7),
                               'month':(24*30),
                               'year':(24*365),
                               'decade':(24*365*10),
                               'century':(24*365*100)},
                    }

# units options
category = list(conversion_factor.keys())
#units = list(conversion_factor[category].keys())
result = None

st.latex(r'''
\text{Converted Value} = \frac{\text{Input value}}{\text{Conversion Factor of Base Unit}} \times \text{Conversion Factorof Target Unit}
''')

st.markdown(
    """
    <style>
    .stbutton button {
        margin-top: 28px;
        }
        
        </style>
        """,
        unsafe_allow_html=True
)

def convert(input_value, base_unit, target_unit,selected_category):
    base_value = input_value * conversion_factor[selected_category][target_unit]
    converted_value = base_value / conversion_factor[selected_category][base_unit]
    
    return converted_value
    
#create a container
with st.container(border = True):
    #split the container into 5 columns
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
    with col1:
        selected_category = st.selectbox("Category",conversion_factor.keys())
                     
    with col2:
        input_value = st.number_input("Input Value", min_value=0.0, step=0.1)
        
    with col3:
        base_unit = st.selectbox("From", conversion_factor[selected_category].keys())
    
    with col4:
        target_unit = st.selectbox("To", conversion_factor[selected_category].keys())
        
    with col5:
        #st.text("Execute")
        if st.button("convert", use_container_width=True):
            if base_unit and target_unit:
                result = convert(input_value, base_unit, target_unit,selected_category)
            
    with col6:
        st.write("Result")
        st.header(result)
