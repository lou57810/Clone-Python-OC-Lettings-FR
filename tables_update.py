import os
import sqlite3
import pandas as pd
import shutil


path_db = "oc-lettings-site.sqlite3"


def create_temp_path():
    """Création d'un fichier temporaire pour l'échange de noms de tables."""
    path_csv = 'data_csv'
    try:
        os.mkdir(path_csv)
        print("Folder %s created!" % path_csv)
        # check whether directory already exists
    except FileExistsError:
        print("Folder %s already exists" % path_csv)


def delete_temp_path(folder):
    """Le répertoire précédemment créé sera détruit après la transaction."""
    path = os.path.join(os.getcwd(), folder)
    try:
        if os.path.isdir(path):
            shutil.rmtree(path)
            print(f"Directory '{path}' has been dropped with success.")
        else:
            print(f"Directory '{path}' don't exist.")
    except Exception as e:
        print(f"Error in dropping directory: {e}")


def data_exchange(src, dst):
    """Fonction qui sera appellée pour l'échange de nom de tables."""
    path_csv = "data_csv/"
    # Extract :
    connection = sqlite3.connect(path_db)
    try:
        data = pd.read_sql_query(f"SELECT * FROM {src}", connection)

        name = src
        """ Parse / underscore: oc_lettings_site_* => ['oc', 'lettings', 'site', '*'] """
        new = name.split('_')
        """ keep last elt """
        new_name = new[-1]
        """ data_csv/*.csv """
        csv = path_csv + f'{new_name}.csv'

        """ Transform to CSV """
        data.to_csv(csv, index=False)

        """ Transfer to existing table """
        connection = sqlite3.connect(path_db)
        data = pd.read_csv(csv)
        data.to_sql(dst, connection, if_exists='replace', index=False)
        connection.close()
    except Exception as e:
        print(f"oc_lettings_site tables have been previously destroyed: {e}")


def drop_old_datas():
    """Les tables devenues inutiles après l'échange sont supprimées."""
    connection = sqlite3.connect(path_db)
    try:
        # drop old table
        connection.execute("DROP TABLE oc_lettings_site_address")
        connection.execute("DROP TABLE oc_lettings_site_letting")
        connection.execute("DROP TABLE oc_lettings_site_profile")
        print("data dropped successfully")
    except Exception as e:
        print(f"oc_lettings_site tables has been previously destroyed!: {e}")
    # close the connection
    connection.close()


create_temp_path()
data_exchange('oc_lettings_site_address', 'lettings_address')
data_exchange('oc_lettings_site_profile', 'profiles_profile')
data_exchange('oc_lettings_site_letting', 'lettings_letting')
drop_old_datas()
delete_temp_path('data_csv')
