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
        self.wayback = self.folder + "wayback.txt"
        self.merged_domains = self.folder + "merged-domains.txt"
        self.live_hosts = self.folder + "live_hosts.txt"


    def assetfinder(self):
        subprocess.run(f"assetfinder --subs-only {self.root} > {self.assetfinder_file}", shell=True)

    
    def sublister(self):
        subprocess.run(f"python3 {SUBLISTER} -d {self.root} -t 50 -v -o {self.sublister_file} > /dev/null", shell=True)
        

    def amass(self):
        subprocess.run(f"amass enum -silent -brute -w ~/tools/Wordlists/riot_subs.txt -max-dns-queries 3000 -active  -d {self.root} -o {self.amass_file}", shell=True)
        
        
    def unify_domains(self):
        subprocess.run(f"cat {self.amass_file} {self.sublister_file} {self.assetfinder_file} | anew > {self.merged_domains}", shell=True)

    
    def waybackurls(self):
        subprocess.run(f"cat {self.merged_domains} | waybackurls > {self.wayback}", shell=True)
        subprocess.run(f"cat {self.wayback} | cut -d '/' -f 3 | cut -d ':' -f 1 | anew {self.merged_domains}", shell=True)


    def httprobe(self):
        subprocess.run(f"cat {self.merged_domains} | httprobe -c 50 -t 3000 >> {self.live_hosts}", shell=True)


    def aquatone(self):

        subprocess.run(f"cat {self.folder}/live_hosts.txt | aquatone -out {self.folder} -ports xlarge -silent", shell=True)



