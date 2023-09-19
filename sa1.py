import plotly.express as px
import streamlit as st
import seaborn as sns

# Load the Iris dataset from Seaborn
df = sns.load_dataset('iris')

# Create a 3D scatter plot using Plotly
fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width', color='species')

# Streamlit app
st.title("Iris Dataset 3D Scatter Plot")
st.write("This interactive 3D scatter plot visualizes the Iris dataset with Petal Width, Petal Length, and Sepal Length as the axes.")

st.plotly_chart(fig, use_container_width=True)




























# import plotly.graph_objects as go
# import streamlit as st
# import seaborn as sns

# df = sns.load_dataset('iris')
# fig = px.scatter_3d(
#     df,
#     x="petal_width",
#     y="petal_length",
#     color="species",
#     color_continuous_scale="greens",
# )

# st.subheader("Iris Scatterplot of Petal width and length by Species")
# st.plotly_chart(fig, theme="streamlit", use_container_width=True)




# import streamlit as st
# import seaborn as sns
# import pandas as pd
# import plotly.figure_factory as ff
# import plotly.express as px


# st.subheader("Iris")
# iris_data = px.data.iris()
# fig = px.scatter(iris_data, x='sepal_width', y='sepal_length', color='sepal_length', color_continuous_scale='pinks')
# tab1, tab2 = st.tabs(["idk1", "i'll figure it out 2"])
# with tab1:
#     st.plotly_chaanart(fig, theme="streamlit", use_container_width=True)
# with tab2:
#     st.plotly_chart(fig,theme=None, use_container_width=True)






# fig = px.scatter(iris_data, x="sepal_width", y="sepal_length")
# st.plotly_chart(fig)


#group_labels = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
#targets = ["species"]

#fig = ff.create_distplot(iris_data, group_labels)

# st.plotly_chart(fig))

# import streamlit as st
# import seaborn as sns
# import pandas as pd
# from sklearn.datasets import load_wine
# import altair as alt
# wine_data = load_wine()
# labels = wine_data.feature_names
# targets = wine_data.target
# print(labels)
# df_form = pd.DataFrame(wine_data.data, columns = labels)
# df_form['targets'] = targets
# st.write("""
# # Italian Wine Dataset
# How are malic acid and alcohol correlated in Italian wines?
# """)
# alt_handle = alt.Chart(df_form).mark_circle(size=60).encode(x='alcohol', y='malic_acid',
#  color='hue', tooltip=['ash', 'magnesium',
#  'proanthocyanins']).interactive()
# st.altair_chart(alt_handle)