# -*- coding: utf-8 -*- 

import wx
import wx.xrc
import wx.lib.scrolledpanel as scrolled
import wx.stc as stc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = 'Avro Schema Generator', pos = wx.DefaultPosition, size = wx.Size( 790,500 ), style = wx.MINIMIZE_BOX|wx.SYSTEM_MENU|
                  wx.CAPTION|wx.CLOSE_BOX|wx.CLIP_CHILDREN)
		#wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL
		
		self.SetIcon(wx.Icon('images\\logo.jpg'))
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer2_options = wx.BoxSizer( wx.VERTICAL )
		
		bSizer_namespace = wx.BoxSizer(wx.HORIZONTAL)
		
		self.static_namespace = wx.StaticText(self, wx.ID_ANY, u"NameSpace", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		self.static_namespace.Wrap(-1)
		bSizer_namespace.Add(self.static_namespace, 0 , wx.ALL,5)
		
		self.textBox_namespace = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 135,-1 ), 0 )
		bSizer_namespace.Add( self.textBox_namespace, 0, wx.ALL, 5 )
		
		bSizer2_options.Add( bSizer_namespace, 1, wx.EXPAND, 5 )
		
		bSizer_type = wx.BoxSizer( wx.HORIZONTAL )
		
		self.static_type = wx.StaticText( self, wx.ID_ANY, u"Type *", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		self.static_type.Wrap( -1 )
		bSizer_type.Add( self.static_type, 0, wx.ALL, 5 )
		
		typeChoices = [ u"record"]
		self.textBox_type = wx.ComboBox(self, -1, pos=wx.DefaultPosition, size=( 135,-1 ), choices=typeChoices, style=wx.CB_READONLY)
		
		
		
		#self.textBox_type = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 135,-1 ), 0 )
		bSizer_type.Add( self.textBox_type, 0, wx.ALL, 5 )
		
		
		bSizer2_options.Add( bSizer_type, 1, wx.EXPAND, 5 )
		
		bSizer_schema_name = wx.BoxSizer( wx.HORIZONTAL )
		
		self.static__schema_name = wx.StaticText( self, wx.ID_ANY, u"Schema Name *", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		self.static__schema_name.Wrap( -1 )
		bSizer_schema_name.Add( self.static__schema_name, 0, wx.ALL, 5 )
		
		self.textBox_schema_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 135,-1 ), 0 )
		bSizer_schema_name.Add( self.textBox_schema_name, 0, wx.ALL, 5 )
		
		
		bSizer2_options.Add( bSizer_schema_name, 1, wx.EXPAND, 5 )
		
		bSizer_fields = wx.BoxSizer( wx.HORIZONTAL )
		
		#self.static_blank1 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		#self.static_blank1.Wrap( -1 )
		#bSizer_fields.Add( self.static_blank1, 0, wx.ALL, 5 )
		
		self.static_fields = wx.StaticText( self, wx.ID_ANY, u"**Only Needed while creating Manual Schema", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.static_fields.Wrap( -1 )
		self.static_fields.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer_fields.Add( self.static_fields, 0, wx.ALL, 5 )
		
		
		bSizer2_options.Add( bSizer_fields, 1, wx.EXPAND, 5 )
		
		bSizer_name = wx.BoxSizer( wx.HORIZONTAL )
		
		self.static_name = wx.StaticText( self, wx.ID_ANY, u"Name **", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		self.static_name.Wrap( -1 )
		bSizer_name.Add( self.static_name, 0, wx.ALL, 5 )
		
		self.textBox_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 135,-1 ), 0 )
		bSizer_name.Add( self.textBox_name, 0, wx.ALL, 5 )
		
		
		bSizer2_options.Add( bSizer_name, 1, wx.EXPAND, 5 )
		
		bSizer_data_type = wx.BoxSizer( wx.VERTICAL )
		
		bSizer_data_type_1 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.static_data_type = wx.StaticText( self, wx.ID_ANY, u"Data Type **", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		self.static_data_type.Wrap( -1 )
		bSizer_data_type_1.Add( self.static_data_type, 0, wx.ALL, 5 )
		
		dropdown_data_typeChoices = [ u"int", u"string", u"long", u"float", u"boolean", u"double"]
		self.dropdown_data_type = wx.ComboBox(self, -1, pos=wx.DefaultPosition, size=( 135,-1 ), choices=dropdown_data_typeChoices, style=wx.CB_READONLY)
		bSizer_data_type_1.Add( self.dropdown_data_type, 0, wx.ALL, 5 )
		
		
		bSizer_data_type.Add( bSizer_data_type_1, 1, wx.EXPAND, 5 )
		
		bSizer_data_type_2 = wx.BoxSizer( wx.HORIZONTAL )
	
		
		self.checkBox_Edit = wx.CheckBox( self, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		bSizer_data_type_2.Add( self.checkBox_Edit, 0, wx.ALL, 5 )
		
		self.checkBox_Null = wx.CheckBox( self, wx.ID_ANY, u"Null", wx.DefaultPosition, wx.Size( 135,-1 ), 0 )
		bSizer_data_type_2.Add( self.checkBox_Null, 0, wx.ALL, 5 )
		
		bSizer_data_type.Add( bSizer_data_type_2, 1, wx.EXPAND, 5 )
		
		
		bSizer2_options.Add( bSizer_data_type, 1, wx.EXPAND, 5 )
		
		bSizer_addRecord = wx.BoxSizer(wx.HORIZONTAL)
		
		self.button_addRecord = wx.Button(self, wx.ID_ANY , u"Add Sub-Record" , wx.DefaultPosition , wx.Size(120,-1),0)
		bSizer_addRecord.Add(self.button_addRecord,0,wx.ALL,5)
		
		self.button_submitRecord = wx.Button(self, wx.ID_ANY , u"Submit Sub-Record" , wx.DefaultPosition , wx.Size(135,-1),0)
		self.button_submitRecord.Disable()
		bSizer_addRecord.Add(self.button_submitRecord,0,wx.ALL,5)
		
		
		bSizer2_options.Add(bSizer_addRecord,1,wx.EXPAND, 5)
		
		
		bSizer_default = wx.BoxSizer( wx.HORIZONTAL )
		
		self.static_default = wx.StaticText( self, wx.ID_ANY, u"Default", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		self.static_default.Wrap( -1 )
		
		bSizer_default.Add( self.static_default, 0, wx.ALL, 5 )
		
		self.textBox_default = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 135,-1 ), 0 )
		bSizer_default.Add( self.textBox_default, 0, wx.ALL, 5 )
		
		
		bSizer2_options.Add( bSizer_default, 1, wx.EXPAND, 5 )
		
		bSizer_desc = wx.BoxSizer( wx.HORIZONTAL )
		
		self.static_desc = wx.StaticText( self, wx.ID_ANY, u"Description", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		self.static_desc.Wrap( -1 )
		bSizer_desc.Add( self.static_desc, 0, wx.ALL, 5 )
		
		self.textBox_desc = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 135,-1 ), 0 )
		bSizer_desc.Add( self.textBox_desc, 0, wx.ALL, 5 )
		
		
		bSizer2_options.Add( bSizer_desc, 1, wx.EXPAND, 5 )
		
		bSizer_add_sub = wx.BoxSizer( wx.HORIZONTAL )
		
		self.button_add = wx.Button( self, wx.ID_ANY, u"Add the field", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		bSizer_add_sub.Add( self.button_add, 0, wx.ALL, 5 )
		
		self.panle_1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_add_sub.Add( self.panle_1, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.button_submit_schema = wx.Button( self, wx.ID_ANY, u"Submit Schema", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		self.button_submit_schema.Disable()
		bSizer_add_sub.Add( self.button_submit_schema, 0, wx.ALL, 5 )
		
		
		bSizer2_options.Add( bSizer_add_sub, 1, wx.EXPAND, 5 )
		
		bSizer_features = wx.BoxSizer( wx.HORIZONTAL )
		
		self.button_import = wx.Button( self, wx.ID_ANY, u"Open .csv", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		bSizer_features.Add( self.button_import, 0, wx.ALL, 5 )
		
		self.panel_2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_features.Add( self.panel_2, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.button_restart = wx.Button( self, wx.ID_ANY, u"Restart", wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		self.button_restart.Disable()
		bSizer_features.Add( self.button_restart, 0, wx.ALL, 5 )
		
		bSizer2_options.Add( bSizer_features, 1, wx.EXPAND, 5 )
		
		bSizer_json = wx.BoxSizer(wx.HORIZONTAL)
		
		self.button_json = wx.Button(self, wx.ID_ANY, u"Open .json", wx.DefaultPosition , wx.Size(120,-1),0)
		bSizer_json.Add(self.button_json,0,wx.ALL,5)
		
		self.panel_3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_json.Add( self.panel_3, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.button_avro = wx.Button(self,wx.ID_ANY,u"Open .avro",wx.DefaultPosition,wx.Size(120,-1),0)
		bSizer_json.Add(self.button_avro,0,wx.ALL,5)
		
		bSizer2_options.Add(bSizer_json ,1, wx.EXPAND,5)
		
		
		
		bSizer1.Add( bSizer2_options, 1, wx.EXPAND, 5 )
		
		bSizer_screen = wx.BoxSizer( wx.VERTICAL )
	
		#self.textBox_screen = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,500 ), wx.TE_MULTILINE|wx.HSCROLL )
		#self.textBox_screen.SetEditable(0)
		

		#text screen
		#self.textBox_screen = stc.StyledTextCtrl(self,wx.TE_MULTILINE)
		#lines = self.textBox_screen.GetLineCount()
		#width = self.textBox_screen.TextWidth(stc.STC_STYLE_LINENUMBER, "       "+str(lines))
		#self.textBox_screen.SetMarginWidth(0, width) 
		self.textBox_screen = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,500 ), wx.TE_MULTILINE|wx.HSCROLL )
		self.textBox_screen.SetEditable(0)
		bSizer_screen.Add( self.textBox_screen, 0, wx.ALL, 5 )
		
		bSizer1.Add( bSizer_screen, 1, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		self.MenuBar = wx.MenuBar( 0 )
		self.menu_file = wx.Menu()
		self.file_item_open = wx.MenuItem( self.menu_file, wx.ID_ANY, u"Open", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.Append( self.file_item_open )
		
		self.file_item_save = wx.MenuItem( self.menu_file, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.Append( self.file_item_save )
		
		self.file_item_exit = wx.MenuItem( self.menu_file, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_file.Append( self.file_item_exit )
		
		
		self.MenuBar.Append( self.menu_file, u"File" ) 
		
		self.menu_help = wx.Menu()
		self.help_item_about = wx.MenuItem( self.menu_help, wx.ID_ANY, u"About", wx.EmptyString, wx.ITEM_NORMAL )
		self.menu_help.Append( self.help_item_about )
		
		self.MenuBar.Append( self.menu_help, u"Help" ) 
		
		self.SetMenuBar( self.MenuBar )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.textBox_default.Bind(wx.EVT_CHAR, self.onChar)
		self.button_add.Bind( wx.EVT_BUTTON, self.addfield )
		self.button_addRecord.Bind(wx.EVT_BUTTON , self.addRecord)
		self.button_submitRecord.Bind(wx.EVT_BUTTON , self.submitRecord)
		self.button_submit_schema.Bind( wx.EVT_BUTTON, self.submit )
		self.button_import.Bind( wx.EVT_BUTTON, self.import_from_excel )
		self.button_json.Bind( wx.EVT_BUTTON, self.import_from_json )
		self.button_avro.Bind( wx.EVT_BUTTON, self.import_from_avro )
		self.button_restart.Bind( wx.EVT_BUTTON, self.restart )
		self.Bind( wx.EVT_MENU, self.openDialog, id = self.file_item_open.GetId() )
		self.Bind( wx.EVT_MENU, self.saveDialog, id = self.file_item_save.GetId() )
		self.Bind( wx.EVT_MENU, self.exit, id = self.file_item_exit.GetId() )
		self.checkBox_Edit.Bind(wx.EVT_CHECKBOX , self.edit)
		self.Bind( wx.EVT_MENU, self.help, id = self.help_item_about.GetId() )
		self.dropdown_data_type.Bind(wx.EVT_COMBOBOX, self.OnSelect)
		
		
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	
	def onChar(self , event):
		data_type = self.dropdown_data_type.GetValue()
		if(data_type == 'int' or data_type == 'long' or data_type == 'double' or data_type == 'float'):
			key = event.GetKeyCode()
			
			acceptable_characters = '1234567890.\b'
			
			if chr(key) in acceptable_characters: 
				event.Skip() 
			#	return
			else:
				dlg = wx.MessageDialog(self, 'Value in default should be integer','', wx.OK | wx.CANCEL | wx.ICON_ERROR)
				val = dlg.ShowModal()
				dlg.Show()
		else:
			event.Skip()
	
	def addfield( self, event ):
		event.Skip()
	
	def addRecord( self, event ):
		event.Skip()
	
	def submitRecord(self, event):
		event.Skip()
		
	def submit( self, event ):
		event.Skip()
	
	def import_from_excel( self, event ):
		event.Skip()
		
	def import_from_json(self , event):
		event.Skip()
		
	def import_from_avro(self , event):
		event.Skip()
		
	def restart( self, event ):
		event.Skip()
	
	def openDialog( self, event ):
		event.Skip()
	
	def saveDialog( self, event ):
		event.Skip()
	
	def exit( self, event ):
		event.Skip()
	
	def edit( self, event ):
		event.Skip()
	
	def help( self, event ):
		event.Skip()
	        
	def OnSelect( self, event ):
		event.Skip()
		
	
		
class Record ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = 'Add Nested Records', pos = wx.DefaultPosition, size = wx.Size( 800,450 ), style = wx.MINIMIZE_BOX|wx.SYSTEM_MENU|
                  wx.CAPTION|wx.CLOSE_BOX|wx.CLIP_CHILDREN )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetIcon(wx.Icon('images\\logo.jpg'))
		bSizer1 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer2_options = wx.BoxSizer( wx.VERTICAL )
		
		bSizer_mainName = wx.BoxSizer( wx.HORIZONTAL)
		
		self.static_mainName = wx.StaticText(self , wx.ID_ANY , u"Name *", wx.DefaultPosition, wx.Size(80,-1),0)
		self.static_mainName.Wrap(-1)
		bSizer_mainName.Add(self.static_mainName , 0, wx.ALL, 5)
		
		self.textbox_main = wx.TextCtrl(self, wx.ID_ANY,wx.EmptyString,wx.DefaultPosition,wx.Size(125,-1),0)
		bSizer_mainName.Add(self.textbox_main , 0, wx.ALL , 5)
		
		bSizer2_options.Add(bSizer_mainName , 1, wx.EXPAND , 5)
		
		bSizer_name = wx.BoxSizer( wx.HORIZONTAL )
		
		self.static_name = wx.StaticText( self, wx.ID_ANY, u"SubrecName*", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.static_name.Wrap( -1 )
		bSizer_name.Add( self.static_name, 0, wx.ALL, 5 )
		
		self.textBox_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,-1 ), 0 )
		bSizer_name.Add( self.textBox_name, 0, wx.ALL, 5 )
		
		
		bSizer2_options.Add( bSizer_name, 1, wx.EXPAND, 5 )
		
		bSizer_nameField = wx.BoxSizer( wx.HORIZONTAL )
		
		self.static__nameField = wx.StaticText( self, wx.ID_ANY, u" FieldName *", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.static__nameField.Wrap( -1 )
		bSizer_nameField.Add( self.static__nameField, 0, wx.ALL, 5 )
		
		self.textBox_nameField = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 125,-1 ), 0 )
		bSizer_nameField.Add( self.textBox_nameField, 0, wx.ALL, 5 )
		
		
		bSizer2_options.Add( bSizer_nameField, 1, wx.EXPAND, 5 )
		
		
		bSizer_data_type_1 = wx.BoxSizer( wx.HORIZONTAL )
		self.static_data_type = wx.StaticText( self, wx.ID_ANY, u"Data Type *", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.static_data_type.Wrap( -1 )
		bSizer_data_type_1.Add( self.static_data_type, 0, wx.ALL, 5 )
		
		dropdown_data_typeChoices = [ u"int", u"string", u"long", u"float", u"boolean", u"double"]
		self.dropdown_data_type = wx.ComboBox(self, -1, pos=wx.DefaultPosition, size=( 125,-1 ), choices=dropdown_data_typeChoices, style=wx.CB_READONLY)
		bSizer_data_type_1.Add( self.dropdown_data_type, 0, wx.ALL, 5 )
		
		bSizer2_options.Add(bSizer_data_type_1,1, wx.EXPAND, 5)
		bSizer_data_type_2 = wx.BoxSizer( wx.HORIZONTAL )
	
		
		self.checkBox_Edit = wx.CheckBox( self, wx.ID_ANY, u"Edit", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		bSizer_data_type_2.Add( self.checkBox_Edit, 0, wx.ALL, 5 )
		
		self.checkBox_Null = wx.CheckBox( self, wx.ID_ANY, u"Null", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		bSizer_data_type_2.Add( self.checkBox_Null, 0, wx.ALL, 5 )
		
		#bSizer_data_type_1.Add( bSizer_data_type_2, 1, wx.EXPAND, 5 )
		
		#bSizer_data_type.Add( bSizer_data_type_1, 1, wx.EXPAND, 5 )
		
		bSizer2_options.Add(bSizer_data_type_2 ,1, wx.EXPAND, 5)
		
		bSizer_nested = wx.BoxSizer(wx.HORIZONTAL)
		
		self.nested = wx.Button( self, wx.ID_ANY, u"+ Sub-Record", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		self.nested.Disable()
		
		self.nestedField = wx.Button( self, wx.ID_ANY, u"Submit Sub-Record", wx.DefaultPosition, wx.Size( 110,-1 ), 0 )
		self.nestedField.Disable()
		
		self.panle_2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		
		
		bSizer_nested.Add(self.nested, 0 ,wx.ALL, 5)
		bSizer_nested.Add( self.panle_2, 1, wx.EXPAND |wx.ALL, 5 )
		bSizer_nested.Add(self.nestedField , 0, wx.ALL, 5)
		
		bSizer2_options.Add(bSizer_nested, 1, wx.EXPAND, 5)
		
		bSizer_add_sub = wx.BoxSizer( wx.HORIZONTAL )
		
		self.button_add = wx.Button( self, wx.ID_ANY, u"Add the record", wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		bSizer_add_sub.Add( self.button_add, 0, wx.ALL, 5 )
		
		self.panle_1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer_add_sub.Add( self.panle_1, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.button_submit_schema = wx.Button( self, wx.ID_ANY, u"Submit", wx.DefaultPosition, wx.Size( 110,-1 ), 0 )
		self.button_submit_schema.Disable()
		bSizer_add_sub.Add( self.button_submit_schema, 0, wx.ALL, 5 )
		
		
		bSizer2_options.Add( bSizer_add_sub, 1, wx.EXPAND, 5 )
		
		
		
		
		bSizer1.Add( bSizer2_options, 1, wx.EXPAND, 3 )
		
		bSizer_screen = wx.BoxSizer( wx.VERTICAL )
		
		self.textBox_screen_second = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 650,400 ), wx.TE_MULTILINE|wx.HSCROLL)
		self.textBox_screen_second.SetEditable(0)
		bSizer_screen.Add( self.textBox_screen_second, 0, wx.ALL, 5 )		
		
		bSizer1.Add( bSizer_screen, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		
		self.Centre( wx.BOTH )
		
		self.nested.Bind(wx.EVT_BUTTON , self.nestedfun)
		self.nestedField.Bind(wx.EVT_BUTTON , self.addnestedField)
		self.button_add.Bind( wx.EVT_BUTTON, self.addrecord )
		self.button_submit_schema.Bind( wx.EVT_BUTTON, self.submit )
		self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
		self.checkBox_Edit.Bind(wx.EVT_CHECKBOX , self.edit)
		
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def addrecord( self, event ):
		event.Skip()
		
	def nestedfun( self, event):
		event.Skip()
		
	def addnestedField( self, event):
		event.Skip()
		
	def edit( self, event ):
		event.Skip()
	def OnCloseWindow(self, event):
		event.Skip()
	def submit( self, event ):
		event.Skip()
	def closeapp(self, event):
		event.Skip()
class MyHelp(wx.Frame):  
    def __init__(self):  
        wx.Frame.__init__(self, None, -1, 'About', size=(620, 670) , style = wx.MINIMIZE_BOX|wx.SYSTEM_MENU|
                  wx.CAPTION|wx.CLOSE_BOX|wx.CLIP_CHILDREN)  
        self.SetBackgroundColour("white")
        self.SetIcon(wx.Icon('images\\logo.jpg'))
        panel1 = wx.Panel(self)
        panel2 = scrolled.ScrolledPanel(self,-1, size=(600,650), pos=(0,28), style=wx.SIMPLE_BORDER)
        panel2.SetupScrolling()
        panel2.SetBackgroundColour('#FFFFFF')
		
        help1 = wx.BoxSizer( wx.VERTICAL )
        Header = wx.BoxSizer(wx.HORIZONTAL)
        self.text = wx.StaticText(panel2, -1, "\n  Avro Schema Generator", wx.DefaultPosition)
        font = wx.Font(14, wx.DECORATIVE, wx.NORMAL, wx.BOLD)
        self.text.SetFont(font)
        Header.Add(self.text)
		
        self.introduction = wx.StaticText(panel2, -1 , "\n Avro Schema Generator is a tool which eases the process of schemas creation and conforms to industry standards. It also helps in improving productivity as well as reliability.")
        fontDefault = wx.Font(11,wx.DECORATIVE,wx.NORMAL,wx.NORMAL)
        self.introduction.SetFont(fontDefault)
        self.introduction.Wrap(580)

        fontHeading = wx.Font(12,wx.DECORATIVE,wx.NORMAL,wx.BOLD)

        self.mainpanel2 = wx.StaticText(panel2, -1 , "\n Navigating the Tool Window : ")
        self.mainpanel2.SetFont(fontHeading)

        self.mainpanel2Intro = wx.StaticText(panel2, -1 , "\n • The Tool Window is divided into two parts Control Panel and Visualisation Panel. The Control Panel enables interaction with the user and get the inputs. The Visualisation Panel enables dynamic view of how your schema is shaping up")
        self.mainpanel2Intro.SetFont(fontDefault)
        self.mainpanel2Intro.Wrap(580)

        self.mainFeature1 = wx.StaticText(panel2, -1 , "\n • User can input the relevant information in the various fields such as: Namespace, Type and Schema Name etc. in the Control Panel to create an Avro Schema. Once the user adds the first field after getting all inputs,'Submit' button gets enabled ")
        self.mainFeature1.SetFont(fontDefault)
        self.mainFeature1.Wrap(580)

        self.mainFeature2 = wx.StaticText(panel2, -1 , "\n • The * Marked items are mandatory in order to add a record to the Visualisation Panel. Other fields are optional but add useful information to the schema ")
        self.mainFeature2.SetFont(fontDefault)
        self.mainFeature2.Wrap(580)
        
        self.mainFeature3 = wx.StaticText(panel2, -1 , "\n • Visualisation window is not editable(Strongly recommended to run the manually edited schema through the Avro Schema Validator) ")
        self.mainFeature3.SetFont(fontDefault)
        self.mainFeature3.Wrap(580)
        
        self.Nested= wx.StaticText(panel2, -1 , "\n Adding Nested Record :")
        self.Nested.SetFont(fontHeading)

        self.mainFeature4 = wx.StaticText(panel2, -1 , "\n • Has a similar user interface like the Tool Window ")
        self.mainFeature4.SetFont(fontDefault)
        self.mainFeature4.Wrap(580)

        self.mainFeature5 = wx.StaticText(panel2, -1 , "\n • * Marked items are mandatory to be filled to add a Nested Record ")
        self.mainFeature5.SetFont(fontDefault)
        self.mainFeature5.Wrap(580)

        self.mainFeature6 = wx.StaticText(panel2, -1 , "\n • User can add the 'Nested Record' by clicking on the 'Add the record' button and see the desired output on the 'Visualization Panel' of 'Nested Record Window' ")
        self.mainFeature6.SetFont(fontDefault)
        self.mainFeature6.Wrap(580)

        self.mainFeature12 = wx.StaticText(panel2, -1 , "\n • To add more levels of nesting.The Tool comes with two special buttons : '+Sub-Record' and 'Submit Sub-Record' ")
        self.mainFeature12.SetFont(fontDefault)
        self.mainFeature12.Wrap(580)

        self.mainFeature13 = wx.StaticText(panel2, -1 , "\n • '+Sub-Record' enables the use to add one more level of nesting (Warning : Use this feature carefully as this feature adds fixed number of spaces ) ")
        self.mainFeature13.SetFont(fontDefault)
        self.mainFeature13.Wrap(580)

        self.mainFeature14 = wx.StaticText(panel2, -1 , "\n • 'Submit Sub-Record' takes input from the Control Panel and shows it in the 'Visualisation Panel' (Note : Submit Sub-Record is only used to add records with more than one level of nesting)")
        self.mainFeature14.SetFont(fontDefault)
        self.mainFeature14.Wrap(580)
		
        self.mainFeature7 = wx.StaticText(panel2, -1 , "\n • After clicking the 'Submit' button in the pop-up window the pop-up window automatically gets closed and the output is stored at a temporary memory location ")
        self.mainFeature7.SetFont(fontDefault)
        self.mainFeature7.Wrap(580)
		
        self.mainFeature8 = wx.StaticText(panel2, -1 , "\n • Once the user clicks on 'Submit Sub-Record' button the tool fetches the output from the temporary memory and adds it to the 'Visualisation Panel' of the Tool Window and 'Add Sub-Record' button will automatically get enable for the user to add more nested records and 'Submit Sub-Record' button will get disabled  ")
        self.mainFeature8.SetFont(fontDefault)
        self.mainFeature8.Wrap(580)
        self.excel_csv= wx.StaticText(panel2, -1 , "\n CSV files : ")
        self.excel_csv.SetFont(fontHeading)

        self.mainFeature10 = wx.StaticText(panel2, -1 , "\n • It enables schema creation through 'csv' files. User can click on the 'Open.csv' button to import the csv from the desired location")
        self.mainFeature10.SetFont(fontDefault)
        self.mainFeature10.Wrap(580)

        self.mainFeature11 = wx.StaticText(panel2, -1 , "\n • Once the user opens the selected file, The tool automatically creates the corresponding'Avro Schema' file. The output of a 'csv' file is visible in the 'Visualisation Panel' and also get stored on the default location i.e. Current location where the tool is installed")
        self.mainFeature11.SetFont(fontDefault)
        self.mainFeature11.Wrap(580)

        self.json= wx.StaticText(panel2, -1 , "\n Json files : ")
        self.json.SetFont(fontHeading)

        self.mainFeature15 = wx.StaticText(panel2, -1 , "\n • It enables schema creation through 'json' files. User can click on the 'Open.json' button to import the 'json' file from the desired location")
        self.mainFeature15.SetFont(fontDefault)
        self.mainFeature15.Wrap(580)

        self.mainFeature16 = wx.StaticText(panel2, -1 , "\n • Once the user opens the selected file, The tool automatically creates the corresponding'Avro Schema' file. The output of an 'json' file is visible in the 'Visualisation Panel' and also get stored on the default location i.e. Current location where the tool is installed")
        self.mainFeature16.SetFont(fontDefault)
        self.mainFeature16.Wrap(580)

        self.avro= wx.StaticText(panel2, -1 , "\n Avro files : ")
        self.avro.SetFont(fontHeading)

        self.mainFeature17 = wx.StaticText(panel2, -1 , "\n • It enables schema creation through 'avro' files. User can click on the 'Open.avro' button to import the 'avro' file from the desired location")
        self.mainFeature17.SetFont(fontDefault)
        self.mainFeature17.Wrap(580)

        self.mainFeature18 = wx.StaticText(panel2, -1 , "\n • Once the user opens the selected file, The tool automatically creates the corresponding'Avro Schema' file. The output of an 'avro' file is visible in the 'Visualisation Panel' and also get stored on the default location i.e. Current location where the tool is installed")
        self.mainFeature18.SetFont(fontDefault)
        self.mainFeature18.Wrap(580)
		
        self.fileMenu = wx.StaticText(panel2, -1 , "\n File Menu : ")
        self.fileMenu.SetFont(fontHeading)

        self.fileFeature1 = wx.StaticText(panel2, -1 , "\n • Save: It Opens the window 'Save Dialog Box' and helps save the (.avsc)file at the specified location   ")
        self.fileFeature1.SetFont(fontDefault)
        self.fileFeature1.Wrap(580)
        
        self.fileFeature2 = wx.StaticText(panel2, -1 , "\n • Open: Enables user to open an already existing 'Avro Schema' and make edits to the schema(It is Strongly recommended to run the manually edited schmema through the Avro Schema Validator)  ")
        self.fileFeature2.SetFont(fontDefault)
        self.fileFeature2.Wrap(580)

        self.fileFeature3 = wx.StaticText(panel2, -1 , "\n • Exit: It is used to close 'Avro Schema Generator' Desktop App.  ")
        self.fileFeature3.SetFont(fontDefault)
        self.fileFeature3.Wrap(580)
        self.fileFeature4 = wx.StaticText(panel2, -1 , "\n 				                                                    ")
        self.fileFeature4.SetFont(fontDefault)
        
        help1.Add(Header , 0 , wx.ALL)
        help1.Add(self.introduction , 0 , wx.ALL)
        #help1.Add(self.Features , 0 , wx.ALL)
        #help1.Add(self.Feature1 , 0 , wx.ALL)
        #help1.Add(self.Feature2 , 0 , wx.ALL)
        help1.Add(self.mainpanel2 , 0 ,wx.ALL)
        help1.Add(self.mainpanel2Intro , 0 ,wx.ALL)
        help1.Add(self.mainFeature1 , 0 ,wx.ALL)
        help1.Add(self.mainFeature2 , 0 ,wx.ALL)
        help1.Add(self.mainFeature3 , 0 ,wx.ALL)
        help1.Add(self.Nested , 0 ,wx.ALL)
        help1.Add(self.mainFeature4 , 0 ,wx.ALL)
        help1.Add(self.mainFeature5 , 0 ,wx.ALL)
        help1.Add(self.mainFeature6 , 0 ,wx.ALL)
        help1.Add(self.mainFeature12 , 0 ,wx.ALL)
        help1.Add(self.mainFeature13 , 0 ,wx.ALL)
        help1.Add(self.mainFeature14 , 0 ,wx.ALL)
        help1.Add(self.mainFeature7 , 0 ,wx.ALL)
        help1.Add(self.mainFeature8 , 0 ,wx.ALL)
        #help1.Add(self.mainFeature9 , 0 ,wx.ALL)
        help1.Add(self.excel_csv , 0 ,wx.ALL)
        help1.Add(self.mainFeature10 , 0 ,wx.ALL)
        help1.Add(self.mainFeature11 , 0 ,wx.ALL)
        help1.Add(self.json , 0 ,wx.ALL)
        help1.Add(self.mainFeature15 , 0 ,wx.ALL)
        help1.Add(self.mainFeature16 , 0 ,wx.ALL)
        help1.Add(self.avro , 0 ,wx.ALL)
        help1.Add(self.mainFeature17 , 0 ,wx.ALL)
        help1.Add(self.mainFeature18 , 0 ,wx.ALL)
        help1.Add(self.fileMenu , 0 ,wx.ALL)
        help1.Add(self.fileFeature1 , 0 ,wx.ALL)
        help1.Add(self.fileFeature2 , 0 ,wx.ALL)
        help1.Add(self.fileFeature3 , 0 ,wx.ALL)
        help1.Add(self.fileFeature4 , 0 ,wx.ALL)
        

        panel2.SetSizer( help1 )
        #self.Layout()		
