with 

source as (

    select * from {{ source('staging', 'car_sales') }}

),

renamed as (

    select
        year,
        make,
        model,
        trim,
        body,
        transmission,
        vin,
        state,
        condition,
        odometer,
        color,
        interior,
        seller,
        mmr,
        sellingprice,
        saledate

    from source

)

select * from renamed
