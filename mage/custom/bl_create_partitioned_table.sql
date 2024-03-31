CREATE TABLE de_zoomcamp_car_sales.car_sales
(
        year INTEGER,
        make STRING,
        model STRING,
        trim STRING,
        body STRING,
        transmission STRING,
        vin STRING,
        state STRING,
        condition INTEGER,
        odometer INTEGER,
        color STRING,
        interior STRING,
        seller STRING,
        mmr INTEGER,
        sellingprice INTEGER,
        saledate TIMESTAMP
) PARTITION BY DATE(saledate)
