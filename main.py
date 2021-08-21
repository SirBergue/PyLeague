#!/usr/bin/python

import wx

from modules.login import LoginScreen
from modules.bugsplat import Bugsplat

if __name__ == '__main__':
    app = wx.App()

    login_screen = LoginScreen(parent=None, id=-1)
    login_screen.Show()

    # bugsplat_screen = Bugsplat(parent=None, id=-1)
    # bugsplat_screen.Show()

    app.MainLoop()
