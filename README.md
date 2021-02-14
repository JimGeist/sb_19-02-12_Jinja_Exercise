# sb_19-02-12_Jinja_Exercise

## Flask MadLibs  

## Assignment Details
#### ASSIGNMENT INVOLVED ####
- Familiarization with Jinja, creation of html templates, passing values to templates, looping in templates, and template inheritance.


### MadLib ###
Application app.py imports stories.py -- stories.py is the MadLib story engine. A sample story was provided in stories.py and a flask application was created to serve up a page which asks for various words for the story. The various prompt words are dynamic and change based on the story. 

When submit is pressed, the prompted words are passed to a story page which presents the story with the prompted words inserted in the correct places in the story. 

Jinja page templates were created for the welcome (prompt words) page and story page. The templates were extended by adding a base template which is extended by the welcome and story pages. 


**ENHANCEMENTS**
The following Enhancements / Further Study endeavours were implemented:
- **Template Inheritance** - templates with inheritance were implemented from the start of the project.
- **Add CSS** - CSS had to get added. The pages look pretty bleak without it. 
- **Safe HTML Filtering** - prompted words are in bold face. Adding **|safe**, {{my_story|safe}} let the html tags inserted in my_story by the Python code remain as html tags. The strong tags were further enhanced by using the color purple as well.


**ISSUES**: 
Yes, I lost cycles with CSS because the styling was never appearing on the welcome page as a result of page caching in FireFox. I am not the best with CSS styling so the immediate thought was I must be doing something wrong combined with finding ways to get around the page caching that I was warned about. A new incognito session / private browsing session did the trick - just wish I thought of it sooner!  


**TIMING**:
An accurate accounting does not exist for this one. At least 3 hours minimum though. As I said, too much time was lost trying to figure out why CSS code was not applying to the welcome page.
