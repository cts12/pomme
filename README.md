# pomme
This is just a small program to help me keep a track of my projects a little better. Basically I have an associated set of tabs for a project, and a tmux session. This means when I execute the program I get back all my research and my tmux session nice and quick. Really just a personal use for me.

You will need the latest version of google chrome which you can get from here https://www.google.co.uk/chrome/browser/desktop/ .

Next you need to install the chrome extension Session buddy from here. https://chrome.google.com/webstore/detail/session-buddy/edacconmaakjimmfgnblocblbcdcpbko?hl=en

Really session buddy has everything you would need for restoring browser sessions, and saving said sessions. However I just want to automate opening and switching a project for me a bit. So I will add project switching. Intermittent update of a projects set of urls. Killing a project. Incorporate pomodoro to automatically switch 'working windows' to 'relax windows'.
And lastly if you find you execute some commands very often, you can use the program to alias them, and only include that projects custom aliases, when the project is active. A nice thing is I don't have to use chrome to open up the browsing session, instead i can use firefox.

To add new projects use session buddy to save a browsing session. This the project available to a session. You can run the program like so.

`python pomme.py -p pomme -b google-chrome`

This will restore the browsers for my project pomme in google chrome, and set up a tmux session.
Sometimes I don't want to open up a tmux session as I was just researching, so this will only open the browsers. Here you really can just use Session buddy instead, but again I can just add more features to that in the future.

`python pomme.py -p pomme -b firefox --research`

There you have it, just a little tool too help me work :)
