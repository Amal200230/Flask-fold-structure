models = mainly databases items related to  SQLALCHEMY

routes = the http end points (get,post,put ,delete)

services = logics or the logics for the routes

bluprint = import it mainly for routing process (http methods)

.env = for sensitive data (passwords ......)

**************************************************************************

MAIN PROJECT                                -------  MAIN [FOLDER ]

     APP   
      blueprint                                    . ----- MAIN PROGRAMMING {FOLDER}
       INIT.PY                                    .    -----CONNECTS FLASK AND DB       
                                                  .
      /MODELS/                                    .               ----- FILE WITH ALL DATABASE MODELS{FOLDER}
        USER.PY                                   .
      /ROUTES/                                    .               -------- MAIN HTTP {FOLDER}
        USER.ROUTES.PY                            .
      /SERVICES/                                  .               ----------  PROG LOGIC    {FOLDER}      
         USER.SERVICES.PY                         .
       CONGIG.PY                                  .  ---------- APP CONFIG


.ENV                                        -------- SECRETS, DB STRING
RUN.PY                                      ------- RUNNING FULL APP
DEPENDENCIES.TXT                            ------- LIBRARIES
README.ME(OPTIONAL)

********************************************************************************

congig.py = contains both the development part and production part 
in the end when the project is ready to deploy we decide wether to add dev or prod in the __init__.py or run.py

.env = load_dotenv 

import os for interavting with operating system
