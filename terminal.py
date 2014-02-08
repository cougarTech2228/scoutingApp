# in match curse
import curses 
import curses.panel
import cmd
screen = curses.initscr() 

#this will eventually be for a structured terminal interface, currently it does nothing

class Terminal:
    def __init__(self):
        (self.W, self.L) = getTerminalSize
        self.matchWin = MatchWindow():
        self.promptWin = PromptWindow(self.w,self.l):
        self.reviewWin = ReviewWindow():
        self.setupWin = SetupWindow():
        
        self.matchPanel = curses.panel.new_panel():
        self.promptPanel = curses.panel.new_panel():
        self.setupPanel = curses.panel.new_panel():
        self.reviewPanel = curses.panel.new_panel():
        
        def changeMode(mode):
            #unhide panel and bring to front
            
        def exit(mode):
            if mode == m
                #clear and hide panel

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
    
    
'''
    #!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import curses 
import curses.textpad
import cmd

def maketextbox(h,w,y,x,value="",deco=None,textColorpair=0,decoColorpair=0):
    # thanks to http://stackoverflow.com/a/5326195/8482 for this
    nw = curses.newwin(h,w,y,x)
    txtbox = curses.textpad.Textbox(nw,insert_mode=True)
    if deco=="frame":
        screen.attron(decoColorpair)
        curses.textpad.rectangle(screen,y-1,x-1,y+h,x+w)
        screen.attroff(decoColorpair)
    elif deco=="underline":
        screen.hline(y+1,x,underlineChr,w,decoColorpair)

    nw.addstr(0,0,value,textColorpair)
    nw.attron(textColorpair)
    screen.refresh()
    return nw,txtbox

class Commands(cmd.Cmd):
    """Simple command processor example."""
    
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "> "
        self.intro  = "Welcome to console!"  ## defaults to None
        self.write("Don't understand '" + line + "'")
    def do_greet(self, line):
        self.write("hello "+line)

    def default(self,line) :
        self.write("Don't understand '" + line + "'")

    def do_quit(self, line):
        curses.endwin()
        return True

    def write(self,text) :
        screen.clear()
        textwin.clear()
        screen.addstr(3,0,text)
        screen.refresh()


if __name__ == '__main__':
    screen = curses.initscr() 	
    curses.noecho()
    textwin,textbox = maketextbox(10,10, 10,10)
    flag = False
    while not flag :
        text = textbox.edit()
        curses.beep()
        flag = Commands().onecmd(text)
'''

