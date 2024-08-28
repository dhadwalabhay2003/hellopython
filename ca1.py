from collections import Counter

# Sample data
data = [
   { "Location": "Tokyo", "Year": 2020, "Distance": 100, "Stroke": "Backstroke", "Relay": False, "Gender": "Men", "Team": "ROC", "Athlete": "Evgeny Rylov", "Results": 51.98, "Rank": 1 },
  {
    "Location": "Tokyo",
    "Year": 2020,
    "Distance": 100,
    "Stroke": "Backstroke",
    "Relay": False,
    "Gender": "Men",
    "Team": "ROC",
    "Athlete": "Kliment Kolesnikov",
    "Results": 52.00,
    "Rank": 2
},
  { "Location": "Tokyo", "Year": 2020, "Distance": 100, "Stroke": "Backstroke", "Relay": False, "Gender": "Men", "Team": "USA", "Athlete": "Ryan Murphy", "Results": 52.19, "Rank": 3 },
    {
    "Location": "Tokyo",
    "Year": 2020,
    "Distance": 100,
    "Stroke": "Backstroke",
    "Relay": False,
    "Gender": "Men",
    "Team": "ITA",
    "Athlete": "Thomas Ceccon",
    "Results": 52.30,
    "Rank": 4
},
   { "Location": "Tokyo", "Year": 2020, "Distance": 100, "Stroke": "Backstroke", "Relay": False, "Gender": "Men", "Team": "CHN", "Athlete": "Jiayu Xu", "Results": 52.51, "Rank": 4 },
   {
    "Location": "Tokyo",
    "Year": 2020,
    "Distance": 100,
    "Stroke": "Backstroke",
    "Relay": False,
    "Gender": "Men",
    "Team": "ESP",
    "Athlete": "Hugo Gonzalez De Oliveira",
    "Results": 52.78,
    "Rank": 4
},
   { "Location": "Tokyo", "Year": 2020, "Distance": 100, "Stroke": "Backstroke", "Relay": False, "Gender": "Men", "Team": "AUS", "Athlete": "Mitchell Larkin", "Results": 52.79, "Rank": 4 },
   {
    "Location": "Tokyo",
    "Year": 2020,
    "Distance": 100,
    "Stroke": "Backstroke",
    "Relay": False,
    "Gender": "Men",
    "Team": "ROU",
    "Athlete": "Robert Glinta",
    "Results": 52.95,
    "Rank": 4
},
   { "Location": "Tokyo", "Year": 2020, "Distance": 100, "Stroke": "Breaststroke", "Relay": False, "Gender": "Men", "Team": "GBR", "Athlete": "Adam Peaty", "Results": 57.37, "Rank": 1 },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 100,
        "Stroke": "Breaststroke",
        "Relay": False,
        "Gender": "Men",
        "Team": "NED",
        "Athlete": "Arno Kamminga",
        "Results": 58,
        "Rank": 2
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 100,
        "Stroke": "Breaststroke",
        "Relay": False,
        "Gender": "Men",
        "Team": "ITA",
        "Athlete": "Nicolo Martinenghi",
        "Results": 58.33,
        "Rank": 3
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 100,
        "Stroke": "Breaststroke",
        "Relay": False,
        "Gender": "Men",
        "Team": "USA",
        "Athlete": "Michael Andrew",
        "Results": 58.84,
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 100,
        "Stroke": "Breaststroke",
        "Relay": False,
        "Gender": "Men",
        "Team": "GBR",
        "Athlete": "James Wilby",
        "Results": 58.96,
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 100,
        "Stroke": "Breaststroke",
        "Relay": False,
        "Gender": "Men",
        "Team": "CHN",
        "Athlete": "Zibei Yan",
        "Results": 58.99,
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 100,
        "Stroke": "Breaststroke",
        "Relay": False,
        "Gender": "Men",
        "Team": "USA",
        "Athlete": "Andrew Wilson",
        "Results": 58.99,
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 100,
        "Stroke": "Breaststroke",
        "Relay": False,
        "Gender": "Men",
        "Team": "BLR",
        "Athlete": "Ilya Shymanovich",
        "Results": 59.36,
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 100,
        "Stroke": "Butterfly",
        "Relay": False,
        "Gender": "Men",
        "Team": "USA",
        "Athlete": "Caeleb Dressel",
        "Results": 49.45,
        "Rank": 1
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 100,
        "Stroke": "Butterfly",
        "Relay": False,
        "Gender": "Men",
        "Team": "HUN",
        "Athlete": "Kristof Milak",
        "Results": 49.68,
        "Rank": 2
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 100,
        "Stroke": "Butterfly",
        "Relay": False,
        "Gender": "Men",
        "Team": "SUI",
        "Athlete": "Noe Ponti",
        "Results": 50.74,
        "Rank": 3
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 100,
        "Stroke": "Butterfly",
        "Relay": False,
        "Gender": "Men",
        "Team": "ROC",
        "Athlete": "Andrei Minakov",
        "Results": 50.88,
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 100,
        "Stroke": "Butterfly",
        "Relay": False,
        "Gender": "Men",
        "Team": "POL",
        "Athlete": "Jakub Majerski",
        "Results": 50.92,
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 100,
        "Stroke": "Butterfly",
        "Relay": False,
        "Gender": "Men",
        "Team": "AUS",
        "Athlete": "Matthew Temple",
        "Results": 50.92,
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 100,
        "Stroke": "Butterfly",
        "Relay": False,
        "Gender": "Men",
        "Team": "GUA",
        "Athlete": "Luis Martinez",
        "Results": 51.09,
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 100,
        "Stroke": "Butterfly",
        "Relay": False,
        "Gender": "Men",
        "Team": "BUL",
        "Athlete": "Josif Miladinov",
        "Results": 51.49,
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 100,
        "Stroke": "Freestyle",
        "Relay": False,
        "Gender": "Men",
        "Team": "USA",
        "Athlete": "Caeleb Dressel",
        "Results": 47.02,
        "Rank": 1
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 100,
        "Stroke": "Freestyle",
        "Relay": False,
        "Gender": "Men",
        "Team": "AUS",
        "Athlete": "Kyle Chalmers",
        "Results": 47.08,
        "Rank": 2
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 100,
        "Stroke": "Freestyle",
        "Relay": False,
        "Gender": "Men",
        "Team": "ROC",
        "Athlete": "Kliment Kolesnikov",
        "Results": 47.44,
        "Rank": 3
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 100,
        "Stroke": "Freestyle",
        "Relay": False,
        "Gender": "Men",
        "Team": "FRA",
        "Athlete": "Maxime Grousset",
        "Results": 47.72,
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 100,
        "Stroke": "Freestyle",
        "Relay": False,
        "Gender": "Men",
        "Team": "KOR",
        "Athlete": "Sunwoo Hwang",
        "Results": 47.82,
        "Rank": 4
    }, {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 100,
        "Stroke": "Freestyle",
        "Relay": False,
        "Gender": "Men",
        "Team": "ITA",
        "Athlete": "Alessandro Miressi",
        "Results": 47.86,
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 100,
        "Stroke": "Freestyle",
        "Relay": False,
        "Gender": "Men",
        "Team": "ROU",
        "Athlete": "David Popovici",
        "Results": 48.04,
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 100,
        "Stroke": "Freestyle",
        "Relay": False,
        "Gender": "Men",
        "Team": "HUN",
        "Athlete": "Nandor Nemeth",
        "Results": 48.10,
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 1500,
        "Stroke": "Freestyle",
        "Relay": False,
        "Gender": "Men",
        "Team": "USA",
        "Athlete": "Robert Finke",
        "Results": "14:39.7",
        "Rank": 1
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 1500,
        "Stroke": "Freestyle",
        "Relay": False,
        "Gender": "Men",
        "Team": "UKR",
        "Athlete": "Mykhailo Romanchuk",
        "Results": "14:40.7",
        "Rank": 2
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 1500,
        "Stroke": "Freestyle",
        "Relay": False,
        "Gender": "Men",
        "Team": "GER",
        "Athlete": "Florian Wellbrock",
        "Results": "14:40.9",
        "Rank": 3
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 1500,
        "Stroke": "Freestyle",
        "Relay": False,
        "Gender": "Men",
        "Team": "ITA",
        "Athlete": "Gregorio Paltrinieri",
        "Results": "14:45.0",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 1500,
        "Stroke": "Freestyle",
        "Relay": False,
        "Gender": "Men",
        "Team": "GBR",
        "Athlete": "Daniel Jervis",
        "Results": "14:55.5",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 1500,
        "Stroke": "Freestyle",
        "Relay": False,
        "Gender": "Men",
        "Team": "ROC",
        "Athlete": "Kirill Martynychev",
        "Results": "14:55.9",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 1500,
        "Stroke": "Freestyle",
        "Relay": False,
        "Gender": "Men",
        "Team": "AUT",
        "Athlete": "Felix Auboeck",
        "Results": "15:03.5",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 1500,
        "Stroke": "Freestyle",
        "Relay": False,
        "Gender": "Men",
        "Team": "UKR",
        "Athlete": "Serhii Frolov",
        "Results": "15:04.3",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Backstroke",
        "Relay": False,
        "Gender": "Men",
        "Team": "ROC",
        "Athlete": "Evgeny Rylov",
        "Results": "01:53.3",
        "Rank": 1
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Backstroke",
        "Relay": False,
        "Gender": "Men",
        "Team": "USA",
        "Athlete": "Ryan Murphy",
        "Results": "01:54.2",
        "Rank": 2
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Backstroke",
        "Relay": False,
        "Gender": "Men",
        "Team": "GBR",
        "Athlete": "Luke Greenbank",
        "Results": "01:54.7",
        "Rank": 3
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Backstroke",
        "Relay": False,
        "Gender": "Men",
        "Team": "USA",
        "Athlete": "Bryce Mefford",
        "Results": "01:55.5",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Backstroke",
        "Relay": False,
        "Gender": "Men",
        "Team": "HUN",
        "Athlete": "Adam Telegdy",
        "Results": "01:56.2",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Backstroke",
        "Relay": False,
        "Gender": "Men",
        "Team": "POL",
        "Athlete": "Radoslaw Kawecki",
        "Results": "01:56.4",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Backstroke",
        "Relay": False,
        "Gender": "Men",
        "Team": "JPN",
        "Athlete": "Ryosuke Irie",
        "Results": "01:57.3",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Backstroke",
        "Relay": False,
        "Gender": "Men",
        "Team": "ESP",
        "Athlete": "Nicolas Garcia Saiz",
        "Results": "01:59.1",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Breaststroke",
        "Relay": False,
        "Gender": "Men",
        "Team": "AUS",
        "Athlete": "Izaac Stubblety-Cook",
        "Results": "02:06.4",
        "Rank": 1
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Breaststroke",
        "Relay": False,
        "Gender": "Men",
        "Team": "AUS",
        "Athlete": "Izaac Stubblety-Cook",
        "Results": "02:06.4",
        "Rank": 1
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Breaststroke",
        "Relay": False,
        "Gender": "Men",
        "Team": "NED",
        "Athlete": "Arno Kamminga",
        "Results": "02:07.0",
        "Rank": 2
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Breaststroke",
        "Relay": False,
        "Gender": "Men",
        "Team": "FIN",
        "Athlete": "Matti Mattsson",
        "Results": "02:07.1",
        "Rank": 3
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Breaststroke",
        "Relay": False,
        "Gender": "Men",
        "Team": "ROC",
        "Athlete": "Anton Chupkov",
        "Results": "02:07.2",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Breaststroke",
        "Relay": False,
        "Gender": "Men",
        "Team": "USA",
        "Athlete": "Nic Fink",
        "Results": "02:07.9",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Breaststroke",
        "Relay": False,
        "Gender": "Men",
        "Team": "GBR",
        "Athlete": "James Wilby",
        "Results": "02:08.2",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Breaststroke",
        "Relay": False,
        "Gender": "Men",
        "Team": "JPN",
        "Athlete": "Ryuya Mura",
        "Results": "02:08.4",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Breaststroke",
        "Relay": False,
        "Gender": "Men",
        "Team": "SWE",
        "Athlete": "Erik Persson",
        "Results": "02:08.9",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Butterfly",
        "Relay": False,
        "Gender": "Men",
        "Team": "HUN",
        "Athlete": "Kristof Kristof Milak",
        "Results": "01:51.3",
        "Rank": 1
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Butterfly",
        "Relay": False,
        "Gender": "Men",
        "Team": "JPN",
        "Athlete": "Tomoru Honda",
        "Results": "01:53.7",
        "Rank": 2
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Butterfly",
        "Relay": False,
        "Gender": "Men",
        "Team": "ITA",
        "Athlete": "Federico Burdisso",
        "Results": "01:54.5",
        "Rank": 3
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Butterfly",
        "Relay": False,
        "Gender": "Men",
        "Team": "HUN",
        "Athlete": "Tamas Kenderesi",
        "Results": "01:54.5",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Butterfly",
        "Relay": False,
        "Gender": "Men",
        "Team": "RSA",
        "Athlete": "Chad Le Clos",
        "Results": "01:54.9",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Butterfly",
        "Relay": False,
        "Gender": "Men",
        "Team": "BRA",
        "Athlete": "Leonardo De Deus",
        "Results": "01:55.2",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Butterfly",
        "Relay": False,
        "Gender": "Men",
        "Team": "USA",
        "Athlete": "Gunnar Bentz",
        "Results": "01:55.5",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Butterfly",
        "Relay": False,
        "Gender": "Men",
        "Team": "POL",
        "Athlete": "Krzysztof Chmielewski",
        "Results": "01:55.9",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Freestyle",
        "Relay": False,
        "Gender": "Men",
        "Team": "GBR",
        "Athlete": "Tom Dean",
        "Results": "01:44.2",
        "Rank": 1
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Freestyle",
        "Relay": False,
        "Gender": "Men",
        "Team": "GBR",
        "Athlete": "Duncan Scott",
        "Results": "01:44.3",
        "Rank": 2
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Freestyle",
        "Relay": False,
        "Gender": "Men",
        "Team": "BRA",
        "Athlete": "Fernando Scheffer",
        "Results": "01:44.7",
        "Rank": 3
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Freestyle",
        "Relay": False,
        "Gender": "Men",
        "Team": "ROU",
        "Athlete": "David Popovici",
        "Results": "01:44.7",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Freestyle",
        "Relay": False,
        "Gender": "Men",
        "Team": "ROC",
        "Athlete": "Martin Malyutin",
        "Results": "01:45.0",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Freestyle",
        "Relay": False,
        "Gender": "Men",
        "Team": "USA",
        "Athlete": "Kieran Smith",
        "Results": "01:45.1",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Freestyle",
        "Relay": False,
        "Gender": "Men",
        "Team": "KOR",
        "Athlete": "Sunwoo Hwang",
        "Results": "01:45.3",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Freestyle",
        "Relay": False,
        "Gender": "Men",
        "Team": "LTU",
        "Athlete": "Danas Rapsys",
        "Results": "01:45.8",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Individual medley",
        "Relay": False,
        "Gender": "Men",
        "Team": "CHN",
        "Athlete": "Shun Wang",
        "Results": "01:55.0",
        "Rank": 1
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Individual medley",
        "Relay": False,
        "Gender": "Men",
        "Team": "GBR",
        "Athlete": "Duncan Scott",
        "Results": "01:55.3",
        "Rank": 2
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Individual medley",
        "Relay": False,
        "Gender": "Men",
        "Team": "SUI",
        "Athlete": "Jeremy Desplanches",
        "Results": "01:56.2",
        "Rank": 3
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Individual medley",
        "Relay": False,
        "Gender": "Men",
        "Team": "JPN",
        "Athlete": "Daiya Seto",
        "Results": "01:56.2",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Individual medley",
        "Relay": False,
        "Gender": "Men",
        "Team": "USA",
        "Athlete": "Michael Andrew",
        "Results": "01:57.3",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Individual medley",
        "Relay": False,
        "Gender": "Men",
        "Team": "JPN",
        "Athlete": "Kosuke Hagino",
        "Results": "01:57.5",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Individual medley",
        "Relay": False,
        "Gender": "Men",
        "Team": "HUN",
        "Athlete": "Laszlo Cseh",
        "Results": "01:57.7",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 200,
        "Stroke": "Individual medley",
        "Relay": False,
        "Gender": "Men",
        "Team": "NZL",
        "Athlete": "Lewis Clareburt",
        "Results": "01:57.7",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 400,
        "Stroke": "Freestyle",
        "Relay": False,
        "Gender": "Men",
        "Team": "TUN",
        "Athlete": "Ahmed Hafnaoui",
        "Results": "03:43.4",
        "Rank": 1
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 400,
        "Stroke": "Freestyle",
        "Relay": False,
        "Gender": "Men",
        "Team": "AUS",
        "Athlete": "Jack Mcloughlin",
        "Results": "03:43.5",
        "Rank": 2
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 400,
        "Stroke": "Freestyle",
        "Relay": False,
        "Gender": "Men",
        "Team": "USA",
        "Athlete": "Kieran Smith",
        "Results": "03:43.9",
        "Rank": 3
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 400,
        "Stroke": "Freestyle",
        "Relay": False,
        "Gender": "Men",
        "Team": "GER",
        "Athlete": "Henning Bennet Muhlleitner",
        "Results": "03:44.1",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 400,
        "Stroke": "Freestyle",
        "Relay": False,
        "Gender": "Men",
        "Team": "AUT",
        "Athlete": "Felix Auboeck",
        "Results": "03:44.1",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 400,
        "Stroke": "Freestyle",
        "Relay": False,
        "Gender": "Men",
        "Team": "ITA",
        "Athlete": "Gabriele Detti",
        "Results": "03:44.9",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 400,
        "Stroke": "Freestyle",
        "Relay": False,
        "Gender": "Men",
        "Team": "AUS",
        "Athlete": "Elijah Winnington",
        "Results": "03:45.2",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 400,
        "Stroke": "Freestyle",
        "Relay": False,
        "Gender": "Men",
        "Team": "USA",
        "Athlete": "Jake Mitchell",
        "Results": "03:45.4",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 400,
        "Stroke": "Individual medley",
        "Relay": False,
        "Gender": "Men",
        "Team": "USA",
        "Athlete": "Chase Kalisz",
        "Results": "04:09.4",
        "Rank": 1
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 400,
        "Stroke": "Individual medley",
        "Relay": False,
        "Gender": "Men",
        "Team": "USA",
        "Athlete": "Jay Litherland",
        "Results": "04:10.3",
        "Rank": 2
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 400,
        "Stroke": "Individual medley",
        "Relay": False,
        "Gender": "Men",
        "Team": "AUS",
        "Athlete": "Brendon Smith",
        "Results": "04:10.4",
        "Rank": 3
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 400,
        "Stroke": "Individual medley",
        "Relay": False,
        "Gender": "Men",
        "Team": "HUN",
        "Athlete": "David Verraszto",
        "Results": "04:10.6",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 400,
        "Stroke": "Individual medley",
        "Relay": False,
        "Gender": "Men",
        "Team": "GBR",
        "Athlete": "Max Litchfield",
        "Results": "04:10.6",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 400,
        "Stroke": "Individual medley",
        "Relay": False,
        "Gender": "Men",
        "Team": "FRA",
        "Athlete": "Leon Marchand",
        "Results": "04:11.2",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 400,
        "Stroke": "Individual medley",
        "Relay": False,
        "Gender": "Men",
        "Team": "NZL",
        "Athlete": "Lewis Clareburt",
        "Results": "04:11.2",
        "Rank": 4
    },
    {
        "Location": "Tokyo",
        "Year": 2020,
        "Distance": 400,
        "Stroke": "Individual medley",
        "Relay": False,
        "Gender": "Men",
        "Team": "ITA",
        "Athlete": "Alberto Razzetti",
        "Results": "04:11.3",
        "Rank": 4
    }
   
    # Add more data as necessary
]

def most_medals_by_country():
    country_medals = Counter([entry['Team'] for entry in data])
    country, count = country_medals.most_common(1)[0]
    print(f"{country} won the most medals with a total of {count} medals.")

def most_gold_by_country():
    gold_medals = Counter([entry['Team'] for entry in data if entry['Rank'] == 1])
    country, count = gold_medals.most_common(1)[0]
    print(f"{country} won the most gold medals with a total of {count} golds.")

def most_silver_by_country():
    silver_medals = Counter([entry['Team'] for entry in data if entry['Rank'] == 2])
    country, count = silver_medals.most_common(1)[0]
    print(f"{country} won the most silver medals with a total of {count} silvers.")

def most_bronze_by_country():
    bronze_medals = Counter([entry['Team'] for entry in data if entry['Rank'] == 3])
    country, count = bronze_medals.most_common(1)[0]
    print(f"{country} won the most bronze medals with a total of {count} bronzes.")

def most_medals_by_athlete():
    athlete_medals = Counter([entry['Athlete'] for entry in data])
    athlete, count = athlete_medals.most_common(1)[0]
    print(f"{athlete} won the most medals with a total of {count} medals.")



def menu():
    while True:
        print("\nMenu:")
        print("1. Show the country with the most medals")
        print("2. Show the country with the most gold medals")
        print("3. Show the country with the most silver medals")
        print("4. Show the country with the most bronze medals")
        print("5. Show the athlete with the most medals")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            most_medals_by_country()
        elif choice == '2':
            most_gold_by_country()
        elif choice == '3':
            most_silver_by_country()
        elif choice == '4':
            most_bronze_by_country()
        elif choice == '5':
            most_medals_by_athlete()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

# Run the menu
menu()
