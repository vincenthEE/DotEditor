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
		fgSizer15 = wx.FlexGridSizer( 1, 10, 0, 0 )
		fgSizer15.AddGrowableCol( 8 )
		fgSizer15.SetFlexibleDirection( wx.BOTH )
		fgSizer15.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel17 = wx.Panel( self.m_panel16, wx.ID_ANY, wx.DefaultPosition, wx.Size( 3,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel17.SetBackgroundColour( wx.Colour( 21, 120, 180 ) )
		
		fgSizer15.Add( self.m_panel17, 1, wx.EXPAND |wx.ALL, 0 )
		
		
		fgSizer15.AddSpacer( ( 8, 30), 1, wx.EXPAND, 5 )
		
		self.m_bpButton_new = wx.BitmapButton( self.m_panel16, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 50,-1 ), wx.BU_AUTODRAW|wx.NO_BORDER )
		
		self.m_bpButton_new.SetBitmapFocus( wx.NullBitmap )
		self.m_bpButton_new.SetBitmapHover( wx.NullBitmap )
		self.m_bpButton_new.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.m_bpButton_new.SetToolTipString( u"Create a new Graph" )
		
		fgSizer15.Add( self.m_bpButton_new, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.m_bpButton_open = wx.BitmapButton( self.m_panel16, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 50,-1 ), wx.BU_AUTODRAW|wx.NO_BORDER )
		
		self.m_bpButton_open.SetBitmapFocus( wx.NullBitmap )
		self.m_bpButton_open.SetBitmapHover( wx.NullBitmap )
		self.m_bpButton_open.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.m_bpButton_open.SetToolTipString( u"Open a existed Graph file" )
		
		fgSizer15.Add( self.m_bpButton_open, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_bpButton_save = wx.BitmapButton( self.m_panel16, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 50,-1 ), wx.BU_AUTODRAW|wx.NO_BORDER )
		
		self.m_bpButton_save.SetBitmapFocus( wx.NullBitmap )
		self.m_bpButton_save.SetBitmapHover( wx.NullBitmap )
		self.m_bpButton_save.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.m_bpButton_save.SetToolTipString( u"Save graph to file" )
		
		fgSizer15.Add( self.m_bpButton_save, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_bpButton_script = wx.BitmapButton( self.m_panel16, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 50,-1 ), wx.BU_AUTODRAW|wx.NO_BORDER )
		
		self.m_bpButton_script.SetBitmapFocus( wx.NullBitmap )
		self.m_bpButton_script.SetBitmapHover( wx.NullBitmap )
		self.m_bpButton_script.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.m_bpButton_script.SetToolTipString( u"View dot script" )
		
		fgSizer15.Add( self.m_bpButton_script, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_bpButton_export = wx.BitmapButton( self.m_panel16, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 50,-1 ), wx.BU_AUTODRAW|wx.NO_BORDER )
		
		self.m_bpButton_export.SetBitmapFocus( wx.NullBitmap )
		self.m_bpButton_export.SetBitmapHover( wx.NullBitmap )
		self.m_bpButton_export.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		self.m_bpButton_export.SetToolTipString( u"Save graph to image file" )
		
		fgSizer15.Add( self.m_bpButton_export, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_button_save_as = wx.Button( self.m_panel16, wx.ID_ANY, u"Save As", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_save_as.Hide()
		
		fgSizer15.Add( self.m_button_save_as, 0, wx.ALL, 5 )
		
		
		fgSizer15.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_bpButton_help = wx.BitmapButton( self.m_panel16, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 50,-1 ), wx.BU_AUTODRAW|wx.NO_BORDER )
		self.m_bpButton_help.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer15.Add( self.m_bpButton_help, 0, wx.ALL, 5 )
		
		
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
		
		fgSizer11 = wx.FlexGridSizer( 1, 5, 0, 0 )
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
		
		self.m_staticText_zoom = wx.StaticText( self.m_panel12, wx.ID_ANY, u"Zoom:100%", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText_zoom.Wrap( -1 )
		fgSizer11.Add( self.m_staticText_zoom, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_button16 = wx.Button( self.m_panel12, wx.ID_ANY, u"1:1", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT|wx.NO_BORDER )
		self.m_button16.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.m_button16.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.m_button16.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer11.Add( self.m_button16, 0, wx.ALIGN_CENTER|wx.FIXED_MINSIZE, 5 )
		
		
		fgSizer11.AddSpacer( ( 3, 0), 1, wx.EXPAND, 5 )
		
		
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
		self.m_bpButton_help.Bind( wx.EVT_BUTTON, self.onHelp )
		self.m_bpButton_graphsetting.Bind( wx.EVT_BUTTON, self.onGraphSetting )
		self.m_bpButton_add.Bind( wx.EVT_BUTTON, self.onAppendItem )
		self.m_bpButton_minus.Bind( wx.EVT_BUTTON, self.onDeleteItem )
		self.m_tree.Bind( wx.EVT_TREE_SEL_CHANGED, self.onItemSelected )
		self.m_pgManager1.Bind( pg.EVT_PG_CHANGED, self.onPGChanged )
		self.m_button16.Bind( wx.EVT_BUTTON, self.onZoom100 )
		self.m_panel_paint.Bind( wx.EVT_SIZE, self.onWindowSizeChanged )
	
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
	
	def onHelp( self, event ):
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
	
	def onZoom100( self, event ):
		event.Skip()
	
	def onWindowSizeChanged( self, event ):
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
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Append Item", pos = wx.DefaultPosition, size = wx.Size( 416,366 ), style = wx.DEFAULT_DIALOG_STYLE )
		
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
		
		fgSizer2 = wx.FlexGridSizer( 3, 2, 0, 0 )
		fgSizer2.AddGrowableCol( 1 )
		fgSizer2.AddGrowableRow( 2 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText1 = wx.StaticText( self.m_panel_node, wx.ID_ANY, u"Node/NodeA:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		fgSizer2.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		m_comboBox_nodeAChoices = []
		self.m_comboBox_nodeA = wx.ComboBox( self.m_panel_node, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox_nodeAChoices, 0 )
		fgSizer2.Add( self.m_comboBox_nodeA, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText2 = wx.StaticText( self.m_panel_node, wx.ID_ANY, u"Node B:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer2.Add( self.m_staticText2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )
		
		m_comboBox_nodeBChoices = []
		self.m_comboBox_nodeB = wx.ComboBox( self.m_panel_node, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, m_comboBox_nodeBChoices, 0 )
		self.m_comboBox_nodeB.Enable( False )
		
		fgSizer2.Add( self.m_comboBox_nodeB, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText16 = wx.StaticText( self.m_panel_node, wx.ID_ANY, u"Lable:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText16.Wrap( -1 )
		fgSizer2.Add( self.m_staticText16, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		self.m_textCtrl_label = wx.TextCtrl( self.m_panel_node, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE|wx.TE_WORDWRAP )
		self.m_textCtrl_label.SetBackgroundColour( wx.Colour( 255, 255, 192 ) )
		self.m_textCtrl_label.SetToolTipString( u"Label of node/edge/subgraph.\nJust leave empty if no label to set." )
		
		fgSizer2.Add( self.m_textCtrl_label, 0, wx.ALL|wx.EXPAND, 5 )
		
		
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
		
		self.m_panel30 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
		fgSizer29 = wx.FlexGridSizer( 1, 1, 0, 0 )
		fgSizer29.AddGrowableCol( 0 )
		fgSizer29.AddGrowableRow( 0 )
		fgSizer29.SetFlexibleDirection( wx.BOTH )
		fgSizer29.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_text_script = wx.TextCtrl( self.m_panel30, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_DONTWRAP|wx.TE_MULTILINE|wx.TE_PROCESS_ENTER|wx.TE_PROCESS_TAB|wx.TE_RICH|wx.NO_BORDER )
		fgSizer29.Add( self.m_text_script, 0, wx.ALL|wx.EXPAND, 0 )
		
		
		self.m_panel30.SetSizer( fgSizer29 )
		self.m_panel30.Layout()
		fgSizer29.Fit( self.m_panel30 )
		fgSizer21.Add( self.m_panel30, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		fgSizer3.Add( fgSizer21, 1, wx.EXPAND, 5 )
		
		self.m_panel22 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel22.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer36 = wx.FlexGridSizer( 1, 4, 0, 0 )
		fgSizer36.AddGrowableCol( 2 )
		fgSizer36.AddGrowableRow( 0 )
		fgSizer36.SetFlexibleDirection( wx.BOTH )
		fgSizer36.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_button20 = wx.Button( self.m_panel22, wx.ID_ANY, u"Chec&k", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
		self.m_button20.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.m_button20.SetForegroundColour( wx.Colour( 51, 160, 44 ) )
		
		fgSizer36.Add( self.m_button20, 0, wx.ALL, 5 )
		
		self.m_panel33 = wx.Panel( self.m_panel22, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER )
		fgSizer36.Add( self.m_panel33, 1, wx.ALL|wx.EXPAND, 5 )
		
		gSizer13 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_button5 = wx.Button( self.m_panel22, wx.ID_OK, u"&Parse && Update", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button5.SetDefault() 
		gSizer13.Add( self.m_button5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_button6 = wx.Button( self.m_panel22, wx.ID_CANCEL, u"&Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer13.Add( self.m_button6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		fgSizer36.Add( gSizer13, 1, wx.EXPAND, 5 )
		
		
		self.m_panel22.SetSizer( fgSizer36 )
		self.m_panel22.Layout()
		fgSizer36.Fit( self.m_panel22 )
		fgSizer3.Add( self.m_panel22, 1, wx.EXPAND |wx.ALL, 0 )
		
		
		self.SetSizer( fgSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_text_script.Bind( wx.EVT_TEXT, self.onText )
		self.m_text_script.Bind( wx.EVT_TEXT_ENTER, self.onTextEnter )
		self.m_button20.Bind( wx.EVT_BUTTON, self.onCheck )
		self.m_button5.Bind( wx.EVT_BUTTON, self.onOK )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onText( self, event ):
		event.Skip()
	
	def onTextEnter( self, event ):
		event.Skip()
	
	def onCheck( self, event ):
		event.Skip()
	
	def onOK( self, event ):
		event.Skip()
	

###########################################################################
## Class DialogAbout
###########################################################################

class DialogAbout ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"About DotEditor", pos = wx.DefaultPosition, size = wx.Size( 405,388 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer4 = wx.FlexGridSizer( 3, 1, 0, 0 )
		fgSizer4.AddGrowableCol( 0 )
		fgSizer4.AddGrowableRow( 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_FIXEDWIDTH )
		self.m_panel28 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer27 = wx.FlexGridSizer( 3, 1, 0, 0 )
		fgSizer27.AddGrowableCol( 0 )
		fgSizer27.AddGrowableRow( 0 )
		fgSizer27.SetFlexibleDirection( wx.BOTH )
		fgSizer27.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_bitmap1 = wx.StaticBitmap( self.m_panel28, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 128,128 ), 0 )
		fgSizer27.Add( self.m_bitmap1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self.m_panel28, wx.ID_ANY, u"Copyright by Vincent.H 2015", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		self.m_staticText4.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		self.m_staticText4.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer27.Add( self.m_staticText4, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.m_hyperlink1 = wx.HyperlinkCtrl( self.m_panel28, wx.ID_ANY, u"DotEditor Website", u"http://vincenthee.github.io/DotEditor/", wx.DefaultPosition, wx.DefaultSize, wx.HL_ALIGN_CENTRE|wx.HL_DEFAULT_STYLE )
		self.m_hyperlink1.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		
		fgSizer27.Add( self.m_hyperlink1, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel28.SetSizer( fgSizer27 )
		self.m_panel28.Layout()
		fgSizer27.Fit( self.m_panel28 )
		self.m_notebook1.AddPage( self.m_panel28, u"&About", True )
		self.m_panel29 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer28 = wx.FlexGridSizer( 1, 1, 0, 0 )
		fgSizer28.AddGrowableCol( 0 )
		fgSizer28.AddGrowableRow( 0 )
		fgSizer28.SetFlexibleDirection( wx.BOTH )
		fgSizer28.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_textCtrl3 = wx.TextCtrl( self.m_panel29, wx.ID_ANY, u"Apache License\n\nVersion 2.0, January 2004\n\nhttp://www.apache.org/licenses/\n\nTERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION\n\n1. Definitions.\n\n\"License\" shall mean the terms and conditions for use, reproduction, and distribution as defined by Sections 1 through 9 of this document.\n\n\"Licensor\" shall mean the copyright owner or entity authorized by the copyright owner that is granting the License.\n\n\"Legal Entity\" shall mean the union of the acting entity and all other entities that control, are controlled by, or are under common control with that entity. For the purposes of this definition, \"control\" means (i) the power, direct or indirect, to cause the direction or management of such entity, whether by contract or otherwise, or (ii) ownership of fifty percent (50%) or more of the outstanding shares, or (iii) beneficial ownership of such entity.\n\n\"You\" (or \"Your\") shall mean an individual or Legal Entity exercising permissions granted by this License.\n\n\"Source\" form shall mean the preferred form for making modifications, including but not limited to software source code, documentation source, and configuration files.\n\n\"Object\" form shall mean any form resulting from mechanical transformation or translation of a Source form, including but not limited to compiled object code, generated documentation, and conversions to other media types.\n\n\"Work\" shall mean the work of authorship, whether in Source or Object form, made available under the License, as indicated by a copyright notice that is included in or attached to the work (an example is provided in the Appendix below).\n\n\"Derivative Works\" shall mean any work, whether in Source or Object form, that is based on (or derived from) the Work and for which the editorial revisions, annotations, elaborations, or other modifications represent, as a whole, an original work of authorship. For the purposes of this License, Derivative Works shall not include works that remain separable from, or merely link (or bind by name) to the interfaces of, the Work and Derivative Works thereof.\n\n\"Contribution\" shall mean any work of authorship, including the original version of the Work and any modifications or additions to that Work or Derivative Works thereof, that is intentionally submitted to Licensor for inclusion in the Work by the copyright owner or by an individual or Legal Entity authorized to submit on behalf of the copyright owner. For the purposes of this definition, \"submitted\" means any form of electronic, verbal, or written communication sent to the Licensor or its representatives, including but not limited to communication on electronic mailing lists, source code control systems, and issue tracking systems that are managed by, or on behalf of, the Licensor for the purpose of discussing and improving the Work, but excluding communication that is conspicuously marked or otherwise designated in writing by the copyright owner as \"Not a Contribution.\"\n\n\"Contributor\" shall mean Licensor and any individual or Legal Entity on behalf of whom a Contribution has been received by Licensor and subsequently incorporated within the Work.\n\n2. Grant of Copyright License. Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license to reproduce, prepare Derivative Works of, publicly display, publicly perform, sublicense, and distribute the Work and such Derivative Works in Source or Object form.\n\n3. Grant of Patent License. Subject to the terms and conditions of this License, each Contributor hereby grants to You a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable (except as stated in this section) patent license to make, have made, use, offer to sell, sell, import, and otherwise transfer the Work, where such license applies only to those patent claims licensable by such Contributor that are necessarily infringed by their Contribution(s) alone or by combination of their Contribution(s) with the Work to which such Contribution(s) was submitted. If You institute patent litigation against any entity (including a cross-claim or counterclaim in a lawsuit) alleging that the Work or a Contribution incorporated within the Work constitutes direct or contributory patent infringement, then any patent licenses granted to You under this License for that Work shall terminate as of the date such litigation is filed.\n\n4. Redistribution. You may reproduce and distribute copies of the Work or Derivative Works thereof in any medium, with or without modifications, and in Source or Object form, provided that You meet the following conditions:\n\nYou must give any other recipients of the Work or Derivative Works a copy of this License; and\nYou must cause any modified files to carry prominent notices stating that You changed the files; and\nYou must retain, in the Source form of any Derivative Works that You distribute, all copyright, patent, trademark, and attribution notices from the Source form of the Work, excluding those notices that do not pertain to any part of the Derivative Works; and\nIf the Work includes a \"NOTICE\" text file as part of its distribution, then any Derivative Works that You distribute must include a readable copy of the attribution notices contained within such NOTICE file, excluding those notices that do not pertain to any part of the Derivative Works, in at least one of the following places: within a NOTICE text file distributed as part of the Derivative Works; within the Source form or documentation, if provided along with the Derivative Works; or, within a display generated by the Derivative Works, if and wherever such third-party notices normally appear. The contents of the NOTICE file are for informational purposes only and do not modify the License. You may add Your own attribution notices within Derivative Works that You distribute, alongside or as an addendum to the NOTICE text from the Work, provided that such additional attribution notices cannot be construed as modifying the License. \n\nYou may add Your own copyright statement to Your modifications and may provide additional or different license terms and conditions for use, reproduction, or distribution of Your modifications, or for any such Derivative Works as a whole, provided Your use, reproduction, and distribution of the Work otherwise complies with the conditions stated in this License.\n5. Submission of Contributions. Unless You explicitly state otherwise, any Contribution intentionally submitted for inclusion in the Work by You to the Licensor shall be under the terms and conditions of this License, without any additional terms or conditions. Notwithstanding the above, nothing herein shall supersede or modify the terms of any separate license agreement you may have executed with Licensor regarding such Contributions.\n\n6. Trademarks. This License does not grant permission to use the trade names, trademarks, service marks, or product names of the Licensor, except as required for reasonable and customary use in describing the origin of the Work and reproducing the content of the NOTICE file.\n\n7. Disclaimer of Warranty. Unless required by applicable law or agreed to in writing, Licensor provides the Work (and each Contributor provides its Contributions) on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE. You are solely responsible for determining the appropriateness of using or redistributing the Work and assume any risks associated with Your exercise of permissions under this License.\n\n8. Limitation of Liability. In no event and under no legal theory, whether in tort (including negligence), contract, or otherwise, unless required by applicable law (such as deliberate and grossly negligent acts) or agreed to in writing, shall any Contributor be liable to You for damages, including any direct, indirect, special, incidental, or consequential damages of any character arising as a result of this License or out of the use or inability to use the Work (including but not limited to damages for loss of goodwill, work stoppage, computer failure or malfunction, or any and all other commercial damages or losses), even if such Contributor has been advised of the possibility of such damages.\n\n9. Accepting Warranty or Additional Liability. While redistributing the Work or Derivative Works thereof, You may choose to offer, and charge a fee for, acceptance of support, warranty, indemnity, or other liability obligations and/or rights consistent with this License. However, in accepting such obligations, You may act only on Your own behalf and on Your sole responsibility, not on behalf of any other Contributor, and only if You agree to indemnify, defend, and hold each Contributor harmless for any liability incurred by, or claims asserted against, such Contributor by reason of your accepting any such warranty or additional liability.\n\nEND OF TERMS AND CONDITIONS", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.SIMPLE_BORDER )
		self.m_textCtrl3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )
		
		fgSizer28.Add( self.m_textCtrl3, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel29.SetSizer( fgSizer28 )
		self.m_panel29.Layout()
		fgSizer28.Fit( self.m_panel29 )
		self.m_notebook1.AddPage( self.m_panel29, u"Licenses", False )
		
		fgSizer4.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
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
	

###########################################################################
## Class DialogHelp
###########################################################################

class DialogHelp ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 773,693 ), style = wx.DEFAULT_DIALOG_STYLE|wx.MAXIMIZE_BOX|wx.RESIZE_BORDER )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer29 = wx.FlexGridSizer( 1, 1, 0, 0 )
		fgSizer29.AddGrowableCol( 0 )
		fgSizer29.AddGrowableRow( 0 )
		fgSizer29.SetFlexibleDirection( wx.BOTH )
		fgSizer29.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel_paint = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.SIMPLE_BORDER|wx.VSCROLL )
		self.m_panel_paint.SetScrollRate( 5, 5 )
		self.m_panel_paint.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		fgSizer29.Add( self.m_panel_paint, 1, wx.EXPAND |wx.ALL, 8 )
		
		
		self.SetSizer( fgSizer29 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class DialogTextEditor
###########################################################################

class DialogTextEditor ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 408,324 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer24 = wx.FlexGridSizer( 2, 1, 0, 0 )
		fgSizer24.AddGrowableCol( 0 )
		fgSizer24.AddGrowableRow( 0 )
		fgSizer24.SetFlexibleDirection( wx.BOTH )
		fgSizer24.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_WORDWRAP )
		fgSizer24.Add( self.m_text, 0, wx.ALL|wx.EXPAND, 5 )
		
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
	
	def __del__( self ):
		pass
	

