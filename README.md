# Spotify2Deezer

Spotify2Deezer is a Python application that transfers tracks from a specified Spotify playlist to a new playlist on Deezer. The app uses the Spotify API to retrieve track information, searches for each track on Deezer, and adds the tracks to a Deezer playlist.

**Note:** Currently, the Deezer developer platform is not accepting new applications, which may prevent some users from obtaining the required permissions for creating and managing playlists.

## Features

- Retrieves tracks from a specified Spotify playlist
- Searches for matching tracks on Deezer
- Generates a CSV of tracks found in Deezer (Track Name, Artist, Album, Deezer Track ID, Deezer Link)
- Creates a new playlist on Deezer and adds matching tracks (**Read note: above** 😞)

## Requirements

To use Spotify2Deezer, you need:

1. **Spotify Developer Account**: Sign up at the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and create an application to obtain a **Client ID** and **Client Secret**.

2. **Deezer Developer Account**: Sign up at the [Deezer Developer Portal](https://developers.deezer.com/) to obtain an access token. Deezer currently requires OAuth 2.0 authentication for managing user playlists.

   > ⚠ **Warning:** Deezer's developer platform is not accepting new applications at this time. Monitor their developer portal for updates on application registration.

## Environment Setup

### Using `pyenv` and `pyenv-virtualenv`

To manage your Python environment, you can use `pyenv` and `pyenv-virtualenv` to create an isolated environment for this project.

1. **Install `pyenv` and `pyenv-virtualenv`** (if you haven't already):

```bash
brew install pyenv pyenv-virtualenv
```

3. **Set Up `pyenv` in Your Shell Configuration**:

Add the following lines to your shell configuration file (e.g., `~/.zshenv` or `~/.bashrc`):

```bash
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Then restart your terminal or source the file:

```bash
source ~/.zshenv
```

3. **Install Python 3.12.4** (or a compatible version):

```bash
pyenv install 3.12.4
```

4. **Create and Activate a Virtual Environment**:

```bash
pyenv virtualenv 3.12.4 spotify2deezer-env
pyenv local spotify2deezer-env
```

5. **Install Dependencies**:

```bash
pip install -r requirements.txt
```

## Setting Up the `.env` File

Create a `.env` file in the project root with the following environment variables:

```env
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
SPOTIFY_PLAYLIST_ID=your_spotify_playlist_id
DEEZER_USER_ID=your_deezer_user_id
```

Replace `your_spotify_client_id`, `your_spotify_client_secret`, `your_spotify_playlist_id`, and `your_deezer_user_id` with your actual credentials.

## Running the Application

To run Spotify2Deezer, follow these steps:

1.  Activate your virtual environment:

```bash
pyenv activate spotify2deezer-env
```

2. Run the main script:

```bash
python src/main.py
```

3. The application will retrieve tracks from the specified Spotify playlist, search for each track on Deezer, and add the tracks to a new playlist on Deezer (if permissions are available).

## Warning: Deezer Developer Platform Restrictions

Due to current restrictions, Deezer is not accepting new applications. This may prevent new users from creating or modifying playlists on Deezer using this application until Deezer reopens app registrations.

## Troubleshooting

- Ensure all required environment variables are set in the `.env` file.
- If you encounter permission errors, ensure that `pyenv` and `pyenv-virtualenv` are set up correctly.
- For any API-specific errors, verify that you have the correct credentials and permissions set up in your Spotify and Deezer developer accounts.
