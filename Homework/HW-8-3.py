def update_population_count(input_dictionaries):
    
        total_of_continents = 0

        for continent in input_dictionaries:
            total_of_country = 0

            for country in input_dictionaries[continent]:
                total_of_states = 0

                for state in input_dictionaries[continent][country]:
                    total_of_cities = 0

                    for cities in input_dictionaries[continent][country][state]:

                        total_of_cities += input_dictionaries[continent][country][state][cities]

                    input_dictionaries[continent][country][state]["total"] = total_of_cities

                    total_of_states += input_dictionaries[continent][country][state]["total"]

                input_dictionaries[continent][country]["total"] = total_of_states

                total_of_country += input_dictionaries[continent][country]["total"]

            input_dictionaries[continent]["total"] = total_of_country

            total_of_continents += input_dictionaries[continent]["total"]

        input_dictionaries["total"] = total_of_continents

        return total_of_continents




population = {
  'North America': {
      'United States': {
          'Tennessee': {
              'Nashville': 692587,
              'Memphis': 628127,
              'Knoxville': 192648
          },
          'Washington': {
              'Seattle': 733919,
              'Spokane': 229071,
              'Tacoma': 219205
          }
      },
      'Canada': {
          'British Columbia': {
              'Vancouver': 675218,
              'Whistler': 11854,
          },
          'Ontario': {
              'Toronto': 2930000,
              'Hamilton': 579200
          }
      }
  }
}

update_population_count(population)
print(population)

# {
#   'North America': {
#       'United States': {
#           'Tennessee': {
#               'Nashville': 692587,
#               'Memphis': 628127,
#               'Knoxville': 192648,
#               'total': 1513362
#           },
#           'Washington': {
#               'Seattle': 733919,
#               'Spokane': 229071,
#               'Tacoma': 219205,
#               'total': 1182195
#           },
#           'total': 2695557
#       },
#       'Canada': {
#           'British Columbia': {
#               'Vancouver': 675218,
#               'Whistler': 11854,
#               'total': 687072
#           },
#           'Ontario': {
#               'Toronto': 2930000,
#               'Hamilton': 579200,
#               'total': 3509200
#           },
#           'total': 4196272
#       },
#       'total': 6891829
#   },
#   'total': 6891829
# }


                
                



