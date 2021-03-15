import tableauserverclient as T
from tableauserverclient import server
from tableauserverclient.models import tableau_auth
import requests

Server=T.Server("https://10ax.online.tableau.com")
Server.use_server_version()

#passing site ID for custom made site
site = '620caa8b-ab01-455e-901b-9164dee04c5b'
#Authorization credentials are passing here
tableau_auth=T.TableauAuth("gunakala.amarnadh@outlook.com","XXXX",site)

with Server.auth.sign_in(tableau_auth):
    new_Workbook=T.WorkbookItem(name="test",project_id='')
    publish_mode=T.Server.PublishMode.CreateNew
   
    overwrite_true = T.Server.PublishMode.Overwrite
    #Publishing into my tableau
    my_Workbook=server.Workbooks.publish(new_Workbook,overwrite_true,"./Test.twbx" , publish_mode)

    print("Workbook published. JOB ID: {0}".format(my_Workbook.id))

    

