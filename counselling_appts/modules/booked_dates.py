from counselling_appts.models import Appointment

def create_appt_dict():
    '''
    creates a dictionary with dates which have
    booked appointments and their respective timeslots
    '''

    items = Appointment.objects.all()
    dates_list = []
    dates_appt_dict = {}

    # creates a list of dates that have appointments booked in them
    for item in items:
        if item.date_strf() not in dates_list:
            dates_list.append(item.date_strf())
            dates_appt_dict[item.date_strf()] = []

    # creates the dictionary
    for item in items:
        dates_appt_dict[item.date_strf()].append(str(item.time_only()) + ":00")

    return dates_appt_dict


def create_available_timeslots(dates_dictionary):
    POSSIBLE_TIME_SLOTS = [9, 10, 11, 13, 14, 15, 16, 17, 18]
    remaining_timeslots = {}

    for key, pair in dates_dictionary.items():
        common_timeslots = list(set(POSSIBLE_TIME_SLOTS).intersection(set(pair)))
        combined = POSSIBLE_TIME_SLOTS + pair

        for item in common_timeslots:
            combined = [element for element in combined if element != item]

        remaining_timeslots[key] = combined
    
    return remaining_timeslots


def create_fully_booked_list(dates_dictionary):
    '''
    Creates a list of dates with no more
    available timeslots. Each day has a
    maximum of 9 appointment slots
    '''

    fully_booked_dates = ""

    for key, pair in dates_dictionary.items():
        if len(pair) >= 9:
            fully_booked_dates += str(key)

    return fully_booked_dates
