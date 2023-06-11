#!/usr/bin/osascript

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Open Screen Recorder
# @raycast.mode silent

# Optional parameters:
# @raycast.icon R

# Documentation:
# @raycast.author Zentaro 

tell application "QuickTime Player"
	if it is running then
		quit
	end if
	delay 1 -- Wait for the application to fully close.
	activate -- Open QuickTime Player.
end tell

delay 1 -- Wait for the application to fully open.

tell application "System Events"
	tell process "QuickTime Player"
		click menu item "New Screen Recording" of menu "File" of menu bar 1
	end tell
end tell
