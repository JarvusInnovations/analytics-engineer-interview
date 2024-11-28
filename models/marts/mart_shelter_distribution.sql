with location_clusters as (
    select * from {{ ref('int_shelter_locations') }}
),

shelter_stats as (
    select
        count(*) as total_clusters,
        sum(shelters_in_area) as total_shelters,
        avg(shelters_in_area)::decimal(10,2) as avg_shelters_per_cluster,
        max(shelters_in_area) as max_shelters_in_cluster,
        avg(cluster_spread)::decimal(10,6) as avg_cluster_spread,
        -- Geographic bounds of the network
        min(min_lat) as network_min_lat,
        max(max_lat) as network_max_lat,
        min(min_long) as network_min_long,
        max(max_long) as network_max_long
    from location_clusters
),

-- Identify dense areas (clusters with above-average shelter count)
dense_areas as (
    select
        lat_group,
        long_group,
        shelters_in_area,
        cluster_spread
    from location_clusters
    where shelters_in_area > (select avg(shelters_in_area) from location_clusters)
)

select
    s.total_clusters,
    s.total_shelters,
    s.avg_shelters_per_cluster,
    s.max_shelters_in_cluster,
    s.avg_cluster_spread,
    s.network_min_lat,
    s.network_max_lat,
    s.network_min_long,
    s.network_max_long,
    (select count(*) from dense_areas) as dense_cluster_count,
    (select sum(shelters_in_area) from dense_areas) as shelters_in_dense_areas
from shelter_stats s
