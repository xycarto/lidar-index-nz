from osgeo import gdal
import os
import sys
import s3fs
import json
import geopandas as gp
from shapely.geometry import box


def main():
    s3 = s3fs.S3FileSystem(anon=True)
    top = s3.ls(f"{BUCKET}")
    
    if os.path.exists(REGIONS_FILE):
        os.remove(REGIONS_FILE)

    with open(REGIONS_FILE,'w') as l:
        for wu in top:
            if 'LICENSE' not in wu and 'catalog' not in wu:
                basename = os.path.basename(wu)
                l.write(f"{basename}\n")   

if __name__ == "__main__":
    BUCKET = 'nz-elevation'
    DATA_DIR = f'data/lists'
    REGIONS_FILE = f'{DATA_DIR}/regions.txt'

    os.makedirs(DATA_DIR, exist_ok=True)

    main()
