from osgeo import gdal
import os
import sys
import s3fs
import json
import geopandas as gp
from shapely.geometry import box


def main():
    gpkg_out = f"{DATA_DIR}/{WORKUNIT}.gpkg"

    s3 = s3fs.S3FileSystem(anon=True)
    top = s3.find(f"{BUCKET}/{REGION}/{WORKUNIT}")
    list_json = [path for path in top if path.endswith('.json')]

    df = []
    for i, jpath in enumerate(list_json):
        if 'collection' not in jpath:
            with s3.open(jpath, 'rb') as f:
                jdata = json.load(f)

            poly = box(*jdata['bbox'])

            df.append(
                {
                    'bucket': BUCKET,
                    'file_name':os.path.basename(jpath).replace('json', 'tiff'),
                    'region':REGION,
                    'workunit': WORKUNIT,
                    's3_loc': jpath.replace('json', 'tiff'),
                    'native_crs': jpath.split('/')[4],
                    'geometry': poly
                }
            )

            # if i >= 5:
            #     break

    gp.GeoDataFrame(df, crs=CRS).to_file(gpkg_out, driver='GPKG')

if __name__ == "__main__":
    REGION = sys.argv[1]
    WORKUNIT = sys.argv[2]
    BUCKET = 'nz-elevation'
    CRS = 4326
    DATA_DIR = f'data/{REGION}'

    os.makedirs(DATA_DIR, exist_ok=True)

    main()
