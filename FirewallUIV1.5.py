#!/usr/bin/python
"""
This file is used to create the UI for Network creation 
"""
from Tkinter import Tk, Frame,Label,Button,Entry
import MyMain
import socket
class main_application(Frame):
	def __init__(self,parent):
		Frame.__init__(self,parent)
		self.parent=parent
		self.grid()
def refresh(widget):
	widget.grid_forget()
	widget.destroy()
def createButton(parent,txt,rw,cn,stick,cmd=None):
	return Button(parent,text=txt,command=cmd).grid(column=cn,row=rw,sticky=stick)
def createLabel(parent,cn,rw,colspan,stick,anch,txt,fore,back):
	Label(parent,anchor=anch,text=txt,fg=fore,bg=back).grid(column=cn,row=rw,columnspan=colspan,sticky=stick)
def uExit():
	root.quit()
def viewTree():
	MyMain.printTree()				
def startFirewall():
	global main_app
	global started
	refresh(main_app)
	main_app=main_application(root)
	createLabel(main_app,0,0,4,'NEWS',"center","Firewall Started ","Red","White")
	createButton(main_app,"Add New Rule",5,1,'NEWS',createRule)
	createButton(main_app,"View Rule Tree",8,1,'NEWS',viewTree)
	#createButton(main_app,"Modify Rules",10,1,'NEWS',modifyRule)
	createButton(main_app,"Exit",10,1,'NEWS',uExit)
	MyMain.main()
	started=True
def cancel():
	global main_app
	global started
	refresh(main_app)
	main_app=main_application(root)
	if not started:
		createButton(main_app,"Start Firewall",5,1,'NEWS',startFirewall)
		
	else:
		createButton(main_app,"View Rule Tree",5,1,'NEWS',viewTree)
		#createButton(main_app,"Modify Rules",10,1,'NEWS',modifyRule)
	createButton(main_app,"Add New Rule",8,1,'NEWS',createRule)
	createButton(main_app,"Exit",10,1,'NEWS',uExit)			
def createRule(Error=False):
	global main_app
	global in_out
	global sourceip
	global destip
	global protocol
	global source_port
	global dest_port
	global action
	refresh(main_app)
	main_app=main_application(root)
	if Error:
		createLabel(main_app,0,0,4,'NEWS',"center","Type error Try! again ","Red","White")
		
	else:
		createLabel(main_app,0,0,4,'NEWS',"center","Add New Rule ","Black","White")	
	nop=1
	for i in ["In_out","SourceIP","DestIP","Protocol","Source_port","Dest_port","Action"]:
		createLabel(main_app,0,nop,1,'NEWS',None,i,"Black","White")
		if i.lower() in globals():
			del globals()[i.lower()]
		if i.lower() not in globals():
			globals().update({i.lower():Entry(main_app)})
			globals()[i.lower()].grid(column=1,row=nop,sticky='NEWS')
		nop+=1
	def on_create(iface,sourceip,destip,protocol,src_port,dst_port,action):
		global main_app
		global started
		file_open=open("rules.csv","a+")
		success=True
		if len(file_open.readlines())==0:
			file_open.write("in_out,src_ip,dst_ip,protocol,src_port,dst_port,action")
			file_open.write("\n")
		try:
			if ((len(str(sourceip).split("."))!=4) or sourceip=="any") and ((len(str(destip).split("."))!=4) or destip=="any") :	
				raise socket.error
			#socket.inet_aton(ipaddr)
			if not (iface=="in" or iface=="out" or iface=="any"):
				success=False
			if not isinstance(protocol, str):
				success=False
			if not (action=="accept" or action == "deny"):
				success=False
			if success:
				createLabel(main_app,0,0,4,'NEWS',"center","Rule added Successfully ","Black","White")
				writ=str(iface)+","+str(sourceip)+","+str(destip)+","+str(protocol)+","+str(src_port)+","+str(dst_port)+","+str(action)
				file_open.write(writ)
				file_open.write("\n")
				file_open.close()
				refresh(main_app)
				main_app=main_application(root)
				if not started:
					createButton(main_app,"Start Firewall",5,1,'NEWS',startFirewall)
					
				else:
					createButton(main_app,"View Rule Tree",5,1,'NEWS',viewTree)
					#createButton(main_app,"Modify Rules",10,1,'NEWS',modifyRule)
				createButton(main_app,"Add New Rule",8,1,'NEWS',createRule)
				createButton(main_app,"Exit",10,1,'NEWS',uExit)			
			else:
				createRule(True)
		except socket.error:
			createRule(True)
	createButton(main_app,"Add rule",12,1,'NEWS',cmd= lambda : on_create(in_out.get(),sourceip.get(),destip.get(),protocol.get(),source_port.get(),dest_port.get(),action.get()))	
	createButton(main_app,"Cancel",14,1,'NEWS',cancel)
def modifyRule():	
	pass
	#createButton(main_app,"create",12,1,'NEWS',cmd= lambda : on_create(name.get(),node1.get(),node2.get(),node_1_interface.get(),node_2_interface.get(),length.get(),typeofconnection.get(),medium.get()))
def main():
	global root
	global main_app
	root=Tk()
	root.title("Self Learning Firewall")
	root.aspect(100, 100, 250, 230)
	main_app=main_application(root)
	createButton(main_app,"Start Firewall",5,1,'NEWS',startFirewall)
	createButton(main_app,"Add New Rule",8,1,'NEWS',createRule)
	#createButton(main_app,"Modify Rule",8,1,'NEWS',modifyRule)
	createButton(main_app,"Exit",10,1,'NEWS',uExit)
	try:
		main_app.mainloop()
	except KeyboardInterrupt:
		pass
if __name__=="__main__":
	started=False
	main()
