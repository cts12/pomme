import sys
import traceback
import webbrowser
from json import JSONDecoder


class BrowserManager():

    def __init__(self, browser, session):
        self.jd = JSONDecoder()
        self.browser = browser
        self.windows = {}
        webbrowser.register(self.browser, None,
                            webbrowser.Chrome(self.browser))
        self.tabs = self._set_session(session)

    def restoreWindows(self):
        controller = webbrowser.get(self.browser)
        try:
            for tab in self.tabs:
                w_id = tab['window']
                if not self.windows[w_id]:
                    controller.open(tab['url'], new=1)
                    self.windows[w_id] = True
                else:
                    controller.open(tab['url'], new=2)

        except:
            e_type, e_val, e_traceback = sys.exc_info()
            traceback.print_tb(e_traceback, limit=4)

    def _set_session(self, session):
        json_session_list = self.jd.decode(session[1])
        tabs = []
        window_ids = set()
        # print json_session_list[1]
        for window in json_session_list:
            for tab in window['tabs']:
                tabs.append({'window': tab['windowId'],
                             'url': tab['url']})
                window_ids.add(tab['windowId'])

        for window_id in window_ids:
            self.windows[window_id] = False

        return tabs
