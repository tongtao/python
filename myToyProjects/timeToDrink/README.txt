
README

(1)程序文件列表
	
timer---(主程序))
	|	settimerdlg.pyw:具备基本界面,功能
	|	minitimer.pyw:增加最小化托盘功能
	|	
	|---(程序图标文件, pyrcc4 -0)
	|	qrc_systray.py
	|	systray.qrc
	|	images
	|	
	|---(pyuic4 -0 命令生成)
	|	ui_SetTimer.py
	|	ui_messageDlg.py
	|	
	|---(QtDesigner生成的界面文件)
	|	messageDlg.ui:消息界面
	|	SetTimer.ui:时间设置界面
	|	
	|---(用于pythonw下执行时收集错误信息)
	|	errlog.txt
	|	
	|---demo:参考程序
	
	
(2)主程序用到的类
	QTimer
	QComboBox
	QIcon
	QAction
	QMenu
	QSystemTrayIcon
		
		