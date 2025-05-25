[app]
title = MovieInfo
package.name = movieinfo
package.domain = org.gity678
source.dir = .
source.include_exts = py,kv,html
version = 1.0
requirements = python3,kivy,flask,requests
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 30
android.minapi = 21
android.archs = arm64-v8a
android.entrypoint = org.kivy.android.PythonActivity
entrypoint = main.py
include_exts = py,kv,png,jpg,html
android.orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 0
