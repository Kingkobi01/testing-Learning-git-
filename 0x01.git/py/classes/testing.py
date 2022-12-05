from something import Country, CountryCatalogue
# num_dict: dict = {
#     "one":1,
#     "two":2,
#     "three":3
# }


# print(num_dict.values())
catalogue = CountryCatalogue()
in_file = open(COUNTRY_DATA_FILE_NAME = "country_data.csv", "r")
for line in in_file:
    split_line = line.split(",")
    country = Country(
        name=split_line[0], continent=split_line[1], population=int(split_line[2]), area=float(split_line[3])
    )
    catalogue.add(country)
in_file.close()


# Alter catalogue contents
england = Country("England", "Europe", 56489800, 130279)
ecuador = Country("Ecuador", "South America", 18048628, 256370)
india = Country("India", "Asia", 1375586000, 3287263)
catalogue.add(england)
catalogue.add(ecuador)
catalogue.add(india)
catalogue.remove(Country("Canada", "North America", 34207000, 9976140.0))
catalogue.remove(Country("South Korea", "Asia", 50503933, 98076.92))



