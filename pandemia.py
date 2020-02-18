def infected(s):
    # split the s list into lists of continents
    continents = s.split('X')
    # initialise infected count and population count
    # used to calc percentage
    infected_count = 0
    population_count = 0
    # iterate the newly created continent lists
    for continent in continents:
        # if there is a 1 then everyone is infected
        if '1' in continent:
            infected_count += len(continent)
        population_count += len(continent)
    # to ensure we dont get ZeroDivisionError, return 0 if no population
    if population_count == 0:
        return 0
    # return the percentage
    return (infected_count / population_count) * 100

print(infected("01000000X000X011X0X"))


    