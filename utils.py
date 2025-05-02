import plotly.express as px
from sklearn.ensemble import RandomForestClassifier,AdaBoostClassifier,GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier


def scatter_plot(x_axis,y_axis):
    df = px.data.iris()
    fig = px.scatter(df, x=x_axis, y=y_axis, color="species",
                     size='petal_length', hover_data=['petal_width'])
    return fig

def get_model(choice):
    if choice=="RanfomForest":
        model=RandomForestClassifier()
    elif choice=="AdaBoost":
        model=AdaBoostClassifier()
    elif choice=="DecisionTreeClassifier":
        model=DecisionTreeClassifier()
    elif choice == "LogisticRegression":
        model=LogisticRegression()
    else:
        model=GradientBoostingClassifier()
    return model

def image_path(id):
    if id == 0:
        path = "images\\Iris_Setosa.jpeg"
    elif id == 1:
        path = "images\\Iris_versicolor.jpg"
    elif id == 2:
        path = "images\\Iris_virginica.jpg"
    
    return path