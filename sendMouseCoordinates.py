from vboxapi import VirtualBoxManager

mgr = VirtualBoxManager(None, None)

vbox = mgr.getVirtualBox()
machine = vbox.findMachine('CentOS')
session = mgr.getSessionObject(vbox)

machine.LockMachine(session, mgr.constants.LockType_Shared)
session.Console.Mouse.putMouseEventAbsolute(100,100,0,0,1)
