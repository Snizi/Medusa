from textwrap import wrap
from src.input import parseArgs
from src.wrappers import Wrappers
from datetime import datetime
from src.constants import RECON_FOLDER
from src.helpers import mkdir





if __name__ == "__main__":
    

    company_name, domains = parseArgs()

    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y-%H:%M") 

    for root in domains:
        recon_folder = RECON_FOLDER + company_name + dt_string + "/" + root + "/"
        recon_folder = mkdir(recon_folder)
        
        wrappers = Wrappers(recon_folder, root)
        
        wrappers.assetfinder()
        wrappers.sublister()
        wrappers.amass()
        wrappers.unify_domains()
        wrappers.waybackurls()
        wrappers.httprobe()
        wrappers.aquatone()