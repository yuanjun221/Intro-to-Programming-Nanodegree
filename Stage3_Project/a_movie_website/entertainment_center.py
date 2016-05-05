import fresh_tomatoes
import media

the_martian = media.Movie("The Martian",
                          'Bring "the Martian" home',
                          "https://goo.gl/SWlIZi",
                          "https://goo.gl/9gpiAj")
the_martian.add_director("Ridley Scott")
the_martian.add_year(2015)
the_martian.add_rating("PG-13")
the_martian.add_cast(["Matt Damon", "Jessica Chastain", "Kristen Wiig"])

a_space_odyssey = media.Movie("2001: A Space Odyssey",
                              "A voyage to Jupiter with the sentient computer Hal",
                              "https://goo.gl/uIOXZj",
                              "https://goo.gl/vxslnx")
a_space_odyssey.add_director("Stanley Kubrick")
a_space_odyssey.add_year(1968)
a_space_odyssey.add_rating("G")
a_space_odyssey.add_cast(["Keir Dullea Gary", "Lockwood William", "Sylvester"])

mad_max = media.Movie("Mad Max: Fury Road",
                      "Survive in the desert wasteland",
                      "https://goo.gl/YWLmvH",
                      "https://goo.gl/Oy2du6")
mad_max.add_director("George Miller")
mad_max.add_year(2015)
mad_max.add_rating("R")
mad_max.add_cast(["Tom Hardy", "Charlize Theron", "Nicholas Hoult"])

source_code = media.Movie("Source Code",
                          "A mission to find the bomber of a Chicago commuter train",
                          "https://goo.gl/2a7MeS",
                          "https://goo.gl/G6mb0I")
source_code.add_director("Duncan Jones")
source_code.add_year(2011)
source_code.add_rating("PG-13")
source_code.add_cast(["Jake Gyllenhaal", "Michelle Monaghan", "Vera Farmiga"])

interstellar = media.Movie("Interstellar",
                           "Travel through a wormhole in search of a new home for humanity",
                           "https://goo.gl/ARs2JS",
                           "https://goo.gl/uuC5vV")
interstellar.add_director("Christopher Nolan")
interstellar.add_year(2014)
interstellar.add_rating("PG-13")
interstellar.add_cast(["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain"])

inception = media.Movie("Inception",
                        "Planting an idea in a person's subconscious",
                        "https://goo.gl/fAvkWK",
                        "https://goo.gl/7YvRkA")
inception.add_director("Christopher Nolan")
inception.add_year(2010)
inception.add_rating("PG-13")
inception.add_cast(["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"])

movies = [the_martian, a_space_odyssey, mad_max, source_code, interstellar, inception]
fresh_tomatoes.open_movies_page(movies)
