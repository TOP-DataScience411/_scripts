def track_to_database(
        title,
        artist,
        album,
        channels, 
        bit_depths,
        sample_rate,
):
    pass


track_to_database('Boom!', 'Boomers', 'BOOM', 5, 8, 44100)


def track_to_database(
        *,
        title,
        artist,
        album,
        channels, 
        bit_depths,
        sample_rate,
):
    pass


track_to_database(
    title='Boom!', 
    artist='Boomers', 
    album='BOOM', 
    channels=5, 
    bit_depths=8, 
    sample_rate=44100
)



def test_func(
        pos1, 
        # pos2=15,
        /, 
        pos_key1, 
        pos_key2='default', 
        *,
        key1, 
        key2 
):
    pass

