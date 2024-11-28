with routes as (
    select * from {{ ref('stg_gtfs_routes') }}
),

agencies as (
    select * from {{ ref('stg_gtfs_agency') }}
)

select
    a.agency_name,
    r.mode_name,
    count(distinct r.route_id) as route_count
from routes r
join agencies a on r.agency_id = a.agency_id
group by 1, 2
order by 1, 2
