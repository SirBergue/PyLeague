import wx
import wx.media

from PIL import Image, ImageEnhance
from modules.config import Config

def PIL2wx(image):
    width, height = image.size
    return wx.Bitmap.FromBuffer(width, height, image.tobytes())


class LeagueLogo(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(
            self,
            parent,
            pos=(45, 38),
            size=(152, 56)
        )

        self.img = Image.open(Config.LEAGUE_LOGO_LOC).convert('RGB')
        self.img = self.img.resize((152, 56), Image.ANTIALIAS)
        self.wx_img = PIL2wx(self.img)

        self.bmp = wx.StaticBitmap(
            self,
            -1,
            self.wx_img,
            pos=(0, 0)
        )


class CloseButton(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(
            self,
            parent,
            pos=(220, 15),
            size=(10, 10)
        )

        self.img = Image.open(Config.CLOSE_BUTTON_LOC).convert('RGB')
        self.img = self.img.resize((10, 10), Image.ANTIALIAS)
        self.bmp = wx.StaticBitmap(self, -1, PIL2wx(self.img))


class VideoPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(
            self,
            parent,
            size=(1200, 720),
            pos=(0, 0),
            style=wx.NO_BORDER
        )

        self.media_widget = wx.media.MediaCtrl(
            self,
            size=(1300, 800),
            pos=(0, -35),
            style=wx.NO_BORDER
        )

        self.media_widget.Bind(wx.media.EVT_MEDIA_LOADED, self.play)
        self.media_widget.Bind(wx.media.EVT_MEDIA_FINISHED, self.quit)

        if self.media_widget.Load(Config.VIDEO_FILE_LOC):
            print('Video concluded!')

        self.media_widget.SetVolume(0.5)

    def play(self, event): self.media_widget.Play()

    def quit(self, event): self.media_widget.Play()


class LoginBtn(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(
            self,
            parent,
            size=(205, 35),
            pos=(20, 500),
            style=wx.BORDER_SIMPLE
        )

        self.btn = wx.Button(
            self,
            wx.ID_ANY,
            'SIGN IN',
            pos=(0, 0),
            size=(205, 35),
            style=wx.BORDER_NONE
        )


class UserLoginPanel(wx.Panel):
    def __init__(self, parent, size=(200, 30), pos=(15, 182)):
        wx.Panel.__init__(
            self,
            parent,
            size=size,
            pos=pos,
            style=wx.BORDER_SIMPLE
        )


        self.SetForegroundColour((89, 93, 80))

        username_textctrl = wx.TextCtrl(
            self,
            pos=(0, 0),
            size=(200, 30),
        )

        username_textctrl.SetBackgroundColour((0, 2, 11))


class LoginScreen(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(
            self,
            parent,
            id,
            size=Config.LOGIN_SIZE,
            style=wx.NO_BORDER
        )

        self.Centre()
        self.SetIcon(wx.Icon(Config.WINDOW_ICON_LOC))
        self.SetTitle(Config.WINDOW_TITLE)

        top_panel = wx.Panel(self)

        self.video_player      = VideoPanel(top_panel)
        self.input_panel       = wx.Panel(top_panel)
        self.league_logo_input = LeagueLogo(self.input_panel)
        self.btn_panel         = LoginBtn(self.input_panel)
        self.close_button      = CloseButton(self.input_panel)

        self.user_login_panel     = UserLoginPanel(self.input_panel)
        self.password_login_panel = UserLoginPanel(self.input_panel, pos=(15, 242))

        font = wx.Font(
            12,
            family=wx.FONTFAMILY_SWISS,
            style=wx.FONTSTYLE_NORMAL,
            weight=wx.FONTWEIGHT_BOLD,
            underline=False,
            faceName='',
            encoding=wx.FONTENCODING_DEFAULT,
        )

        wx.StaticText(
			self.input_panel,
            pos=(15, 115),
            size=(80, 40),
            label='SIGN IN',
		).SetFont(font)

        font_region = wx.Font(
            9,
            family=wx.FONTFAMILY_TELETYPE,
            style=wx.FONTSTYLE_NORMAL,
            weight=wx.FONTWEIGHT_BOLD,
            underline=False,
            faceName='',
            encoding=wx.FONTENCODING_DEFAULT,
        )

        username_st = wx.StaticText(
            self.input_panel,
            pos=(15, 160),
            size=(80, 40),
            label='Username'
        )

        username_st.SetFont(font_region)
        username_st.SetForegroundColour((144, 154, 163))

        password_st = wx.StaticText(
            self.input_panel,
            pos=(15, 220),
            size=(80, 40),
            label='Password'
        )

        password_st.SetFont(font_region)
        password_st.SetForegroundColour((144, 154, 163))

        top_panel.SetBackgroundColour((0, 10, 19, 255))

        self.sl = wx.StaticLine(
            top_panel,
            size=(1450, 2),
            style=wx.LI_HORIZONTAL
        )

        self.sl.SetBackgroundColour((104, 92, 70, 255))

        self.blue_line_bottom = wx.StaticLine(
            self.input_panel,
            size=(250, 1),
            pos=(0, 685),
            style=wx.LI_HORIZONTAL
        )

        self.blue_line_left = wx.StaticLine(
            self.input_panel,
            size=(2, 720),
            pos=(0, 0),
            style=wx.LI_VERTICAL
        )

        region_language_st = wx.StaticText(
			self.input_panel,
            pos=(15, 340),
            size=(110, 40),
            label='Region/Language',
		)

        region_language_st.SetFont(font_region)
        region_language_st.SetForegroundColour((144, 154, 163))

        self.language_region = wx.Choice(
            self.input_panel,
            choices=Config.COMBO_BOX_REGION_LIST,
            pos=(15, 370)
        )

        self.language_region.SetSelection(0)

        self.chk_box = wx.CheckBox(
            self.input_panel,
            label='  Remember Me',
            pos=(15, 285)
        )

        self.chk_box.SetForegroundColour((144, 154, 163))

        self.blue_line_bottom.SetBackgroundColour((32, 42, 51, 255))
        self.blue_line_left.SetBackgroundColour((32, 42, 51, 255))

        # blue_font = wx.Font(
        #     9,
        #     family=wx.FONTFAMILY_MODERN,
        #     style=wx.FONTSTYLE_NORMAL,
        #     weight=wx.FONTWEIGHT_BOLD,
        #     underline=False,
        #     faceName='',
        #     encoding=wx.FONTENCODING_DEFAULT,
        # )

        wx.StaticText(
			self.input_panel,
            pos=(15, 580),
            size=(180, 40),
            label='Forgot your username?'
		).SetForegroundColour((41, 114, 124))

        wx.StaticText(
			self.input_panel,
            pos=(15, 600),
            size=(180, 40),
            label='Forgot your password?'
		).SetForegroundColour((41, 114, 124))

        wx.StaticText(
			self.input_panel,
            pos=(15, 620),
            size=(180, 40),
            label='Create an account'
		).SetForegroundColour((41, 114, 124))

        wx.StaticText(
            self.input_panel,
            pos=(15, 650),
            size=(180, 40),
            label='Launch legacy client'
        ).SetForegroundColour((146, 144, 114))

        wx.StaticText(
            self.input_panel,
            pos=(60, 693),
            size=(40 * len(Config.VERSION_NUMBER), 40),
            label=Config.VERSION_NUMBER
        ).SetForegroundColour((51, 57, 66))

        self.window_move_set(
            [self,
             top_panel,
             self.video_player,
             self.video_player.media_widget,
             self.sl]
        )

        self.close_button.Bind(wx.EVT_ENTER_WINDOW, self.close_btn_hover)
        self.close_button.Bind(wx.EVT_LEAVE_WINDOW, self.close_btn_hover_exit)

        self.close_button.bmp.Bind(wx.EVT_LEFT_UP, self.close_btn_event)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer_v = wx.BoxSizer(wx.VERTICAL)

        sizer.Add(self.video_player, 0, wx.EXPAND | wx.ALL, border=0)
        sizer.Add(self.input_panel, 0, wx.EXPAND | wx.ALL, border=0)

        sizer_v.Add(self.sl, 0, wx.EXPAND | wx.ALL, border=0)
        sizer_v.Add(sizer, 0, wx.EXPAND | wx.ALL, border=0)

        top_panel.SetSizer(sizer_v)

        self.click_x = 0
        self.click_y = 0
        self.clicked = False

    def window_move_set(self, bind_list):
        for obj in bind_list:
            obj.Bind(wx.EVT_MOTION, self.on_mouse_move)
            obj.Bind(wx.EVT_LEFT_DOWN, self.on_left_down)
            obj.Bind(wx.EVT_LEFT_UP, self.on_left_up)

    def on_left_down(self, event):
        pt = event.GetPosition()
        print(pt)

        self.click_x = pt[0]
        self.click_y = pt[1]

        self.clicked = True

    def on_left_up(self, event): self.clicked = False

    def on_mouse_move(self, event):
        if self.clicked:
            pt = event.GetPosition()
            win_position = self.GetPosition()

            x = pt[0] - self.click_x + win_position[0]
            y = pt[1] - self.click_y + win_position[1]

            self.Move(wx.Point(x, y))

    def close_btn_event(self, event):
        self.Destroy()
        exit()

    def close_btn_hover(self, event):
        img_brightness = ImageEnhance.Brightness(self.close_button.img)
        enhanced_img = img_brightness.enhance(2.0)

        wx.StaticBitmap(self.close_button, -1, PIL2wx(enhanced_img))

    def close_btn_hover_exit(self, event):
        wx.StaticBitmap(
            self.close_button,
            -1,
            PIL2wx(self.close_button.img)
        )
