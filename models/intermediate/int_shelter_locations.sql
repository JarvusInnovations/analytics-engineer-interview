with shelters as (
    select * from {{ ref('stg_bus_shelters') }}
),

-- Round coordinates to 3 decimal places to group nearby shelters
location_clusters as (
    select
        round(latitude::float, 3) as lat_group,
        round(longitude::float, 3) as long_group,
        count(*) as shelters_in_area,
        array_agg(shelter_id) as shelter_ids,
        array_agg(location_name) as location_names,
        array_agg(stop_id) as stop_ids,
        min(latitude::float) as min_lat,
        max(latitude::float) as max_lat,
        min(longitude::float) as min_long,
        max(longitude::float) as max_long
    from shelters
    group by
        round(latitude::float, 3),
        round(longitude::float, 3)
)

select
    lat_group,
    long_group,
    shelters_in_area,
    shelter_ids,
    location_names,
    stop_ids,
    min_lat,
    max_lat,
    min_long,
    max_long,
    -- Calculate the spread of shelters in the cluster
    sqrt(power(max_lat - min_lat, 2) + power(max_long - min_long, 2)) as cluster_spread
from location_clusters
