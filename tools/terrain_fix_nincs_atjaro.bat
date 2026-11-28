@echo off
chcp 65001 >nul
cd /d "%~dp0.."
where py >nul 2>nul && (py -3 tools\terrain_fix.py cappadocia crete oahu kilimanjaro okavango sossusvlei atacama bhutan serengeti-mara iceland-south lake-geneva santiago-andes cabo jomsom-mustang san-diego salta-humahuaca yerevan-ararat samarkand red-sea-sinai almaty arequipa-colca mcmurdo persepolis darjeeling-sikkim trabzon-kackar stol-icy-strait stol-jumla) || (python tools\terrain_fix.py cappadocia crete oahu kilimanjaro okavango sossusvlei atacama bhutan serengeti-mara iceland-south lake-geneva santiago-andes cabo jomsom-mustang san-diego salta-humahuaca yerevan-ararat samarkand red-sea-sinai almaty arequipa-colca mcmurdo persepolis darjeeling-sikkim trabzon-kackar stol-icy-strait stol-jumla)
