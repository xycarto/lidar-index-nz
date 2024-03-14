# lidar-index-nz

**IN DEVELOPMENT**

Method for indexing LINZ LiDAR Elevations hosted on S3. Outputs to **GPKG**

## Basic Method

Pull Docker

```
make docker-pull
```

## Single Acquisition

```
make get-data region=[REGION NAME HERE] workunit=[WORKUNIT NAME HERE]
```

Example

```
make get-data region=auckland workunit=auckland-north_2016-2018
```

## Full Region

Create index for requested region

```
make index-region region=[REGION NAME]
```

Exmaple

```
make index-region region=auckland
```

## Merge GPKGS

After creating indexes, method to merge them into a single file

```
make merge-region region=[REGION NAME]
```

Example
```
make merge-region region=auckland
```

## Entire Country

Index the entire S3 data collection

```
make all-regions
```