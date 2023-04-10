def feet_parse(feet_inches):
    """ splitta la misura in 2 parti:
        feet
        inches
         """
    parti = feet_inches.split(" ")
    feet = float(parti[0])
    inches = float(parti[1])
    return {"feet": feet, "inches":inches}
