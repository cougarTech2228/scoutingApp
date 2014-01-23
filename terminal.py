# in match curse
import curses 
import curses.panel
import cmd

class Terminal:
    def __init__(self):
        screen = curses.initscr() 
        (self.W, self.L) = getTerminalSize
        self.matchWin = MatchWindow():
        self.promptWin = PromptWindow():
        self.reviewWin = ReviewWindow():
        self.setupWin = SetupWindow():
        
        self.matchPanel = curses.panel.new_panel():
        self.promptPanel = curses.panel.new_panel():
        self.setupPanel = curses.panel.new_panel():
        self.reviewPanel = curses.panel.new_panel():
        
        
def getTerminalSize():
    import os
    env = os.environ
    def ioctl_GWINSZ(fd):
        try:
            import fcntl, termios, struct, os
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,
        '1234'))
        except:
            return
        return cr
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        cr = (env.get('LINES', 25), env.get('COLUMNS', 80))

        ### Use get(key[, default]) instead of a try/catch
        #try:
        #    cr = (env['LINES'], env['COLUMNS'])
        #except:
        #    cr = (25, 80)
    return int(cr[1]), int(cr[0])