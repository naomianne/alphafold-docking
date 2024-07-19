import requests

# TODO: enable download dataset. Starter code

def download_structures(uniprot_id):
    """
    download structure predictions from 
    """
    url = f"https://www.alphafold.ebi.ac.uk/entry/{uniprot_id}"
    response = requests.get(url)

def parse_downloads(dir: dir) -> None:
    """
    extract and filter out files
    """
    pass