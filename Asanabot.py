def tasksTypes(deadlines, day):

# deadlines is an array, day is a "date"
# 
# due today (which is parameter *day*) or overdue --> "Today"
    # deadline <= day
# due tomorrow or within the next week --> "Upcoming" 
    # or day + 1 <= deadline <= day + 7
# due after this week --> "Later"
    # or day + 7 < deadline

# return COUNT of tasks for each label type in an array such that:
    # [Today, Upcoming, Later]

    today = 0
    upcoming = 0
    later = 0

    for deadline in deadlines:
        if deadline <= day:
            today += 1
        elif (day + 1) <= deadline <= (day + 7):
            upcoming += 1
        else:
            later += 1

    return [today, upcoming, later]

    
    
    


    def smartAssigning(names, statuses, projects, tasks):

    # names, statuses, projects and tasks are all arrays
    # each index corresponds between arrays for the same person
        # (they all have the same length)
    # it says names contains only uppercase or lowercase letters, but the
        # example shows otherwise ... names = ["John", "Martin"]
    # the order of importance for task assignment is:
        # - vacation (which is represented as True)
        # - tasks
            # if tasks are equal, then the person with fewer different projects
    
    # return the person with the highest availability, who can be assigned a task

    
    # What if there is only one person? What if that one person is on vacation?
    # Directions do not handle all edge cases...

    fewest_tasks = tasks[0]
    fewest_projects = projects[0]
    most_available = names[0]
    is_vacationing = statuses[0]

    for i in xrange(len(names)):

        if statuses[i] is False:
        # checks for truthiness of status; we want to proceed if False

            if tasks[i] < fewest_tasks:
                fewest_tasks = tasks[i]
                fewest_projects = projects[i]
                most_available = names[i]
                is_vacationing = False

            elif tasks[i] == fewest_tasks:
                if projects[i] < fewest_projects:
                    fewest_projects = projects[i]
                    most_available = names[i]
                    is_vacationing = False
            
    if is_vacationing is True:
        return "No one available."
    return most_available
            
            