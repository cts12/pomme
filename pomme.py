import argparse
import sqlite3
import os
from os.path import expanduser
from browser_manager import BrowserManager

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    profile = expanduser('~') + '/.config/google-chrome/Default/'
    ext_app = 'chrome-extension_edacconmaakjimmfgnblocblbcdcpbko_0'
    db = '%s/databases/%s/2' % (profile, ext_app)
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute('SELECT name FROM SavedSessions;')
    proj_choices = cur.fetchall()

    parser.add_argument("-p", "--project",
                        choices=list(proj_choices[0]),
                        help="Choose project from the list",
                        required=True)
    parser.add_argument("-b", "--browser",
                        choices=['google-chrome', 'firefox'],
                        help="Choose browser to restore tabs in")

    parser.add_argument("--research", dest='research', action='store_true')
    parser.add_argument("--no-research", dest='research', action='store_false')
    parser.set_defaults(research=False)

    # set up commandline arguments to choose browser etc.
    args = parser.parse_args()
    name = (args.project,)
    browser = args.browser

    # Provide access to the saved sessions
    cur.execute('SELECT id, windows FROM SavedSessions WHERE name=?;', name)
    session = cur.fetchone()

    # Restore all the windows for this project
    bm = BrowserManager(browser, session)
    bm.restoreWindows()

    if not args.research:
        ret = os.system('tmux new -s ' + name[0] + ' 2> /dev/null')
        if ret > 0:
            os.system('tmux a -t ' + name[0])
