def ask_about_medication(medications, interface='cli'):
    """
    Asks the user about their medication intake.

    Parameters:
        medications (list): A list of medication names to inquire about.
        interface (str): The interface through which to interact with the user. 
                         Supports 'cli' for command line and 'streamlit' for Streamlit apps.

    Returns:
        dict: A dictionary mapping each medication to a boolean indicating whether the user
              has taken it.
    """
    intake_status = {}
    
    for medication in medications:
        if interface == 'cli':
            response = input(f"Have you taken your medication {medication}? (yes/no): ").strip().lower()
            intake_status[medication] = response == 'yes'
        elif interface == 'streamlit':
            import streamlit as st
            response = st.radio(f"Have you taken your medication {medication}?", ('Yes', 'No'), key=medication)
            intake_status[medication] = response == 'Yes'
        else:
            raise ValueError("Unsupported interface specified.")
    
    return intake_status
