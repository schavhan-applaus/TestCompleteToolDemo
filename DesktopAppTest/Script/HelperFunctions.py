# Step Definitions for Edge Browser Desktop Application Testing

# Helper Functions
def launch_edge_browser():
    TestedApps.msedge.Run()

def navigate_to_url(url):
  #Opens the specified URL in a running instance of the specified browser.
  Browsers.Item[btEdge].Navigate(url)
  
def click_On_Appearance_Option():
  OCR.Recognize(Aliases.browser.wndChrome_WidgetWin_1.Chrome_RenderWidgetHostHWND).BlockByText("Appearance", spLeftMost).Click()
  
def click_On_Mode_Option():
  OCR.Recognize(Aliases.browser.wndChrome_WidgetWin_1.Chrome_RenderWidgetHostHWND).BlockByText("Mode", spTopMost).Click()
  
def set_Light_Mode():
  Aliases.browser.wndChrome_WidgetWin_1.Chrome_RenderWidgetHostHWND.Click(249, 261)
  Aliases.browser.wndChrome_WidgetWin_1.Chrome_RenderWidgetHostHWND.Click(763, 251)
  Aliases.browser.wndChrome_WidgetWin_1.Chrome_RenderWidgetHostHWND.Click(753, 408)
  
def set_Dark_Mode():
  #Clicks the 'Dark Mode' object.
  Aliases.browser.wndChrome_WidgetWin_1.Chrome_RenderWidgetHostHWND.Click(927, 450)
  
def is_Dark_Mode_Selected():
  #Checks whether the Dark mode is Enabled.
  aqObject.CheckProperty(Aliases.browser.wndChrome_WidgetWin_1.Chrome_RenderWidgetHostHWND, "Enabled", cmpEqual, True)
  #Checks whether the Dark mode is Enabled.
  aqObject.CheckProperty(Aliases.browser.pageThemes, "Enabled", cmpEqual, True)
  #Checks whether the Dark mode is visible.
  aqObject.CheckProperty(Aliases.browser.pageThemes, "Visible", cmpEqual, True)
  
def is_Light_Mode_Selected():
  #Checks whether the light mode is Enabled.
  aqObject.CheckProperty(Aliases.browser.pageThemes, "Enabled", cmpEqual, True)
  #Checks whether the Light Mode is visible.
  aqObject.CheckProperty(Aliases.browser.pageThemes, "Visible", cmpEqual, True)

def close_browser_window():
    Aliases.browser.BrowserWindow.Close()