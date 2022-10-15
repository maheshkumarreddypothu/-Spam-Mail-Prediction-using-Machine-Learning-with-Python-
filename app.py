#importing all the dependencies
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix, plot_roc_curve, plot_precision_recall_curve
from sklearn.metrics import precision_score, recall_score
from sklearn.neighbors import KNeighborsClassifier 
#Main function
def main():
    st.title('Binary Classification Web App')
    st.sidebar.title("Binary classification web app")
    st.markdown('Are your mushrooms edible or poisnous')
    st.sidebar.markdown("Are your mushrooms edible or poisnous")
    #Loading the data
    @st.cache(persist=True)
    def load_data():
        data=pd.read_csv("C:\\Users\\subbareddy\\Desktop\\VSCode\\mushrooms.csv")
        label=LabelEncoder()
        for col in data.columns:
            data[col]=label.fit_transform(data[col])
        return data
    #Splitting the data into training data and testing data
    @st.cache(persist=True) 
    def split(df):
        y=df.type
        x=df.drop(columns=['type'])
        x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)
        return x_train,x_test,y_train,y_test
    #Plotting the metrics for evaluation of performance
    def plot_metrics(metrics_list):
        if "Confusion Matrix" in metrics_list:
            st.subheader("Confusion Matrix")
            plot_confusion_matrix(model,x_test,y_test,display_labels=class_names)
            st.pyplot()
        if 'ROC Curve' in metrics_list:
            st.subheader("ROC Curve")
            plot_roc_curve(model,x_test,y_test)
            st.pyplot()  #display the matplot figure
        if 'Precision-Recall Curve' in metrics_list:
            st.subheader("Precision-Recall Curve")
            plot_precision_recall_curve(model,x_test,y_test)
            st.pyplot()


    df=load_data()
    x_train,x_test,y_train,y_test=split(df)
    class_names=['edible','poisnous']
    #The parametres of checkbox are st.sidebar.checkbox(label="",value=False,disabled=False,key=None)
    data=st.sidebar.checkbox(label="Show raw data",disabled=False,value=False,key='data')
    if data:
        st.subheader("Mushroom Dataset {classification}")
        st.write(df)
    st.sidebar.subheader("Choose Classifier")
    classifier=st.sidebar.selectbox("Classifier",("Support Vector Machine(SVM)","Logistic Regression(LR)","Random Forest Classifier(RFC)","KNN Classifier(KNN)"))
    #Providing the parametres for different models
    if classifier=="Support Vector Machine(SVM)":
        st.sidebar.subheader("Model Hyperparametres")
        C=st.sidebar.number_input(label="C (Regularisation parameter)",min_value=0.01,max_value=10.0,step=0.01,key='C')
        kernel=st.sidebar.radio(label="Kernel",options=("rbf","linear"),key='kernel')
        gamma=st.sidebar.radio(label="Gamma (Kernel Coeffecient)",options=("scale","auto"),key="Gamma")
        metrics=st.sidebar.multiselect("What metrics to plot?",("Confusion Matrix","ROC Curve","Precision-Recall Curve"))
        if st.sidebar.button("Classify",key='classify'):
            st.subheader("Support Vector Machine (SVM) Results")
            model=SVC(C=C,kernel=kernel,gamma=gamma)
            model.fit(x_train,y_train)
            accuracy=model.score(x_test,y_test)
            y_pred=model.predict(x_test)
            st.write("Accuracy: ",accuracy.round(2))
            st.write("Precision: ",precision_score(y_test,y_pred,labels=class_names).round(2))
            st.write("Recall: ",recall_score(y_test,y_pred,labels=class_names).round(2))
            plot_metrics(metrics)
    if classifier=="Logistic Regression(LR)":
        st.sidebar.subheader("Model Hyperparametres")
        C=st.sidebar.number_input(label="C (Regularisation parameter)",min_value=0.01,max_value=10.0,step=0.01,key='C')
        max_iter1=st.sidebar.slider("Maximum number of iterations",100,500,key='max_iter')
        metrics=st.sidebar.multiselect("What metrics to plot?",("Confusion Matrix","ROC Curve","Precision-Recall Curve"))
        if st.sidebar.button("Classify",key='classify'):
            st.subheader("Logistic Regression(LR) Results")
            model=SVC(C=C,max_iter=max_iter1)
            model.fit(x_train,y_train)
            accuracy=model.score(x_test,y_test)
            y_pred=model.predict(x_test)
            st.write("Accuracy: ",accuracy.round(2))
            st.write("Precision: ",precision_score(y_test,y_pred,labels=class_names).round(2))
            st.write("Recall: ",recall_score(y_test,y_pred,labels=class_names).round(2))
            plot_metrics(metrics)
    if classifier=="Random Forest Classifier(RFC)":
        st.sidebar.subheader("Model Hyperparametres")
        n_estimators=st.sidebar.number_input("The number of trees in the forest",min_value=100,max_value=5000,step=10,key='n_estimators')
        max_depth=st.sidebar.number_input("The maximum depth of the tree",min_value=1,max_value=20,key='max_depth')
        bootstrap=st.sidebar.radio("Bootstrap samples when building trees",('True','False'),key='bootstrap')
        metrics=st.sidebar.multiselect("What metrics to plot?",("Confusion Matrix","ROC Curve","Precision-Recall Curve"))
        if st.sidebar.button("Classify",key='classify'):
            st.subheader("Random Forest Classifier(RFC) Results")
            model=RandomForestClassifier(n_estimators=n_estimators,max_depth=max_depth,bootstrap=bootstrap)
            model.fit(x_train,y_train)
            accuracy=model.score(x_test,y_test)
            y_pred=model.predict(x_test)
            st.write("Accuracy: ",accuracy.round(2))
            st.write("Precision: ",precision_score(y_test,y_pred,labels=class_names).round(2))
            st.write("Recall: ",recall_score(y_test,y_pred,labels=class_names).round(2))
            plot_metrics(metrics)
    if classifier=="KNN Classifier(KNN)":
        st.sidebar.subheader("Model Hyperparametres")
        n_neighbors=st.sidebar.number_input("Number of neignbors",min_value=1,max_value=20,step=1,key='n_neighbors')
        metrics=st.sidebar.multiselect("What metrics to plot?",("Confusion Matrix","ROC Curve","Precision-Recall Curve"))
        if st.sidebar.button("Classify",key='classify'):
            st.subheader("KNN Classifier(KNN) Results")
            model=KNeighborsClassifier (n_neighbors=n_neighbors)
            model.fit(x_train,y_train)
            accuracy=model.score(x_test,y_test)
            y_pred=model.predict(x_test)
            st.write("Accuracy: ",accuracy.round(2))
            st.write("Precision: ",precision_score(y_test,y_pred,labels=class_names).round(2))
            st.write("Recall: ",recall_score(y_test,y_pred,labels=class_names).round(2))
            plot_metrics(metrics)
    


if __name__=="__main__":
    main()

