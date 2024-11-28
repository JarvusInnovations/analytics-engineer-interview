with source as (
    select * from raw_gtfs_routes
)

select
    route_id,
    agency_id,
    route_short_name,
    route_long_name,
    route_type,
    mode_name,
    data_source
from source
