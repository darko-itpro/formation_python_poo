import pylib.utils.file_helper as fu  # Module de la fonction chargeant les informations de séries.
import stage.mediatheque as media  # Module contenant les objets liés à la gestion des médias
from pylib.utils import cli
from pathlib import Path
import os.path


def load_data_from_path(path:str, shows:dict[str, media.TvShow] = {}) -> dict[str, media.TvShow]:
    """
    Charge les données d'une série à partir d'une source et retourne un dictionnaire de séries.

    Le paramètre optionnel `shows` permet de compléter une collection existante. La valeur par
    défaut est `None` car le dictionnaire est un type mutable.

    :param path: Chemin vers la source de données. Doit être un fichier csv ou un répertoire.
    :param shows: Dictionnaire de TvShows dont la clef est le titre. Optionnel. Si absent
    un nouveau dictionnaire est créé.
    :return: Un dictionnaire de TvShows dont la clef est le titre. Si un dictionnaire a été passé en
    argument, l'original n'est pas modifié.
    """
    if os.path.isdir(path):
        my_episodes = fu.load_from_filenames(path)
    elif os.path.isfile(path):
        my_episodes = fu.load_from_csv(path)
    else:
        raise ValueError(f"Provided path does not exist {path}")

    shows = shows.copy()

    for show_name, season, number, title, duration, year in my_episodes:  # *other permet de récupérer d'autres données
        if show_name not in shows:
            shows[show_name] = media.TvShow(show_name)

        show = shows[show_name]

        try:
            show.add_episode(title, number, season, duration, year)
        except ValueError:
            print(f"Episode {title} for {show_name} exists")

    return shows


if __name__ == "__main__":
    paths = []
    paths.append(Path(__file__).parent.parent / "assets" / "showslist.csv")

    shows = {}  # Servira à stocker des données titre:show

    for source_path in paths:
        try:
            shows = load_data_from_path(source_path, shows)
        except ValueError as e:
            print(f"Impossible de charger les données de {source_path}")

    cli.display_shows(shows)
