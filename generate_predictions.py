import subprocess

# P2Rank predictions

# Created separate function so we can test it with one structure
def predict_docking_site(file: str, output_dir: str) -> None:
    """
    Use p2rank to predict docking site for a single structure.
    Takes: .pdb, .cif, .bcif, .pdb.gz, .cif.zst
    """
    command = f"prank predict -f {file} -o {output_dir}"
    try:
        result = subprocess.run(command, shell=True, check=True)
    except: 
        "Error generating p2rank predictions"
    return result


def predict_sites(file: str, output_dir: str) -> None:
    """
    For batch predictions
    """
    command = f"prank predict -c alphafold {file} -o {output_dir}"
    # TODO