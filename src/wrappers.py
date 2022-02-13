import subprocess
from .helpers import remove_empty_strings
from .constants import RECON_FOLDER, SUBLISTER, DNS_JHADDIX



class Wrappers:

    def __init__(self, folder, domain) -> None:
        self.root = domain
        self.folder = folder
        self.assetfinder_file = self.folder + "assetfinder.txt"
        self.sublister_file = self.folder + "sublister.txt"
        self.amass_file = self.folder + "amass.txt"
        self.merged_domains = self.folder + "merged-domains.txt"


    def assetfinder(self):
        subprocess.run(f"assetfinder --subs-only {self.root} > {self.assetfinder_file}", shell=True)

    
    def sublister(self):
        subprocess.run(f"python3 {SUBLISTER} -d {self.root} -t 50 -v -o {self.sublister_file} > /dev/null", shell=True)
        

    def amass(self):
        subprocess.run(f"amass enum -silent -active -brute -w {DNS_JHADDIX} -max-dns-queries 3000 -d {self.root} -o {self.amass_file}", shell=True)
        
        
    def unify_domains(self):
        subprocess.run(f"cat {self.amass_file} {self.sublister_file} {self.assetfinder_file} | anew > {self.merged_domains}", shell=True)




