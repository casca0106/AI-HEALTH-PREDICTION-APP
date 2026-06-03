import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from datetime import date
from models.predict import predict_risk
from utils.validation import (
    validate_email,
    validate_name,
    validate_glucose,
    validate_haemoglobin,
    validate_cholesterol
)

from utils.db import (
    create_table,
    add_patient,
    get_all_patients,
    update_patient,
    delete_patient
)

create_table()
patients = get_all_patients()
menu = st.sidebar.selectbox(
    "Navigation",
    [
        "Dashboard",
        "Add Patient",
        "View Patients",
        "Manage Patients"
    ]
)
st.title("AI Health Prediction App")

if menu == "Dashboard":

    st.header("Dashboard")

    total_patients = len(patients)

    high_risk = len(
        [p for p in patients if p[7] == "High Risk"]
    )

    medium_risk = len(
        [p for p in patients if p[7] == "Medium Risk"]
    )

    low_risk = len(
        [p for p in patients if p[7] == "Low Risk"]
    )

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Patients", total_patients)
        st.metric("High Risk Patients", high_risk)

    with col2:
        st.metric("Medium Risk Patients", medium_risk)
        st.metric("Low Risk Patients", low_risk)

    risk_data = {
        "Low Risk": low_risk,
        "Medium Risk": medium_risk,
        "High Risk": high_risk
    }

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        fig, ax = plt.subplots(figsize=(5,3))
        ax.bar(
            risk_data.keys(),
            risk_data.values()
        )
        ax.set_title("Patient Risk Distribution")
        ax.set_xlabel("Risk Category")
        plt.xticks(rotation=0)
        ax.set_ylabel("Number of Patients")
        fig.tight_layout()
        st.pyplot(fig)

    with chart_col2:
        fig2, ax2 = plt.subplots(figsize=(4, 3))
        ax2.pie(
            risk_data.values(),
            labels=risk_data.keys(),
            autopct='%1.1f%%',
            startangle=90
        )
        ax2.axis('equal')
        ax2.set_title("Risk Percentage Distribution")
        fig2.tight_layout()
        st.pyplot(fig2)
    

if menu == "Add Patient":

        st.header("Add Patient")

        full_name = st.text_input("Full Name")
        from datetime import date


        dob = st.date_input(
            "Date of Birth",
            min_value=date(1950, 1, 1),
            max_value=date.today()
        )
        email = st.text_input("Email Address")

        glucose = st.number_input("Glucose", min_value=0.0)
        haemoglobin = st.number_input("Haemoglobin", min_value=0.0)
        cholesterol = st.number_input("Cholesterol", min_value=0.0)
        predicted_risk = predict_risk(
            glucose,
            haemoglobin,
            cholesterol
       )

        st.subheader("Predicted Risk")

        if predicted_risk == "Low Risk":
           st.success(predicted_risk)

        elif predicted_risk == "Medium Risk":
            st.warning(predicted_risk)

        else:
            st.error(predicted_risk)

        prediction = "Low Risk"

        if st.button("Add Patient"):

            if not validate_name(full_name):
                st.error("Name cannot be empty.")

            elif not validate_email(email):
                st.error("Please enter a valid email address.")

            elif not validate_glucose(glucose):
                st.error("Glucose value must be between 50 and 300.")

            elif not validate_haemoglobin(haemoglobin):
                st.error("Haemoglobin value must be between 5 and 20.")

            elif not validate_cholesterol(cholesterol):
                st.error("Cholesterol value must be between 100 and 400.")

            else:

                prediction = predicted_risk

                add_patient(
                    full_name,
                    str(dob),
                    email,
                    glucose,
                    haemoglobin,
                    cholesterol,
                   prediction
                )
        
                st.success("Patient added successfully!")


if menu == "View Patients":

        st.header("View Patients")
        search_name = st.text_input("Search Patient by Name")
        risk_filter = st.selectbox(
            "Filter by Risk",
            ["All", "Low Risk", "Medium Risk", "High Risk"]
        )

        patients = get_all_patients()
        if search_name:

            patients = [
                patient for patient in patients
                if search_name.lower() in patient[1].lower()
            ]
        if risk_filter != "All":

            patients = [
                patient for patient in patients
                if patient[7] == risk_filter
            ]
        if patients:

            df = pd.DataFrame(
                patients,
                columns=[
                    "ID",
                    "Full Name",
                    "DOB",
                    "Email",
                    "Glucose",
                    "Haemoglobin",
                    "Cholesterol",
                    "Prediction"
                ]
            )
            df.index = range(1, len(df) + 1)

            st.dataframe(df)
            st.subheader("Patient Cards")

            for patient in patients:

                with st.container():

                    st.markdown(f"""
                    ### {patient[1]}

                    - DOB: {patient[2]}
                    - Email: {patient[3]}
                    - Glucose: {patient[4]}
                    - Haemoglobin: {patient[5]}
                    - Cholesterol: {patient[6]}
                    - Prediction: {patient[7]}
                    """)

                    st.divider()
            csv = df.to_csv(index=False).encode('utf-8')

            st.download_button(
                label="Download Patient Data as CSV",
                data=csv,
                file_name='patient_records.csv',
                mime='text/csv'
            )

        else:
            st.info("No patient records found.")

if menu == "Manage Patients":
        st.header("Update Patient")
        search_manage = st.text_input("Search Patient")

        patient_ids = [patient[0] for patient in patients]
        if search_manage:
            patients = [
                patient for patient in patients
                if search_manage.lower() in patient[1].lower()
            ]

        selected_id = st.selectbox(
            "Select Patient ID to Update",
            patient_ids
        )

        selected_patient = None

        for patient in patients:
            if patient[0] == selected_id:
                selected_patient = patient
                break


        updated_name = st.text_input(
            "Update Full Name",
            value=selected_patient[1]
        )

        updated_dob = st.text_input(
            "Update DOB",
            value=selected_patient[2]
        )

        updated_email = st.text_input(
            "Update Email",
            value=selected_patient[3]
        )

        updated_glucose = st.number_input(
            "Update Glucose",
             value=float(selected_patient[4])
        )

        updated_haemoglobin = st.number_input(
            "Update Haemoglobin",
            value=float(selected_patient[5])
        )

        updated_cholesterol = st.number_input(
            "Update Cholesterol",
            value=float(selected_patient[6])
        )


        if st.button("Update Patient"):

            update_patient(
                selected_id,
                updated_name,
                updated_dob,
                updated_email,
                updated_glucose,
                updated_haemoglobin,
                updated_cholesterol
         )

            st.success("Patient updated successfully!")
            
        st.header("Delete Patient")

        delete_id = st.selectbox(
            "Select Patient ID to Delete",
            patient_ids
        )

        if st.button("Delete Patient"):

            delete_patient(delete_id)

            st.warning("Patient deleted successfully!")