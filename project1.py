# Capstone Project Module 1
# Author: Anintyo Herdadi
# Class : JCAIEH-002

# Case Study: Data pasien rumah sakit


import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# --- Connect to MySQL ---
conn = mysql.connector.connect(
    host="localhost",
    user="root",       # change to your MySQL username
    password="root",  # change to your MySQL password
    database="pasien_db"
)
cursor = conn.cursor()

# --- Function ---
def read_table():
    cursor.execute("SELECT * FROM datapasien")
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=["Patient_ID", "Full_Name", "Gender", "Age", "Diagnosis"])
    print("\n--- Patient Records ---")
    print(df)
    return df

def show_statistics():
    df = read_table()
    print("\n--- Statistics ---")
    print("Average Age:", df["Age"].mean())
    print("Diagnosis Counts:\n", df["Diagnosis"].value_counts())
    print("Gender Distribution:\n", df["Gender"].value_counts())

def visualize_data():
    df = read_table()

    # --- Bar chart for diagnosis ---
    diagnosis_counts = df["Diagnosis"].value_counts()
    diagnosis_counts.plot(kind="bar", color="skyblue")
    plt.title("Diagnosis Distribution")
    plt.xlabel("Diagnosis")
    plt.ylabel("Count")
    plt.show()

    # --- Pie chart for gender ---
    gender_counts = df["Gender"].value_counts()
    gender_counts.plot(kind="pie", autopct='%1.1f%%', startangle=90, colors=["lightblue","pink"])
    plt.title("Gender Distribution")
    plt.ylabel("")  # remove y-label
    plt.show()

def add_patient():
     while True:
        pid = input("Enter Patient ID: ")
        
        # Check if Patient ID already exists
        cursor.execute("SELECT Patient_ID FROM datapasien WHERE Patient_ID = %s", (pid,))
        existing_patient = cursor.fetchone()
        
        if existing_patient:
            print("❌ Warning: Patient ID already exists! Please use a different ID.")
            continue  # Re-input
        else:
            break  # Next step

     fullname = input("Enter Full Name: ")  
     gender = input("Enter Gender (Male/Female): ")
     age = int(input("Enter Age: "))
     diagnosis = input("Enter Diagnosis: ")
     cursor.execute("INSERT INTO datapasien VALUES (%s,%s,%s,%s,%s)", (pid, fullname, gender, age, diagnosis))
     conn.commit()
     print("✅ Patient added successfully.")

#  --- Main Menu ---
def menu():
    while True:
        print("\n--- Patient Management System---")
        print("1. Read Table")
        print("2. Show Statistics")
        print("3. Visualize Data")
        print("4. Add Patient")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            read_table()
        elif choice == "2":
            show_statistics()
        elif choice == "3":
            visualize_data()
        elif choice == "4":
            add_patient()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("❌ Invalid choice, try again.")

# --- Run Program ---
menu()