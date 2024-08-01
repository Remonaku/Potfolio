# import streamlit as st 
# import tensorflow as tf
# from tensorflow.keras.preprocessing.image import img_to_array, load_img
# from tensorflow.keras.applications import ResNet50
# from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
# import numpy as np
# from PIL import Image

# model = ResNet50(weights='imagenet')

# st.title('Image Classification')
# st.header('Choose as Image')

# uploaded_file = st.file_uploader('upload image...', type=['jpg', 'jpeg', 'png'])

# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
#     st.image(image, caption='uploaded image', use_column_width=True)
#     st.write("")
#     st.write('classifying...')
    
#     img = load_img(uploaded_file, target_size=(224,224))
#     img_array = img_to_array(img)
#     img_array_expanded_dims = np.expand_dims(img_array, axis=0)
#     processed_img = preprocess_input(img_array_expanded_dims)
    
#     predictions = model.predict(processed_img)
#     label = decode_predictions(predictions)
    
#     for i, (imagenet_id, desc, score) in enumerate(label[0]):
#         st.write(f"(i+1): {desc} ({score*100: .2f}%)")
        
        
import streamlit as st
from PIL import Image

# CSS

st.markdown("""
<style>
	img {
        width: 46rem;
        padding: 5px;
        border: 2px solid #c8c8c8;
    }
</style>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Image Upload", "Scores"])



# 첫 번째 탭의 내용
with tab1:
    st.title('Mainboard parts Detect Tool',)

    uploaded_file = st.file_uploader('Please Upload files in this area', type=['jpg', 'jpeg', 'png','avi','mp4', 'mkv', 'wav'])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, use_column_width=True) #caption='Uploaded Image'

# 두 번째 탭의 내용
with tab2:
    st.header("This is Tab 2")
    st.write("And this is Tab 2's content")