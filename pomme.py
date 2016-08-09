import argparse
import sqlite3
from os.path import expanduser
from browser_manager import BrowserManager

if __name__ == "__main__":
    # tables = ["SavedSessions", "PreviousSessions"]
    # dir_path = os.getcwd()
    # file_path = dir_path + '/extension_3_4_7.crx'
    # parse commandline arguments
    parser = argparse.ArgumentParser()
    #TODO: add config files for the projects.
    
    profile = expanduser('~') + '/.config/google-chrome/Default/'
    ext_app = 'chrome-extension_edacconmaakjimmfgnblocblbcdcpbko_0'
    db = '%s/databases/%s/2' % (profile, ext_app)

    #parser.add_argument("-p","--project",
     #                   help="Choose project from the list",
      #                  required=True)
    # set up commandline arguments to choose browser etc.
    name = ('pomme',)
    browser = 'google-chrome'

    # Provide access to the saved sessions
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('SELECT id, windows FROM SavedSessions WHERE name=?;', name)
    session = cur.fetchone()

    bm = BrowserManager(browser, session)
    bm.restoreWindows()

    # try:

    # except:

    # finally:
