from osgeo import gdal
import os
import sys
import s3fs
import json
import geopandas as gp
from shapely.geometry import box


def main():
    s3 = s3fs.S3FileSystem(anon=True)
    top = s3.ls(f"{BUCKET}/{REGION}")
    
    if os.path.exists(LIST_FILE):
        os.remove(LIST_FILE)

    with open(LIST_FILE,'w') as l:
        for wu in top:
            basename = os.path.basename(wu)
            l.write(f"{basename}\n")   

if __name__ == "__main__":
    REGION = sys.argv[1]
    BUCKET = 'nz-elevation'
    DATA_DIR = f'data/lists'
    LIST_FILE = f'{DATA_DIR}/{REGION}.txt'

    os.makedirs(DATA_DIR, exist_ok=True)

    main()
