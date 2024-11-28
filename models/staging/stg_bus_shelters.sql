with source as (
    select *
    from {{ source('raw', 'raw_bus_shelters') }}
),

renamed as (
    select
        objectid as shelter_id,
        site as location_name,
        siteid as site_id,
        stopid as stop_id,
        lat as latitude,
        long_ as longitude,
        productgroup as product_group,
        x as x_coordinate,
        y as y_coordinate
    from source
)

select * from renamed
where shelter_id is not null
