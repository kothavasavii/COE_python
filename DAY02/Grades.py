import streamlit as st

project_score=st.number_input("Enter project score:")
internal_score=st.number_input("Enter internal score")
external_score=st.number_input("Enter external score")
if st.button("claculate grade"):
    if project_score>=50 and internal_score>=50 and external_score>=50:
        total=project_score+internal_score+external_score
        if total>=90:
            st.success("Grade:A")
        elif total>80:
            st.success("Grade:B")
        else:
            st.success("Grade:c")
    else:
        if project_score<50:
            st.write("failed in project and your score is "+str(project_score))
        if internal_score<50:
            st.write("failed in internal and your score is" +str(internal_score))
        if external_score<50:
            st.write("failed in external and your score is "+str(external_score))