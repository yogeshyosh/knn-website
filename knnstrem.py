import streamlit as st
import pickle
import sklearn
def g1():
    gr1=st.text_input('gene 1')
    return gr1
def g2():
    gr2=st.text_input('gene 2')
    return gr2
def predict(gr1, gr2):
    lmod=pickle.load(open('knn_model.pkl', 'rb'))
    nd=[[float(gr1), float(gr2)]]
    pre=lmod.predict(nd)
    st.write('the cancer is')
    if pre==0:
        st.write('not present')
    else:
        st.write('present')

if __name__ == "__main__":
    st.title('cancer presence prediction')
    st.image('canceer.webp') 
    g1st = g1()
    g2nd = g2()
    st.write("The parameters you entered are: ")
    st.write("gene1 ", g1st)
    st.write("gene2", g2nd)
if st.button('check it'):
    predict(g1st,g2nd)
