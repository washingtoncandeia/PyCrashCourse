# 6-12. Extensions

bands = {
    'red light skyscraper': {'disco': '4AM', 'ano': 2020, 'gênero': 'psychedelic rock'},
    'samsara blues experiment': {'disco': 'waiting for the flood', 'ano': 2020, 'gênero': 'psychedelic rock'},
    'kyuss': {'disco': 'welcome to sky valley', 'ano': 1994, 'gênero': 'stoner, desert'},
    'orchid': {'disco': 'the mouths of madness', 'ano': 2013, 'gênero': 'stoner'},
    'red fang': {'disco': 'arrows', 'ano': 2021, 'gênero': 'stoner'},
    'witchcraft': {'disco': 'legend', 'ano': 2012, 'gênero': 'vintage rock, stoner'},
    'clutch': {'disco': 'book of bad decisions', 'ano': 2018, 'gênero': 'heavy rock'},
    'orange goblin': {'disco': 'time travelling blues', 'ano': 1998, 'gênero': 'stoner'},
    'colour haze': {'disco': 'tempel', 'ano': 2006, 'gênero': 'psychedelic rock'},
    'nebula': {'disco': 'live in mojave desert, vol.2', 'ano': 2021, 'gênero': 'stoner'},
    'fu manchu': {'disco': 'clone of the universe', 'ano': 2018, 'gênero': 'stoner'},
    'khruangbin': {'disco': 'mordechai', 'ano': 2020, 'gênero': 'psychedelic, classic, rock n roll'},
    'king gizzard & the lizard wizard': {'disco': "infest the rats' nest", 'ano': 2019, 'gênero': 'heavy rock, psycedelic, experimentation'},
    'all them witches': {'disco': 'nothing as the ideal', 'ano': 2020, 'gênero': 'stoner, heavy rock'},
    'electric citizen': {'disco': 'helltown', 'ano': 2018, 'gênero': 'heavy rock , vintage'},
    'ruby the hatchet': {'disco': 'planetary space child', 'ano': 2017, 'gênero': 'psychedelic, hard rock'},
    'uncle acid & the deadbeats': {'disco': 'wasteland', 'ano': 2018, 'gênero': 'psychedelic'},
    'lucifer': {'disco': 'lucifer III', 'ano': 2020, 'gênero': 'vintage rock'},
    'fireball ministry': {'disco': 'their rock is not our rock', 'ano': 2005, 'gênero': 'stoner'},
    'acid king': {'disco': 'III', 'ano': 2005, 'gênero': 'stoner'},
    'asteroid': {'disco': 'III', 'ano': 2016, 'gênero': 'vintage rock'},
    'siena root': {'disco': 'a dream of lasting peace', 'ano': 2017, 'gênero': 'vintage rock'},
    'sheavy': {'disco': 'celestial hifi', 'ano': 2015, 'gênero': 'stoner'},
    'yawning man': {'disco': 'historical graffiti', 'ano': 2020, 'gênero': 'experimental rock, stoner, desert'},
    'graveyard': {'disco': 'hisingen blues', 'ano': 2011, 'gênero': 'vintage rock'},
    'electric wizard': {'disco': 'wizard bloody wizard', 'ano': 2017, 'gênero': 'heavy rock, doom'},
    'the flying eyes': {'disco': 'bad blook & winter', 'ano': 2009, 'gênero': 'psychedelic rock'},
    'dozer': {'disco': 'through the eyes of heathens', 'ano': 2006, 'gênero': 'stoner'},
    'dead meadow': {'disco': 'the nothing they need', 'ano': 2018, 'gênero': 'psychedelic rock, stoner'},
    'black mountain': {'disco': 'destroyer', 'ano': 2019, 'gênero': 'heavy rock, psychedelic'},
    'stoned jesus': {'disco': 'seven thunders roar', 'ano': 2012, 'gênero': 'stoner, heavy rock'},
    'kadavar': {'disco': 'the isolation tapes', 'ano': 2020, 'gênero': 'vintage rock'},
    'horisont': {'disco': 'about time', 'ano': 2017, 'gênero': 'heavy rock'},
    'blues pills': {'disco': 'holy moly!', 'ano': 2020, 'gênero': 'vintage rock'},
    'black rainbows': {'disco': 'cosmic ritual supertrip', 'ano': 2020, 'gênero': 'psychedelic rock'},
    'mars red sky': {'disco': 'the task eternal', 'ano': 2019, 'gênero': 'heavy rock'},
    'the heavy eyes': {'disco': 'love like machines', 'ano': 2020, 'gênero': 'psychedelic blues rock'},
    'monster magnet': {'disco': 'a better dystopia', 'ano': 2021, 'gênero': 'heavy rock'},
    'blood ceremony': {'disco': 'the eldritch dark', 'ano': 2013, 'gênero': 'doom-psych-heavy prog'},
    'somali yacht club': {'disco': 'the sun', 'ano': 2016, 'gênero': 'psychedelic, stoner'},
}

# Informações
for band, info in bands.items():
    print(f"\nA banda {band.title()} é excelente. O seu gênero é o {info['gênero'].title()}.")
    print(f"Um bom album é o {info['disco'].title()} lançado em {info['ano']}.")
