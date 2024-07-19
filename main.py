# Main file to run workflow
import import_files, constants, generate_predictions

if __name__ == "__main__":
    # Download PDB structures
    download_format = input("Enter 1 to predict docking for a single protein structure, 2 "
                            "to predict docking for a set of downloaded structures")
    while download_format.strip() not in ["1", "2"]:
        download_format = input(constants.INVALID_MSG)
    
    # Predict for a single protein format
    if download_format.strip() == "1":
        filepath = input("Enter the filepath for your structure")
        # TODO

    # Batch predictions
    elif download_format.strip() == "2":
        # TODO: option to download with script
        download = input("Download from alphafold? (Y/n)")
        if download not in ["Y", ["n"]]:
            download = input(constants.INVALID_MSG)
        filepath = input("Enter the filepath for your downloaded structures")

