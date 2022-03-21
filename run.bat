@echo off

Set /a num=(%Random% %%9)+1

color %num%

echo Start converting ...
echo.
echo      .-.
echo     /   \         .-.
echo    /     \       /   \       .-.     .-.     _   _
echo --/-------\-----/-----\-----/---\---/---\---/-\-/-\/\/---
echo  /         \   /       \   /     '-'     '-'
echo /           '-'         '-'
echo.

py convert.py

echo.
echo Done ! Have fun
echo.

pause