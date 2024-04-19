def album_de_usuario(album, artista, qt_musicas = None):
    album_usuario = {
        'artista': artista,
        'album': album,
        'quantidades de musicas': qt_musicas
        
    }
    return album_usuario

while True:
    print("(digite (q) para sair.)")

    artista  = input("Digite o nome do artista: ")
    if artista == 'q':
        break

    album = input("Digite o album: ")
    if album == 'q':
        break

    qt_musicas = input('Quantidade de musicas no album: ')
    if qt_musicas == 'q':
        break

    

    cd = album_de_usuario(artista, album, qt_musicas)

print(cd)

