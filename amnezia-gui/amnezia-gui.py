#!/usr/bin/env python3
import gi
import subprocess
import threading
from gi.repository import Gtk, Gdk

gi.require_version("Gtk", "3.0")

class VPNApp(Gtk.Window):
    def __init__(self):
        super().__init__(title="VPN Control")
        self.set_border_width(10)
        self.set_default_size(300, 200)

        # Create a vertical container
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)

        # Title
        title_label = Gtk.Label(label="VPN Control")
        title_label.set_justify(Gtk.Justification.CENTER)
        title_label.set_margin_bottom(10)
        vbox.pack_start(title_label, True, True, 0)

        # Status indicator
        self.status_label = Gtk.Label(label="VPN is disabled")
        self.status_label.set_justify(Gtk.Justification.CENTER)
        self.status_label.set_margin_bottom(10)
        vbox.pack_start(self.status_label, True, True, 0)

        # Password entry
        self.password_entry = Gtk.Entry()
        self.password_entry.set_visibility(False)  # Hide password
        self.password_entry.set_placeholder_text("Enter VPN password")
        vbox.pack_start(self.password_entry, True, True, 0)

        # Button to enable VPN
        self.enable_button = Gtk.Button(label="Enable VPN")
        self.enable_button.connect("clicked", self.on_enable_vpn)
        vbox.pack_start(self.enable_button, True, True, 0)

        # Button to disable VPN
        self.disable_button = Gtk.Button(label="Disable VPN")
        self.disable_button.connect("clicked", self.on_disable_vpn)
        vbox.pack_start(self.disable_button, True, True, 0)

        # Set button styles
        self.enable_button.set_name("enable-button")
        self.disable_button.set_name("disable-button")

        # Set CSS for styles
        self.apply_css()

    def apply_css(self):
        css = """
        button {
            padding: 10px;
            font-size: 16px;
            border-radius: 5px;
        }
        #enable-button {
            background-color: #4CAF50; /* Green */
            color: white;
        }
        #disable-button {
            background-color: #f44336; /* Red */
            color: white;
        }
        """
        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(css.encode('utf-8'))  # Encode string to bytes
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_USER
        )

    def on_enable_vpn(self, widget):
        password = self.password_entry.get_text()
        self.run_vpn_command(["sudo", "-S", "awg-quick", "up", "/home/askodon/amnezia/awg.conf"], password)

    def on_disable_vpn(self, widget):
        self.run_vpn_command(["sudo", "-S", "awg-quick", "down", "/home/askodon/amnezia/awg.conf"])

    def run_vpn_command(self, command, password=None):
        def target():
            process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if password:
                # Send password to the process if needed
                output, error = process.communicate(input=password + "\n")
            else:
                output, error = process.communicate()

            # Update the status label based on the output
            if process.returncode == 0:
                self.status_label.set_text("VPN command executed successfully")
            else:
                self.status_label.set_text(f"Error: {error.strip()}")

        # Run the command in a separate thread to avoid blocking the UI
        threading.Thread(target=target).start()

if __name__ == "__main__":
    app = VPNApp()
    app.connect("destroy", Gtk.main_quit)
    app.show_all()
    Gtk.main()

