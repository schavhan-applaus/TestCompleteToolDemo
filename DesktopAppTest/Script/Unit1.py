def EdgeDekstopAppTestCase1():
    #Runs the "msedge" tested application.
    TestedApps.msedge.Run()
    #Opens the specified URL in a running instance of the specified browser.
    Browsers.Item[btEdge].Navigate("edge://settings/")
    #Maximizes the specified Window object.
    Aliases.browser.BrowserWindow.Maximize()
    #Checks whether the 'Enabled' property of the Aliases.browser.wndChrome_WidgetWin_1.Chrome_RenderWidgetHostHWND object equals True.
    aqObject.CheckProperty(Aliases.browser.wndChrome_WidgetWin_1.Chrome_RenderWidgetHostHWND, "Enabled", cmpEqual, True)
    OCR.Recognize(Aliases.browser.wndChrome_WidgetWin_1.Chrome_RenderWidgetHostHWND).BlockByText("Appearance", spLeftMost).Click()
    OCR.Recognize(Aliases.browser.wndChrome_WidgetWin_1.Chrome_RenderWidgetHostHWND).BlockByText("Mode", spTopMost).Click()
    #Checks whether the 'Enabled' property of the Aliases.browser.mangeCoockies object equals True.
    aqObject.CheckProperty(Aliases.browser.mangeCoockies, "Enabled", cmpEqual, True)
    #Checks whether the 'Visible' property of the Aliases.browser.mangeCoockies object equals True.
    aqObject.CheckProperty(Aliases.browser.mangeCoockies, "Visible", cmpEqual, True)
    #Checks whether the 'VisibleOnScreen' property of the Aliases.browser.mangeCoockies object equals True.
    aqObject.CheckProperty(Aliases.browser.mangeCoockies, "VisibleOnScreen", cmpEqual, True)
    #Checks whether the 'Enabled' property of the Aliases.browser.wndChrome_WidgetWin_1.Chrome_RenderWidgetHostHWND object equals True.
    aqObject.CheckProperty(Aliases.browser.wndChrome_WidgetWin_1.Chrome_RenderWidgetHostHWND, "Enabled", cmpEqual, True)
    #Clicks the 'Chrome_RenderWidgetHostHWND' object.
    Aliases.browser.wndChrome_WidgetWin_1.Chrome_RenderWidgetHostHWND.Click(927, 450)
    #Closes the 'BrowserWindow' window.
    Aliases.browser.BrowserWindow.Close()
    #Runs the "msedge" tested application.
    TestedApps.msedge.Run()
    #Clicks the 'BrowserWindow' object.
    Aliases.browser.BrowserWindow.Click(1850, 66)
    #Opens the specified URL in a running instance of the specified browser.
    Browsers.Item[btEdge].Navigate("edge://settings/")
    #Maximizes the specified Window object.
    Aliases.browser.BrowserWindow.Maximize()
    #Clicks the 'Chrome_RenderWidgetHostHWND' object.
    Aliases.browser.wndChrome_WidgetWin_1.Chrome_RenderWidgetHostHWND.Click(249, 261)
    #Clicks the 'Chrome_RenderWidgetHostHWND' object.
    Aliases.browser.wndChrome_WidgetWin_1.Chrome_RenderWidgetHostHWND.Click(763, 251)
    #Clicks the 'Chrome_RenderWidgetHostHWND' object.
    Aliases.browser.wndChrome_WidgetWin_1.Chrome_RenderWidgetHostHWND.Click(753, 408)
    #Closes the 'BrowserWindow' window.
    Aliases.browser.BrowserWindow.Close()
    #Checks whether the 'Enabled' property of the Aliases.browser.wndChrome_WidgetWin_1.Chrome_RenderWidgetHostHWND object equals True.
    aqObject.CheckProperty(Aliases.browser.wndChrome_WidgetWin_1.Chrome_RenderWidgetHostHWND, "Enabled", cmpEqual, True)
