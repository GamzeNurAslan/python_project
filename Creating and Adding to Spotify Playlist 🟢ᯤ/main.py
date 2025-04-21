from spotify import spotify_login, get_billboard_songs, search_songs, create_playlist

def main():
    sp = spotify_login()
    user_id = sp.current_user()["id"]

    date = input("Tarihi gir (YYYY-MM-DD): ")
    songs = get_billboard_songs(date)
    uris = search_songs(sp, songs)

    playlist_name = f"{date} Billboard Top 100"
    create_playlist(sp, user_id, playlist_name, uris)

    print(f"✔️ {len(uris)} şarkı ile '{playlist_name}' çalma listesi oluşturuldu!")

if __name__ == "__main__":
    main()
