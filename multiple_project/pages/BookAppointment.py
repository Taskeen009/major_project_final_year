import sqlite3
import streamlit as st

# Define the correct password
PASSWORD = "12345"

def create_database():
    conn = sqlite3.connect('appointment.db')
    c = conn.cursor()
    c.execute("""
    SELECT name FROM sqlite_master WHERE type='table' AND name='appointments'
    """)
    if not c.fetchone():
        c.execute('''CREATE TABLE appointments
                     (name text, address text, phone text, appointment_type text, date text, time text)''')
        conn.commit()
    conn.close()

def add_customer(name, address, phone, appointment_type, date, time):
    conn = sqlite3.connect('appointment.db')
    c = conn.cursor()
    c.execute("INSERT INTO appointments VALUES (?, ?, ?, ?, ?, ?)", (name, address, phone, appointment_type, date, time))
    conn.commit()
    conn.close()

def delete_customer(name, password):
    # Check if password is correct
    if password != PASSWORD:
        st.error("Incorrect password. Please try again.")
        return

    conn = sqlite3.connect('appointment.db')
    c = conn.cursor()
    c.execute("DELETE FROM appointments WHERE name=?", (name,))
    conn.commit()
    conn.close()

def update_customer(name, address, phone, appointment_type, date, time, password):
    # Check if password is correct
    if password != PASSWORD:
        st.error("Incorrect password. Please try again.")
        return

    conn = sqlite3.connect('appointment.db')
    c = conn.cursor()
    c.execute("UPDATE appointments SET address = ?, phone = ?, appointment_type = ?, date = ?, time = ? WHERE name = ?", (address, phone, appointment_type, date, time, name))
    conn.commit()
    conn.close()

def view_customers(password):
    # Check if password is correct
    if password != PASSWORD:
        st.error("Incorrect password. Please try again.")
        return

    # Connect to the database and execute query
    conn = sqlite3.connect('appointment.db')
    c = conn.cursor()
    c.execute("SELECT * FROM appointments")
    customers = c.fetchall()
    conn.close()

    # Display the results in a table
    st.header("Customers File")
    st.table(customers)


def main():
    st.title("Book Your Appointment")

    create_database()

    name = st.text_input("Name")
    address = st.text_input("Disease Predicted")
    phone = st.text_input("Phone Number")
    appointment_type = st.text_input("Doctor Name")
    date = st.text_input("Date")
    time = st.text_input("Time")

    password = st.text_input("Password", type="password")

    st.sidebar.header("Click for operations")
    if st.sidebar.button("Add Appointment"):
        add_customer(name, address, phone, appointment_type, date, time)

    if st.sidebar.button("Delete Appointment"):
        delete_customer(name, password)

    if st.sidebar.button("Update Appointment"):
        update_customer(name, address, phone, appointment_type, date, time, password)

    if st.sidebar.button("Search Appointment"):
        conn = sqlite3.connect('appointment.db')
        c = conn.cursor()
        c.execute("SELECT * FROM appointments WHERE name=? OR phone=?", (name, phone))
        customer = c.fetchall()
        conn.close()

        st.header("Customers File")
        st.table(customer)

    if st.sidebar.button("View"):
        view_customers(password)


if __name__ == '__main__':
    main()
