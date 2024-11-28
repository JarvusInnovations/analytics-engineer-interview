{% test positive_value(model, column_name, min_value=0) %}

with validation as (
    select
        {{ column_name }} as value
    from {{ model }}
    where {{ column_name }} < {{ min_value }}
)

select *
from validation

{% endtest %}
