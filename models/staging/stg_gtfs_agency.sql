with source as (
    select * from raw_gtfs_agency
)

select
    agency_id,
    agency_name,
    agency_url,
    agency_timezone,
    data_source
from source
