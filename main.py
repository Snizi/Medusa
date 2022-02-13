from textwrap import wrap
from src.input import parseArgs
from src.wrappers import Wrappers
from datetime import datetime
from src.constants import RECON_FOLDER
from src.helpers import mkdir





if __name__ == "__main__":
    

    domains = parseArgs()


    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y-%H:%M") 
    

    


    
    for root in domains:
        recon_folder = mkdir(RECON_FOLDER + dt_string + "/" + root + "/")
        
        wrappers = Wrappers(recon_folder, root)
        
        wrappers.assetfinder()
        wrappers.amass()
        wrappers.sublister()

        wrappers.unify_domains()