import pyqrcode
import wx
import datetime
class main(wx.Frame):
	def __init__(self):
		super().__init__(None, title="qrGenerator")
		self.Centre()
		p = wx.Panel(self)
		wx.StaticText(p, -1, "text")
		self.edit = wx.TextCtrl(p,-1,value="",name="")
		generate = wx.Button(p,-1,label="&get qr code ")
		generate.Bind(wx.EVT_BUTTON,self.onGenerate)
		exit = wx.Button(p, -1, "&back")
		exit.Bind(wx.EVT_BUTTON, self.onback)
		self.Show()
	def onGenerate(self,event):
		if self.edit.GetValue() == "":
			wx.MessageBox("error Please enter text","error")
			self.SetFocus(self.edit)
		else:
			qr = pyqrcode.create(self.edit.GetValue())
			path = wx.SaveFileSelector(" ",".png","qr")
			qr.png(path,scale=8)

			self.edit.Value = ""
	def onback(self, event):
		self.Close()

app=wx.App()
w=main()
w.Show()
app.MainLoop()