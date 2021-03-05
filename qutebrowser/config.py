c.tabs.position = "bottom"

# ~/.local/share/qutebrowser/sessions/myqbsession.yml
c.auto_save.session = True
c.session.default_name = "myqbsession"

c.url.searchengines = {
    "DEFAULT": "https://www.baidu.com/s?wd={}",
    "awk": "https://wiki.archlinux.org/?search={}",
    "gh": "https://github.com/search?q={}",
    "gwk": "https://wiki.gentoo.org/?search={}"
}

c.url.default_page = "https://www.baidu.com"
c.fonts.default_size = "15pt"
c.fonts.hints = "bold 15pt default_family"
c.downloads.position = 'bottom'
c.tabs.show = 'never'
c.completion.height = '30%'
c.downloads.remove_finished = 5000

# view for flash content(www-plugins/adobe-flash)
c.content.plugins = True

# Bindings for normal mode(Vimium compatible keybind)
config.bind('x', 'tab-close')
config.bind('X', 'undo')
config.bind('J', 'tab-prev')
config.bind('K', 'tab-next')

config.bind('j', 'scroll-px 0 100')
config.bind('k', 'scroll-px 0 -100')

config.bind('f', 'hint all tab-fg')

# openup buffer list
config.bind(',ls', 'set-cmd-text -s :buffer')

# toggle between two tabs(vim like toggle between two buffers)
config.bind(',bb', 'tab-focus last')

config.bind('<Ctrl-p>', 'tab-prev', mode='normal')
config.bind('<Ctrl-n>', 'tab-next', mode='normal')

# Bindings for insert mode
config.bind('<Ctrl-a>', 'fake-key <Home>', mode='insert')
config.bind('<Ctrl-e>', 'fake-key <End>', mode='insert')
config.bind('<Ctrl-d>', 'fake-key <Delete>', mode='insert')
config.bind('<Ctrl-h>', 'fake-key <Backspace>', mode='insert')
config.bind('<Ctrl-k>', 'fake-key <Ctrl-Shift-Right> ;; fake-key <Backspace>', mode='insert')
config.bind('<Ctrl-f>', 'fake-key <Right>', mode='insert')
config.bind('<Ctrl-b>', 'fake-key <Left>', mode='insert')
config.bind('<Ctrl-n>', 'fake-key <Down>', mode='insert')
config.bind('<Ctrl-p>', 'fake-key <Up>', mode='insert')
#config.bind('i', 'enter-mode insert ;; spawn fcitx-remote -t')
#config.bind('gi', 'hint inputs --first ;; spawn fcitx-remote -t')
#config.bind('<Escape>', 'spawn fcitx-remote -t ;; leave-mode ;; fake-key <Escape>', mode='insert')

# turn off the notification
c.content.notifications = False
