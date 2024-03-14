#!/bin/bash

REGION_LIST="data/lists/regions.txt"

region_gpkgs=data/${REGION}
merged_gpkg=${region_gpkgs}/${REGION}.gpkg

mrg_arry=()
while read REGION; do
    region_gpkgs=data/${REGION}
    merged_gpkg=${region_gpkgs}/${REGION}.gpkg
    mrg_arry+="$merged_gpkg "
done < $REGION_LIST

ogrmerge.py -single -overwrite_ds -f GPKG -o data/merged-lidar-index.gpkg ${mrg_arry}

ogr2ogr -t_srs EPSG:2193 data/merged-lidar-index-2193.gpkg data/merged-lidar-index.gpkg