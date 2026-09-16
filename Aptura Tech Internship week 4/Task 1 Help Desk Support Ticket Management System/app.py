import streamlit as st

from database.database import initialize_database
from models.ticket import Ticket
from models.staff import Staff

from services.ticket_service import TicketService
from services.staff_service import StaffService
from services.report_service import ReportService

from utils.validation import validate_ticket_data
from utils.logger import logger


# PAGE CONFIGURATION

st.set_page_config(
    page_title="HelpDesk Support System",
    page_icon="🎫",
    layout="wide"
)


# INITIALIZE DATABASE

initialize_database()


# SERVICES

ticket_service = TicketService()
staff_service = StaffService()
report_service = ReportService(ticket_service)


# CONSTANTS

CATEGORIES = [
    "Network",
    "Software",
    "Hardware",
    "Account",
    "Email",
    "Other"
]

PRIORITIES = [
    "Low",
    "Medium",
    "High",
    "Critical"
]

STATUSES = [
    "Open",
    "In Progress",
    "Resolved",
    "Closed"
]

AVAILABILITY = [
    "Available",
    "Busy",
    "Offline"
]


# SESSION STATE

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"


def change_page(page):
    st.session_state.page = page


# CUSTOM CSS

st.markdown("""
<style>

/* MAIN APP*/

.stApp {
    background:
        radial-gradient(
            circle at 0% 0%,
            rgba(99, 102, 241, 0.12),
            transparent 30%
        ),
        radial-gradient(
            circle at 100% 0%,
            rgba(14, 165, 233, 0.10),
            transparent 28%
        ),
        linear-gradient(
            180deg,
            #f5f7ff 0%,
            #f8fafc 45%,
            #f1f5f9 100%
        );
}

.block-container {
    max-width: 1400px;
    padding-top: 1.5rem;
    padding-bottom: 4rem;
}


/* NAVBAR */

.navbar {
    background:
        linear-gradient(
            135deg,
            #312e81 0%,
            #4f46e5 48%,
            #2563eb 100%
        );

    padding: 24px 30px;
    border-radius: 0 0 22px 22px;
    margin-bottom: 22px;

    box-shadow:
        0 12px 35px rgba(79, 70, 229, 0.22);
}

.brand {
    color: white;
    font-size: 32px;
    font-weight: 850;
    letter-spacing: -0.8px;
}

.brand-subtitle {
    color: rgba(255,255,255,0.88);
    font-size: 16px;
    font-weight: 500;
    margin-top: 5px;
}


/* NAVIGATION BUTTONS */

div.stButton > button {
    min-height: 50px;

    border-radius: 13px;
    border: 1px solid #dbe3ef;

    background: rgba(255,255,255,0.96);
    color: #1e293b;

    font-size: 17px;
    font-weight: 650;

    box-shadow:
        0 3px 10px rgba(15,23,42,0.04);

    transition:
        all 0.2s ease;
}

div.stButton > button:hover {
    border-color: #6366f1;
    color: #4338ca;

    background:
        linear-gradient(
            135deg,
            #eef2ff,
            #eff6ff
        );

    transform: translateY(-2px);

    box-shadow:
        0 8px 18px rgba(79,70,229,0.13);
}


/* HERO SECTION */

.hero {
    position: relative;

    background:
        linear-gradient(
            135deg,
            #ffffff 0%,
            #f5f7ff 55%,
            #eef2ff 100%
        );

    padding: 38px 42px;
    border-radius: 22px;

    border: 1px solid #dbe4ff;

    margin-top: 24px;
    margin-bottom: 28px;

    box-shadow:
        0 12px 30px rgba(15,23,42,0.06);

    overflow: hidden;
}

.hero::after {
    content: "";
    position: absolute;

    width: 180px;
    height: 180px;

    right: -55px;
    top: -65px;

    background:
        radial-gradient(
            circle,
            rgba(99,102,241,0.15),
            transparent 70%
        );

    border-radius: 50%;
}

.hero-title {
    color: #17164c;

    font-size: 40px;
    line-height: 1.15;

    font-weight: 850;

    letter-spacing: -1px;

    margin-bottom: 10px;
}

.hero-text {
    color: #64748b;

    font-size: 18px;
    line-height: 1.6;

    font-weight: 450;

    margin: 0;
}


/*METRIC CARDS*/

.metric-card {
    position: relative;

    background: white;

    padding: 24px;

    border-radius: 18px;

    border: 1px solid #e2e8f0;

    min-height: 125px;

    box-shadow:
        0 7px 22px rgba(15,23,42,0.055);

    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease;
}

.metric-card:hover {
    transform: translateY(-4px);

    box-shadow:
        0 14px 30px rgba(79,70,229,0.12);
}

.metric-title {
    color: #64748b;

    font-size: 15px;
    font-weight: 700;

    text-transform: uppercase;

    letter-spacing: 0.7px;
}

.metric-value {
    color: #172033;

    font-size: 36px;
    font-weight: 850;

    margin-top: 8px;
}


/*STREAMLIT METRIC WIDGETS*/

div[data-testid="stMetric"] {
    background: white;

    padding: 22px 24px;

    border-radius: 18px;

    border: 1px solid #e2e8f0;

    box-shadow:
        0 7px 22px rgba(15,23,42,0.055);

    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease;
}

div[data-testid="stMetric"]:hover {
    transform: translateY(-3px);

    box-shadow:
        0 12px 26px rgba(79,70,229,0.11);
}

div[data-testid="stMetricLabel"] {
    color: #64748b !important;

    font-size: 15px !important;
    font-weight: 700 !important;
}

div[data-testid="stMetricValue"] {
    color: #172033 !important;

    font-size: 34px !important;
    font-weight: 850 !important;
}


/*SECTION HEADINGS */

h1 {
    color: #17164c !important;
    font-size: 36px !important;
    font-weight: 850 !important;
}

h2 {
    color: #1e293b !important;
    font-size: 28px !important;
    font-weight: 800 !important;
}

h3 {
    color: #1e293b !important;
    font-size: 22px !important;
    font-weight: 750 !important;
}

p {
    font-size: 16px;
}


/* FORMS / CONTAINERS */

[data-testid="stForm"] {
    background: white;

    padding: 28px;

    border-radius: 20px;

    border: 1px solid #e2e8f0;

    box-shadow:
        0 9px 28px rgba(15,23,42,0.055);
}


/* INPUT FIELDS */

.stTextInput input,
.stTextArea textarea {
    border-radius: 11px !important;

    border: 1px solid #cbd5e1 !important;

    font-size: 16px !important;

    padding: 10px 13px !important;
}

.stTextInput input:focus,
.stTextArea textarea:focus {
    border-color: #6366f1 !important;

    box-shadow:
        0 0 0 3px rgba(99,102,241,0.12) !important;
}


/* SELECTBOX */

div[data-baseweb="select"] > div {
    border-radius: 11px !important;

    border-color: #cbd5e1 !important;

    font-size: 16px !important;
}


/* NUMBER INPUT */

input[type="number"] {
    font-size: 16px !important;
}


/* PRIMARY BUTTONS */

button[kind="primary"],
button[kind="primaryFormSubmit"] {

    background:
        linear-gradient(
            135deg,
            #4f46e5,
            #2563eb
        ) !important;

    color: white !important;

    border: none !important;

    border-radius: 11px !important;

    min-height: 46px !important;

    font-size: 16px !important;

    font-weight: 700 !important;

    box-shadow:
        0 6px 16px rgba(79,70,229,0.22);

    transition:
        all 0.2s ease;
}

button[kind="primary"]:hover,
button[kind="primaryFormSubmit"]:hover {

    background:
        linear-gradient(
            135deg,
            #4338ca,
            #1d4ed8
        ) !important;

    transform: translateY(-2px);

    box-shadow:
        0 9px 20px rgba(79,70,229,0.28);
}


/* DATAFRAMES / TABLES */

[data-testid="stDataFrame"] {

    border-radius: 16px;

    overflow: hidden;

    border: 1px solid #dfe5ef;

    box-shadow:
        0 6px 20px rgba(15,23,42,0.045);
}


/* TABS */

button[data-baseweb="tab"] {

    font-size: 16px !important;

    font-weight: 650 !important;
}

button[data-baseweb="tab"][aria-selected="true"] {

    color: #4f46e5 !important;

    font-weight: 750 !important;
}


/* ALERTS */

div[data-testid="stAlert"] {

    border-radius: 13px;

    font-size: 15px;
}


/*  DIVIDERS */

hr {
    border-color: #dbe3ef;

    margin-top: 24px;
    margin-bottom: 24px;
}


/* CHECKBOX */

div[data-testid="stCheckbox"] label {

    font-size: 15px !important;
}


/* CAPTION / SMALL TEXT */

.stCaption {

    font-size: 14px !important;

    color: #64748b !important;
}


/* SCROLLBAR */

::-webkit-scrollbar {
    width: 9px;
}

::-webkit-scrollbar-track {
    background: #f1f5f9;
}

::-webkit-scrollbar-thumb {
    background: #c7d2fe;
    border-radius: 10px;
}

::-webkit-scrollbar-thumb:hover {
    background: #818cf8;
}

</style>
""", unsafe_allow_html=True)

# NAVBAR

st.markdown("""
<div class="navbar">
    <div class="brand">🎫 HelpDesk</div>
    <div class="brand-subtitle">
        Smart Support Ticket Management • Task Management Portal
    </div>
</div>
""", unsafe_allow_html=True)


nav1, nav2, nav3, nav4, nav5 = st.columns(5)

with nav1:
    if st.button(
        "🏠 Dashboard",
        key="nav_dashboard",
        use_container_width=True
    ):
        change_page("Dashboard")
        st.rerun()

with nav2:
    if st.button(
        "➕ New Ticket",
        key="nav_new_ticket",
        use_container_width=True
    ):
        change_page("New Ticket")
        st.rerun()

with nav3:
    if st.button(
        "🎫 Tickets",
        key="nav_tickets",
        use_container_width=True
    ):
        change_page("Tickets")
        st.rerun()

with nav4:
    if st.button(
        "👥 Staff",
        key="nav_staff",
        use_container_width=True
    ):
        change_page("Staff")
        st.rerun()

with nav5:
    if st.button(
        "📊 Reports",
        key="nav_reports",
        use_container_width=True
    ):
        change_page("Reports")
        st.rerun()


st.divider()


# DASHBOARD

if st.session_state.page == "Dashboard":

    st.markdown("""
    <div class="hero">
        <div class="hero-title">Help Desk Dashboard</div>
        <p class="hero-text">
            Monitor support tickets, staff assignments,
            priorities and ticket activity.
        </p>
    </div>
    """, unsafe_allow_html=True)

    summary = report_service.get_ticket_summary()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">🎫 Total Tickets</div>
            <div class="metric-value">{summary["total"]}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">🟢 Open Tickets</div>
            <div class="metric-value">{summary["open"]}</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">🔵 In Progress</div>
            <div class="metric-value">{summary["in_progress"]}</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-title">✅ Resolved</div>
            <div class="metric-value">{summary["resolved"]}</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    col5, col6, col7 = st.columns(3)

    with col5:
        st.metric(
            "Closed Tickets",
            summary["closed"]
        )

    with col6:
        st.metric(
            "High Priority",
            summary["high_priority"]
        )

    with col7:
        st.metric(
            "Critical Priority",
            summary["critical_priority"]
        )

    st.subheader("Recent Tickets")

    tickets = ticket_service.get_all_tickets()

    if tickets:

        display_data = []

        for ticket in tickets:
            display_data.append({
                "Ticket ID": ticket[0],
                "Requester": ticket[1],
                "Title": ticket[3],
                "Category": ticket[4],
                "Priority": ticket[5],
                "Status": ticket[7],
                "Assigned To": ticket[8] or "Unassigned",
                "Created": ticket[9]
            })

        st.dataframe(
            display_data,
            use_container_width=True,
            hide_index=True
        )

    else:
        st.info("No tickets have been created yet.")



# CREATE NEW TICKET

elif st.session_state.page == "New Ticket":

    st.markdown("""
    <div class="hero">
        <div class="hero-title">Create New Ticket</div>
        <p class="hero-text">
            Submit a new support request for the help desk.
        </p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("create_ticket_form"):

        col1, col2 = st.columns(2)

        with col1:

            requester_name = st.text_input(
                "Requester Name",
                placeholder="Enter requester name"
            )

            email = st.text_input(
                "Email",
                placeholder="example@gmail.com"
            )

            title = st.text_input(
                "Issue Title",
                placeholder="Enter issue title"
            )

            category = st.selectbox(
                "Category",
                ["Select Category"] + CATEGORIES
            )

        with col2:

            priority = st.selectbox(
                "Priority",
                ["Select Priority"] + PRIORITIES
            )

            description = st.text_area(
                "Description",
                placeholder="Describe the issue..."
            )

            available_staff = staff_service.get_available_staff()

            staff_options = ["Unassigned"]

            for staff in available_staff:
                staff_options.append(
                    f"{staff[0]} - {staff[1]}"
                )

            assigned_staff = st.selectbox(
                "Assign To",
                staff_options
            )

        submitted = st.form_submit_button(
            "🎫 Create Ticket",
            use_container_width=True
        )

        if submitted:

            if category == "Select Category":
                category = ""

            if priority == "Select Priority":
                priority = ""

            assigned_to = None

            if assigned_staff != "Unassigned":
                assigned_to = assigned_staff.split(" - ")[0]

            valid, message = validate_ticket_data(
                requester_name,
                email,
                title,
                category,
                priority,
                description,
                CATEGORIES,
                PRIORITIES
            )

            if not valid:
                st.error(message)

            else:

                try:

                    ticket = Ticket(
                        ticket_id=None,
                        requester_name=requester_name,
                        email=email,
                        title=title,
                        category=category,
                        priority=priority,
                        description=description,
                        status="Open",
                        assigned_to=assigned_to,
                        created_at=None,
                        updated_at=None,
                        resolved_at=None
                    )

                    created_ticket = ticket_service.create_ticket(ticket)

                    st.success(
                        f"Ticket {created_ticket.ticket_id} created successfully!"
                    )

                    logger.info(
                        f"New ticket created from UI: "
                        f"{created_ticket.ticket_id}"
                    )

                except Exception as error:

                    logger.error(
                        f"Ticket creation failed: {error}"
                    )

                    st.error(
                        f"Unable to create ticket: {error}"
                    )


# TICKET MANAGEMENT

elif st.session_state.page == "Tickets":

    st.markdown("""
    <div class="hero">
        <div class="hero-title">Ticket Management</div>
        <p class="hero-text">
            Search, update, assign and manage support tickets.
        </p>
    </div>
    """, unsafe_allow_html=True)

    tickets = ticket_service.get_all_tickets()

    if not tickets:
        st.info("No tickets available.")
    else:

        ticket_ids = [
            ticket[0]
            for ticket in tickets
        ]

        selected_ticket_id = st.selectbox(
            "Select Ticket",
            ["Select Ticket"] + ticket_ids
        )

        if selected_ticket_id != "Select Ticket":

            ticket = ticket_service.get_ticket(
                selected_ticket_id
            )

            if ticket:

                st.subheader(
                    f"Ticket {selected_ticket_id}"
                )

                col1, col2 = st.columns(2)

                with col1:

                    st.write(
                        f"**Requester:** {ticket[1]}"
                    )

                    st.write(
                        f"**Email:** {ticket[2]}"
                    )

                    st.write(
                        f"**Title:** {ticket[3]}"
                    )

                    st.write(
                        f"**Category:** {ticket[4]}"
                    )

                with col2:

                    st.write(
                        f"**Priority:** {ticket[5]}"
                    )

                    st.write(
                        f"**Status:** {ticket[7]}"
                    )

                    st.write(
                        f"**Assigned To:** "
                        f"{ticket[8] or 'Unassigned'}"
                    )

                    st.write(
                        f"**Created:** {ticket[9]}"
                    )

                st.write("### Description")
                st.info(ticket[6])

                st.divider()

                st.subheader("Update Ticket")

                with st.form("update_ticket_form"):

                    col1, col2 = st.columns(2)

                    with col1:

                        new_status = st.selectbox(
                            "Status",
                            ["No Change"] + STATUSES
                        )

                        new_priority = st.selectbox(
                            "Priority",
                            ["No Change"] + PRIORITIES
                        )

                    with col2:

                        staff_list = staff_service.get_all_staff()

                        staff_options = ["No Change", "Unassigned"]

                        for staff in staff_list:
                            staff_options.append(
                                f"{staff[0]} - {staff[1]}"
                            )

                        new_staff = st.selectbox(
                            "Assign Staff",
                            staff_options
                        )

                        resolution_note = st.text_area(
                            "Resolution Note",
                            placeholder="Add resolution/update note..."
                        )

                    update_button = st.form_submit_button(
                        "💾 Update Ticket",
                        use_container_width=True
                    )

                    if update_button:

                        status_value = None
                        priority_value = None
                        staff_value = None

                        if new_status != "No Change":
                            status_value = new_status

                        if new_priority != "No Change":
                            priority_value = new_priority

                        if new_staff != "No Change":

                            if new_staff == "Unassigned":
                                staff_value = ""

                            else:
                                staff_value = new_staff.split(
                                    " - "
                                )[0]

                        if (
                            status_value is None
                            and priority_value is None
                            and staff_value is None
                            and not resolution_note.strip()
                        ):
                            st.warning(
                                "Please make at least one change."
                            )

                        else:

                            try:

                                ticket_service.update_ticket(
                                    selected_ticket_id,
                                    status=status_value,
                                    priority=priority_value,
                                    assigned_to=staff_value,
                                    resolution_note=resolution_note.strip()
                                )

                                st.success(
                                    "Ticket updated successfully."
                                )


                            except Exception as error:

                                logger.error(
                                    f"Ticket update failed: {error}"
                                )

                                st.error(
                                    f"Update failed: {error}"
                                )

                st.divider()

                st.subheader("Ticket History")

                updates = ticket_service.get_ticket_updates(
                    selected_ticket_id
                )

                if updates:

                    history_data = []

                    for update in updates:
                        history_data.append({
                            "Type": update[2],
                            "Details": update[3],
                            "Date & Time": update[4]
                        })

                    st.dataframe(
                        history_data,
                        use_container_width=True,
                        hide_index=True
                    )

                else:
                    st.info(
                        "No update history available."
                    )
                st.divider()

                st.subheader("Delete Ticket")

                delete_confirm = st.checkbox(
                    "I confirm that I want to permanently delete this ticket."
                )

                if st.button(
                    "🗑️ Delete Ticket",
                    type="primary",
                    use_container_width=True
                ):

                    if not delete_confirm:
                        st.warning(
                            "Please confirm before deleting the ticket."
                        )

                    else:

                        try:

                            deleted = ticket_service.delete_ticket(
                                selected_ticket_id
                            )

                            if deleted:
                                st.success(
                                    f"Ticket {selected_ticket_id} deleted successfully."
                                )
                                

                            else:
                                st.error(
                                    "Ticket could not be deleted."
                                )

                        except Exception as error:

                            logger.error(
                                f"Ticket deletion failed: {error}"
                            )

                            st.error(
                                f"Delete failed: {error}"
                            )

# STAFF MANAGEMENT

elif st.session_state.page == "Staff":

    st.markdown("""
    <div class="hero">
        <div class="hero-title">Staff Management</div>
        <p class="hero-text">
            Manage support staff and their availability.
        </p>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs([
        "➕ Add Staff",
        "👥 Staff Records"
    ])

    # ADD STAFF

    with tab1:

        with st.form("add_staff_form"):

            col1, col2 = st.columns(2)

            with col1:

                staff_id = st.text_input(
                    "Staff ID",
                    placeholder="S001"
                )

                staff_name = st.text_input(
                    "Name",
                    placeholder="Enter staff name"
                )

                staff_email = st.text_input(
                    "Email",
                    placeholder="staff@gmail.com"
                )

            with col2:

                department = st.text_input(
                    "Department",
                    placeholder="IT Support"
                )

                role = st.text_input(
                    "Role",
                    placeholder="Support Agent"
                )

                availability = st.selectbox(
                    "Availability",
                    AVAILABILITY
                )

            add_button = st.form_submit_button(
                "➕ Add Staff",
                use_container_width=True
            )

            if add_button:

                if not staff_id.strip():
                    st.error("Staff ID is required.")

                elif not staff_name.strip():
                    st.error("Staff name is required.")

                elif not staff_email.strip():
                    st.error("Email is required.")

                elif not department.strip():
                    st.error("Department is required.")

                elif not role.strip():
                    st.error("Role is required.")

                else:

                    try:

                        staff = Staff(
                            staff_id=staff_id.strip(),
                            name=staff_name.strip(),
                            email=staff_email.strip(),
                            department=department.strip(),
                            role=role.strip(),
                            availability=availability
                        )

                        staff_service.add_staff(staff)

                        st.success(
                            "Staff member added successfully."
                        )

                        logger.info(
                            f"Staff added from UI: {staff_id}"
                        )

                    except Exception as error:

                        logger.error(
                            f"Staff creation failed: {error}"
                        )

                        st.error(
                            f"Unable to add staff: {error}"
                        )

    # STAFF RECORDS

    with tab2:

        staff_members = staff_service.get_all_staff()

    if staff_members:
        staff_data = []

    for staff in staff_members:

        staff_data.append({
            "Staff ID": staff[0],
            "Name": staff[1],
            "Email": staff[2],
            "Department": staff[3],
            "Role": staff[4],
            "Availability": staff[5]
        })

    st.dataframe(
        staff_data,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    st.subheader("Delete Staff")

    staff_ids = [staff[0] for staff in staff_members]

    selected_staff_id = st.selectbox(
        "Select Staff Member",
        staff_ids,
        key="delete_staff_select"
    )

    delete_staff_confirm = st.checkbox(
        "I confirm that I want to permanently delete this staff member.",
        key="delete_staff_confirm"
    )

    if st.button(
        "🗑️ Delete Staff",
        type="primary",
        use_container_width=True,
        key="delete_staff_button"
    ):

        if not delete_staff_confirm:

            st.warning(
                "Please confirm before deleting the staff member."
            )

        else:

            try:

                deleted = staff_service.delete_staff(
                    selected_staff_id
                )

                if deleted:

                    st.success(
                        f"Staff member {selected_staff_id} deleted successfully."
                    )

                    logger.info(
                        f"Staff deleted from UI: {selected_staff_id}"
                    )

                    

                else:

                    st.error(
                        "Staff member could not be deleted."
                    )

            except Exception as error:

                logger.error(
                    f"Staff deletion failed: {error}"
                )

                st.error(
                    f"Delete failed: {error}"
                )
                
                if staff_members:
                    staff_data = []
                    for staff in staff_members:
                        staff_data.append({
                            
                            "Staff ID": staff[0],
                            "Name": staff[1],
                            "Email": staff[2],
                            "Department": staff[3],
                            "Role": staff[4],
                            "Availability": staff[5]
                            })
                        
                        st.dataframe(
                            staff_data,
                            use_container_width=True,
                            hide_index=True
                        )
                        st.divider()

                        st.subheader("Delete Staff")
                        staff_ids = [staff[0] for staff in staff_members]
                        
                        selected_staff_id = st.selectbox(
                              "Select Staff Member",
                              staff_ids,
                              key="delete_staff_select"
                              
                              )
                        
                        delete_staff_confirm = st.checkbox(

                            "I confirm that I want to permanently delete this staff member.",
                            key="delete_staff_confirm"
                            )
                        
                        if st.button(
                            
                            "🗑️ Delete Staff",
                            type="primary",
                            use_container_width=True,
                            key="delete_staff_button"
                            ):
                                                      

                            if not delete_staff_confirm:
                                st.warning(
                                    "Please confirm before deleting the staff member."
                                )
                                
                            else:
                                try:                                                               
                                    deleted = staff_service.delete_staff(  
                                    selected_staff_id
                                )
                                    
                                    if deleted:
                                        st.success(                                                                                       
                                            f"Staff member {selected_staff_id} deleted successfully."
                                )
                                        
                                        logger.info(
                                            f"Staff deleted from UI: {selected_staff_id}"
                                            )
                                        
                                    else:
                                        st.error(
                                            "Staff member could not be deleted."
                                            )                                       
                                       
                                except Exception as error:
                                    logger.error(
                                        f"Staff deletion failed: {error}"
                                    )
                                    
                                    st.error(
                                        f"Delete failed: {error}"
                                        )
                                else:
                                    st.info(
                                        "No staff members have been added yet."
                                        )

                                    
# REPORTS

elif st.session_state.page == "Reports":

    st.markdown("""
    <div class="hero">
        <div class="hero-title">Reports & Analytics</div>
        <p class="hero-text">
            Analyze ticket status, categories and priorities.
        </p>
    </div>
    """, unsafe_allow_html=True)

    summary = report_service.get_ticket_summary()

    st.subheader("Ticket Summary")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Total",
            summary["total"]
        )

    with col2:
        st.metric(
            "Open",
            summary["open"]
        )

    with col3:
        st.metric(
            "Resolved",
            summary["resolved"]
        )

    with col4:
        st.metric(
            "Closed",
            summary["closed"]
        )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Category Report")

        category_report = (
            report_service.get_category_report()
        )

        if category_report:

            category_data = []

            for category, count in category_report.items():
                category_data.append({
                    "Category": category,
                    "Tickets": count
                })

            st.dataframe(
                category_data,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info("No category data available.")

    with col2:

        st.subheader("Priority Report")

        priority_report = (
            report_service.get_priority_report()
        )

        if priority_report:

            priority_data = []

            for priority, count in priority_report.items():
                priority_data.append({
                    "Priority": priority,
                    "Tickets": count
                })

            st.dataframe(
                priority_data,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info("No priority data available.")

    st.subheader("Status Report")

    status_report = (
        report_service.get_status_report()
    )

    if status_report:

        status_data = []

        for status, count in status_report.items():
            status_data.append({
                "Status": status,
                "Tickets": count
            })

        st.dataframe(
            status_data,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info("No status data available.")