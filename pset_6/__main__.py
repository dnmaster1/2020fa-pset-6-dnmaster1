import pandas as pd
from .io import atomic_write
from .hash_str import get_csci_salt, get_user_id, hash_str


def get_user_hash(username, salt=None):
    salt = salt or get_csci_salt()
    return hash_str(username, salt=salt)


if __name__ == "__main__":

    for user in ["gorlins", "dnmaster1"]:
        print("Id for {}: {}".format(user, get_user_id(user)))

    data_source = "data/hashed.xlsx"

    # TODO: read in, save as new parquet file, read back just id column, print
    df_xlsx = pd.read_excel(data_source)  # Reading Excel copied from AWS S3

    parquet_fname = "hashed.parquet"  # File name for Parquet per instructions

    with atomic_write(parquet_fname, "wb") as f:
        df_xlsx.to_parquet(f)  # yield yo parquet write from atomic_write

    df_parquet_id = pd.read_parquet(
        parquet_fname, columns=["hashed_id"]
    )  # reading hashed_id column per instruction
    print(df_parquet_id)
