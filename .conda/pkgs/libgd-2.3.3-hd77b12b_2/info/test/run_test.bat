



if not exist %PREFIX%\\Library\\bin\\libgd.dll exit 1
IF %ERRORLEVEL% NEQ 0 exit /B 1
if not exist %PREFIX%\\Library\\lib\\libgd.lib exit 1
IF %ERRORLEVEL% NEQ 0 exit /B 1
exit /B 0
