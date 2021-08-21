import wx

from modules.config import Config

class Bugsplat(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(
            self,
            parent,
            id,
            size=(600, 800),
            #style=wx.NO_BORDER
        )

        self.Centre()
        self.SetIcon(wx.Icon(Config.WINDOW_ICON_LOC))
        self.SetTitle(Config.WINDOW_BUGSPLAT_TITLE)

        panel = wx.Panel(self)

        wx.StaticText(
			panel,
			label=Config.BUGSPLAT_STATICTEXT,
            style=wx.ALIGN_CENTRE_HORIZONTAL
		)

        #box = wx.TextCtrl(panel,size = (200,100),style = wx.TE_MULTILINE)
