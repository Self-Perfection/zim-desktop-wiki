
# Copyright 2026 Self-Perfection <alexander.s.m@gmail.com>


import tests

from zim.plugins.trayicon import StatusIconTrayIcon


class TestStatusIconTrayIcon(tests.TestCase):

	def runTest(self):
		# "do_popup_menu" is the default handler for the "popup-menu"
		# signal of Gtk.StatusIcon - if it is connected to the signal as
		# well, the menu shows up twice for a single click
		class MyStatusIconTrayIcon(StatusIconTrayIcon):

			def __init__(self):
				self.menus = []
				StatusIconTrayIcon.__init__(self)

			def do_popup_menu(self, button=3, activate_time=0):
				# Build the menu, but don't show it during tests
				self.menus.append(self.get_trayicon_menu())

		icon = MyStatusIconTrayIcon()
		icon.emit('popup-menu', 3, 0)
		self.assertEqual(len(icon.menus), 1)
		icon.destroy()
