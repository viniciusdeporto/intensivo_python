def make_album(artista, album, qt_musicas=None):

    album_favorito = {
        'artista': artista,
        'album': album,   
    }

    if qt_musicas:
        album_favorito['qt_musicas'] = qt_musicas

    return album_favorito

cd = make_album('led', 'led zeppelin', qt_musicas = 11)
print(cd)