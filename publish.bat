REM .\publish "some comment" # when called inside PS
call publish_private.bat %1
call publish_public.bat
ECHO Done