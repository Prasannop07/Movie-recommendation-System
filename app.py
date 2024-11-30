import streamlit as st
from recommend import recommend, new_df
from recommend import recommend, fetch_poster, new_df


# Streamlit app title
st.title("BADSUURAT TANVI Movie Recommendation System")

# Dropdown for movie selection
movies_list = new_df['title'].values
selected_movie = st.selectbox("Choose a movie", movies_list)

# Button to get recommendations
if st.button("Get Recommendations"):
    recommendations = recommend(selected_movie)
    if recommendations:
        st.write("**Recommended Movies:**")
        cols = st.columns(len(recommendations) * 2 - 1)  # Add spacer columns
        for i, movie in enumerate(recommendations):
            with cols[i * 2]:  # Use every alternate column for posters
                poster_url = fetch_poster(movie)
                if poster_url:
                    st.image(poster_url, width=10000)
                    st.markdown(f"<p style='text-align: center; font-weight: bold;'>{movie}</p>", unsafe_allow_html=True)
            # Spacer columns are automatically empty
    else:
        st.write("No recommendations found. Please try another movie.")

# BLACK BACKGROUND EFFECTS -
st.markdown(
    """
    <style>
    div.stButton > button {
        background-color: #FF5733;
        color: white;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        border-radius: 8px;
        transition: 0.3s;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3); /* Add shadow effect */
    }
    div.stButton > button:hover {
        background-color: #C70039;
        color: white;
        transform: scale(1.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)


#toggle night mode switch - 
dark_mode = st.checkbox("Enable Dark Mode")

if dark_mode:
    st.markdown(
        """
        <style>
        body {
            background-color: #333 !important;
            color: white !important;
        }
        div[data-testid="stAppViewContainer"] {
            background-color: #333 !important;
            color: white !important;
        }
        div[data-testid="stSidebar"] {
            background-color: #444 !important;
            color: white !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        <style>
        body {
            background-color: white !important;
            color: black !important;
        }
        div[data-testid="stAppViewContainer"] {
            background-color: white !important;
            color: black !important;
        }
        div[data-testid="stSidebar"] {
            background-color: #f0f0f0 !important;
            color: black !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

