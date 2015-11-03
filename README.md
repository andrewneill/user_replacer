# user_replacer
ABB RobotWare 6 fix to replace the username in system folder

The RobotStudio 6 and RobotWare 6 changed the installation directory of
RobotWare by the Microsoft “certification requirements for Windows desktop apps.”
They are now installing RobotWare in your Users\<username>\AppData folder. This is
not a generic path though, so when you build a system with RobotWare 6, the links are
directed to YOUR app data. Then, if someone else tries to start your controller it will
throw errors and won’t start. The work around until they (hopefully) fix it is to replace the
username. This script will quickly do just that:

Just run the script and it will prompt you for the system. Find the system you want to fix, 
it will pull out the old username and confirm with you, then you can let it run with your 
username or tell it which username you want it to find and replace. It will search through 
only the .xml files and .id files and replace all instances, then report its findings.

I highly recommend that you make a copy of the system and save it in an
“archive” folder before running this. Just in case something goes horribly wrong. Also,
sometimes this is not necessary. If the controller was built on your computer I have
found that RobotStudio can still find it through the other user’s account. So try the
controller first.
