# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.propgrid as pg

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"DotEditor", pos = wx.DefaultPosition, size = wx.Size( 942,688 ), style = wx.DEFAULT_FRAME_STYLE|wx.NO_BORDER )
		
		self.SetSizeHintsSz( wx.Size( 800,600 ), wx.DefaultSize )
		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer14 = wx.FlexGridSizer( 3, 1, 0, 0 )
		fgSizer14.AddGrowableCol( 0 )
		fgSizer14.AddGrowableRow( 1 )
		fgSizer14.SetFlexibleDirection( wx.BOTH )
		fgSizer14.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel16 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER|wx.TAB_TRAVERSAL )
		fgSizer15 = wx.FlexGridSizer( 1, 8, 0, 0 )
		fgSizer15.AddGrowableCol( 7 )
		fgSizer15.SetFlexibleDirection( wx.BOTH )
		fgSizer15.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel17 = wx.Panel( self.m_panel16, wx.ID_ANY, wx.DefaultPosition, wx.Size( 3,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel17.SetBackgroundColour( wx.Colour( 21, 120, 180 ) )
		
		fgSizer15.Add( self.m_panel17, 1, wx.EXPAND |wx.ALL, 0 )
		
		
		fgSizer15.AddSpacer( ( 8, 30), 1, wx.EXPAND, 5 )
		
		self.m_bpButton_new = wx.BitmapButton( self.m_panel16, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 40,-1 ), wx.BU_AUTODRAW|wx.NO_BORDER )
		
		self.m_bpButton_new.SetBitmapFocus( wx.NullBitmap )
		self.m_bpButton_new.SetBitmapHover( wx.NullBitmap )
		self.m_bpButton_new.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.m_bpButton_new.SetToolTipString( u"Create a new Graph" )
		
		fgSizer15.Add( self.m_bpButton_new, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.m_bpButton_open = wx.BitmapButton( self.m_panel16, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 40,-1 ), wx.BU_AUTODRAW|wx.NO_BORDER )
		
		self.m_bpButton_open.SetBitmapFocus( wx.NullBitmap )
		self.m_bpButton_open.SetBitmapHover( wx.NullBitmap )
		self.m_bpButton_open.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.m_bpButton_open.SetToolTipString( u"Open a existed Graph file" )
		
		fgSizer15.Add( self.m_bpButton_open, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_bpButton_save = wx.BitmapButton( self.m_panel16, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 40,-1 ), wx.BU_AUTODRAW|wx.NO_BORDER )
		
		self.m_bpButton_save.SetBitmapFocus( wx.NullBitmap )
		self.m_bpButton_save.SetBitmapHover( wx.NullBitmap )
		self.m_bpButton_save.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.m_bpButton_save.SetToolTipString( u"Save graph to file" )
		
		fgSizer15.Add( self.m_bpButton_save, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_bpButton_script = wx.BitmapButton( self.m_panel16, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 40,-1 ), wx.BU_AUTODRAW|wx.NO_BORDER )
		
		self.m_bpButton_script.SetBitmapFocus( wx.NullBitmap )
		self.m_bpButton_script.SetBitmapHover( wx.NullBitmap )
		self.m_bpButton_script.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.m_bpButton_script.SetToolTipString( u"View dot script" )
		
		fgSizer15.Add( self.m_bpButton_script, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_bpButton_export = wx.BitmapButton( self.m_panel16, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 40,-1 ), wx.BU_AUTODRAW|wx.NO_BORDER )
		
		self.m_bpButton_export.SetBitmapFocus( wx.NullBitmap )
		self.m_bpButton_export.SetBitmapHover( wx.NullBitmap )
		self.m_bpButton_export.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.m_bpButton_export.SetToolTipString( u"Save graph to image file" )
		
		fgSizer15.Add( self.m_bpButton_export, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_button_save_as = wx.Button( self.m_panel16, wx.ID_ANY, u"Save As", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_save_as.Hide()
		
		fgSizer15.Add( self.m_button_save_as, 0, wx.ALL, 5 )
		
		
		self.m_panel16.SetSizer( fgSizer15 )
		self.m_panel16.Layout()
		fgSizer15.Fit( self.m_panel16 )
		fgSizer14.Add( self.m_panel16, 1, wx.EXPAND |wx.ALL, 0 )
		
		self.m_splitter2 = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
		self.m_splitter2.Bind( wx.EVT_IDLE, self.m_splitter2OnIdle )
		self.m_splitter2.SetMinimumPaneSize( 50 )
		
		self.m_splitter2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		self.m_panel1 = wx.Panel( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER|wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_splitter4 = wx.SplitterWindow( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_splitter4.Bind( wx.EVT_IDLE, self.m_splitter4OnIdle )
		self.m_splitter4.SetMinimumPaneSize( 50 )
		
		self.m_panel4 = wx.Panel( self.m_splitter4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER|wx.TAB_TRAVERSAL )
		self.m_panel4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer1 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer1.AddGrowableCol( 0 )
		fgSizer1.AddGrowableRow( 1 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel7 = wx.Panel( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		self.m_panel7.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		fgSizer7 = wx.FlexGridSizer( 0, 6, 0, 0 )
		fgSizer7.AddGrowableCol( 0 )
		fgSizer7.AddGrowableRow( 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText4 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Item List", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		self.m_staticText4.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		fgSizer7.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 2 )
		
		self.m_bpButton_graphsetting = wx.BitmapButton( self.m_panel7, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|wx.NO_BORDER )
		
		self.m_bpButton_graphsetting.SetBitmapFocus( wx.NullBitmap )
		self.m_bpButton_graphsetting.SetBitmapHover( wx.NullBitmap )
		self.m_bpButton_graphsetting.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		fgSizer7.Add( self.m_bpButton_graphsetting, 0, wx.ALL, 5 )
		
		
		fgSizer7.AddSpacer( ( 12, 0), 1, wx.EXPAND, 5 )
		
		self.m_bpButton_add = wx.BitmapButton( self.m_panel7, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|wx.NO_BORDER )
		
		self.m_bpButton_add.SetBitmapFocus( wx.NullBitmap )
		self.m_bpButton_add.SetBitmapHover( wx.NullBitmap )
		self.m_bpButton_add.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		fgSizer7.Add( self.m_bpButton_add, 0, wx.ALL, 5 )
		
		self.m_bpButton_minus = wx.BitmapButton( self.m_panel7, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|wx.NO_BORDER )
		
		self.m_bpButton_minus.SetBitmapFocus( wx.NullBitmap )
		self.m_bpButton_minus.SetBitmapHover( wx.NullBitmap )
		self.m_bpButton_minus.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		fgSizer7.Add( self.m_bpButton_minus, 0, wx.ALL, 5 )
		
		
		fgSizer7.AddSpacer( ( 5, 0), 1, wx.EXPAND, 5 )
		
		
		self.m_panel7.SetSizer( fgSizer7 )
		self.m_panel7.Layout()
		fgSizer7.Fit( self.m_panel7 )
		fgSizer1.Add( self.m_panel7, 0, wx.ALL|wx.EXPAND, 1 )
		
		self.m_tree = wx.TreeCtrl( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE|wx.TR_FULL_ROW_HIGHLIGHT|wx.TR_NO_LINES|wx.NO_BORDER )
		self.m_tree.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, "Consolas" ) )
		self.m_tree.SetForegroundColour( wx.Colour( 40, 40, 40 ) )
		
		fgSizer1.Add( self.m_tree, 0, wx.ALL|wx.EXPAND, 2 )
		
		
		self.m_panel4.SetSizer( fgSizer1 )
		self.m_panel4.Layout()
		fgSizer1.Fit( self.m_panel4 )
		self.m_panel5 = wx.Panel( self.m_splitter4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer5 = wx.FlexGridSizer( 2, 0, 0, 0 )
		fgSizer5.AddGrowableCol( 0 )
		fgSizer5.AddGrowableRow( 1 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel8 = wx.Panel( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		self.m_panel8.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		fgSizer10 = wx.FlexGridSizer( 0, 0, 0, 0 )
		fgSizer10.AddGrowableCol( 0 )
		fgSizer10.AddGrowableRow( 0 )
		fgSizer10.SetFlexibleDirection( wx.BOTH )
		fgSizer10.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText_pg = wx.StaticText( self.m_panel8, wx.ID_ANY, u"Item Properties", wx.DefaultPosition, wx.DefaultSize, 0|wx.NO_BORDER )
		self.m_staticText_pg.Wrap( -1 )
		self.m_staticText_pg.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		fgSizer10.Add( self.m_staticText_pg, 0, wx.ALL|wx.EXPAND, 2 )
		
		
		self.m_panel8.SetSizer( fgSizer10 )
		self.m_panel8.Layout()
		fgSizer10.Fit( self.m_panel8 )
		fgSizer5.Add( self.m_panel8, 1, wx.EXPAND |wx.ALL, 1 )
		
		self.m_pgManager1 = pg.PropertyGridManager(self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.propgrid.PGMAN_DEFAULT_STYLE|wx.propgrid.PG_BOLD_MODIFIED|wx.propgrid.PG_SPLITTER_AUTO_CENTER|wx.propgrid.PG_TOOLBAR|wx.propgrid.PG_TOOLTIPS|wx.TAB_TRAVERSAL|wx.NO_BORDER)
		self.m_pgManager1.SetExtraStyle( wx.propgrid.PG_EX_MODE_BUTTONS ) 
		self.m_pgManager1.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		fgSizer5.Add( self.m_pgManager1, 2, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 2 )
		
		
		self.m_panel5.SetSizer( fgSizer5 )
		self.m_panel5.Layout()
		fgSizer5.Fit( self.m_panel5 )
		self.m_splitter4.SplitHorizontally( self.m_panel4, self.m_panel5, 264 )
		bSizer5.Add( self.m_splitter4, 2, wx.EXPAND, 0 )
		
		
		self.m_panel1.SetSizer( bSizer5 )
		self.m_panel1.Layout()
		bSizer5.Fit( self.m_panel1 )
		self.m_panel81 = wx.Panel( self.m_splitter2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer8 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer8.AddGrowableCol( 0 )
		fgSizer8.AddGrowableRow( 1 )
		fgSizer8.SetFlexibleDirection( wx.BOTH )
		fgSizer8.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel12 = wx.Panel( self.m_panel81, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		self.m_panel12.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		fgSizer11 = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgSizer11.AddGrowableCol( 0 )
		fgSizer11.AddGrowableRow( 0 )
		fgSizer11.SetFlexibleDirection( wx.BOTH )
		fgSizer11.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText6 = wx.StaticText( self.m_panel12, wx.ID_ANY, u" Graph Preview", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText6.Wrap( -1 )
		self.m_staticText6.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText6.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		fgSizer11.Add( self.m_staticText6, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 1 )
		
		
		fgSizer11.AddSpacer( ( 0, 26), 1, wx.EXPAND, 5 )
		
		
		self.m_panel12.SetSizer( fgSizer11 )
		self.m_panel12.Layout()
		fgSizer11.Fit( self.m_panel12 )
		fgSizer8.Add( self.m_panel12, 1, wx.EXPAND |wx.ALL, 1 )
		
		self.m_panel_paint = wx.ScrolledWindow( self.m_panel81, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.NO_BORDER|wx.VSCROLL )
		self.m_panel_paint.SetScrollRate( 5, 5 )
		self.m_panel_paint.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		fgSizer8.Add( self.m_panel_paint, 1, wx.EXPAND |wx.ALL, 1 )
		
		
		self.m_panel81.SetSizer( fgSizer8 )
		self.m_panel81.Layout()
		fgSizer8.Fit( self.m_panel81 )
		self.m_splitter2.SplitVertically( self.m_panel1, self.m_panel81, 295 )
		fgSizer14.Add( self.m_splitter2, 1, wx.EXPAND, 0 )
		
		self.m_panel18 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		fgSizer151 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer151.AddGrowableCol( 1 )
		fgSizer151.AddGrowableRow( 0 )
		fgSizer151.SetFlexibleDirection( wx.BOTH )
		fgSizer151.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel171 = wx.Panel( self.m_panel18, wx.ID_ANY, wx.DefaultPosition, wx.Size( 3,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel171.SetBackgroundColour( wx.Colour( 21, 120, 180 ) )
		
		fgSizer151.Add( self.m_panel171, 1, wx.EXPAND |wx.ALL, 0 )
		
		self.m_staticText1_hint = wx.StaticText( self.m_panel18, wx.ID_ANY, u"Hint", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1_hint.Wrap( 50 )
		self.m_staticText1_hint.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 72, 90, 90, False, wx.EmptyString ) )
		self.m_staticText1_hint.SetForegroundColour( wx.Colour( 21, 120, 180 ) )
		
		fgSizer151.Add( self.m_staticText1_hint, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel18.SetSizer( fgSizer151 )
		self.m_panel18.Layout()
		fgSizer151.Fit( self.m_panel18 )
		fgSizer14.Add( self.m_panel18, 1, wx.EXPAND |wx.ALL, 0 )
		
		
		self.SetSizer( fgSizer14 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_bpButton_new.Bind( wx.EVT_BUTTON, self.onNewGraph )
		self.m_bpButton_open.Bind( wx.EVT_BUTTON, self.onOpenGraph )
		self.m_bpButton_save.Bind( wx.EVT_BUTTON, self.onSaveGraph )
		self.m_bpButton_script.Bind( wx.EVT_BUTTON, self.onViewSource )
		self.m_bpButton_export.Bind( wx.EVT_BUTTON, self.onExportImage )
		self.m_button_save_as.Bind( wx.EVT_BUTTON, self.onSaveAs )
		self.m_bpButton_graphsetting.Bind( wx.EVT_BUTTON, self.onGraphSetting )
		self.m_bpButton_add.Bind( wx.EVT_BUTTON, self.onAppendItem )
		self.m_bpButton_minus.Bind( wx.EVT_BUTTON, self.onDeleteItem )
		self.m_tree.Bind( wx.EVT_TREE_SEL_CHANGED, self.onItemSelected )
		self.m_pgManager1.Bind( pg.EVT_PG_CHANGED, self.onPGChanged )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onNewGraph( self, event ):
		event.Skip()
	
	def onOpenGraph( self, event ):
		event.Skip()
	
	def onSaveGraph( self, event ):
		event.Skip()
	
	def onViewSource( self, event ):
		event.Skip()
	
	def onExportImage( self, event ):
		event.Skip()
	
	def onSaveAs( self, event ):
		event.Skip()
	
	def onGraphSetting( self, event ):
		event.Skip()
	
	def onAppendItem( self, event ):
		event.Skip()
	
	def onDeleteItem( self, event ):
		event.Skip()
	
	def onItemSelected( self, event ):
		event.Skip()
	
	def onPGChanged( self, event ):
		event.Skip()
	
	def m_splitter2OnIdle( self, event ):
		self.m_splitter2.SetSashPosition( 295 )
		self.m_splitter2.Unbind( wx.EVT_IDLE )
	
	def m_splitter4OnIdle( self, event ):
		self.m_splitter4.SetSashPosition( 264 )
		self.m_splitter4.Unbind( wx.EVT_IDLE )
	

###########################################################################
## Class DialogAppend
###########################################################################

class DialogAppend ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Append Item", pos = wx.DefaultPosition, size = wx.Size( 373,226 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer18 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer18.AddGrowableCol( 0 )
		fgSizer18.AddGrowableRow( 0 )
		fgSizer18.SetFlexibleDirection( wx.BOTH )
		fgSizer18.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel27 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel27.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		fgSizer16 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer16.AddGrowableCol( 1 )
		fgSizer16.AddGrowableRow( 0 )
		fgSizer16.SetFlexibleDirection( wx.BOTH )
		fgSizer16.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel21 = wx.Panel( self.m_panel27, wx.ID_ANY, wx.DefaultPosition, wx.Size( 3,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel21.SetBackgroundColour( wx.Colour( 21, 120, 180 ) )
		
		fgSizer16.Add( self.m_panel21, 1, wx.ALL|wx.EXPAND, 0 )
		
		fgSizer17 = wx.FlexGridSizer( 4, 1, 0, 0 )
		fgSizer17.AddGrowableCol( 0 )
		fgSizer17.AddGrowableRow( 1 )
		fgSizer17.SetFlexibleDirection( wx.BOTH )
		fgSizer17.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		m_radioBox_typeChoices = [ u"Node", u"Edge", u"Subgraph" ]
		self.m_radioBox_type = wx.RadioBox( self.m_panel27, wx.ID_ANY, u"Item Type", wx.DefaultPosition, wx.DefaultSize, m_radioBox_typeChoices, 3, wx.RA_SPECIFY_COLS )
		self.m_radioBox_type.SetSelection( 0 )
		fgSizer17.Add( self.m_radioBox_type, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel_node = wx.Panel( self.m_panel27, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel_node.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		fgSizer2 = wx.FlexGridSizer( 2, 2, 0, 0 )
		fgSizer2.AddGrowableCol( 1 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1 = wx.StaticText( self.m_panel_node, wx.ID_ANY, u"Node/NodeA:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer2.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		m_comboBox_nodeAChoices = []
		self.m_comboBox_nodeA = wx.ComboBox( self.m_panel_node, wx.ID_ANY, u"NewNode", wx.DefaultPosition, wx.DefaultSize, m_comboBox_nodeAChoices, 0 )
		fgSizer2.Add( self.m_comboBox_nodeA, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText2 = wx.StaticText( self.m_panel_node, wx.ID_ANY, u"Node B:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer2.Add( self.m_staticText2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		m_comboBox_nodeBChoices = []
		self.m_comboBox_nodeB = wx.ComboBox( self.m_panel_node, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox_nodeBChoices, 0 )
		self.m_comboBox_nodeB.Enable( False )
		
		fgSizer2.Add( self.m_comboBox_nodeB, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel_node.SetSizer( fgSizer2 )
		self.m_panel_node.Layout()
		fgSizer2.Fit( self.m_panel_node )
		fgSizer17.Add( self.m_panel_node, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		fgSizer16.Add( fgSizer17, 1, wx.EXPAND, 5 )
		
		
		self.m_panel27.SetSizer( fgSizer16 )
		self.m_panel27.Layout()
		fgSizer16.Fit( self.m_panel27 )
		fgSizer18.Add( self.m_panel27, 1, wx.EXPAND |wx.ALL, 0 )
		
		self.m_panel8 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel8.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.m_panel8.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_button3 = wx.Button( self.m_panel8, wx.ID_OK, u"&OK", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_button3.SetDefault() 
		gSizer2.Add( self.m_button3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_button4 = wx.Button( self.m_panel8, wx.ID_CANCEL, u"&Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.m_button4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		self.m_panel8.SetSizer( gSizer2 )
		self.m_panel8.Layout()
		gSizer2.Fit( self.m_panel8 )
		fgSizer18.Add( self.m_panel8, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer18 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.onClose )
		self.m_radioBox_type.Bind( wx.EVT_RADIOBOX, self.onTypeChange )
		self.m_comboBox_nodeA.Bind( wx.EVT_COMBOBOX, self.onNodeAChanged )
		self.m_comboBox_nodeA.Bind( wx.EVT_TEXT_ENTER, self.onNodeAChanged )
		self.m_button3.Bind( wx.EVT_BUTTON, self.OnOK )
		self.m_button4.Bind( wx.EVT_BUTTON, self.onCancel )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onClose( self, event ):
		event.Skip()
	
	def onTypeChange( self, event ):
		event.Skip()
	
	def onNodeAChanged( self, event ):
		event.Skip()
	
	
	def OnOK( self, event ):
		event.Skip()
	
	def onCancel( self, event ):
		event.Skip()
	

###########################################################################
## Class DialogScript
###########################################################################

class DialogScript ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Dot Script", pos = wx.DefaultPosition, size = wx.Size( 600,600 ), style = wx.DEFAULT_DIALOG_STYLE|wx.MAXIMIZE_BOX|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		fgSizer3 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer3.AddGrowableCol( 0 )
		fgSizer3.AddGrowableRow( 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		fgSizer21 = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgSizer21.AddGrowableCol( 1 )
		fgSizer21.AddGrowableRow( 0 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel21 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 3,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel21.SetBackgroundColour( wx.Colour( 21, 120, 180 ) )
		
		fgSizer21.Add( self.m_panel21, 1, wx.EXPAND |wx.ALL, 0 )
		
		self.m_text_script = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_PROCESS_ENTER|wx.TE_PROCESS_TAB|wx.TE_RICH2|wx.SIMPLE_BORDER|wx.WANTS_CHARS )
		self.m_text_script.SetFont( wx.Font( 10, 70, 90, 90, False, "Consolas" ) )
		
		fgSizer21.Add( self.m_text_script, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer3.Add( fgSizer21, 1, wx.EXPAND, 5 )
		
		self.m_panel22 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel22.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_button5 = wx.Button( self.m_panel22, wx.ID_OK, u"&Parse && Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button5.SetDefault() 
		gSizer3.Add( self.m_button5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_button6 = wx.Button( self.m_panel22, wx.ID_CANCEL, u"&Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		self.m_panel22.SetSizer( gSizer3 )
		self.m_panel22.Layout()
		gSizer3.Fit( self.m_panel22 )
		fgSizer3.Add( self.m_panel22, 1, wx.EXPAND |wx.ALL, 0 )
		
		
		self.SetSizer( fgSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_text_script.Bind( wx.EVT_TEXT_ENTER, self.onTextEnter )
		self.m_button5.Bind( wx.EVT_BUTTON, self.onOK )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onTextEnter( self, event ):
		event.Skip()
	
	def onOK( self, event ):
		event.Skip()
	

###########################################################################
## Class DialogAbout
###########################################################################

class DialogAbout ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"About DotEditor", pos = wx.DefaultPosition, size = wx.Size( 285,256 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer4 = wx.FlexGridSizer( 3, 1, 0, 0 )
		fgSizer4.AddGrowableCol( 0 )
		fgSizer4.AddGrowableRow( 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"resource/icon/DE.ico", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_bitmap1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"DotEditor, 2015 Copyright by Vincent.H", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer4.Add( self.m_staticText4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_button7 = wx.Button( self, wx.ID_OK, u"&OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer4.Add( self.m_button7, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		self.SetSizer( fgSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class DialogGraphSetting
###########################################################################

class DialogGraphSetting ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Top Graph Setting", pos = wx.DefaultPosition, size = wx.Size( 384,236 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer13 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer13.AddGrowableCol( 0 )
		fgSizer13.AddGrowableRow( 0 )
		fgSizer13.SetFlexibleDirection( wx.BOTH )
		fgSizer13.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel15 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel15.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )
		
		fgSizer22 = wx.FlexGridSizer( 1, 2, 0, 0 )
		fgSizer22.AddGrowableCol( 1 )
		fgSizer22.AddGrowableRow( 0 )
		fgSizer22.SetFlexibleDirection( wx.BOTH )
		fgSizer22.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel23 = wx.Panel( self.m_panel15, wx.ID_ANY, wx.DefaultPosition, wx.Size( 3,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel23.SetBackgroundColour( wx.Colour( 21, 120, 180 ) )
		
		fgSizer22.Add( self.m_panel23, 1, wx.EXPAND |wx.ALL, 0 )
		
		fgSizer14 = wx.FlexGridSizer( 5, 2, 0, 0 )
		fgSizer14.AddGrowableCol( 1 )
		fgSizer14.AddGrowableRow( 4 )
		fgSizer14.SetFlexibleDirection( wx.BOTH )
		fgSizer14.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText7 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Graph Type:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText7.Wrap( -1 )
		fgSizer14.Add( self.m_staticText7, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		m_radioBox_typeChoices = [ u"digraph", u"graph" ]
		self.m_radioBox_type = wx.RadioBox( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_radioBox_typeChoices, 1, wx.RA_SPECIFY_ROWS|wx.NO_BORDER )
		self.m_radioBox_type.SetSelection( 0 )
		fgSizer14.Add( self.m_radioBox_type, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText8 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Strict:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText8.Wrap( -1 )
		fgSizer14.Add( self.m_staticText8, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL|wx.EXPAND, 5 )
		
		self.m_checkBox_strict = wx.CheckBox( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer14.Add( self.m_checkBox_strict, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText9 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Graph Name/Id:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText9.Wrap( -1 )
		fgSizer14.Add( self.m_staticText9, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_textCtrl_name = wx.TextCtrl( self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer14.Add( self.m_textCtrl_name, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText13 = wx.StaticText( self.m_panel15, wx.ID_ANY, u"Layout CMD:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText13.Wrap( -1 )
		fgSizer14.Add( self.m_staticText13, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		m_choice_layout_cmdChoices = []
		self.m_choice_layout_cmd = wx.Choice( self.m_panel15, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_layout_cmdChoices, 0 )
		self.m_choice_layout_cmd.SetSelection( 0 )
		fgSizer14.Add( self.m_choice_layout_cmd, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		fgSizer14.AddSpacer( ( 0, 5), 1, wx.EXPAND, 5 )
		
		
		fgSizer14.AddSpacer( ( 0, 5), 1, wx.EXPAND, 5 )
		
		
		fgSizer22.Add( fgSizer14, 1, wx.EXPAND, 5 )
		
		
		self.m_panel15.SetSizer( fgSizer22 )
		self.m_panel15.Layout()
		fgSizer22.Fit( self.m_panel15 )
		fgSizer13.Add( self.m_panel15, 1, wx.EXPAND |wx.ALL, 0 )
		
		self.m_panel16 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel16.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_button9 = wx.Button( self.m_panel16, wx.ID_OK, u"&OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button9.SetDefault() 
		gSizer3.Add( self.m_button9, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_button10 = wx.Button( self.m_panel16, wx.ID_CANCEL, u"&Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_button10, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		self.m_panel16.SetSizer( gSizer3 )
		self.m_panel16.Layout()
		gSizer3.Fit( self.m_panel16 )
		fgSizer13.Add( self.m_panel16, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( fgSizer13 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button9.Bind( wx.EVT_BUTTON, self.onOK )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onOK( self, event ):
		event.Skip()
	

###########################################################################
## Class ImageSingleChoiceDialog
###########################################################################

class ImageSingleChoiceDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 313,339 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer21 = wx.FlexGridSizer( 3, 1, 0, 0 )
		fgSizer21.AddGrowableCol( 0 )
		fgSizer21.AddGrowableRow( 1 )
		fgSizer21.SetFlexibleDirection( wx.BOTH )
		fgSizer21.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_message = wx.StaticText( self, wx.ID_ANY, u"Select a item:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_message.Wrap( -1 )
		fgSizer21.Add( self.m_message, 0, wx.ALL, 10 )
		
		self.m_panel24 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer22 = wx.FlexGridSizer( 1, 1, 0, 0 )
		fgSizer22.AddGrowableCol( 0 )
		fgSizer22.AddGrowableRow( 0 )
		fgSizer22.SetFlexibleDirection( wx.BOTH )
		fgSizer22.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_list = wx.ListCtrl( self.m_panel24, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_ICON|wx.LC_SINGLE_SEL )
		fgSizer22.Add( self.m_list, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel24.SetSizer( fgSizer22 )
		self.m_panel24.Layout()
		fgSizer22.Fit( self.m_panel24 )
		fgSizer21.Add( self.m_panel24, 1, wx.ALL|wx.EXPAND, 0 )
		
		self.m_panel25 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_button11 = wx.Button( self.m_panel25, wx.ID_OK, u"&OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button11.SetDefault() 
		gSizer5.Add( self.m_button11, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_button12 = wx.Button( self.m_panel25, wx.ID_CANCEL, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_button12, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		self.m_panel25.SetSizer( gSizer5 )
		self.m_panel25.Layout()
		gSizer5.Fit( self.m_panel25 )
		fgSizer21.Add( self.m_panel25, 1, wx.EXPAND |wx.ALL, 0 )
		
		
		self.SetSizer( fgSizer21 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class ArrowTypeDialog
###########################################################################

class ArrowTypeDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Arrow Type", pos = wx.DefaultPosition, size = wx.Size( 602,354 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer23 = wx.FlexGridSizer( 3, 1, 0, 0 )
		fgSizer23.AddGrowableCol( 0 )
		fgSizer23.AddGrowableRow( 1 )
		fgSizer23.SetFlexibleDirection( wx.BOTH )
		fgSizer23.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText14 = wx.StaticText( self, wx.ID_ANY, u"Select a arrow type:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		fgSizer23.Add( self.m_staticText14, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 10 )
		
		self.m_panel26 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gbSizer3 = wx.GridBagSizer( 0, 0 )
		gbSizer3.SetFlexibleDirection( wx.BOTH )
		gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		m_radioBox_arrowpartChoices = [ u"Both", u"Left", u"Right" ]
		self.m_radioBox_arrowpart = wx.RadioBox( self.m_panel26, wx.ID_ANY, u"Arrow Part", wx.DefaultPosition, wx.DefaultSize, m_radioBox_arrowpartChoices, 1, wx.RA_SPECIFY_COLS )
		self.m_radioBox_arrowpart.SetSelection( 0 )
		gbSizer3.Add( self.m_radioBox_arrowpart, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_checkBox_arrowfilled = wx.CheckBox( self.m_panel26, wx.ID_ANY, u"Filled", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox_arrowfilled.SetValue(True) 
		gbSizer3.Add( self.m_checkBox_arrowfilled, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
		
		self.m_bitmap_preview = wx.StaticBitmap( self.m_panel26, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER )
		gbSizer3.Add( self.m_bitmap_preview, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		gbSizer3.AddSpacer( ( 0, 0 ), wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.EXPAND, 5 )
		
		self.m_list = wx.ListCtrl( self.m_panel26, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_ICON )
		gbSizer3.Add( self.m_list, wx.GBPosition( 0, 1 ), wx.GBSpan( 4, 1 ), wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		
		gbSizer3.AddGrowableCol( 1 )
		gbSizer3.AddGrowableRow( 3 )
		
		self.m_panel26.SetSizer( gbSizer3 )
		self.m_panel26.Layout()
		gbSizer3.Fit( self.m_panel26 )
		fgSizer23.Add( self.m_panel26, 1, wx.ALL|wx.EXPAND, 0 )
		
		self.m_panel27 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_button13 = wx.Button( self.m_panel27, wx.ID_OK, u"&OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button13.SetDefault() 
		gSizer6.Add( self.m_button13, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_button14 = wx.Button( self.m_panel27, wx.ID_CANCEL, u"&Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_button14, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		self.m_panel27.SetSizer( gSizer6 )
		self.m_panel27.Layout()
		gSizer6.Fit( self.m_panel27 )
		fgSizer23.Add( self.m_panel27, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( fgSizer23 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_radioBox_arrowpart.Bind( wx.EVT_RADIOBOX, self.onArrowChanged )
		self.m_checkBox_arrowfilled.Bind( wx.EVT_CHECKBOX, self.onArrowChanged )
		self.m_list.Bind( wx.EVT_LIST_ITEM_SELECTED, self.onATSelected )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onArrowChanged( self, event ):
		event.Skip()
	
	
	def onATSelected( self, event ):
		event.Skip()
	

###########################################################################
## Class ColorSingleChoiceDialog
###########################################################################

class ColorSingleChoiceDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pick a color", pos = wx.DefaultPosition, size = wx.Size( 305,372 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer24 = wx.FlexGridSizer( 5, 1, 0, 0 )
		fgSizer24.AddGrowableCol( 0 )
		fgSizer24.AddGrowableRow( 2 )
		fgSizer24.SetFlexibleDirection( wx.BOTH )
		fgSizer24.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel30 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer25 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer25.AddGrowableCol( 1 )
		fgSizer25.AddGrowableRow( 0 )
		fgSizer25.SetFlexibleDirection( wx.BOTH )
		fgSizer25.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText_message = wx.StaticText( self.m_panel30, wx.ID_ANY, u"Select a color:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText_message.Wrap( -1 )
		fgSizer25.Add( self.m_staticText_message, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		self.m_panel30.SetSizer( fgSizer25 )
		self.m_panel30.Layout()
		fgSizer25.Fit( self.m_panel30 )
		fgSizer24.Add( self.m_panel30, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_searchCtrl = wx.SearchCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_LEFT )
		self.m_searchCtrl.ShowSearchButton( True )
		self.m_searchCtrl.ShowCancelButton( False )
		fgSizer24.Add( self.m_searchCtrl, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_list = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_HRULES|wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		self.m_list.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		fgSizer24.Add( self.m_list, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel29 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer7 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_button15 = wx.Button( self.m_panel29, wx.ID_OK, u"&OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.m_button15, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_button16 = wx.Button( self.m_panel29, wx.ID_CANCEL, u"&Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.m_button16, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		self.m_panel29.SetSizer( gSizer7 )
		self.m_panel29.Layout()
		gSizer7.Fit( self.m_panel29 )
		fgSizer24.Add( self.m_panel29, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( fgSizer24 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_searchCtrl.Bind( wx.EVT_TEXT, self.onSearch )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onSearch( self, event ):
		event.Skip()
	

###########################################################################
## Class ColorSchemeDialog
###########################################################################

class ColorSchemeDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pick a color scheme", pos = wx.DefaultPosition, size = wx.Size( 305,372 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer24 = wx.FlexGridSizer( 5, 1, 0, 0 )
		fgSizer24.AddGrowableCol( 0 )
		fgSizer24.AddGrowableRow( 1 )
		fgSizer24.SetFlexibleDirection( wx.BOTH )
		fgSizer24.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_searchCtrl = wx.SearchCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_LEFT )
		self.m_searchCtrl.ShowSearchButton( True )
		self.m_searchCtrl.ShowCancelButton( False )
		fgSizer24.Add( self.m_searchCtrl, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_list = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_ICON|wx.LC_SINGLE_SEL )
		self.m_list.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer24.Add( self.m_list, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel29 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer7 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_button15 = wx.Button( self.m_panel29, wx.ID_OK, u"&OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.m_button15, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_button16 = wx.Button( self.m_panel29, wx.ID_CANCEL, u"&Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.m_button16, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		self.m_panel29.SetSizer( gSizer7 )
		self.m_panel29.Layout()
		gSizer7.Fit( self.m_panel29 )
		fgSizer24.Add( self.m_panel29, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( fgSizer24 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_searchCtrl.Bind( wx.EVT_TEXT, self.onSearch )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onSearch( self, event ):
		event.Skip()
	

