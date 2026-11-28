@echo off
chcp 65001 >nul
cd /d "%~dp0.."
where py >nul 2>nul && (py -3 tools\terrain_snap.py bagan/mid machu-picchu/full) || (python tools\terrain_snap.py bagan/mid machu-picchu/full)
