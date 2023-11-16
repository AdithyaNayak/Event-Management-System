import streamlit as st
import mysql.connector
import pandas as pd
import requests
from streamlit_lottie import st_lottie
config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'port': 3306,  # change this port number to match your MySQL port
    'database':'event_management_system'
}

def loti(url):
    r = requests.get(url)
    if r.status_code != 200:
       return None
    else:
        return r.json()
def create_connection():
    """Create a connection to the MySQL database."""
    db = mysql.connector.connect(**config)
    return db

def create_database(db):
    """Create the 'event_management_system' database if it doesn't exist."""
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS event_management_system")
    cursor.close()

def insert_user_record(db, UserID, Username, Password, Email, PhoneNo, FirstName, LastName, Role):
    """Insert a new user record into the 'User' table."""
    cursor = db.cursor()

    # Select the database
    cursor.execute("USE event_management_system")

    insert_user_query = """
    INSERT INTO User (UserID, Username, Password, Email, PhoneNo, FirstName, LastName, Role)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    user_data = (UserID, Username, Password, Email, PhoneNo, FirstName, LastName, Role)

    cursor.execute(insert_user_query, user_data)
    db.commit()
    st.write("User record inserted successfully.") 

def insert_event_record(db, event_id, event_name, event_description, event_date, event_time, location, max_capacity, event_type, event_status):
    """Insert a new event record into the 'Event' table."""
    cursor = db.cursor()

    # Select the database
    cursor.execute("USE event_management_system")

    insert_event_query = """
    INSERT INTO Event (EventID, EventName, EventDescription, EventDate, EventTime, Location, MaxCapacity, EventType, EventStatus)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    event_data = (event_id, event_name, event_description, event_date, event_time, location, max_capacity, event_type, event_status)

    cursor.execute(insert_event_query, event_data)
    db.commit()
    st.write("Event record inserted successfully.")

def fetch_event_by_id(db, event_id):
    """Fetch an event's record from the 'Event' table based on ID."""
    cursor = db.cursor()

    # Select the database
    cursor.execute("USE event_management_system")

    # Fetch the event by ID
    select_event_query = """
       SELECT EventID, EventName, EventDescription, EventDate, CAST(EventTime AS CHAR) as EventTime, Location, MaxCapacity, EventType, EventStatus
       FROM Event
       WHERE EventID = %s
       """
    cursor.execute(select_event_query, (event_id,))
    event = cursor.fetchone()

    return event

def fetch_event_by_name(db, event_name):
    """Fetch an event's record from the 'Event' table based on Name."""
    cursor = db.cursor()

    # Select the database
    cursor.execute("USE event_management_system")

    # Fetch the event by Name
    select_event_query = """
       SELECT EventID, EventName, EventDescription, EventDate, CAST(EventTime AS CHAR) as EventTime, Location, MaxCapacity, EventType, EventStatus
       FROM Event
       WHERE EventName = %s
       """
    cursor.execute(select_event_query, (event_name,))
    event = cursor.fetchone()

    return event

def fetch_event_by_date(db, event_date):
    """Fetch an event's record from the 'Event' table based on Date."""
    cursor = db.cursor()

    # Select the database
    cursor.execute("USE event_management_system")

    # Fetch the event by Date
    select_event_query = """
       SELECT EventID, EventName, EventDescription, EventDate, CAST(EventTime AS CHAR) as EventTime, Location, MaxCapacity, EventType, EventStatus
       FROM Event
       WHERE EventDate = %s
       """
    cursor.execute(select_event_query, (event_date,))
    event = cursor.fetchone()

    return event

def edit_event(db):
    event = st.session_state.edit_event
    st.subheader("Edit Event Details")
    new_event_name = st.text_input("Event Name", value=event[1])
    new_event_description = st.text_input("Event Description", value=event[2])
    new_event_date = st.date_input("Event Date", value=event[3])
    new_event_time = st.text_input("Event Time", value=event[4])
    new_location = st.text_input("Location", value=event[5])
    new_max_capacity = st.number_input("Max Capacity", value=event[6])
    new_event_type = st.text_input("Event Type", value=event[7])
    new_event_status = st.text_input("Event Status", value=event[8])

    if st.button("Update Event"):
        event_id = event[0]
        update_event_info(db, event_id, new_event_name, new_event_description, new_event_date, new_event_time, new_location, new_max_capacity, new_event_type, new_event_status)
        st.write("Event record updated successfully.")
        del st.session_state.edit_event

def update_event_info(db, event_id, new_event_name, new_event_description, new_event_date, new_event_time, new_location, new_max_capacity, new_event_type, new_event_status):
    """Update an event's record in the 'Event' table."""
    cursor = db.cursor()

    # Select the database
    cursor.execute("USE event_management_system")

    # Update the event record
    update_event_query = """
    UPDATE Event
    SET EventName = %s, EventDescription = %s, EventDate = %s, EventTime = CAST(%s AS TIME), Location = %s, MaxCapacity = %s, EventType = %s, EventStatus = %s
    WHERE EventID = %s
    """
    event_data = (new_event_name, new_event_description, new_event_date, new_event_time, new_location, new_max_capacity, new_event_type, new_event_status, event_id)

    cursor.execute(update_event_query, event_data)
    db.commit()

def delete_event_record(db, delete_option, delete_value):
    """Delete an event's record from the 'Event' table based on ID, Name, or Date."""
    cursor = db.cursor()

    # Select the database
    cursor.execute("USE event_management_system")

    # Delete the event record
    if delete_option == "ID":
        delete_event_query = "DELETE FROM Event WHERE EventID = %s"
    elif delete_option == "Name":
        delete_event_query = "DELETE FROM Event WHERE EventName = %s"
    elif delete_option == "Date":
        delete_event_query = "DELETE FROM Event WHERE EventDate = %s"

    cursor.execute(delete_event_query, (delete_value,))
    db.commit()
    st.write("Event record deleted successfully.")

def insert_participant_record(db, ParticipantID, UserID, DateOfBirth, PhoneNo, Address, PaymentInfo):
    """Insert a new participant record into the 'Participant' table."""
    cursor = db.cursor()

    # Select the database
    cursor.execute("USE event_management_system")

    insert_participant_query = """
    INSERT INTO Participant (ParticipantID, UserID, DateOfBirth, PhoneNo, Address, PaymentInfo)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    participant_data = (ParticipantID, UserID, DateOfBirth, PhoneNo, Address, PaymentInfo)

    cursor.execute(insert_participant_query, participant_data)
    db.commit()
    st.write("Participant record inserted successfully.")

def insert_eventfeedback_record(db, FeedbackID, EventID, ParticipantID, Rating, Comments, FeedbackDate):
    """Insert a new eventfeedback record into the 'EventFeedback' table."""
    cursor = db.cursor()

    # Select the database
    cursor.execute("USE event_management_system")

    insert_eventfeedback_query = """
    INSERT INTO EventFeedback (FeedbackID, EventID, ParticipantID, Rating, Comments, FeedbackDate)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    eventfeedback_data = (FeedbackID, EventID, ParticipantID, Rating, Comments, FeedbackDate)

    cursor.execute(insert_eventfeedback_query, eventfeedback_data)
    db.commit()
    st.write("EventFeedback record inserted successfully.")

def insert_eventplanner_record(db, PlannerID, UserID, CompanyName, PhoneNo, EventsOrganized):
    """Insert a new eventplanner record into the 'EventPlanner' table."""
    cursor = db.cursor()

    # Select the database
    cursor.execute("USE event_management_system")

    insert_eventplanner_query = """
    INSERT INTO EventPlanner (PlannerID, UserID, CompanyName, PhoneNo, EventsOrganized)
    VALUES (%s, %s, %s, %s, %s)
    """

    eventplanner_data = (PlannerID, UserID, CompanyName, PhoneNo, EventsOrganized)

    cursor.execute(insert_eventplanner_query, eventplanner_data)
    db.commit()
    st.write("EventPlanner record inserted successfully.")






def main():
    # Title and sidebar
    st.title("Event Management System 🎪")
    st.sidebar.header("Menu ")
    lott1 = loti( "https://assets6.lottiefiles.com/packages/lf20_olluraqu.json")
    lotipatient = loti("https://assets6.lottiefiles.com/packages/lf20_vPnn3K.json")
    db = create_connection()

    #create_database(db)

    #config['database'] = 'event_management_system'  # Update the database name
    #db = create_connection()

    #create_patients_table(db)
    #create_appointments_table(db)
    #modify_patients_table(db)

    menu = ["Home", "Create DB User", "Add User", "Show Users", 
        "Add Event", "Show Events", "Search and Edit Event",
        "Add Participant", "Show Participants", 
        "Add EventFeedback", "Show EventFeedbacks",
        "Add EventPlanner", "Show EventPlanners",
        "Book Ticket", "Show Tickets", "Cancel Ticket",
        "Show Analytics Data", "Show Event Statistics"]
    options = st.sidebar.radio("Select an Option :dart:",menu)
    if options== "Home":
        st.subheader("Welcome to Event Management System :smile:")
        st.write("Navigate from sidebar to access database")
        st_lottie(lott1,height=500)
        #st.image('hospital.jpg', width=600)

    elif options == "Create DB User":
        cursor = db.cursor()
        st.subheader("Create a New DB User")
        
        username = st.text_input("Enter username")
        password = st.text_input("Enter password", type="password")
        privileges = st.multiselect("Select Privileges", ["SELECT", "INSERT", "UPDATE", "DELETE"])
        
        if st.button("Create User"):
            try:
                # Create user
                cursor.execute(f"CREATE USER '{username}'@'localhost' IDENTIFIED BY '{password}';")
                
                # Grant privileges
                for privilege in privileges:
                    cursor.execute(f"GRANT {privilege} ON event_management_system.* TO '{username}'@'localhost';")
                
                st.success("User created successfully")
                # # Update the config with the new user's credentials
                # config['user'] = username
                # config['password'] = password

                # # Close the existing connection
                # db.close()

                # # Establish a new connection with the new user's credentials
                # db = create_connection()

            except Exception as e:
                st.error(f"Error: {e}")

    elif options == "Add User":
        st.subheader("Enter user details 👤")
        #st_lottie(lotipatient, height=200)
        cursor = db.cursor()

        cursor.execute("SELECT MAX(UserID) FROM User")
        last_user_id = cursor.fetchone()[0]
        UserID = last_user_id + 1 if last_user_id else 1

        Username = st.text_input("Enter Username", key="Username")
        Password = st.text_input("Enter Password", key="Password")
        Email = st.text_input("Enter Email", key="Email")
        PhoneNo = st.text_input("Enter PhoneNo", key="PhoneNo")
        FirstName = st.text_input("Enter FirstName", key="FirstName")
        LastName = st.text_input("Enter LastName", key="LastName")
        Role = st.text_input("Enter Role", key="Role")
        
        if st.button("Add User"):
            cursor = db.cursor()
            select_query = """
            SELECT * FROM User WHERE UserID=%s
            """
            cursor.execute(select_query, (UserID,))
            existing_user = cursor.fetchone()
            if existing_user:
                st.warning("A user with the same UserID already exist")
            else:
                insert_user_record(db, UserID, Username, Password, Email, PhoneNo, FirstName, LastName, Role)

    elif options == "Show Users":
        cursor = db.cursor()
        select_query = """
        SELECT * FROM User
        """
        cursor.execute(select_query)
        records = cursor.fetchall()

        if records:
            st.subheader("All User Records 👥")
            df = pd.DataFrame(records, columns=['UserID', 'Username', 'Password', 'Email', 'PhoneNo', 'FirstName', 'LastName', 'Role'])
            st.dataframe(df)
        else:
            st.write("No users found") 

    elif options == "Add Event":
        st.subheader("Enter event details")
        cursor = db.cursor()

        cursor.execute("SELECT MAX(EventID) FROM Event")
        last_event_id = cursor.fetchone()[0]
        event_id = last_event_id + 1 if last_event_id else 1

        event_name = st.text_input("Enter event name", key="event_name")
        event_description = st.text_input("Enter event description", key="event_description")
        event_date = st.date_input("Enter event date", key="event_date")
        event_time = st.time_input("Enter event time", key="event_time")
        location = st.text_input("Enter location", key="location")
        max_capacity = st.number_input("Enter max capacity", key="max_capacity")
        event_type = st.text_input("Enter event type", key="event_type")
        event_status = st.text_input("Enter event status", key="event_status")

        if st.button("Add Event"):
            insert_event_record(db, event_id, event_name, event_description, event_date, event_time, location, max_capacity, event_type, event_status) 

    elif options == "Show Events":
        cursor = db.cursor()
        select_query = """
        SELECT EventID, EventName, EventDescription, EventDate, CAST(EventTime AS CHAR) as EventTime, Location, MaxCapacity, EventType, EventStatus FROM Event
        """
        cursor.execute(select_query)
        records = cursor.fetchall()

        if records:
            st.subheader("All Event Records")
            df = pd.DataFrame(records, columns=['EventID', 'EventName', 'EventDescription', 'EventDate', 'EventTime', 'Location', 'MaxCapacity', 'EventType', 'EventStatus'])
            st.dataframe(df)
        else:
            st.write("No events found")
    
    elif options == "Search and Edit Event":
        search_option = st.selectbox("Select search option", ["ID", "Name", "Date"], key="search_option")
        search_value = st.text_input("Enter search value", key="search_value")

        if st.button("Search"):
            if search_option == "ID":
                event = fetch_event_by_id(db, search_value)
            elif search_option == "Name":
                event = fetch_event_by_name(db, search_value)
            elif search_option == "Date":
                event = fetch_event_by_date(db, search_value)

            if event:
                st.subheader("Event Details")
                df = pd.DataFrame([event], columns=['ID', 'Name', 'Description', 'Date', 'Time', 'Location', 'Max Capacity', 'Type', 'Status'])
                st.dataframe(df)
                st.session_state.edit_event = event
            else:
                st.write("Event not found")

        if 'edit_event' in st.session_state:
            edit_event(db)

    elif options == "Add Participant":
        st.subheader("Enter participant details")
        cursor = db.cursor()

        cursor.execute("SELECT MAX(ParticipantID) FROM Participant")
        last_participant_id = cursor.fetchone()[0]
        ParticipantID = last_participant_id + 1 if last_participant_id else 1

        select_query = """
        SELECT UserID FROM User
        """
        cursor.execute(select_query)
        user_ids = [item[0] for item in cursor.fetchall()]
        UserID = st.selectbox("Select UserID", user_ids, key="UserID")

        DateOfBirth = st.date_input("Enter DateOfBirth", key="DateOfBirth")
        PhoneNo = st.text_input("Enter PhoneNo", key="PhoneNo")
        Address = st.text_input("Enter Address", key="Address")
        PaymentInfo = st.text_input("Enter PaymentInfo", key="PaymentInfo")
        if st.button("Add Participant"):
            select_query = """
            SELECT * FROM Participant WHERE ParticipantID=%s
            """
            cursor.execute(select_query, (ParticipantID,))
            existing_participant = cursor.fetchone()
            if existing_participant:
                st.warning("A participant with the same ParticipantID already exist")
            else:
                insert_participant_record(db, ParticipantID, UserID, DateOfBirth, PhoneNo, Address, PaymentInfo)

    elif options == "Show Participants":
        cursor = db.cursor()
        select_query = """
        SELECT * FROM Participant
        """
        cursor.execute(select_query)
        records = cursor.fetchall()

        if records:
            st.subheader("All Participant Records")
            df = pd.DataFrame(records, columns=['ParticipantID', 'UserID', 'DateOfBirth', 'PhoneNo', 'Address', 'PaymentInfo'])
            st.dataframe(df)
        else:
            st.write("No participants found")
    
    elif options == "Add EventFeedback":
        st.subheader("Enter event feedback details")
        cursor = db.cursor()
        cursor.execute("SELECT MAX(FeedbackID) FROM EventFeedback")
        last_feedback_id = cursor.fetchone()[0]
        FeedbackID = last_feedback_id + 1 if last_feedback_id else 1

        select_query = """
        SELECT EventID FROM Event
        """
        cursor.execute(select_query)
        event_ids = [item[0] for item in cursor.fetchall()]
        EventID = st.selectbox("Select EventID", event_ids, key="EventID")

        select_query = """
        SELECT ParticipantID FROM Participant
        """
        cursor.execute(select_query)
        participant_ids = [item[0] for item in cursor.fetchall()]
        ParticipantID = st.selectbox("Select ParticipantID", participant_ids, key="ParticipantID")

        Rating = st.number_input("Enter Rating 0-5", key="Rating")
        Comments = st.text_input("Enter Comments", key="Comments")
        FeedbackDate = st.date_input("Enter FeedbackDate", key="FeedbackDate")
        if st.button("Add EventFeedback"):
            select_query = """
            SELECT * FROM EventFeedback WHERE FeedbackID=%s
            """
            cursor.execute(select_query, (FeedbackID,))
            existing_eventfeedback = cursor.fetchone()
            if existing_eventfeedback:
                st.warning("A eventfeedback with the same FeedbackID already exist")
            else:
                insert_eventfeedback_record(db, FeedbackID, EventID, ParticipantID, Rating, Comments, FeedbackDate)

    elif options == "Show EventFeedbacks":
        cursor = db.cursor()
        select_query = """
        SELECT * FROM EventFeedback
        """
        cursor.execute(select_query)
        records = cursor.fetchall()

        if records:
            st.subheader("All EventFeedback Records")
            df = pd.DataFrame(records, columns=['FeedbackID', 'EventID', 'ParticipantID', 'Rating', 'Comments', 'FeedbackDate'])
            st.dataframe(df)
        else:
            st.write("No eventfeedbacks found")

    elif options == "Add EventPlanner":
        st.subheader("Enter event planner details :hospital:")
        cursor = db.cursor()
        cursor.execute("SELECT MAX(PlannerID) FROM EventPlanner")  
        last_planner_id = cursor.fetchone()[0]
        PlannerID = last_planner_id + 1 if last_planner_id else 1

        select_query = """
        SELECT UserID FROM User
        """
        cursor.execute(select_query)
        user_ids = [item[0] for item in cursor.fetchall()]
        UserID = st.selectbox("Select UserID", user_ids, key="UserID")

        CompanyName = st.text_input("Enter CompanyName", key="CompanyName")
        PhoneNo = st.text_input("Enter PhoneNo", key="PhoneNo")
        EventsOrganized = st.number_input("Enter EventsOrganized", key="EventsOrganized")

        if st.button("Add EventPlanner"):
            select_query = """
            SELECT * FROM EventPlanner WHERE PlannerID=%s
            """
            cursor.execute(select_query, (PlannerID,))
            existing_eventplanner = cursor.fetchone()
            if existing_eventplanner:
                st.warning("A eventplanner with the same PlannerID already exist")
            else:
                insert_eventplanner_record(db, PlannerID, UserID, CompanyName, PhoneNo, EventsOrganized)

    elif options == "Show EventPlanners":
        cursor = db.cursor()
        select_query = """
        SELECT * FROM EventPlanner
        """
        cursor.execute(select_query)
        records = cursor.fetchall()

        if records:
            st.subheader("All EventPlanner Records")
            df = pd.DataFrame(records, columns=['PlannerID', 'UserID', 'CompanyName', 'PhoneNo', 'EventsOrganized'])
            st.dataframe(df)
        else:
            st.write("No eventplanners found")

    elif options == "Book Ticket":
        st.subheader("Book a Ticket")
        cursor = db.cursor()
        # Get list of event IDs
        cursor.execute("SELECT EventID FROM Event")
        event_ids = [item[0] for item in cursor.fetchall()]

        # Get list of participant IDs
        cursor.execute("SELECT ParticipantID FROM Participant")
        participant_ids = [item[0] for item in cursor.fetchall()]

        # User inputs
        cursor.execute("SELECT MAX(TicketID) FROM Ticket")
        last_ticket_id = cursor.fetchone()[0]
        TicketID = last_ticket_id + 1 if last_ticket_id else 1
        selected_event_id = st.selectbox("Select Event ID", event_ids)
        selected_participant_id = st.selectbox("Select Participant ID", participant_ids)
        ticket_prices = {
            "Regular": 150.0,
            "VIP": 350.0,
            "Early Bird": 125.0,
            "Student": 100.0,
            "Group/Corporate": 1000.0
        }
        ticket_type = st.selectbox("Select Ticket Type", list(ticket_prices.keys()))
        ticket_price = ticket_prices[ticket_type]
        st.write(f"Price for {ticket_type} ticket: Rs.{ticket_price}")
        payment_status = st.selectbox("Select Payment Status", ["Paid", "Not Paid"])

        if st.button("Book Ticket"):
            select_query = """
            SELECT * FROM Ticket WHERE TicketID=%s
            """
            cursor.execute(select_query, (TicketID,))
            existing_ticket = cursor.fetchone()
            if existing_ticket:
                st.warning("A ticket with the same TicketID already exist")
            else:
                insert_query = """
                INSERT INTO Ticket (TicketID, EventID, ParticipantID, TicketType, TicketPrice, PurchaseDate, PaymentStatus) 
                VALUES (%s, %s, %s, %s, %s, NOW(), %s)
                """
                cursor.execute(insert_query, (TicketID, selected_event_id, selected_participant_id, ticket_type, ticket_price, payment_status))
                db.commit()  # commit the transaction
                st.success("Ticket booked successfully!")

    elif options == "Show Tickets":
        cursor = db.cursor()
        select_query = """
        SELECT Ticket.TicketID, Ticket.EventID, Ticket.ParticipantID, Ticket.TicketType, Ticket.TicketPrice, Ticket.PurchaseDate, Ticket.PaymentStatus, Event.EventName 
        FROM Ticket
        INNER JOIN Event ON Ticket.EventID = Event.EventID
        """
        cursor.execute(select_query)
        records = cursor.fetchall()

        if records:
            st.subheader("All Ticket Records")
            df = pd.DataFrame(records, columns=['TicketID', 'EventID', 'ParticipantID', 'TicketType', 'TicketPrice', 'PurchaseDate', 'PaymentStatus', 'EventName'])
            st.dataframe(df)
        else:
            st.write("No tickets found")

    elif options == "Cancel Ticket":
        st.subheader("Cancel a Ticket")
        cursor = db.cursor()
        # Get list of ticket IDs
        cursor.execute("SELECT TicketID FROM Ticket")
        ticket_ids = [item[0] for item in cursor.fetchall()]

        # User inputs
        selected_ticket_id = st.selectbox("Select Ticket ID", ticket_ids)

        if st.button("Cancel Ticket"):
            delete_query = """
            DELETE FROM Ticket WHERE TicketID=%s
            """
            cursor.execute(delete_query, (selected_ticket_id,))
            db.commit()  # commit the transaction
            st.success("Ticket cancelled successfully!")

    elif options == "Show Analytics Data":
        cursor = db.cursor()
        select_query = """
        SELECT * FROM AnalyticsData
        """
        print("Executing query:", select_query)  # Debug print
        cursor.execute(select_query)
        records = cursor.fetchall()
        print("Query results:", records)  # Debug print

        if records:
            st.subheader("All Analytics Data Records")
            df = pd.DataFrame(records, columns=['AnalyticsID', 'EventID', 'AttendanceCount', 'Revenue', 'ReportDate'])
            st.dataframe(df)
            
            # nested query to calculate average revenue of top 5 events by revenue
            avg_revenue_query = """
            SELECT AVG(Revenue) FROM (
                SELECT Revenue FROM AnalyticsData ORDER BY Revenue DESC LIMIT 10
            ) AS TopEvents
            """
            cursor.execute(avg_revenue_query)
            avg_revenue = cursor.fetchone()[0]

            st.write(f"Average Revenue of Top 5 Events by Revenue: {avg_revenue}")
        else:
            st.write("No analytics data found") 

    elif options == "Show Event Statistics":
        st.subheader("Select an event to show its analytics")
        cursor = db.cursor()
        select_query = """
        SELECT EventID FROM Event
        """
        cursor.execute(select_query)
        event_ids = [item[0] for item in cursor.fetchall()]
        selected_event_id = st.selectbox("Select EventID", event_ids, key="selected_event_id")

        if st.button("Show Analytics"):
            # Calculate total revenue
            select_query = """
            SELECT CalculateTotalRevenue(%s)
            """
            cursor.execute(select_query, (selected_event_id,))
            total_revenue = cursor.fetchone()[0]

            # Get average feedback rating
            select_query = """
            SELECT GetEventFeedbackAverageRating(%s)
            """
            cursor.execute(select_query, (selected_event_id,))
            avg_rating = cursor.fetchone()[0]

            # Get attendance count
            select_query = """
            SELECT AttendanceCount FROM AnalyticsData WHERE EventID = %s
            """
            cursor.execute(select_query, (selected_event_id,))
            result = cursor.fetchone()
            attendance_count = result[0] if result is not None else 0

            # Count tickets sold
            select_query = """
            SELECT CountTicketsSold(%s)
            """
            cursor.execute(select_query, (selected_event_id,))
            result = cursor.fetchone()
            tickets_sold = result[0] if result is not None else 0

            st.write(f"Total Revenue: {total_revenue}")
            st.write(f"Average Feedback Rating: {avg_rating}")
            st.write(f"Attendance Count: {attendance_count}")
            st.write(f"Tickets Sold: {tickets_sold}")              

    db.close()

if __name__ == "__main__":
    main()
